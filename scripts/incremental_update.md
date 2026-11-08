# 增量更新备忘 / Incremental Update Cheatsheet

新插件（`.uplugin`）或新模块（`*.Build.cs`）出现后，如何**只补它们**的“使用方法”，而不全量重生成。

整套流水线分两段，天然增量、幂等：

- **页面生成**：`scripts/generate_docs.py` — 只生成“新出现 / 上次失败”的页面，已存在默认跳过。
- **用法填充**：`scripts/ai_usage/*.json` + `scripts/apply_ai_usage.py` — 按 `(kind, slug)` 命中才写用法卡，内容没变就跳过。

---

## 标准流程

```bash
# 1) 从新引擎源码树生成新页面（旧页不动，新页会带 data-usage-source="pending" 的占位卡）
python scripts/generate_docs.py --engine-root <UE安装路径> --docs-root .

# 2) 刷新 catalog，拿到新 slug（旧条目 slug 不变）
python scripts/export_catalog.py

# 3) 列出“待补用法”的条目（按 catalog 比对 + 扫描 pending 页面）
python scripts/_pending.py

# 4) 只对新 slug 新增一个 ai_usage 分块 JSON（结构见下），文件名任意，如
#    scripts/ai_usage/plugins_XXXX_XXXX.json 或 modules_XXXX_XXXX.json

# 5) 注入用法（幂等，只改命中页）
python scripts/apply_ai_usage.py

# 6) 复核，应输出 ALL COVERED
python scripts/_pending.py
```

---

## ai_usage 记录结构

每个文件是一个 JSON 数组，元素：

```json
{
  "slug": "页面文件名（不含 .md；插件/模块均为小写 slug）",
  "kind": "plugin 或 module",
  "cn_steps": ["中文步骤1", "中文步骤2"],
  "en_steps": ["English step 1", "English step 2"],
  "note_cn": "一句中文备注",
  "note_en": "one-line English note"
}
```

约定：
- `slug` 必须等于页面文件名（`plugins/<slug>.md`、`modules/<slug>.md`）。
- `cn_steps` 与 `en_steps` 条数必须一一对应。
- 步骤里用反引号 `` `代码` ``，会渲染成 `usage-code` 行内代码块。
- 模块页 slug 一般是小写页面名（如 `core`、`ubadetours`）。

---

## 检测到位没有

```bash
python scripts/_pending.py
# [1] items with NO ai_usage record    -> 新/漏的条目
# [2] pages not sourced from AI        -> pending/template/缺卡的页面
```

也可直接扫页面属性：

```bash
rg 'data-usage-source="pending"' plugins modules
```

`data-usage-source` 取值：`ai`（已写）、`pending`（占位待补）、`template`（类别模板）、或无卡。

---

## 注意 / 坑

- `generate_docs.py` 里 `AI_USAGE` 是 **import 时加载一次**。若同进程先生成页面后补 JSON，需再跑 `apply_ai_usage.py`（标准流程本就会跑）。
- `apply_ai_usage.py` **只增改、不清删**：删掉某记录，页面旧卡不会自动消失，需重生成该页或手动清。
- 别用 `--force`：会全量重调 AI 重写“引言”，昂贵且与用法卡无关。
- 改名/改路径导致 slug 变化 → 旧记录对不上，新页变 `pending`，需按新 slug 补记录。
- 模块内容可数据驱动生成：每个模块的真实 `path`（Runtime/Editor/Developer/Programs/ThirdParty/Experimental）、依赖列表都在 `scripts/catalog/modules.json` 里。

---

## 网页运行时从 FlatBuffers 读取（方案 1）

GitHub Pages / Jekyll **没有运行时、没有数据库**。Jekyll 只在构建期把文件变成静态 HTML。
详情页的用法数据走「静态兜底 + 浏览器读 `.fb`」：

1. 构建时仍可把用法卡烤进 `plugins/*.md` / `modules/*.md`（无 JS 也能看、利于 SEO）。
2. 详情页由 `_layouts/default.html` 注入 `window.__USAGE_PAGE__`（kind/slug 来自 `page.path`），并加载：
   - `assets/usage.fb` — 1995 条用法的 FlatBuffers 二进制
   - `assets/usage-fb.js` — 零依赖读取器
   - `assets/usage-runtime.js` — 覆盖 `#usage` 卡片；没有卡时会插入一张再填充
3. `fetch` 失败则保留页面上已有的静态卡。总览页不加载 `.fb`。

更新数据后重建二进制：

```bash
python scripts/build_usage_fb.py    # -> assets/usage.fb
```

schema 见 `scripts/usage.fbs`。演示页：`usage-demo.html`。

---

## 相关脚本速查

| 脚本 | 作用 |
|---|---|
| `scripts/generate_docs.py` | 发现 `.uplugin`/`.Build.cs`，生成/跳过页面，写入用法卡 |
| `scripts/export_catalog.py` | 由页面重建 `scripts/catalog/*.json`（含 slug/path/deps） |
| `scripts/inject_usage.py` | 用法卡渲染与注入核心（`load_ai_usage` / `usage_card_html`） |
| `scripts/apply_ai_usage.py` | 入口：把 `ai_usage` 记录应用到所有命中页面（幂等） |
| `scripts/_pending.py` | 增量检测：列出缺 AI 用法的 catalog 条目与非 ai 来源页面 |
| `scripts/build_usage_fb.py` | 把全部 ai_usage 序列化成 `assets/usage.fb` |
| `assets/usage-fb.js` | 浏览器端读取 `.fb` |
| `assets/usage-runtime.js` | 详情页运行时覆盖用法卡 |
