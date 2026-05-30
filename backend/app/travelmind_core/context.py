"""TravelMindContext 构造逻辑。"""

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict

from ..models.schemas import TripRequest
from .amap import AmapTravelMindClient
from .compact import compact_for_travelmind as compact_travelmind_context
from .dates import trip_date_strings, unknown_weather_row
from .debug import (
    TRAVELMIND_CONTEXT_PRINT_LIMIT,
    print_summary as print_context_summary,
    print_visualization as print_context_visualization,
)
from .high_end_candidates import (
    rank_food_for_budget_context,
    rank_hotels_for_budget_context,
    summarize_high_end_candidates,
    strip_budget_context_metadata,
)
from .local_poi_table import local_high_end_pois, should_use_high_end_local_pois
from .pois import (
    annotate_food_pois,
    build_budget_upgrade_keywords,
    build_food_budget_supplement_keywords,
    build_food_keyword_groups,
    build_hotel_keyword_groups,
    build_poi_keywords,
    filter_food_by_constraints,
    merge_poi_buckets,
)
from .policy import build_empty_context
from .pricing import with_hotel_cost_hints, with_meal_cost_hints, with_ticket_price_hints
from .weather import align_trip_weather, normalize_weather


TRAVELMIND_CONTEXT_POI_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_POI_LIMIT", "20"))
TRAVELMIND_CONTEXT_CLASSIC_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_CLASSIC_LIMIT", "12"))
TRAVELMIND_CONTEXT_PREFERENCE_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_PREFERENCE_LIMIT", "16"))
TRAVELMIND_CONTEXT_HOTEL_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_HOTEL_LIMIT", "10"))
TRAVELMIND_CONTEXT_FOOD_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_FOOD_LIMIT", "40"))
TRAVELMIND_CONTEXT_FOOD_GROUP_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_FOOD_GROUP_LIMIT", "8"))
TRAVELMIND_CONTEXT_FOOD_BREAKFAST_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_FOOD_BREAKFAST_LIMIT", "8"))
TRAVELMIND_CONTEXT_FOOD_BASE_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_FOOD_BASE_LIMIT", "20"))
TRAVELMIND_CONTEXT_FOOD_UPGRADE_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_FOOD_UPGRADE_LIMIT", "20"))
TRAVELMIND_CONTEXT_FOOD_SUPPLEMENT_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_FOOD_SUPPLEMENT_LIMIT", "20"))
TRAVELMIND_CONTEXT_HOTEL_UPGRADE_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_HOTEL_UPGRADE_LIMIT", "6"))
TRAVELMIND_CONTEXT_ATTRACTION_UPGRADE_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_ATTRACTION_UPGRADE_LIMIT", "10"))
TRAVELMIND_CONTEXT_EXPERIENCE_UPGRADE_LIMIT = int(os.getenv("TRAVELMIND_CONTEXT_EXPERIENCE_UPGRADE_LIMIT", "8"))
FOOD_CONTEXT_MIN_BY_BUDGET_LEVEL = {
    "comfortable": 80,
    "premium": 120,
    "luxury": 180,
}

class TravelMindContextBuilder:
    """构造最终 TravelMind 使用的结构化上下文。"""

    def __init__(self, amap_api_key: str):
        self.amap_client = AmapTravelMindClient(amap_api_key)

    def collect(self, request: TripRequest) -> Dict[str, Any]:
        """并行获取 TravelMind 所需的结构化上下文。"""
        context = self.empty_context(request)
        jobs = {
            "attractions": self._collect_attraction_snapshot,
            "weather": self._collect_weather_snapshot,
            "hotels": self._collect_hotel_snapshot,
        }

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(func, request): name for name, func in jobs.items()}
            for future in as_completed(futures):
                name = futures[future]
                try:
                    result = future.result()
                    context["tool_snapshot"].update(result.get("tool_snapshot", {}))
                    context["tool_snapshot"]["tool_status"][name] = result.get(
                        "status",
                        self._tool_status(True, "ok"),
                    )
                except Exception as exc:
                    context["tool_snapshot"]["tool_status"][name] = self._tool_status(False, str(exc))
                    print(f"⚠️  {name}工具快照获取失败: {exc}")

        # 当前主线不生成粗糙路线 hint：直接把酒店/景点/餐饮候选的
        # address、district 和 location 交给 TravelMind 判断动线。
        # 真正的路线时间增强后续应接入地图路线 API，并配套缓存和校验。
        context["tool_snapshot"]["route_hints"] = []
        context["tool_snapshot"]["tool_status"]["routes"] = self._tool_status(
            True,
            "disabled; TravelMind uses poi address/district/location",
        )
        return context

    def empty_context(self, request: TripRequest) -> Dict[str, Any]:
        """创建空 TravelMindContext，工具失败时也保持输入协议稳定。"""
        return build_empty_context(request)

    def print_summary(self, travelmind_context: Dict[str, Any]) -> None:
        """打印结构化工具快照摘要。"""
        print_context_summary(travelmind_context)

    def print_visualization(self, travelmind_context: Dict[str, Any], limit: int = TRAVELMIND_CONTEXT_PRINT_LIMIT) -> None:
        """在命令行打印步骤1工具快照明细，便于直接审查。"""
        print_context_visualization(travelmind_context, limit)

    def compact_for_travelmind(self, travelmind_context: Dict[str, Any]) -> Dict[str, Any]:
        """把原始工具快照压缩成模型真正需要看的 TravelMind 输入。

        原始 travelmind_context 仍用于日志、命令行审查和后置校验；
        这里单独裁剪给 LLM 的版本，避免 POI id/typecode/photo_count 等字段
        把上下文撑得过长，也减少外部模型服务商的误杀概率。
        """
        return compact_travelmind_context(travelmind_context)

    def _collect_attraction_snapshot(self, request: TripRequest) -> Dict[str, Any]:
        """搜索景点、体验和餐饮候选。"""
        classic_keywords = build_poi_keywords(request, "classic")
        preference_keywords = build_poi_keywords(request, "preference")
        experience_keywords = build_poi_keywords(request, "experience")
        food_keyword_groups = build_food_keyword_groups(request)
        budget_level = request.budget_constraint.budget_level or ""
        use_local_high_end_scenic = should_use_high_end_local_pois(budget_level, "scenic")
        use_local_high_end_experience = should_use_high_end_local_pois(budget_level, "experience")
        use_local_high_end_food = should_use_high_end_local_pois(budget_level, "food")

        classic_pois = self.amap_client.search_classic_pois(
            request.city,
            classic_keywords,
            TRAVELMIND_CONTEXT_CLASSIC_LIMIT,
        )
        if not classic_pois:
            classic_pois = self.amap_client.search_keywords(
                request.city,
                classic_keywords,
                source_role="scenic",
                limit=TRAVELMIND_CONTEXT_CLASSIC_LIMIT,
                source_bucket="classic",
            )
        classic_pois = with_ticket_price_hints(classic_pois, request)

        preference_pois = self.amap_client.search_keywords(
            request.city,
            preference_keywords,
            source_role="scenic",
            limit=TRAVELMIND_CONTEXT_PREFERENCE_LIMIT,
            source_bucket="preference",
        )
        preference_pois = with_ticket_price_hints(preference_pois, request)
        attraction_upgrade_pois = []
        attraction_upgrade_keywords = build_budget_upgrade_keywords(request, "scenic")
        if attraction_upgrade_keywords:
            attraction_upgrade_pois = self.amap_client.search_keywords(
                request.city,
                attraction_upgrade_keywords,
                source_role="scenic",
                limit=TRAVELMIND_CONTEXT_ATTRACTION_UPGRADE_LIMIT,
                source_bucket="attraction_budget_upgrade",
            )
            attraction_upgrade_pois = with_ticket_price_hints(attraction_upgrade_pois, request)
        local_scenic_pois = []
        if use_local_high_end_scenic:
            local_scenic_pois = with_ticket_price_hints(
                local_high_end_pois(request.city, "scenic", "attraction_budget_upgrade"),
                request,
            )
        scenic_pois = merge_poi_buckets(
            [local_scenic_pois, attraction_upgrade_pois, classic_pois, preference_pois],
            TRAVELMIND_CONTEXT_POI_LIMIT,
        )
        experience_pois = self.amap_client.search_keywords(
            request.city,
            experience_keywords,
            source_role="experience",
            limit=TRAVELMIND_CONTEXT_POI_LIMIT,
            source_bucket="experience",
        )
        experience_upgrade_keywords = build_budget_upgrade_keywords(request, "experience")
        if experience_upgrade_keywords:
            experience_upgrade_pois = self.amap_client.search_keywords(
                request.city,
                experience_upgrade_keywords,
                source_role="experience",
                limit=TRAVELMIND_CONTEXT_EXPERIENCE_UPGRADE_LIMIT,
                source_bucket="experience_budget_upgrade",
            )
            experience_pois = merge_poi_buckets(
                [experience_upgrade_pois, experience_pois],
                TRAVELMIND_CONTEXT_POI_LIMIT,
            )
        if use_local_high_end_experience:
            experience_pois = merge_poi_buckets(
                [
                    local_high_end_pois(request.city, "experience", "experience_budget_upgrade"),
                    experience_pois,
                ],
                TRAVELMIND_CONTEXT_POI_LIMIT,
            )
        experience_pois = with_ticket_price_hints(experience_pois, request)
        scenic_pois = strip_budget_context_metadata(scenic_pois)
        experience_pois = strip_budget_context_metadata(experience_pois)
        food_buckets = []
        if use_local_high_end_food:
            food_buckets.append(local_high_end_pois(request.city, "food", "food_budget_upgrade"))
        for group in food_keyword_groups:
            if group["bucket"] == "food_base":
                food_limit = TRAVELMIND_CONTEXT_FOOD_BASE_LIMIT
            elif group["bucket"] == "food_breakfast":
                food_limit = TRAVELMIND_CONTEXT_FOOD_BREAKFAST_LIMIT
            elif group["bucket"] == "food_budget_upgrade":
                food_limit = TRAVELMIND_CONTEXT_FOOD_UPGRADE_LIMIT
            else:
                food_limit = TRAVELMIND_CONTEXT_FOOD_GROUP_LIMIT
            food_buckets.append(
                self.amap_client.search_keywords(
                    request.city,
                    group["keywords"],
                    source_role="food",
                    limit=food_limit,
                    require_location=False,
                    source_bucket=group["bucket"],
                )
            )
        food_pois = merge_poi_buckets(food_buckets, TRAVELMIND_CONTEXT_FOOD_LIMIT)
        food_pois = filter_food_by_constraints(food_pois, request)
        food_pois = annotate_food_pois(food_pois, request)
        food_pois = with_meal_cost_hints(food_pois, request)
        food_pois = self._supplement_food_budget_candidates_if_needed(request, food_pois)
        food_pois = rank_food_for_budget_context(food_pois, request, TRAVELMIND_CONTEXT_FOOD_LIMIT)
        food_budget_summary = summarize_high_end_candidates(food_pois, "meal_cost_hint")
        food_pois = strip_budget_context_metadata(food_pois)

        return {
            "tool_snapshot": {
                "classic_pois": classic_pois,
                "preference_pois": preference_pois,
                "scenic_pois": scenic_pois,
                "experience_pois": experience_pois,
                "food_pois": food_pois,
                "food_query_groups": food_keyword_groups,
            },
            "status": self._tool_status(
                bool(classic_pois or preference_pois or experience_pois),
                (
                    f"classic={len(classic_pois)}, preference={len(preference_pois)}, "
                    f"scenic={len(scenic_pois)}, experience={len(experience_pois)}, "
                    f"food={len(food_pois)}, food_high_end_verified={food_budget_summary['high_end_verified']}, "
                    f"food_high_end_estimated={food_budget_summary['high_end_estimated']}"
                ),
            ),
        }

    def _collect_hotel_snapshot(self, request: TripRequest) -> Dict[str, Any]:
        """搜索酒店候选。"""
        hotel_buckets = []
        if should_use_high_end_local_pois(request.budget_constraint.budget_level or "", "hotel"):
            hotel_buckets.append(local_high_end_pois(request.city, "hotel", "hotel_budget_upgrade"))
        for group in build_hotel_keyword_groups(request):
            hotel_limit = (
                TRAVELMIND_CONTEXT_HOTEL_UPGRADE_LIMIT
                if group["bucket"] == "hotel_budget_upgrade"
                else TRAVELMIND_CONTEXT_HOTEL_LIMIT
            )
            hotel_buckets.append(
                self.amap_client.search_keywords(
                    request.city,
                    group["keywords"],
                    source_role="hotel",
                    limit=hotel_limit,
                    require_location=False,
                    source_bucket=group["bucket"],
                )
            )
        hotels = merge_poi_buckets(hotel_buckets, TRAVELMIND_CONTEXT_HOTEL_LIMIT)
        hotels = with_hotel_cost_hints(hotels, request)
        hotels = rank_hotels_for_budget_context(hotels, request, TRAVELMIND_CONTEXT_HOTEL_LIMIT)
        hotel_budget_summary = summarize_high_end_candidates(hotels, "estimated_cost_hint")
        hotels = strip_budget_context_metadata(hotels)

        return {
            "tool_snapshot": {"hotel_pois": hotels},
            "status": self._tool_status(
                bool(hotels),
                (
                    f"hotels={len(hotels)}, hotel_high_end_verified={hotel_budget_summary['high_end_verified']}, "
                    f"hotel_high_end_estimated={hotel_budget_summary['high_end_estimated']}"
                ),
            ),
        }

    def _collect_weather_snapshot(self, request: TripRequest) -> Dict[str, Any]:
        """查询天气，并把短期预报对齐到真实行程日期。"""
        raw = self.amap_client.get("/weather/weatherInfo", {"city": request.city, "extensions": "all"})
        available_weather = normalize_weather(raw)
        trip_weather = align_trip_weather(request, available_weather)
        covered = [item for item in trip_weather if item.get("source") == "amap_forecast"]

        return {
            "tool_snapshot": {
                "available_weather": available_weather,
                "trip_weather": trip_weather,
            },
            "status": self._tool_status(
                bool(available_weather),
                f"available={len(available_weather)}, covered_trip_days={len(covered)}/{request.travel_days}",
            ),
        }

    def _supplement_food_budget_candidates_if_needed(
        self,
        request: TripRequest,
        food_pois: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """高预算午晚餐候选不足时，用更宽的正餐关键词二次补召回。"""
        budget_level = request.budget_constraint.budget_level or ""
        min_cost = FOOD_CONTEXT_MIN_BY_BUDGET_LEVEL.get(budget_level)
        if min_cost is None:
            return food_pois

        target_count = max(request.travel_days * 2, 6)
        if self._count_budget_meal_candidates(food_pois, min_cost) >= target_count:
            return food_pois

        keywords = build_food_budget_supplement_keywords(request)
        if not keywords:
            return food_pois

        supplemental = self.amap_client.search_keywords(
            request.city,
            keywords,
            source_role="food",
            limit=TRAVELMIND_CONTEXT_FOOD_SUPPLEMENT_LIMIT,
            require_location=False,
            source_bucket="food_budget_upgrade",
        )
        supplemental = filter_food_by_constraints(supplemental, request)
        supplemental = annotate_food_pois(supplemental, request)
        supplemental = with_meal_cost_hints(supplemental, request)
        return merge_poi_buckets(
            [food_pois, supplemental],
            max(TRAVELMIND_CONTEXT_FOOD_LIMIT, len(food_pois) + len(supplemental)),
        )

    def _count_budget_meal_candidates(self, rows: list[dict[str, Any]], min_cost: int) -> int:
        """统计满足当前预算档的 lunch/dinner 候选数。"""
        count = 0
        for row in rows:
            if row.get("source_bucket") == "food_breakfast":
                continue
            roles = {str(role or "").strip().lower() for role in row.get("meal_roles") or []}
            if roles == {"breakfast"}:
                continue
            try:
                cost = int(float(row.get("meal_cost_hint") or 0))
            except (TypeError, ValueError):
                cost = 0
            if cost >= min_cost:
                count += 1
        return count

    def _tool_status(self, ok: bool, message: str) -> Dict[str, Any]:
        """统一工具状态格式，方便 TravelMind 和日志同时读取。"""
        return {"ok": ok, "message": message}




