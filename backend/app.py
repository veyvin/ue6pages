"""FastAPI 应用入口。"""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CONFIG
from .routers import router
from .scanner import invalidate_cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时的钩子：可选重扫 / 记录版本
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


@app.get("/")
def root() -> dict:
    return {
        "ok": True,
        "service": "UE Plugin Docs API",
        "engine_root": CONFIG.engine_root,
        "ai_enabled": CONFIG.ai.enabled,
        "ai_model": CONFIG.ai.model,
        "docs": "/docs",
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
