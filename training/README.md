training/ 保存 TravelMind 的轻量评估集和评测说明，用于从预算满足率、偏好匹配度、路线合理性和约束违反率等维度检查 Agent 生成质量。完整模型训练产物、历史实验记录和大规模数据不纳入公开仓库。

## 分工
```text
前端收集用户意图
  -> 后端结构化人数、预算、偏好、住宿和工具候选
  -> TravelMindContext 冻结模型可见事实
  -> TravelMind Agent生成 TripPlan JSON
  -> 规则评测脚本检查 schema、grounding、预算和偏好指标
```

SFT 主要学习确定性协议：

- JSON 可解析，`TripPlan` schema 通过。
- 日期、天数、天气和住宿晚数正确。
- 景点、酒店、餐饮尽量来自工具候选。
- 酒店、门票、餐饮预算口径稳定。
- `budget.total` 和预算分项关系可校验。

DPO 主要学习合法候选之间的偏好：

- 更符合预算档位。
- 更贴合同行人、饮食、节奏和负向约束。
- 更可执行、更少重复、更适合真实用户。


```


## 评估集

构建 standard eval：

```bash
.venv-training-py311/bin/python3 training/scripts/travelmind/eval/build_eval_set.py \
  --count 200 \
  --start-index 0 \
  --id-prefix standard200_eval \
  --request-source controlled \
  --date-mode mixed \
  --workers 4 \
  --resume
```

构建 hard eval：

当前 hard eval 使用原 `harder` 压力分布构建，主路径统一命名为 `eval_hard`。

```bash
.venv-training-py311/bin/python3 training/scripts/travelmind/eval/build_eval_set.py \
  --count 300 \
  --start-index 0 \
  --id-prefix harder_eval \
  --request-source controlled \
  --date-mode mixed \
  --difficulty harder \
  --workers 2 \
  --output-dir training/data/travelmind/eval_hard \
  --resume
```

公开仓库保留的评估入口：

- `training/data/travelmind/eval/records.jsonl`
- `training/data/travelmind/eval_hard/records.jsonl`

所有 baseline、SFT、DPO 对比都应复用这些冻结输入，避免请求分布、工具快照或天气来源变化影响模型对比。

## 当前评测口径

评测固定输出两层主要 pass：

- `sft_hard_pass`：线上可用的确定性协议，包括 schema、日期、天气、住宿、grounding、预算账本和硬预算约束。
- `dpo_soft_pass`：在合法输出基础上看餐饮多样性、餐饮 grounding、预算偏好和整体可用性。

阶段性还记录：

- `sft_budget_semantic_hard_pass`
- `hotel_budget_relation_ok`
- `attraction_budget_party_relation_ok`
- `meal_cost_scale_ok`
- `budget_relationship_ok`

完整口径见评测指标文档。

## 当前公开结果

当前评测输出统一按新目录组织：

```text
training/outputs/eval/by_model/<model>/<YYMMDD>_<run_slug>/
training/outputs/eval/comparisons/<YYMMDD>_<comparison_slug>/
training/outputs/eval/audits/<YYMMDD>_<audit_slug>/
training/outputs/eval/logs/<YYMMDD>_<log_slug>/
training/outputs/eval/reports/<YYMMDD>_<report_slug>/
```

当前可公开引用的报告都整理到 `reports/`：

- `outputs/eval/reports/260512_bestofn_replay_extended_w10/`：2026-05-12 Best-of-N replay 扩展对比，包含多个 checkpoint、上一轮 replay、前序 LoRA、旧路线对照与外部 Mimo reference 的 500 条合并/standard/hard 主要指标。
- `outputs/eval/reports/260511_usage700_followup_w10/`：usage700 SFT follow-up 对比。
- `outputs/eval/reports/260511_high_end_context_mainline/`：高端 POI 上下文重构后三模型主线对比。

`by_model/`、`comparisons/`、`audits/`、`logs/` 默认视为本地生成产物；需要公开的评估结论先整理成 `reports/<YYMMDD>_<slug>/`。

## DPO 状态

当前主线把 DPO 定位为偏好训练，而不是修坏 JSON 或坏 schema。DPO prompt source 来自 `TravelMindContext` 和 `travelmind_query`，不直接使用 teacher answer。

当前 DPO prompt source 只在本地保留，不进入公开仓库：

- `training/data/travelmind/dpo/prompts.jsonl`
- `training/data/travelmind/dpo/prompt_source/records.jsonl`

公开仓库只保留 DPO 口径和轻量说明。pair 构造、judge、prompt source 和训练产物仍按本地实验资产处理；当前公开参考为 `docs/后训练产物/03_DPO阶段/README.md`、`docs/后训练产物/04_Rerank阶段/README.md`、`scripts/travelmind/README.md` 和 `scripts/travelmind/bestofn/README.md`。单生成最佳点是 `260519 checkpoint-138`；最终展示版本是 `260521 checkpoint-64 rerank n4`。






