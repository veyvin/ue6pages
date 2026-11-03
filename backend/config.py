"""后端配置加载 — YAML + 环境变量覆盖。"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class AIConfig(BaseModel):
    enabled: bool = True
    model: str = "gpt-4o-mini"
    endpoint: str = "https://api.openai.com/v1"
    api_key: str = ""
    timeout: int = 60
    stream_chunk_size: int = 128


class ScanConfig(BaseModel):
    plugins_dir: str = "Engine/Plugins"
    source_dir: str = "Engine/Source"
    parallel: bool = True


class SiteConfig(BaseModel):
    docs_root: str = "/tmp/ghpages"
    rebuild_on_start: bool = False


class CorsConfig(BaseModel):
    origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])


class AppConfig(BaseModel):
    engine_root: str = "/tmp/mock-engine"
    ai: AIConfig = Field(default_factory=AIConfig)
    scan: ScanConfig = Field(default_factory=ScanConfig)
    site: SiteConfig = Field(default_factory=SiteConfig)
    cors: CorsConfig = Field(default_factory=CorsConfig)

    # 环境变量覆盖：UE_AI_API_KEY 优先
    def __init__(self, **data: Any):
        super().__init__(**data)
        env_key = os.environ.get("UE_AI_API_KEY")
        if env_key:
            self.ai.api_key = env_key


# ---- 加载 ----
_CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config(path: Path | str | None = None) -> AppConfig:
    p = Path(path) if path else _CONFIG_PATH
    data: dict = {}
    if p.exists():
        with open(p, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    return AppConfig(**data)


# 全局单例，启动时载入；--reload 模式下每次 import 都重新读 yaml，天然热更新
CONFIG = load_config()
