"""路由层：/api/plugins · /api/modules · /api/config · /api/ai/stream · /api/ai/batch"""
from __future__ import annotations

import asyncio
import json
import os
import time
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response, StreamingResponse
from pydantic import ValidationError

from .ai_service import generate_usage_doc, stream_chat, test_connection
from .config import CONFIG, config_path, public_config, save_config
from .scanner import scan_all, invalidate_cache
from . import usage_docs, usage_fb
from .schemas import (
    PluginInfo, PluginSummary, ModuleInfo, ModuleSummary,
    Stats, AiBatchRequest, AiChatRequest,
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
    have = usage_docs.existing_slugs()["plugins"]
    return [
        PluginSummary(
            slug=p.slug, name=p.name, category=p.category,
            version_name=p.version_name, description=p.description, path=p.path,
            usage_doc=p.slug in have,
        )
        for p in out
    ]


@router.get("/plugins/{slug}", response_model=PluginInfo)
def get_plugin(slug: str) -> PluginInfo:
    plugins, _ = scan_all()
    for p in plugins:
        if p.slug == slug:
            have = usage_docs.existing_slugs()["plugins"]
            return p.model_copy(update={"usage_doc": p.slug in have})
    raise HTTPException(404, f"plugin {slug!r} not found")


@router.get("/modules", response_model=list[ModuleSummary])
def list_modules(q: str | None = None) -> list[ModuleSummary]:
    _, modules = scan_all()
    out = modules
    if q:
        ql = q.lower()
        out = [m for m in out if ql in m.name.lower() or ql in m.path.lower()]
    have = usage_docs.existing_slugs()["modules"]
    return [
        ModuleSummary(
            slug=m.slug, name=m.name, type=m.type, path=m.path,
            usage_doc=m.slug in have,
        )
        for m in out
    ]


@router.get("/modules/{slug}", response_model=ModuleInfo)
def get_module(slug: str) -> ModuleInfo:
    _, modules = scan_all()
    for m in modules:
        if m.slug == slug:
            have = usage_docs.existing_slugs()["modules"]
            return m.model_copy(update={"usage_doc": m.slug in have})
    raise HTTPException(404, f"module {slug!r} not found")


@router.post("/rescan")
def rescan() -> dict:
    """手动触发重新扫描（engine_root 变了的时候用）。"""
    invalidate_cache()
    plugins, modules = scan_all(force=True)
    return {"ok": True, "plugins": len(plugins), "modules": len(modules)}


# ---------- 配置 ----------
@router.get("/config")
def get_config() -> dict:
    return {
        "config": public_config(),
        "path": str(config_path()),
        "engine_exists": Path(CONFIG.engine_root).exists(),
        "env_api_key": bool(os.environ.get("UE_AI_API_KEY")),
    }


@router.put("/config")
def put_config(payload: dict) -> dict:
    try:
        save_config(payload)
    except ValidationError as e:
        raise HTTPException(422, detail=str(e))
    invalidate_cache()
    return get_config()


# ---------- AI ----------
@router.post("/ai/test")
async def ai_test() -> dict:
    try:
        reply = await test_connection()
    except Exception as exc:
        raise HTTPException(502, detail=str(exc))
    return {"ok": True, "model": CONFIG.ai.model, "reply": reply}

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
            # 每帧数据用 JSON 编码，保留换行与首尾空格；空行分隔帧
            yield f"data: {json.dumps(piece, ensure_ascii=False)}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        sse_body(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


# ---------- 《使用方法》文档（AI 批量生成） ----------
@router.get("/usage-docs/stats")
def usage_docs_stats() -> dict:
    """《使用方法》文档覆盖率统计（与 /usage-docs/{kind}/{slug} 路由同名冲突前先注册）。"""
    plugins, modules = scan_all()
    have = usage_docs.existing_slugs()
    return {
        "root": str(usage_docs.usage_root()),
        "plugins": {
            "total": len(plugins),
            "have": len({p.slug for p in plugins} & have["plugins"]),
        },
        "modules": {
            "total": len(modules),
            "have": len({m.slug for m in modules} & have["modules"]),
        },
    }


@router.get("/usage-docs/{kind}/{slug}")
def read_usage_doc(kind: str, slug: str) -> dict:
    if kind not in ("plugin", "module"):
        raise HTTPException(404, f"unknown kind {kind!r}")
    return usage_docs.read_doc(kind, slug)


# ---------- usage.fb（FlatBuffers，前端直接解析） ----------
@router.get("/usage-fb/meta")
def usage_fb_meta() -> dict:
    """二进制与文档覆盖率概况：设置页展示用，不触发打包。"""
    payload = usage_fb.get_payload()
    return {
        "docs": payload["docs"],
        "bytes": len(payload["payload"]),
        "generated_at": payload["generated_at"],
        "disk": usage_fb.disk_status(),
        **usage_docs_stats(),
    }


@router.get("/usage-fb")
def usage_fb_download(request: Request) -> Response:
    """完整 usage.fb 二进制。带 ETag，前端与 CDN 可复用缓存。"""
    info = usage_fb.get_payload()
    etag = info["etag"]
    if request.headers.get("if-none-match") == etag:
        return Response(status_code=304, headers={"ETag": etag})
    return Response(
        content=info["payload"],
        media_type="application/octet-stream",
        headers={
            "ETag": etag,
            "X-Usage-Docs": str(info["docs"]),
            "X-Usage-Generated-At": info["generated_at"],
            "Cache-Control": "public, max-age=60",
        },
    )


@router.post("/usage-fb/rebuild")
def usage_fb_rebuild() -> dict:
    """强制重建一次二进制，并落盘到 usage_fb_root（部署时也走这里）。"""
    usage_fb.invalidate()
    return usage_fb.write_files(force=True)


@router.post("/ai/batch")
async def ai_batch(req: AiBatchRequest) -> StreamingResponse:
    """批量生成《使用方法》文档，SSE 进度流。

    每帧为 `data: <JSON>`：
      {"type":"start", "total":N, "model":..., "workers":..., "output_root":...}
      {"type":"item",  "kind","slug","name","index","total",
                       "status":"ok|skip|fail", "file"?:str, "error"?:str}
      {"type":"summary","total","seconds","ok","skip","fail"}
    结束帧 `data: [DONE]`。客户端断开时取消剩余任务。
    """
    plugins, modules = scan_all()
    tasks: list[tuple[str, Any]] = []
    if req.kind in ("plugin", "all"):
        tasks += [("plugin", p) for p in plugins]
    if req.kind in ("module", "all"):
        tasks += [("module", m) for m in modules]
    if req.slugs:
        wanted = set(req.slugs)
        tasks = [(k, it) for k, it in tasks if it.slug in wanted]
    skipped_existing = 0
    if not req.overwrite:
        have_md = usage_docs.existing_slugs()
        have_fb = usage_fb.load_ai_usage_keys()
        kept: list[tuple[str, Any]] = []
        for kind, item in tasks:
            folder = "plugins" if kind == "plugin" else "modules"
            if item.slug in have_md[folder] or (kind, item.slug) in have_fb:
                skipped_existing += 1
                continue
            kept.append((kind, item))
        tasks = kept
    if not tasks and skipped_existing == 0:
        raise HTTPException(404, "没有匹配到任何条目（检查 kind / slugs 或 engine_root）")
    if req.limit > 0:
        tasks = tasks[:req.limit]

    workers = max(1, CONFIG.ai.workers)

    def frame(payload: dict) -> str:
        return "data: " + json.dumps(payload, ensure_ascii=False) + "\n\n"

    async def sse_body():
        started = time.monotonic()
        counters = {"ok": 0, "skip": 0, "fail": 0}
        pending: list[asyncio.Task] = []
        try:
            yield frame({
                "type": "start",
                "total": len(tasks),
                "skipped_existing": skipped_existing,
                "model": CONFIG.ai.model,
                "workers": workers,
                "output_root": str(usage_docs.usage_root()),
            })

            sem = asyncio.Semaphore(workers)

            async def run_one(index: int, kind: str, item: Any) -> dict:
                async with sem:
                    payload = {
                        "type": "item",
                        "kind": kind,
                        "slug": item.slug,
                        "name": item.name,
                        "index": index,
                        "total": len(tasks),
                    }
                    target = usage_docs.doc_path(kind, item.slug)
                    try:
                        content = await generate_usage_doc(kind, item)
                        usage_docs.write_doc(kind, item.slug, content)
                        usage_fb.invalidate()
                        payload.update(status="ok", file=str(target))
                    except Exception as exc:  # noqa: BLE001
                        payload.update(status="fail", error=str(exc)[:400])
                    return payload

            pending = [
                asyncio.create_task(run_one(i, k, it))
                for i, (k, it) in enumerate(tasks)
            ]
            for done in asyncio.as_completed(pending):
                payload = await done
                counters[payload["status"]] = counters.get(payload["status"], 0) + 1
                yield frame(payload)

            yield frame({
                "type": "summary",
                "total": len(tasks) + skipped_existing,
                "seconds": round(time.monotonic() - started, 1),
                **{**counters, "skip": counters["skip"] + skipped_existing},
            })
            try:
                usage_fb.write_files(force=True)
            except Exception:  # noqa: BLE001
                pass
            yield "data: [DONE]\n\n"
        finally:
            # 客户端断开 / 生成器取消时，停掉还没跑完的任务
            for t in pending:
                t.cancel()

    return StreamingResponse(
        sse_body(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )