"""AI 服务：调 OpenAI-compatible 端点，支持流式 SSE。"""
from __future__ import annotations

import json
from typing import Any, AsyncIterator

import httpx

from .config import CONFIG
from .schemas import PluginInfo, ModuleInfo


# ---------- Prompt ----------
def _plugin_system_prompt() -> str:
    return (
        "You are an expert on Unreal Engine plugin usage, C++, and gameplay programming.\n"
        "Answer in concise, practical Markdown. Prefer bullet lists and code snippets over prose.\n"
        "When the user asks 'how to use this plugin', walk through:\n"
        "  1. What it does (1 sentence)\n"
        "  2. Key classes / nodes / settings\n"
        "  3. Minimal C++ or Blueprint example\n"
        "  4. Common pitfalls\n"
        "If the info in context is insufficient, say so explicitly — do not hallucinate APIs."
    )


def _module_system_prompt() -> str:
    return (
        "You are an expert on Unreal Engine module authoring.\n"
        "Answer in concise Markdown. Focus on:\n"
        "  1. Role of this module in the engine\n"
        "  2. Key public types / namespaces\n"
        "  3. How to depend on it from another module (Build.cs snippet)\n"
        "  4. Practical use cases\n"
        "Do not invent APIs."
    )


def _plugin_context(p: PluginInfo) -> str:
    return (
        f"Plugin: {p.name} ({p.version_name})\n"
        f"Path: {p.path}\n"
        f"Category: {p.category}\n"
        f"Author: {p.author}\n"
        f"Engine: {p.engine_version}\n"
        f"Modules: {', '.join(m.name for m in p.modules)}\n"
        f"Description: {p.description}\n"
    )


def _module_context(m: ModuleInfo) -> str:
    return (
        f"Module: {m.name} ({m.type})\n"
        f"Path: {m.path}\n"
        f"Base rules: {m.base}\n"
        f"Public deps: {', '.join(m.public_deps) or '(none)'}\n"
        f"Private deps: {', '.join(m.private_deps) or '(none)'}\n"
        f"Description: {m.description}\n"
    )


# ---------- 流式主逻辑 ----------
async def _stream_chat(
    system_prompt: str,
    context: str,
    user_message: str,
    history: list[tuple[str, str]],
) -> AsyncIterator[str]:
    if not CONFIG.ai.api_key:
        yield f"⚠ AI API key not configured. Set `ai.api_key` in config.yaml or env `UE_AI_API_KEY`.\n\n(Dev mode — here is the context I would have sent)\n\n```\n{context}\n```"
        return

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": f"=== Item context ===\n{context}"},
    ]
    for role, text in history:
        if role in ("user", "assistant"):
            messages.append({"role": role, "content": text})
    messages.append({"role": "user", "content": user_message})

    url = f"{CONFIG.ai.endpoint.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {CONFIG.ai.api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": CONFIG.ai.model,
        "stream": True,
        "messages": messages,
    }

    async with httpx.AsyncClient(timeout=CONFIG.ai.timeout * 2) as client:
        async with client.stream("POST", url, headers=headers, json=payload) as resp:
            if resp.status_code != 200:
                body = (await resp.aread()).decode()[:500]
                yield f"⚠ AI provider returned HTTP {resp.status_code}\n\n```\n{body}\n```"
                return

            async for line in resp.aiter_lines():
                if not line.startswith("data:"):
                    continue
                payload = line[5:].strip()
                if not payload or payload == "[DONE]":
                    continue
                try:
                    chunk = json.loads(payload)
                    delta = chunk["choices"][0].get("delta", {})
                    content = delta.get("content")
                    if content:
                        yield content
                except Exception:
                    continue


async def stream_chat(
    kind: str,
    item: PluginInfo | ModuleInfo,
    user_message: str,
    history: list[tuple[str, str]],
) -> AsyncIterator[str]:
    if kind == "plugin":
        system = _plugin_system_prompt()
        ctx = _plugin_context(item)
    else:
        system = _module_system_prompt()
        ctx = _module_context(item)

    async for piece in _stream_chat(system, ctx, user_message, history):
        yield piece
