"""后端配置加载 / 保存 — YAML + 环境变量覆盖。"""
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
    workers: int = Field(default=4, ge=1, le=32)  # 批量生成《使用方法》时的并发数


class ScanConfig(BaseModel):
    plugins_dir: str = "Engine/Plugins"
    source_dir: str = "Engine/Source"
    parallel: bool = True


class SiteConfig(BaseModel):
    usage_docs_root: str = "usage_docs"  # AI 生成的《使用方法》文档目录（相对 backend/ 或绝对路径）
    usage_fb_root: str = "static/assets" # usage.fb / usage.bin，由 /assets 静态托管
    frontend_dist: str = "../frontend/dist"  # 前端构建产物目录，存在即由后端托管


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
_FILE_HEADER = (
    "# === UE Plugin Docs 后端配置 ===\n"
    "# 由前端「设置」页保存生成，也可以手动编辑\n\n"
)


def config_path() -> Path:
    return _CONFIG_PATH


def load_config(path: Path | str | None = None) -> AppConfig:
    p = Path(path) if path else _CONFIG_PATH
    data: dict = {}
    if p.exists():
        with open(p, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    return AppConfig(**data)


def read_raw() -> dict:
    """读取 config.yaml 原始内容（不含环境变量覆盖）。"""
    if not _CONFIG_PATH.exists():
        return {}
    with open(_CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def mask_secret(value: str) -> str:
    if not value:
        return ""
    return "*" * 8 + value[-4:] if len(value) > 4 else "*" * 8


def public_config() -> dict:
    """返回给前端的配置，api_key 做掩码处理。"""
    data = CONFIG.model_dump()
    data["ai"]["api_key"] = mask_secret(CONFIG.ai.api_key)
    return data


def save_config(payload: dict) -> None:
    """校验并写入 config.yaml，同时热更新内存中的 CONFIG。

    api_key 含 `*` 说明是前端回传的掩码值，此时保留 yaml 里原有的 key，
    避免把密钥覆盖掉。校验失败时抛出 pydantic.ValidationError，文件和内存都不变。
    """
    raw = read_raw()
    ai_in = dict(payload.get("ai") or {})
    key = str(ai_in.get("api_key") or "")
    if "*" in key:
        key = str((raw.get("ai") or {}).get("api_key") or "")
    ai_in["api_key"] = key
    incoming = {**payload, "ai": ai_in}

    fresh = AppConfig(**incoming)  # 校验，并带上环境变量覆盖（仅用于内存）

    to_file = fresh.model_dump()
    to_file["ai"]["api_key"] = key  # 文件里只写用户输入的 key，不写环境变量的值
    _CONFIG_PATH.write_text(
        _FILE_HEADER + yaml.safe_dump(to_file, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    for name in AppConfig.model_fields:
        setattr(CONFIG, name, getattr(fresh, name))


# 全局单例，启动时载入；save_config 会原地更新它
CONFIG = load_config()