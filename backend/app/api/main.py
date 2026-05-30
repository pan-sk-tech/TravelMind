"""TravelMind FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..config import get_settings, print_config, validate_config
from .routes import map as map_routes
from .routes import poi, travelmind


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "TravelMind 个性化旅行规划 Agent API，基于 Hello-Agents 框架二次开发，"
        "支持需求采集、景点知识检索、天气工具、预算估算和行程合理性检查。"
    ),
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_cors_origins_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(travelmind.router, prefix="/api")
app.include_router(poi.router, prefix="/api")
app.include_router(map_routes.router, prefix="/api")


@app.on_event("startup")
async def startup_event():
    print("\n" + "=" * 60)
    print(f"TravelMind Agent v{settings.app_version}")
    print("=" * 60)
    print_config()

    try:
        validate_config()
        print("\n配置验证通过")
    except ValueError as error:
        print(f"\n配置验证失败:\n{error}")
        print("\n请检查 backend/.env 中的 AMAP_API_KEY、LLM_API_KEY、LLM_BASE_URL 和 LLM_MODEL_ID。")
        raise

    print("\n" + "=" * 60)
    print(f"API Docs: http://localhost:{settings.port}/docs")
    print(f"ReDoc: http://localhost:{settings.port}/redoc")
    print("=" * 60 + "\n")


@app.on_event("shutdown")
async def shutdown_event():
    print("\nTravelMind is shutting down...\n")


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.api.main:app",
        host=settings.host,
        port=settings.port,
        reload=False,
    )



