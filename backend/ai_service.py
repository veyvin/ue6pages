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
    if not CONFIG.ai.enabled:
        yield "⚠ AI 已在设置中关闭。"
        return

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


# ---------- 《使用方法》文档批量生成（非流式） ----------
def _usage_system_prompt() -> str:
    return (
        "You are a senior Unreal Engine technical writer. Write a practical "
        "《使用方法》(usage guide) document in Simplified Chinese Markdown.\n"
        "Rules:\n"
        "- Keep API/class names and code in their original language (English).\n"
        "- Only describe what can be reasonably inferred from the provided metadata; "
        "state uncertainty explicitly. Never invent APIs, class names, or file paths.\n"
        "- Be concise: roughly 300-800 Chinese characters plus short code snippets.\n"
        "- Output only the Markdown body — no surrounding code fences, no leading title."
    )


def _usage_user_prompt(kind: str, name: str) -> str:
    if kind == "plugin":
        return (
            f"请为 Unreal Engine 插件「{name}」写一篇《使用方法》文档，Markdown 输出。\n"
            "结构要求：\n"
            "1. 以 `## 使用方法` 开头；\n"
            "2. 第一段：一句话定位这个插件；\n"
            "3. 「启用方式」：如何在项目里启用（插件列表 / .uproject 的 AdditionalDependencies 等，"
            "仅依据上下文可推断时给出代码，用 ```cpp 标注）；\n"
            "4. 「典型用法」：1-2 个步骤式示例或场景描述，确有把握时给最小 C++ / 蓝图片段；\n"
            "5. 「注意事项」：常见坑（仅基于上下文合理推断）。"
        )
    return (
        f"请为 Unreal Engine 构建模块「{name}」写一篇《使用方法》文档，Markdown 输出。\n"
        "结构要求：\n"
        "1. 以 `## 使用方法` 开头；\n"
        "2. 第一段：一句话说明该模块在引擎中的职责；\n"
        "3. 「如何依赖」：在另一个模块 Build.cs 里的声明方式"
        "（仅当上下文能推断出模块名时给 PublicDependencyModuleNames 片段，用 ```cpp 标注）；\n"
        "4. 「典型场景」：1-2 个使用场景；\n"
        "5. 「注意事项」：常见坑（仅基于上下文合理推断）。"
    )


async def generate_usage_doc(kind: str, item: PluginInfo | ModuleInfo) -> str:
    """非流式生成一篇《使用方法》文档；失败抛 RuntimeError（含 HTTP 状态与响应片段）。"""
    if not CONFIG.ai.enabled:
        raise RuntimeError("AI 已在设置中关闭")
    if not CONFIG.ai.api_key:
        raise RuntimeError("未配置 API Key：请在设置中填写，或设置环境变量 UE_AI_API_KEY")

    ctx = _plugin_context(item) if kind == "plugin" else _module_context(item)
    messages = [
        {"role": "system", "content": _usage_system_prompt()},
        {"role": "system", "content": f"=== Item context ===\n{ctx}"},
        {"role": "user", "content": _usage_user_prompt(kind, item.name)},
    ]

    url = f"{CONFIG.ai.endpoint.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {CONFIG.ai.api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": CONFIG.ai.model,
        "stream": False,
        "temperature": 0.3,
        "max_tokens": 1200,
        "messages": messages,
    }

    async with httpx.AsyncClient(timeout=CONFIG.ai.timeout * 2) as client:
        resp = await client.post(url, headers=headers, json=payload)

    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:300]}")
    try:
        content = str(resp.json()["choices"][0]["message"]["content"]).strip()
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise RuntimeError(f"响应格式异常: {resp.text[:300]}") from exc
    if not content:
        raise RuntimeError("模型返回了空内容")
    return content


async def test_connection() -> str:
    """用当前已保存的配置发一条极短请求，返回模型回复；失败抛 RuntimeError。"""
    if not CONFIG.ai.api_key:
        raise RuntimeError("未配置 API Key：请在设置中填写，或设置环境变量 UE_AI_API_KEY")

    url = f"{CONFIG.ai.endpoint.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {CONFIG.ai.api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": CONFIG.ai.model,
        "messages": [{"role": "user", "content": "Reply with the single word: OK"}],
    }
    async with httpx.AsyncClient(timeout=CONFIG.ai.timeout) as client:
        resp = await client.post(url, headers=headers, json=payload)

    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:300]}")
    try:
        return str(resp.json()["choices"][0]["message"]["content"]).strip()[:200]
    except (KeyError, IndexError, TypeError, ValueError):
        raise RuntimeError(f"响应格式异常: {resp.text[:300]}")
