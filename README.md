# ue6pages

> 🇺🇸 English | 🇨🇳 中文

## 🌐 Generated Documentation

Visit: **https://ue.veyvin.com**

---

## 📋 Overview (English)

Automated Unreal Engine plugin/module documentation generator.

This repository automates the generation of documentation for Unreal Engine plugins and modules. It uses:

- **GitHub Models API** for AI-written introductions
- **Epic Developer Assistant** for detailed AI descriptions
- **Google Translate** for Chinese translations
- **GitHub Actions** for daily automated runs

### 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  Private Repo: veyvin/UnrealEngine                             │
│  └── Sync Fork (sync upstream) + Deploy Pages                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Public Repo: veyvin/ue6pages (this one)                       │
│  ├── Generate & Deploy UE Docs (daily 07:00 UTC)               │
│  │   ├─ Pull UE source (sparse checkout)                       │
│  │   ├─ Generate plugin/module docs (GitHub Models)            │
│  │   ├─ Translate to Chinese                                   │
│  │   └── Deploy to GitHub Pages                                │
│  │                                                              │
│  └── UE AI Plugin Describer (daily 01:00 UTC)                  │
│      ├─ 5 parallel jobs (Playwright + Epic Developer Assistant)│
│      ├─ Max 4 hours per job                                    │
│      └── Round-robin distribution                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   https://ue.veyvin.com
```

### ⚙️ Configuration

**Required Secrets**

| Secret | Description |
|--------|-------------|
| `PRIVATE_REPO_PAT` | Classic PAT with `repo` scope, to access veyvin/UnrealEngine |

**Optional Variables**

| Variable | Default | Description |
|----------|---------|-------------|
| `AI_MODEL` | `openai/gpt-4o-mini` | Model for GitHub Models API |
| `AI_WORKERS` | `8` | Number of parallel AI calls |
| `AI_ENABLED` | `true` | Enable AI-generated intros |
| `TRANSLATE_ENABLED` | `true` | Enable Chinese translation |

**Manual Trigger Options**

- **Generate & Deploy UE Docs**: `force_regenerate`, `seed_from_private`
- **UE AI Plugin Describer**: `count`, `dry_run`

### 🚀 Getting Started

1. **Fork this repo** or clone it to your own account
2. **Configure Secrets**: Add `PRIVATE_REPO_PAT` in Settings
3. **Enable GitHub Pages**: Set Source to GitHub Actions
4. **Run Workflows**: Manually trigger with `seed_from_private` enabled

### 📊 Performance

| Workflow | Parallel | Time Limit | Daily Capacity |
|----------|----------|-----------|---------------|
| Generate UE Docs | 8 threads | 6h | ~1800 docs |
| UE AI Describer | 5 jobs | 4h/job | ~350-600 descriptions |

---

## 📋 概述 (中文)

自动化 Unreal Engine 插件/模块文档生成器。

本仓库自动化生成 Unreal Engine 插件和模块的文档，使用以下技术：

- **GitHub Models API** 用于 AI 生成介绍
- **Epic Developer Assistant** 用于详细 AI 描述
- **Google Translate** 用于中文翻译
- **GitHub Actions** 用于每日自动运行

### 🏗️ 架构

```
┌─────────────────────────────────────────────────────────────────┐
│  私有仓库: veyvin/UnrealEngine                                  │
│  └── Sync Fork (同步上游) + Deploy Pages                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  公有仓库: veyvin/ue6pages (本仓库)                             │
│  ├── Generate & Deploy UE Docs (每日 07:00 UTC)                 │
│  │   ├─ 拉取 UE 源码 (sparse checkout)                         │
│  │   ├─ 生成插件/模块文档 (GitHub Models)                       │
│  │   ├─ 翻译为中文                                             │
│  │   └── 部署到 GitHub Pages                                   │
│  │                                                              │
│  └── UE AI Plugin Describer (每日 01:00 UTC)                   │
│      ├─ 5 个并行 job (Playwright + Epic Developer Assistant)    │
│      ├─ 每个 job 最长 4 小时                                    │
│      └── 轮询分配                                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   https://ue.veyvin.com
```

### ⚙️ 配置

**必需的 Secrets**

| Secret | 说明 |
|--------|------|
| `PRIVATE_REPO_PAT` | 具有 `repo` 权限的 Classic PAT，用于访问 veyvin/UnrealEngine |

**可选变量**

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `AI_MODEL` | `openai/gpt-4o-mini` | GitHub Models API 使用的模型 |
| `AI_WORKERS` | `8` | 并行 AI 调用数量 |
| `AI_ENABLED` | `true` | 启用 AI 生成介绍 |
| `TRANSLATE_ENABLED` | `true` | 启用中文翻译 |

**手动触发选项**

- **Generate & Deploy UE Docs**: `force_regenerate`（强制重新生成）, `seed_from_private`（从私有仓库初始化）
- **UE AI Plugin Describer**: `count`（数量限制）, `dry_run`（预览模式）

### 🚀 快速开始

1. **Fork 本仓库**或克隆到自己的账号
2. **配置 Secrets**: 在 Settings 中添加 `PRIVATE_REPO_PAT`
3. **启用 GitHub Pages**: 将 Source 设置为 GitHub Actions
4. **运行 Workflows**: 手动触发并启用 `seed_from_private`

### 📊 性能指标

| Workflow | 并行数 | 时间限制 | 每日处理能力 |
|----------|--------|---------|-------------|
| Generate UE Docs | 8 线程 | 6 小时 | ~1800 文档 |
| UE AI Describer | 5 个 job | 4 小时/job | ~350-600 描述 |

---

## 📁 Project Structure / 项目结构

```
├── .github/workflows/
│   ├── generate-ue-docs.yml    # Main doc generation workflow
│   └── ue-ai-describer.yml     # AI description enhancement
├── scripts/
│   ├── generate_docs.py        # Python doc generator
│   ├── ue-ai-describer/        # Node.js Playwright scripts
│   │   ├── index.js            # Main entry
│   │   ├── scanner.js          # Markdown file scanner
│   │   ├── ue-ai-client.js     # Playwright AI client
│   │   └── package.json
│   └── sync-and-deploy-minimal.yml  # Private repo workflow reference
└── README.md
```

## 📄 License / 许可

MIT