#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
cd "${PROJECT_ROOT}"

PYTHON="${PROJECT_ROOT}/.venv-training-py311/bin/python3"
RUN_TAG="${RUN_TAG:-260512_anti_leak1200_vllm01}"
LIMIT="${LIMIT:-1200}"
SEED="${SEED:-20260512}"
WORKERS="${WORKERS:-10}"
CHECK_INTERVAL_SECONDS="${CHECK_INTERVAL_SECONDS:-300}"
UTIL_THRESHOLD="${UTIL_THRESHOLD:-20}"
MEM_THRESHOLD_MIB="${MEM_THRESHOLD_MIB:-12000}"
MAX_TOKENS="${MAX_TOKENS:-12000}"
TIMEOUT_SECONDS="${TIMEOUT_SECONDS:-900}"
VLLM_MAXLEN="${VLLM_MAXLEN:-32768}"
VLLM_GPU_UTIL="${VLLM_GPU_UTIL:-0.85}"
UPDATE_DATASET_INFO="${UPDATE_DATASET_INFO:-1}"
PREPARE_ONLY="${PREPARE_ONLY:-0}"
REUSE_SERVICES="${REUSE_SERVICES:-0}"

ADAPTER_PATH="${ADAPTER_PATH:-${PROJECT_ROOT}/training/outputs/qwen25_7b/sft_260512_replay_usage700_plus_bestofn600_from_replay_r32_b32_lr1e5_ctx24576_ep2_20260512}"
OUT_DIR="${OUT_DIR:-${PROJECT_ROOT}/training/data/planner/bestofn/${RUN_TAG}}"
LOG_DIR="${LOG_DIR:-${PROJECT_ROOT}/training/outputs/eval/logs/${RUN_TAG}_wait_gpu01_w10}"
LF_PREFIX="${LF_PREFIX:-trip_planner_bestofn_${RUN_TAG}}"

IFS=',' read -r -a GPUS <<< "${GPUS_CSV:-0,1}"
IFS=',' read -r -a PORTS <<< "${PORTS_CSV:-4436,4437}"
if [[ "${#GPUS[@]}" -ne "${#PORTS[@]}" ]]; then
  echo "GPUS_CSV and PORTS_CSV must have the same number of entries." >&2
  exit 2
fi

mkdir -p "${OUT_DIR}" "${LOG_DIR}"

log() {
  printf '[%s] %s\n' "$(date '+%F %T')" "$*" | tee -a "${LOG_DIR}/launcher.log"
}

line_count() {
  local path="$1"
  if [[ -f "${path}" ]]; then
    wc -l < "${path}" | tr -d ' '
  else
    printf '0'
  fi
}

prepare_inputs() {
  log "Preparing records/prompts under ${OUT_DIR}"
  if [[ ! -s "${OUT_DIR}/records.jsonl" || "${FORCE_PREPARE:-0}" == "1" ]]; then
    "${PYTHON}" training/scripts/planner/bestofn/prepare_anti_leak_records.py \
      --output "${OUT_DIR}/records.jsonl" \
      --summary-output "${OUT_DIR}/records_selection_summary.json" \
      --limit "${LIMIT}" \
      --seed "${SEED}" \
      --id-prefix "bestofn_anti_leak1200" \
      | tee "${LOG_DIR}/prepare_records.log"
  else
    log "records.jsonl exists; set FORCE_PREPARE=1 to rebuild."
  fi

  if [[ ! -s "${OUT_DIR}/prompts.jsonl" || "${FORCE_PREPARE:-0}" == "1" ]]; then
    "${PYTHON}" training/scripts/planner/bestofn/build_prompts.py \
      --records "${OUT_DIR}/records.jsonl" \
      --output "${OUT_DIR}/prompts.jsonl" \
      --summary-output "${OUT_DIR}/prompts_summary.json" \
      --source "${RUN_TAG}" \
      | tee "${LOG_DIR}/build_prompts.log"
  else
    log "prompts.jsonl exists; set FORCE_PREPARE=1 to rebuild."
  fi

  "${PYTHON}" - "${OUT_DIR}" "${GPUS[@]}" <<'PY'
import json
import sys
from pathlib import Path

out_dir = Path(sys.argv[1])
gpus = sys.argv[2:]
handles = {
    gpu: (out_dir / f"prompts_accel_gpu{gpu}.jsonl").open("w", encoding="utf-8")
    for gpu in gpus
}
try:
    with (out_dir / "prompts.jsonl").open(encoding="utf-8") as src:
        for idx, line in enumerate(src):
            gpu = gpus[idx % len(gpus)]
            handles[gpu].write(line)
finally:
    for handle in handles.values():
        handle.close()

summary = {
    "total_prompts": sum(1 for _ in (out_dir / "prompts.jsonl").open(encoding="utf-8")),
    "shards": {
        f"gpu{gpu}": sum(1 for _ in (out_dir / f"prompts_accel_gpu{gpu}.jsonl").open(encoding="utf-8"))
        for gpu in gpus
    },
}
(out_dir / "accel_split_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
PY
}

gpu_stats() {
  local gpu="$1"
  nvidia-smi --id="${gpu}" --query-gpu=utilization.gpu,memory.used --format=csv,noheader,nounits | tr -d ' '
}

gpu_is_free() {
  local gpu="$1"
  local stats util mem
  stats="$(gpu_stats "${gpu}")"
  util="${stats%,*}"
  mem="${stats#*,}"
  log "GPU ${gpu}: util=${util}% mem=${mem}MiB thresholds util<=${UTIL_THRESHOLD}% mem<=${MEM_THRESHOLD_MIB}MiB"
  [[ "${util}" -le "${UTIL_THRESHOLD}" && "${mem}" -le "${MEM_THRESHOLD_MIB}" ]]
}

wait_service_ready() {
  local port="$1"
  local log_file="$2"
  for _ in $(seq 1 90); do
    if "${PYTHON}" - "${port}" >/dev/null 2>&1 <<'PY'
import json
import sys
import urllib.request

port = int(sys.argv[1])
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
with opener.open(f"http://127.0.0.1:{port}/v1/models", timeout=5) as response:
    data = json.loads(response.read().decode("utf-8"))
if not data.get("data"):
    raise SystemExit(1)
PY
    then
      log "Service on port ${port} is ready."
      return 0
    fi
    sleep 10
  done
  log "Service on port ${port} did not become ready. Tail ${log_file}:"
  tail -n 80 "${log_file}" | tee -a "${LOG_DIR}/launcher.log" || true
  return 1
}

shard_complete() {
  local gpu="$1"
  local prompt_file="${OUT_DIR}/prompts_accel_gpu${gpu}.jsonl"
  local candidate_file="${OUT_DIR}/candidates_accel_gpu${gpu}.jsonl"
  local prompts candidates
  prompts="$(line_count "${prompt_file}")"
  candidates="$(line_count "${candidate_file}")"
  [[ "${prompts}" -gt 0 && "${candidates}" -ge "${prompts}" ]]
}

start_gpu_worker() {
  local gpu="$1"
  local port="$2"
  local api_model="trip-planner-bestofn1200-gpu${gpu}"
  local service_log="${LOG_DIR}/serve_gpu${gpu}_${port}.log"
  local gen_log="${LOG_DIR}/generate_gpu${gpu}.log"
  local prompt_file="${OUT_DIR}/prompts_accel_gpu${gpu}.jsonl"
  local candidate_file="${OUT_DIR}/candidates_accel_gpu${gpu}.jsonl"

  if [[ "${REUSE_SERVICES}" == "1" ]]; then
    log "Reusing vLLM service on GPU ${gpu}, port ${port}"
  else
    log "Starting vLLM service on GPU ${gpu}, port ${port}"
    "${PYTHON}" training/scripts/serving/manage_planner_service.py restart \
      --port "${port}" \
      --variant sft \
      --infer-backend vllm \
      --cuda-visible-devices "${gpu}" \
      --adapter-path "${ADAPTER_PATH}" \
      --api-model-name "${api_model}" \
      --vllm-maxlen "${VLLM_MAXLEN}" \
      --vllm-gpu-util "${VLLM_GPU_UTIL}" \
      --log-file "${service_log}" \
      | tee -a "${LOG_DIR}/launcher.log"
  fi

  wait_service_ready "${port}" "${service_log}"

  log "Starting candidate generation on GPU ${gpu}: prompts=$(line_count "${prompt_file}") workers=${WORKERS}"
  nohup "${PYTHON}" -u training/scripts/planner/bestofn/generate_candidates.py \
    --prompts "${prompt_file}" \
    --output "${candidate_file}" \
    --base-url "http://127.0.0.1:${port}/v1" \
    --api-model "${api_model}" \
    --spec t02:0.2:2 \
    --spec t05:0.5:2 \
    --spec t08:0.8:2 \
    --workers "${WORKERS}" \
    --resume \
    --timeout "${TIMEOUT_SECONDS}" \
    --max-tokens "${MAX_TOKENS}" \
    > "${gen_log}" 2>&1 &

  local pid=$!
  printf '%s\t%s\t%s\t%s\t%s\n' "${gpu}" "${port}" "${pid}" "${gen_log}" "$(date '+%F %T')" >> "${LOG_DIR}/launch_pids.tsv"
  log "Generation pid=${pid} log=${gen_log}"
  GEN_PIDS["${gpu}"]="${pid}"
}

postprocess() {
  log "Merging candidates and selecting winners."
  : > "${OUT_DIR}/candidates.jsonl"
  for gpu in "${GPUS[@]}"; do
    cat "${OUT_DIR}/candidates_accel_gpu${gpu}.jsonl" >> "${OUT_DIR}/candidates.jsonl"
  done

  local update_args=()
  if [[ "${UPDATE_DATASET_INFO}" == "1" ]]; then
    update_args=(--update-dataset-info)
  fi

  "${PYTHON}" training/scripts/planner/bestofn/select_best.py \
    --prompts "${OUT_DIR}/prompts.jsonl" \
    --candidates "${OUT_DIR}/candidates.jsonl" \
    --selected-output "${OUT_DIR}/selected.jsonl" \
    --summary-output "${OUT_DIR}/bestofn_summary.json" \
    --lf-sft-train "training/data/llamafactory/${LF_PREFIX}_sft_train.json" \
    --lf-sft-val "training/data/llamafactory/${LF_PREFIX}_sft_val.json" \
    --lf-pair-train "training/data/llamafactory/${LF_PREFIX}_pair_train.json" \
    --lf-pair-val "training/data/llamafactory/${LF_PREFIX}_pair_val.json" \
    --sft-train-name "${LF_PREFIX}_sft_train" \
    --sft-val-name "${LF_PREFIX}_sft_val" \
    --pair-train-name "${LF_PREFIX}_pair_train" \
    --pair-val-name "${LF_PREFIX}_pair_val" \
    "${update_args[@]}" \
    | tee "${LOG_DIR}/select_best.log"

  "${PYTHON}" training/scripts/planner/bestofn/render_review.py \
    --prompts "${OUT_DIR}/prompts.jsonl" \
    --candidates "${OUT_DIR}/candidates.jsonl" \
    --selected "${OUT_DIR}/selected.jsonl" \
    --summary "${OUT_DIR}/bestofn_summary.json" \
    --output "${OUT_DIR}/review.md" \
    | tee "${LOG_DIR}/render_review.log"
  log "Done. Summary: ${OUT_DIR}/bestofn_summary.json"
}

declare -A GEN_PIDS=()
declare -A STARTED=()

prepare_inputs
if [[ "${PREPARE_ONLY}" == "1" ]]; then
  log "PREPARE_ONLY=1; prepared inputs and exiting before GPU wait."
  exit 0
fi

printf 'gpu\tport\tpid\tlog\tstarted_at\n' > "${LOG_DIR}/launch_pids.tsv"

for gpu in "${GPUS[@]}"; do
  if shard_complete "${gpu}"; then
    STARTED["${gpu}"]="complete"
    log "GPU ${gpu} shard already complete; skip launch."
  fi
done

while [[ "${#STARTED[@]}" -lt "${#GPUS[@]}" ]]; do
  for idx in "${!GPUS[@]}"; do
    gpu="${GPUS[$idx]}"
    port="${PORTS[$idx]}"
    if [[ -n "${STARTED[$gpu]:-}" ]]; then
      continue
    fi
    if [[ "${REUSE_SERVICES}" == "1" ]] || gpu_is_free "${gpu}"; then
      STARTED["${gpu}"]="started"
      start_gpu_worker "${gpu}" "${port}"
    else
      log "GPU ${gpu} is still busy; will check again."
    fi
  done
  if [[ "${#STARTED[@]}" -lt "${#GPUS[@]}" ]]; then
    log "Sleeping ${CHECK_INTERVAL_SECONDS}s before next GPU util check."
    sleep "${CHECK_INTERVAL_SECONDS}"
  fi
done

for gpu in "${!GEN_PIDS[@]}"; do
  pid="${GEN_PIDS[$gpu]}"
  log "Waiting for GPU ${gpu} generation pid=${pid}"
  wait "${pid}"
  log "GPU ${gpu} generation finished."
done

if shard_complete 0 && shard_complete 1; then
  postprocess
else
  log "Generation is not complete on both shards; leaving partial outputs for resume."
  exit 1
fi
