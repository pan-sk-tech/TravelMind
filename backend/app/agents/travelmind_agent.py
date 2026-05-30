"""TravelMind 个性化旅行规划 Agent"""

import os
import time
from typing import Dict, Any, List, Optional

from hello_agents import SimpleAgent
from ..services.llm_service import get_llm, get_travelmind_llm
from ..models.schemas import TripRequest, TripPlan
from ..config import get_settings
from .travelmind_feedback import (
    TRAVELMIND_FAILURE_LOG,
    TravelMindGenerationError,
    append_jsonl,
    build_failure_row,
    is_non_retryable_llm_error,
    log_preference_candidates,
)
from ..travelmind_core.context import TravelMindContextBuilder
from ..travelmind_core.output import (
    create_fallback_plan,
    enrich_trip_plan_poi_details,
    extract_json_object,
    validate_trip_plan_shape,
)
from ..travelmind_core.rerank import RerankCandidate, rerank_trip_plan_candidates
from .travelmind_query import build_travelmind_query, travelmind_max_output_tokens
from .prompts import TRAVELMIND_AGENT_PROMPT


TRAVELMIND_MAX_ATTEMPTS = int(os.getenv("TRAVELMIND_MAX_ATTEMPTS", "2"))
TRAVELMIND_REQUEST_TIMEOUT = int(os.getenv("TRAVELMIND_REQUEST_TIMEOUT", "180"))
TRAVELMIND_TEMPERATURE = float(os.getenv("TRAVELMIND_TEMPERATURE", "0.2"))
TRAVELMIND_PRIMARY_CALL_FAILURE_LIMIT = int(os.getenv("TRAVELMIND_PRIMARY_CALL_FAILURE_LIMIT", "3"))
TRAVELMIND_FALLBACK_CALL_FAILURE_LIMIT = int(os.getenv("TRAVELMIND_FALLBACK_CALL_FAILURE_LIMIT", "3"))
TRAVELMIND_ENABLE_RERANK = os.getenv("TRAVELMIND_ENABLE_RERANK", "0") == "1"
TRAVELMIND_RERANK_CANDIDATE_COUNT = max(1, int(os.getenv("TRAVELMIND_RERANK_CANDIDATE_COUNT", "3")))
TRAVELMIND_RERANK_TEMPERATURE_STEP = float(os.getenv("TRAVELMIND_RERANK_TEMPERATURE_STEP", "0.08"))


class TravelMindAgent:
    """TravelMind 个性化旅行规划 Agent"""

    def __init__(self):
        """初始化 TravelMind Agent"""
        print("🔄 开始初始化 TravelMind 个性化旅行规划 Agent...")
        self.last_generation_status = "idle"
        self.last_generation_message = ""

        try:
            settings = get_settings()
            self.settings = settings
            self.amap_api_key = settings.amap_api_key or os.getenv("AMAP_MAPS_API_KEY") or os.getenv("AMAP_API_KEY")
            self.travelmind_context_builder = TravelMindContextBuilder(self.amap_api_key)
            self.tool_llm = get_llm()
            self.travelmind_llm = get_travelmind_llm()
            self.llm = self.tool_llm

            # 后端不再让工具 Agent 先写自然语言摘要。
            # 这里直接调用高德 HTTP API，拿到结构化快照后交给 TravelMind。
            print("  - 使用高德HTTP API获取结构化工具快照...")

            # 创建 TravelMind 行程规划 Agent(不需要工具)
            print("  - 创建 TravelMind 行程规划 Agent...")
            self.travelmind_agent = SimpleAgent(
                name="TravelMind行程规划专家",
                llm=self.travelmind_llm,
                system_prompt=TRAVELMIND_AGENT_PROMPT
            )
            self.fallback_travelmind_agent = SimpleAgent(
                name="默认TravelMind行程规划专家",
                llm=self.tool_llm,
                system_prompt=TRAVELMIND_AGENT_PROMPT
            )

            print(f"✅ TravelMind Agent 初始化成功")
            print(f"   工具查询: 高德HTTP API(景点/天气/酒店并行)")
            print(f"   TravelMind模型: {'个性化模型' if self.travelmind_llm is not self.tool_llm else '默认模型'}")

        except Exception as e:
            print(f"❌ 多智能体系统初始化失败: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

    def plan_trip(self, request: TripRequest) -> TripPlan:
        """
        使用 TravelMind Agent 生成旅行计划

        Args:
            request: 旅行请求

        Returns:
            旅行计划
        """
        total_started_at = time.perf_counter()
        try:
            print(f"\n{'='*60}")
            print(f"🚀 开始 TravelMind 个性化旅行规划...")
            print(f"目的地: {request.city}")
            print(f"日期: {request.start_date} 至 {request.end_date}")
            print(f"天数: {request.travel_days}天")
            print(f"人数: {request.party.total}人 ({request.party.companion_type})")
            print(f"预算: {request.budget_constraint.amount or '未指定'} {request.budget_constraint.currency}")
            print(f"偏好: {', '.join(request.preferences) if request.preferences else '无'}")
            print(f"{'='*60}\n")

            # 步骤1: 并行获取结构化工具快照
            print("📍 步骤1: 并行获取景点/天气/酒店工具快照...")
            step_started_at = time.perf_counter()
            travelmind_context = self.travelmind_context_builder.collect(request)
            self._log_timer("步骤1 工具快照获取", step_started_at)
            self.travelmind_context_builder.print_summary(travelmind_context)
            self.travelmind_context_builder.print_visualization(travelmind_context)

            # 步骤2: TravelMind Agent 整合信息生成计划
            print("📋 步骤2: 生成行程计划...")
            step_started_at = time.perf_counter()
            travelmind_query = build_travelmind_query(self.travelmind_context_builder, request, travelmind_context)
            self._log_timer("步骤2 TravelMind输入构造", step_started_at)
            print(f"TravelMind输入长度: {len(travelmind_query)} 字符")

            self.last_generation_status = "running"
            self.last_generation_message = "TravelMind生成中"
            primary_label = "个性化 TravelMind" if self.travelmind_llm is not self.tool_llm else "默认 TravelMind"
            used_travelmind_label = primary_label

            # 解析最终计划
            try:
                trip_plan = self._generate_trip_plan_with_retries(
                    agent=self.travelmind_agent,
                    travelmind_query=travelmind_query,
                    request=request,
                    label=primary_label,
                    max_attempts=TRAVELMIND_MAX_ATTEMPTS,
                    travelmind_context=travelmind_context,
                    max_call_failures=TRAVELMIND_PRIMARY_CALL_FAILURE_LIMIT,
                )
            except TravelMindGenerationError as parse_error:
                if self.travelmind_llm is self.tool_llm:
                    raise
                print(f"⚠️  个性化 TravelMind 失败，将回退到默认 LLM: {parse_error}")
                used_travelmind_label = "默认 TravelMind"
                trip_plan = self._generate_trip_plan_with_retries(
                    agent=self.fallback_travelmind_agent,
                    travelmind_query=travelmind_query,
                    request=request,
                    label="默认 TravelMind",
                    max_attempts=TRAVELMIND_MAX_ATTEMPTS,
                    travelmind_context=travelmind_context,
                    max_call_failures=TRAVELMIND_FALLBACK_CALL_FAILURE_LIMIT,
                )
                log_preference_candidates(travelmind_query, request, trip_plan, parse_error.failures)
            except Exception as travelmind_error:
                if self.travelmind_llm is self.tool_llm:
                    raise
                print(f"⚠️  个性化 TravelMind 调用失败，将回退到默认 LLM: {travelmind_error}")
                used_travelmind_label = "默认 TravelMind"
                append_jsonl(
                    TRAVELMIND_FAILURE_LOG,
                    build_failure_row(
                        label="个性化 TravelMind",
                        attempt=1,
                        max_attempts=TRAVELMIND_MAX_ATTEMPTS,
                        request=request,
                        travelmind_query=travelmind_query,
                        response="",
                        error=travelmind_error,
                        preference_reason="travelmind_llm_call_failed",
                    ),
                )
                trip_plan = self._generate_trip_plan_with_retries(
                    agent=self.fallback_travelmind_agent,
                    travelmind_query=travelmind_query,
                    request=request,
                    label="默认 TravelMind",
                    max_attempts=TRAVELMIND_MAX_ATTEMPTS,
                    travelmind_context=travelmind_context,
                    max_call_failures=TRAVELMIND_FALLBACK_CALL_FAILURE_LIMIT,
                )

            self.last_generation_status = "llm_success"
            self.last_generation_message = f"{used_travelmind_label} 生成成功"
            print(f"{'='*60}")
            print(f"✅ 旅行计划生成完成: {self.last_generation_message}")
            self._log_timer("旅行计划总耗时", total_started_at)
            print(f"{'='*60}\n")

            return trip_plan

        except Exception as e:
            print(f"❌ 生成旅行计划失败: {str(e)}")
            import traceback
            traceback.print_exc()
            self.last_generation_status = "fallback_success"
            self.last_generation_message = f"TravelMind失败，已返回fallback计划: {str(e)}"
            print(f"⚠️  {self.last_generation_message}")
            self._log_timer("旅行计划总耗时", total_started_at)
            return create_fallback_plan(request)

    def _log_timer(self, label: str, started_at: float) -> None:
        """打印轻量耗时日志，便于定位慢点。"""
        elapsed = time.perf_counter() - started_at
        print(f"[TIMER] {label}: {elapsed:.2f}s", flush=True)

    def _run_agent_stateless(self, agent: SimpleAgent, input_text: str, **kwargs) -> str:
        """Run a SimpleAgent without carrying history across trip requests."""
        if hasattr(agent, "_history"):
            agent._history = []

        try:
            return agent.run(input_text, **kwargs)
        finally:
            if hasattr(agent, "_history"):
                agent._history = []

    def _generate_trip_plan_with_retries(
        self,
        agent: SimpleAgent,
        travelmind_query: str,
        request: TripRequest,
        label: str,
        max_attempts: int,
        travelmind_context: Optional[Dict[str, Any]] = None,
        max_call_failures: Optional[int] = None,
    ) -> TripPlan:
        """Generate and parse a TripPlan with clean retries.

        这里故意不把上一次失败输出拼回下一次请求。TravelMindContext 已经很长，
        修复式重试会快速放大上下文，并且容易把错误格式再次强化给模型。
        """
        last_error = None
        failures: List[Dict[str, Any]] = []
        call_failures = 0
        rerank_enabled = (
            TRAVELMIND_ENABLE_RERANK
            and travelmind_context is not None
            and TRAVELMIND_RERANK_CANDIDATE_COUNT > 1
        )
        target_candidate_count = (
            min(max_attempts, TRAVELMIND_RERANK_CANDIDATE_COUNT)
            if rerank_enabled
            else 1
        )
        valid_candidates: List[tuple[int, TripPlan]] = []

        if rerank_enabled:
            print(
                f"{label} 启用rerank: 目标候选={target_candidate_count}, "
                f"temperature_step={TRAVELMIND_RERANK_TEMPERATURE_STEP}",
                flush=True,
            )

        for attempt in range(1, max_attempts + 1):
            print(f"{label} 第 {attempt}/{max_attempts} 次生成...", flush=True)
            call_started_at = time.perf_counter()
            max_output_tokens = travelmind_max_output_tokens(request)
            if rerank_enabled:
                temperature = min(
                    0.95,
                    max(0.0, TRAVELMIND_TEMPERATURE + (attempt - 1) * TRAVELMIND_RERANK_TEMPERATURE_STEP),
                )
            else:
                temperature = TRAVELMIND_TEMPERATURE
            print(f"{label} 第 {attempt} 次max_tokens: {max_output_tokens}", flush=True)
            print(f"{label} 第 {attempt} 次temperature: {temperature:.2f}", flush=True)
            try:
                travelmind_response = self._run_agent_stateless(
                    agent,
                    travelmind_query,
                    max_tokens=max_output_tokens,
                    temperature=temperature,
                    timeout=TRAVELMIND_REQUEST_TIMEOUT,
                )
            except Exception as error:
                call_failures += 1
                self._log_timer(f"{label} 第 {attempt} 次LLM调用失败耗时", call_started_at)
                last_error = error
                failure = build_failure_row(
                    label=label,
                    attempt=attempt,
                    max_attempts=max_attempts,
                    request=request,
                    travelmind_query=travelmind_query,
                    response="",
                    error=error,
                    preference_reason="travelmind_llm_call_failed",
                )
                failures.append(failure)
                append_jsonl(TRAVELMIND_FAILURE_LOG, failure)
                print(f"⚠️  {label} 第 {attempt} 次调用失败: {error}", flush=True)

                # 400 内容风控类错误通常是服务商直接拒绝同一份输入，
                # 干净重试也不会改变结果，立刻切到下一个兜底模型更合理。
                if is_non_retryable_llm_error(error):
                    print(f"⚠️  {label} 遇到非重试型接口拒绝，停止当前模型重试", flush=True)
                    break

                # 本地个性化 TravelMind 如果服务不可用，连续重试只会拖慢线上响应。
                # 解析失败仍然走 max_attempts；纯接口调用失败按更小阈值快速切兜底。
                if max_call_failures is not None and call_failures >= max_call_failures:
                    print(
                        f"⚠️  {label} LLM调用失败已达 {call_failures} 次，停止当前模型重试",
                        flush=True,
                    )
                    break
                continue

            self._log_timer(f"{label} 第 {attempt} 次LLM调用", call_started_at)
            print(f"{label} 输出: {travelmind_response[:300]}...\n", flush=True)

            parse_started_at = time.perf_counter()
            try:
                trip_plan = self._parse_response(
                    travelmind_response,
                    request,
                    use_fallback=False,
                    travelmind_context=travelmind_context,
                )
                self._log_timer(f"{label} 第 {attempt} 次解析校验", parse_started_at)
                if not rerank_enabled:
                    print(f"✅ {label} 第 {attempt} 次输出解析成功")
                    if failures:
                        log_preference_candidates(travelmind_query, request, trip_plan, failures, label)
                    return trip_plan

                valid_candidates.append((attempt, trip_plan))
                print(
                    f"✅ {label} 第 {attempt} 次输出解析成功，"
                    f"候选收集 {len(valid_candidates)}/{target_candidate_count}",
                    flush=True,
                )
                if len(valid_candidates) >= target_candidate_count:
                    break
            except Exception as error:
                self._log_timer(f"{label} 第 {attempt} 次解析校验失败耗时", parse_started_at)
                last_error = error
                failure = build_failure_row(
                    label=label,
                    attempt=attempt,
                    max_attempts=max_attempts,
                    request=request,
                    travelmind_query=travelmind_query,
                    response=travelmind_response,
                    error=error,
                )
                failures.append(failure)
                append_jsonl(TRAVELMIND_FAILURE_LOG, failure)
                print(f"⚠️  {label} 第 {attempt} 次输出解析失败: {error}")

        if valid_candidates:
            ranked_candidates = rerank_trip_plan_candidates(valid_candidates, request, travelmind_context)
            selected_candidate = ranked_candidates[0]
            self._print_rerank_result(label, ranked_candidates)
            if failures:
                log_preference_candidates(
                    travelmind_query,
                    request,
                    selected_candidate.trip_plan,
                    failures,
                    label,
                )
            return selected_candidate.trip_plan

        raise TravelMindGenerationError(
            f"{label} 未成功生成合法 TripPlan JSON: {last_error}",
            failures=failures,
        )

    def _print_rerank_result(self, label: str, ranked_candidates: List[RerankCandidate]) -> None:
        """打印 rerank 结果摘要，便于线上观察。"""
        if not ranked_candidates:
            return

        best = ranked_candidates[0]
        print(
            f"🏁 {label} rerank选中 attempt={best.attempt}, score={best.score:.2f}, "
            f"recomputed_total={best.metrics.get('recomputed_budget_total')}",
            flush=True,
        )
        for row in ranked_candidates:
            metrics = row.metrics
            print(
                "   "
                f"attempt={row.attempt} score={row.score:.2f} "
                f"fit={metrics.get('recomputed_budget_fit_ok')} "
                f"hard_budget={metrics.get('budget_hard_constraint_ok')} "
                f"meal_div={metrics.get('meal_diversity_ok')} "
                f"meal_ground={metrics.get('meal_grounding_rate')} "
                f"attr_ground={metrics.get('attraction_grounding_rate')}",
                flush=True,
            )

    def _parse_response(
        self,
        response: str,
        request: TripRequest,
        use_fallback: bool = True,
        travelmind_context: Optional[Dict[str, Any]] = None,
    ) -> TripPlan:
        """
        解析Agent响应

        Args:
            response: Agent响应文本
            request: 原始请求

        Returns:
            旅行计划
        """
        try:
            data = extract_json_object(response)

            # 转换为TripPlan对象
            trip_plan = TripPlan(**data)
            if travelmind_context:
                enrich_trip_plan_poi_details(trip_plan, travelmind_context)
            validate_trip_plan_shape(trip_plan, request, travelmind_context)

            return trip_plan

        except Exception as e:
            if not use_fallback:
                raise
            print(f"⚠️  解析响应失败: {str(e)}")
            print(f"   将使用备用方案生成计划")
            return create_fallback_plan(request)


# 全局多智能体系统实例
_multi_agent_travelmind = None


def get_travelmind_agent() -> TravelMindAgent:
    """获取TravelMind 个性化旅行规划 Agent实例(单例模式)"""
    global _multi_agent_travelmind

    if _multi_agent_travelmind is None:
        _multi_agent_travelmind = TravelMindAgent()

    return _multi_agent_travelmind






