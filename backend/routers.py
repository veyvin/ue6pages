"""路由层：/api/plugins · /api/modules · /api/ai/stream"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .ai_service import stream_chat
from .scanner import scan_all, invalidate_cache
from .schemas import (
    PluginInfo, PluginSummary, ModuleInfo, ModuleSummary,
    Stats, AiChatRequest,
)

router = APIRouter()


# ---------- 列表 + 详情 ----------
@router.get("/stats", response_model=Stats)
def get_stats() -> Stats:
    plugins, modules = scan_all()
    cats = sorted({p.category for p in plugins if p.category})
    eng = next((p.engine_version for p in plugins if p.engine_version), "")
    return Stats(
        total_plugins=len(plugins),
        total_modules=len(modules),
        categories=cats,
        engine_version=eng,
    )


@router.get("/plugins", response_model=list[PluginSummary])
def list_plugins(category: str | None = None, q: str | None = None) -> list[PluginSummary]:
    plugins, _ = scan_all()
    out = plugins
    if category:
        out = [p for p in out if p.category.lower() == category.lower()]
    if q:
        ql = q.lower()
        out = [p for p in out
               if ql in p.name.lower()
               or ql in p.description.lower()
               or ql in p.category.lower()]
    return [
        PluginSummary(
            slug=p.slug, name=p.name, category=p.category,
            version_name=p.version_name, description=p.description, path=p.path,
        )
        for p in out
    ]


@router.get("/plugins/{slug}", response_model=PluginInfo)
def get_plugin(slug: str) -> PluginInfo:
    plugins, _ = scan_all()
    for p in plugins:
        if p.slug == slug:
            return p
    raise HTTPException(404, f"plugin {slug!r} not found")


@router.get("/modules", response_model=list[ModuleSummary])
def list_modules(q: str | None = None) -> list[ModuleSummary]:
    _, modules = scan_all()
    out = modules
    if q:
        ql = q.lower()
        out = [m for m in out if ql in m.name.lower() or ql in m.path.lower()]
    return [
        ModuleSummary(slug=m.slug, name=m.name, type=m.type, path=m.path)
        for m in out
    ]


@router.get("/modules/{slug}", response_model=ModuleInfo)
def get_module(slug: str) -> ModuleInfo:
    _, modules = scan_all()
    for m in modules:
        if m.slug == slug:
            return m
    raise HTTPException(404, f"module {slug!r} not found")


@router.post("/rescan")
def rescan() -> dict:
    """手动触发重新扫描（engine_root 变了的时候用）。"""
    invalidate_cache()
    plugins, modules = scan_all(force=True)
    return {"ok": True, "plugins": len(plugins), "modules": len(modules)}


# ---------- AI ----------
@router.post("/ai/stream")
async def ai_stream(req: AiChatRequest) -> StreamingResponse:
    plugins, modules = scan_all()
    item = None
    if req.kind == "plugin":
        for p in plugins:
            if p.slug == req.slug:
                item = p; break
    else:
        for m in modules:
            if m.slug == req.slug:
                item = m; break
    if item is None:
        raise HTTPException(404, f"{req.kind} {req.slug!r} not found")

    async def sse_body():
        async for piece in stream_chat(req.kind, item, req.message, req.history):
            # SSE 协议：每条 message 以 data: 开头，空行分隔
            safe = piece.replace("\n", "\\n")
            yield f"data: {safe}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        sse_body(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
