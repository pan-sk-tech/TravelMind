"""Application configuration."""

import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BACKEND_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load both common .env locations. backend/.env wins when both exist.
load_dotenv(PROJECT_ROOT / ".env", override=False)
load_dotenv(BACKEND_DIR / ".env", override=True)

# Keep compatibility with an adjacent HelloAgents checkout if present.
helloagents_env = PROJECT_ROOT.parent / "HelloAgents" / ".env"
if helloagents_env.exists():
    load_dotenv(helloagents_env, override=False)


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables."""

    app_name: str = "TravelMind 个性化旅行规划 Agent"
    app_version: str = "1.0.0"
    debug: bool = False

    host: str = "0.0.0.0"
    port: int = 7000
    cors_origins: str = (
        "http://localhost:5173,http://localhost:3000,"
        "http://127.0.0.1:5173,http://127.0.0.1:3000"
    )

    amap_api_key: str = ""

    unsplash_access_key: str = ""
    unsplash_secret_key: str = ""

    # OpenAI-compatible LLM config. For Qwen/DashScope, put the DashScope
    # compatible-mode values in backend/.env.
    openai_api_key: str = ""
    openai_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    openai_model: str = "qwen-plus"

    use_personalized_travelmind: bool = False
    personalized_llm_api_key: str = ""
    personalized_llm_base_url: str = ""
    personalized_llm_model: str = ""
    personalized_llm_provider: str = "openai"

    log_level: str = "INFO"
    travelmind_demo_mode: bool = False

    class Config:
        env_file = (PROJECT_ROOT / ".env", BACKEND_DIR / ".env")
        case_sensitive = False
        extra = "ignore"

    def get_cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]


settings = Settings()


def effective_llm_api_key() -> str:
    return os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or settings.openai_api_key


def effective_llm_base_url() -> str:
    return os.getenv("LLM_BASE_URL") or os.getenv("OPENAI_BASE_URL") or settings.openai_base_url


def effective_llm_model() -> str:
    return os.getenv("LLM_MODEL_ID") or os.getenv("OPENAI_MODEL") or settings.openai_model


def sync_llm_env_from_settings() -> None:
    """Expose Settings values through env vars expected by HelloAgentsLLM."""
    api_key = effective_llm_api_key()
    base_url = effective_llm_base_url()
    model = effective_llm_model()

    aliases = {
        "LLM_API_KEY": api_key,
        "OPENAI_API_KEY": api_key,
        "LLM_BASE_URL": base_url,
        "OPENAI_BASE_URL": base_url,
        "LLM_MODEL_ID": model,
        "OPENAI_MODEL": model,
    }
    for key, value in aliases.items():
        if value and not os.getenv(key):
            os.environ[key] = value


sync_llm_env_from_settings()


def get_settings() -> Settings:
    return settings


def validate_config() -> bool:
    errors = []
    warnings = []

    if not settings.amap_api_key:
        errors.append("AMAP_API_KEY未配置")

    if not effective_llm_api_key():
        warnings.append("LLM_API_KEY或OPENAI_API_KEY未配置, LLM功能可能无法使用")

    if errors:
        error_msg = "配置错误:\n" + "\n".join(f"  - {error}" for error in errors)
        raise ValueError(error_msg)

    if warnings:
        print("\n⚠️  配置警告:")
        for warning in warnings:
            print(f"  - {warning}")

    return True


def print_config() -> None:
    """Print current config without exposing secrets."""
    print(f"应用名称: {settings.app_name}")
    print(f"版本: {settings.app_version}")
    print(f"服务器: {settings.host}:{settings.port}")
    print(f"高德地图API Key: {'已配置' if settings.amap_api_key else '未配置'}")
    print(f"LLM API Key: {'已配置' if effective_llm_api_key() else '未配置'}")
    print(f"LLM Base URL: {effective_llm_base_url()}")
    print(f"LLM Model: {effective_llm_model()}")
    print(f"TravelMind Demo Mode: {'启用' if settings.travelmind_demo_mode else '关闭'}")
    print(f"Personalized TravelMind: {'启用' if settings.use_personalized_travelmind else '关闭'}")
    if settings.use_personalized_travelmind:
        personalized_model = os.getenv("PERSONALIZED_LLM_MODEL_ID") or settings.personalized_llm_model
        print(f"Personalized TravelMind Base URL: {settings.personalized_llm_base_url or '未配置'}")
        print(f"Personalized TravelMind Model: {personalized_model or '未配置'}")
    print(f"日志级别: {settings.log_level}")



