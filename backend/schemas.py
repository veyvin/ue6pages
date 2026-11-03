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
    usage_doc: bool = False  # 是否已有 AI 生成的《使用方法》文档


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
    usage_doc: bool = False  # 是否已有 AI 生成的《使用方法》文档


# ---------- 列表接口 ----------
class PluginSummary(BaseModel):
    slug: str
    name: str
    category: str
    version_name: str
    description: str
    path: str
    usage_doc: bool = False


class ModuleSummary(BaseModel):
    slug: str
    name: str
    type: str
    path: str
    usage_doc: bool = False


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


class AiBatchRequest(BaseModel):
    """批量生成《使用方法》文档的入参（POST /api/ai/batch）。"""
    kind: str = Field("all", pattern="^(plugin|module|all)$")
    slugs: list[str] = Field(
        default_factory=list, description="只生成这些 slug；为空表示全部"
    )
    limit: int = Field(0, ge=0, description="最多生成多少条，0 = 不限（试跑用）")
    overwrite: bool = Field(False, description="True 时覆盖已有文档，False 时跳过已有的")


class AiChatResponse(BaseModel):
    reply: str
    model: str
    cached: bool = False
