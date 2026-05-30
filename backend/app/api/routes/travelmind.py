"""TravelMind trip planning API routes."""

from fastapi import APIRouter, HTTPException
from starlette.concurrency import run_in_threadpool

from ...agents.travelmind_agent import get_travelmind_agent
from ...config import get_settings
from ...memory.preference_memory import get_preference_memory
from ...models.schemas import TripPlanResponse, TripRequest
from ...rag.attraction_knowledge import get_attraction_knowledge_base
from ...travelmind_core.output import create_fallback_plan


router = APIRouter(prefix="/travelmind", tags=["TravelMind 行程规划"])


def _enrich_request_with_travelmind_context(request: TripRequest) -> TripRequest:
    """Attach lightweight RAG and memory hints to the free-text context."""
    memory = get_preference_memory()
    knowledge_base = get_attraction_knowledge_base()

    recalled_memory = memory.recall("default", request.city)
    rag_hits = knowledge_base.retrieve(request.city, request.preferences, limit=4)

    hint_blocks = []
    if recalled_memory:
        hint_blocks.append("TravelMind偏好记忆:\n" + recalled_memory)
    if rag_hits:
        lines = []
        for hit in rag_hits:
            lines.append(
                "- {name}: {summary}; 开放时间: {open_time}; 门票: {ticket_price}; "
                "建议游玩: {duration}; 交通建议: {transport}".format(**hit)
            )
        hint_blocks.append("TravelMind城市景点RAG召回:\n" + "\n".join(lines))

    if hint_blocks:
        user_text = request.free_text_input or ""
        request.free_text_input = user_text + "\n\n" + "\n\n".join(hint_blocks)

    return request


@router.post(
    "/plan",
    response_model=TripPlanResponse,
    summary="生成 TravelMind 个性化旅行计划",
    description="根据城市、天数、预算、兴趣偏好、交通方式和历史偏好记忆生成旅行计划。",
)
async def plan_trip(request: TripRequest):
    try:
        print("\n" + "=" * 60)
        print("TravelMind received a planning request")
        print(f"City: {request.city}")
        print(f"Dates: {request.start_date} - {request.end_date}")
        print(f"Days: {request.travel_days}")
        print("=" * 60 + "\n")

        enriched_request = _enrich_request_with_travelmind_context(request)
        if get_settings().travelmind_demo_mode:
            trip_plan = create_fallback_plan(enriched_request)
            return TripPlanResponse(
                success=True,
                message="TravelMind 演示模式已启用：未调用千问 API，已返回本地示例行程。",
                data=trip_plan,
            )

        agent = get_travelmind_agent()
        trip_plan = await run_in_threadpool(agent.plan_trip, enriched_request)

        await run_in_threadpool(get_preference_memory().remember, "default", enriched_request, trip_plan)

        generation_status = getattr(agent, "last_generation_status", "unknown")
        generation_message = (
            getattr(agent, "last_generation_message", "")
            or "TravelMind 行程生成完成"
        )

        if generation_status == "fallback_success":
            print(f"TravelMind fallback response: {generation_message}\n")
        else:
            print(f"TravelMind response ready: {generation_message}\n")

        return TripPlanResponse(
            success=True,
            message=generation_message,
            data=trip_plan,
        )

    except Exception as error:
        print(f"TravelMind 生成失败: {error}")
        import traceback

        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"TravelMind 生成失败: {error}",
        )


@router.get(
    "/health",
    summary="TravelMind Agent 健康检查",
    description="检查 TravelMind 行程规划服务是否可用。",
)
async def health_check():
    try:
        if get_settings().travelmind_demo_mode:
            return {
                "status": "healthy",
                "service": "travelmind-agent",
                "agent_class": "DemoModeFallback",
                "demo_mode": True,
            }

        agent = get_travelmind_agent()
        return {
            "status": "healthy",
            "service": "travelmind-agent",
            "agent_class": agent.__class__.__name__,
        }
    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail=f"TravelMind 服务不可用: {error}",
        )



