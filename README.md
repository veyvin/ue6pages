# ue6pages

Automated Unreal Engine plugin/module documentation generator.

## 🌐 Generated Documentation

Visit: **https://ue.veyvin.com**

## 📋 Overview

This repository automates the generation of documentation for Unreal Engine plugins and modules. It uses:

- **GitHub Models API** for AI-written introductions
- **Epic Developer Assistant** for detailed AI descriptions
- **Google Translate** for Chinese translations
- **GitHub Actions** for daily automated runs

## 🏗️ Architecture

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
│  │   └─ Deploy to GitHub Pages                                 │
│  │                                                              │
│  └── UE AI Plugin Describer (daily 01:00 UTC)                  │
│      ├─ 5 parallel jobs (Playwright + Epic Developer Assistant)│
│      ├─ Max 4 hours per job                                    │
│      └─ Round-robin distribution                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   https://ue.veyvin.com
```

## ⚙️ Configuration

### Required Secrets

| Secret | Description |
|--------|-------------|
| `PRIVATE_REPO_PAT` | Classic PAT with `repo` scope, to access veyvin/UnrealEngine |

### Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AI_MODEL` | `openai/gpt-4o-mini` | Model for GitHub Models API |
| `AI_WORKERS` | `8` | Number of parallel AI calls |
| `AI_ENABLED` | `true` | Enable AI-generated intros |
| `TRANSLATE_ENABLED` | `true` | Enable Chinese translation |

### Manual Trigger Options

**Generate & Deploy UE Docs**
- `force_regenerate`: Regenerate all docs even if they exist
- `seed_from_private`: Copy existing docs from private repo gh-pages

**UE AI Plugin Describer**
- `count`: Limit items per job (empty = no limit)
- `dry_run`: Preview without making changes

## 📁 Project Structure

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

## 🚀 Getting Started

1. **Fork this repo** or clone it to your own account

2. **Configure Secrets**
   - Go to `Settings > Secrets and variables > Actions`
   - Add `PRIVATE_REPO_PAT` with a classic PAT

3. **Enable GitHub Pages**
   - Go to `Settings > Pages`
   - Set Source to **GitHub Actions**

4. **Run Workflows**
   - Go to `Actions` tab
   - Manually trigger **Generate & Deploy UE Docs** with `seed_from_private` enabled

## 📝 Scripts

### generate_docs.py

```bash
python scripts/generate_docs.py \
  --engine-root /path/to/ue-source \
  --docs-root /path/to/ghpages \
  --model "openai/gpt-4o-mini" \
  --workers 8 \
  --force false \
  --translate
```

### ue-ai-describer

```bash
cd scripts/ue-ai-describer
npm install
npx playwright install chromium
node index.js /path/to/ghpages \
  --step 5 \
  --offset 0 \
  --max-runtime-minutes 220
```

## 📊 Performance

| Workflow | Parallel Jobs | Time Limit | Daily Capacity |
|----------|--------------|-----------|---------------|
| Generate UE Docs | 8 threads (Python) | 6h | ~1800 docs |
| UE AI Describer | 5 parallel jobs | 4h/job | ~350-600 descriptions |

## 📄 License

MIT