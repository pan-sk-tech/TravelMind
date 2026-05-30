"""TravelMind 在线失败样本和偏好候选落盘逻辑。"""

import json
from datetime import datetime, timezone
from typing import Any, Dict, List

from ..models.schemas import TripPlan, TripRequest
from ..services.mcp_env import PROJECT_ROOT


ONLINE_FEEDBACK_DIR = PROJECT_ROOT / "training" / "data" / "online_feedback"
TRAVELMIND_FAILURE_LOG = ONLINE_FEEDBACK_DIR / "travelmind_failures.jsonl"
TRAVELMIND_DPO_CANDIDATE_LOG = ONLINE_FEEDBACK_DIR / "travelmind_dpo_candidates.jsonl"

# Backward-compatible names used by the existing generation code.
TRAVELMIND_FAILURE_LOG = TRAVELMIND_FAILURE_LOG
TRAVELMIND_DPO_CANDIDATE_LOG = TRAVELMIND_DPO_CANDIDATE_LOG


class TravelMindGenerationError(ValueError):
    """Raised when a TravelMind cannot produce valid TripPlan JSON."""

    def __init__(self, message: str, failures: List[Dict[str, Any]]):
        super().__init__(message)
        self.failures = failures


def is_non_retryable_llm_error(error: Exception) -> bool:
    """判断同一 prompt 继续重试也很难恢复的 LLM 接口错误。"""
    text = str(error).lower()
    return (
        "content exists risk" in text
        or ("invalid_request_error" in text and "400" in text)
    )


def build_failure_row(
    label: str,
    attempt: int,
    max_attempts: int,
    request: TripRequest,
    travelmind_query: str,
    response: str,
    error: Exception,
    preference_reason: str = "travelmind_schema_invalid",
) -> Dict[str, Any]:
    """Build an online feedback row for invalid TravelMind output."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "label": label,
        "attempt": attempt,
        "max_attempts": max_attempts,
        "request": request.model_dump(),
        "prompt": travelmind_query,
        "rejected": response,
        "error_type": type(error).__name__,
        "error": str(error),
        "preference_reason": preference_reason,
    }


def log_preference_candidates(
    travelmind_query: str,
    request: TripRequest,
    chosen_plan: TripPlan,
    failures: List[Dict[str, Any]],
    chosen_label: str = "默认 TravelMind",
) -> None:
    """Log DPO candidate rows using invalid TravelMind outputs as rejected."""
    chosen_value = json.dumps(chosen_plan.model_dump(), ensure_ascii=False)
    for failure in failures:
        row = {
            "conversations": [{"from": "human", "value": travelmind_query}],
            "chosen": {"from": "gpt", "value": chosen_value},
            "rejected": {"from": "gpt", "value": failure["rejected"]},
            "preference_reason": failure.get("preference_reason", "travelmind_schema_invalid"),
            "metadata": {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "request": request.model_dump(),
                "rejected_label": failure.get("label"),
                "rejected_attempt": failure.get("attempt"),
                "chosen_label": chosen_label,
                "error": failure.get("error"),
            },
        }
        append_jsonl(TRAVELMIND_DPO_CANDIDATE_LOG, row)


def append_jsonl(path, row: Dict[str, Any]) -> None:
    """Append one JSONL row, creating the directory on demand."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(row, ensure_ascii=False) + "\n")





