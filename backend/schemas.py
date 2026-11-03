"""API 入参 / 出参的 Pydantic Schema。"""
from __future__ import annotations

from pydantic import BaseModel, Field


# ---------- Item 基础 ----------
class PluginModule(BaseModel):
    name: str
    type: str = "Runtime"   # Runtime / Editor / Developer


class PluginInfo(BaseModel):
    slug: str
    name: str
    version: str = ""
    version_name: str = ""
    category: str = ""
    author: str = ""
    engine_version: str = ""
    description: str = ""
    path: str               # 相对 engine_root，例如 Plugins/Rendering/Lumen
    modules: list[PluginModule] = Field(default_factory=list)


class ModuleInfo(BaseModel):
    slug: str
    name: str
    type: str = "Runtime"
    path: str
    description: str = ""
    base: str = "ModuleRules"
    public_deps: list[str] = Field(default_factory=list)
    private_deps: list[str] = Field(default_factory=list)
    platform: str = ""       # Win64 / Linux / Mac / ""


# ---------- 列表接口 ----------
class PluginSummary(BaseModel):
    slug: str
    name: str
    category: str
    version_name: str
    description: str
    path: str


class ModuleSummary(BaseModel):
    slug: str
    name: str
    type: str
    path: str


class Stats(BaseModel):
    total_plugins: int
    total_modules: int
    categories: list[str]
    engine_version: str = ""


# ---------- AI ----------
class AiChatRequest(BaseModel):
    kind: str = Field(..., pattern="^(plugin|module)$")
    slug: str
    message: str
    history: list[tuple[str, str]] = Field(
        default_factory=list, description="[(role, text), ...]"
    )


class AiChatResponse(BaseModel):
    reply: str
    model: str
    cached: bool = False
