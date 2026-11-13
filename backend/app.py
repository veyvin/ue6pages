"""FastAPI 应用入口。"""
from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import CONFIG
from .routers import router
from .scanner import invalidate_cache
from . import usage_fb


@asynccontextmanager
async def lifespan(app: FastAPI):
    usage_fb.output_root().mkdir(parents=True, exist_ok=True)
    yield
    invalidate_cache()


app = FastAPI(
    title="UE Plugin Docs API",
    version="1.0.0",
    lifespan=lifespan,
    description=(
        "Scan Unreal Engine source tree for plugins & modules, "
        "expose a REST API + AI chat endpoint."
    ),
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=list(CONFIG.cors.origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

_assets = usage_fb.output_root()
_assets.mkdir(parents=True, exist_ok=True)
app.mount("/assets", StaticFiles(directory=str(_assets)), name="assets")

_dist = Path(CONFIG.site.frontend_dist)
if not _dist.is_absolute():
    _dist = Path(__file__).resolve().parent / _dist
if _dist.is_dir():
    app.mount("/", StaticFiles(directory=str(_dist), html=True), name="frontend")
else:
    @app.get("/")
    def root() -> dict:
        return {
            "ok": True,
            "service": "UE Plugin Docs API",
            "engine_root": CONFIG.engine_root,
            "ai_enabled": CONFIG.ai.enabled,
            "ai_model": CONFIG.ai.model,
            "docs": "/docs",
            "usage_fb": "/assets/usage.fb",
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.app:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        reload_dirs=["backend"],
    )
