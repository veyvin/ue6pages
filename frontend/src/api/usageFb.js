/**
 * usage.fb 的浏览器端解析器 —— 零依赖，和后端 backend/usage_fb.py、gh-pages 的
 * assets/usage-fb.js 共用同一套 wire 布局（file identifier "UEUG"）：
 *
 *   UsageBundle: version(slot0 int32) generated_at(slot1 string) docs(slot2 [UsageDoc])
 *   UsageDoc:    kind(0) slug(1) name(2) category(3)
 *                cn_steps(4 [string]) en_steps(5 [string]) note_cn(6) note_en(7)
 *                ai_usage(8 bool) 已完成 AI 使用说明；旧文件无 slot8 时用步骤是否非空判断
 *                in_source(9 bool) 仍在 UE 源码中；旧文件无 slot9 时视为仍存在
 *
 * 拉取顺序与 gh-pages 一致：先读静态 /assets/usage.fb，没有再回落已发布的
 * gh-pages 文件，最后才打后端 /api/usage-fb（开发时现场打包）。
 */

const IDENT = 'UEUG'
const SESSION_KEY = 'ue-usage-fb-etag'
const SESSION_URL = 'ue-usage-fb-url'

function withBase(path) {
  const root = import.meta.env.BASE_URL || '/'
  return `${root}${String(path).replace(/^\//, '')}`
}

const LOCAL_CANDIDATES = [
  withBase('assets/usage.fb'),
  withBase('assets/usage.bin'),
]
const PUBLISHED_CANDIDATES = [
  'https://cdn.jsdelivr.net/gh/veyvin/ue6pages@gh-pages/assets/usage.fb',
  'https://raw.githubusercontent.com/veyvin/ue6pages/gh-pages/assets/usage.fb',
]
const API_CANDIDATES = ['/api/usage-fb']

export const USAGE_FB_CANDIDATES = [
  ...LOCAL_CANDIDATES,
  ...PUBLISHED_CANDIDATES,
  ...API_CANDIDATES,
]

const state = {
  loaded: false,
  loading: null,
  docs: 0,
  generatedAt: '',
  error: '',
  source: '',
  index: null,
}

function view(arrayBuffer) {
  const dv = new DataView(arrayBuffer)
  const bytes = new Uint8Array(arrayBuffer)

  const u16 = (p) => dv.getUint16(p, true)
  const u32 = (p) => dv.getUint32(p, true)
  const i32 = (p) => dv.getInt32(p, true)

  function fieldOffset(tbl, slot) {
    const vt = tbl - i32(tbl)
    if (4 + slot * 2 >= u16(vt)) return 0
    return u16(vt + 4 + slot * 2)
  }

  function bytesToString(start, len) {
    return new TextDecoder('utf-8').decode(bytes.subarray(start, start + len))
  }

  function readString(tbl, slot) {
    const off = fieldOffset(tbl, slot)
    if (!off) return ''
    const pos = tbl + off
    const sp = pos + u32(pos)
    return bytesToString(sp + 4, u32(sp))
  }

  function readStringVec(tbl, slot) {
    const off = fieldOffset(tbl, slot)
    if (!off) return []
    const pos = tbl + off
    const vec = pos + u32(pos)
    const n = u32(vec)
    const out = []
    for (let i = 0; i < n; i += 1) {
      const ep = vec + 4 + i * 4
      const sp = ep + u32(ep)
      out.push(bytesToString(sp + 4, u32(sp)))
    }
    return out
  }

  function readTableVec(tbl, slot) {
    const off = fieldOffset(tbl, slot)
    if (!off) return []
    const pos = tbl + off
    const vec = pos + u32(pos)
    const n = u32(vec)
    const out = []
    for (let i = 0; i < n; i += 1) {
      const ep = vec + 4 + i * 4
      out.push(ep + u32(ep))
    }
    return out
  }

  function readBool(tbl, slot, fallback = false) {
    const off = fieldOffset(tbl, slot)
    if (!off) return fallback
    return bytes[tbl + off] !== 0
  }

  return { ident: bytesToString(4, 4), u32, i32, fieldOffset, readString, readStringVec, readTableVec, readBool }
}

function parse(arrayBuffer) {
  const r = view(arrayBuffer)
  if (r.ident !== IDENT) throw new Error(`usage.fb 标识符异常：${r.ident || '(空)'}`)

  const root = r.u32(0)
  const versionOff = r.fieldOffset(root, 0)
  const version = versionOff ? r.i32(root + versionOff) : 0
  const generatedAt = r.readString(root, 1)

  const index = new Map()
  let count = 0
  for (const tbl of r.readTableVec(root, 2)) {
    const doc = {
      kind: r.readString(tbl, 0),
      slug: r.readString(tbl, 1),
      name: r.readString(tbl, 2),
      category: r.readString(tbl, 3),
      cnSteps: r.readStringVec(tbl, 4),
      enSteps: r.readStringVec(tbl, 5),
      noteCn: r.readString(tbl, 6),
      noteEn: r.readString(tbl, 7),
      aiUsage: false,
      inSource: true,
    }
    doc.aiUsage = r.readBool(tbl, 8) || doc.cnSteps.length > 0 || doc.enSteps.length > 0
    doc.inSource = r.readBool(tbl, 9, true)
    if (!doc.slug) continue
    index.set(`${doc.kind}:${doc.slug}`, doc)
    count += 1
  }

  return { version, generatedAt, index, count }
}

function applyParsed(parsed, source, etag) {
  state.index = parsed.index
  state.docs = parsed.count
  state.generatedAt = parsed.generatedAt
  state.loaded = true
  state.error = ''
  state.source = source
  if (etag) sessionStorage.setItem(SESSION_KEY, etag)
  sessionStorage.setItem(SESSION_URL, source)
}

async function fetchOne(url, { force = false } = {}) {
  const headers = {}
  if (!force && sessionStorage.getItem(SESSION_URL) === url) {
    const etag = sessionStorage.getItem(SESSION_KEY)
    if (etag) headers['If-None-Match'] = etag
  }
  const resp = await fetch(url, { headers })
  if (resp.status === 304 && state.index) return { kind: 'not-modified', url }
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`)
  const buf = await resp.arrayBuffer()
  if (buf.byteLength < 12) throw new Error('usage.fb 太短')
  return {
    kind: 'ok',
    url,
    parsed: parse(buf),
    etag: resp.headers.get('ETag') || '',
  }
}

export function usageFbState() {
  return {
    loaded: state.loaded,
    loading: Boolean(state.loading),
    docs: state.docs,
    generatedAt: state.generatedAt,
    error: state.error,
    source: state.source,
  }
}

/** 拉取并解析 usage.fb；并发调用共享同一个请求。失败时返回 null，不影响 Markdown 回退。 */
export function ensureUsageFb({ force = false } = {}) {
  if (state.loaded && !force) return Promise.resolve(state)
  if (state.loading && !force) return state.loading

  state.loading = (async () => {
    const errors = []

    async function tryUrl(url) {
      const result = await fetchOne(url, { force })
      if (result.kind === 'not-modified') {
        state.loaded = true
        state.source = url
        return state
      }
      applyParsed(result.parsed, result.url, result.etag)
      return state
    }

    async function tryGroup(urls, { parallel = false } = {}) {
      if (!parallel) {
        for (const url of urls) {
          try {
            return await tryUrl(url)
          } catch (err) {
            errors.push(`${url}: ${err?.message || err}`)
          }
        }
        return null
      }
      try {
        return await Promise.any(urls.map((url) => tryUrl(url)))
      } catch (agg) {
        const reasons = agg?.errors || []
        urls.forEach((url, i) => {
          errors.push(`${url}: ${reasons[i]?.message || reasons[i] || 'failed'}`)
        })
        return null
      }
    }

    return (
      await tryGroup(LOCAL_CANDIDATES)
      || await tryGroup(PUBLISHED_CANDIDATES, { parallel: true })
      || await tryGroup(API_CANDIDATES)
      || ((state.loaded = false), (state.error = errors.join(' · ') || 'usage.fb 读取失败'), state)
    )
  })().finally(() => {
    state.loading = null
  })

  return state.loading
}

export function listUsageDocs() {
  if (!state.index) return []
  return [...state.index.values()]
}

export function hasAiUsage(doc) {
  if (!doc) return false
  if (doc.aiUsage) return true
  return Boolean((doc.cnSteps && doc.cnSteps.length) || (doc.enSteps && doc.enSteps.length))
}

export function itemStatus(item) {
  if (!item) return 'ok'
  if (item.in_source === false) return 'gone'
  if (!item.usage_doc) return 'missing'
  return 'ok'
}

export function getUsageDoc(kind, slug) {
  if (!state.index) return null
  return state.index.get(`${kind}:${slug}`) || null
}

export function getUsageDocBySlug(slug) {
  if (!state.index) return null
  return state.index.get(`plugin:${slug}`) || state.index.get(`module:${slug}`) || null
}

/** 把二进制里的要点整理成和 /api/usage-docs 一致的形态，方便详情页统一渲染。 */
export function toUsageDoc(doc) {
  if (!doc) return null
  const steps = doc.cnSteps.length ? doc.cnSteps : doc.enSteps
  const note = doc.noteCn || doc.noteEn
  const markdown = [
    note ? note : '',
    steps.length ? steps.map((s) => `- ${s}`).join('\n') : '',
  ].filter(Boolean).join('\n\n')
  return {
    found: Boolean(markdown),
    content: markdown,
    steps,
    note,
    source: 'flatbuffers',
    mtime: 0,
  }
}

export function catalogFromUsageFb() {
  const plugins = []
  const modules = []
  for (const doc of listUsageDocs()) {
    const description = doc.noteCn || doc.noteEn || ''
    if (doc.kind === 'plugin') {
      plugins.push({
        slug: doc.slug,
        name: doc.name || doc.slug,
        category: doc.category || '',
        version_name: '',
        description,
        path: `plugins/${doc.slug}`,
        usage_doc: hasAiUsage(doc),
        in_source: doc.inSource !== false,
      })
    } else if (doc.kind === 'module') {
      modules.push({
        slug: doc.slug,
        name: doc.name || doc.slug,
        type: 'Runtime',
        path: `modules/${doc.slug}`,
        description,
        usage_doc: hasAiUsage(doc),
        in_source: doc.inSource !== false,
        public_deps: [],
        private_deps: [],
        base: 'ModuleRules',
        platform: '',
      })
    }
  }
  return {
    plugins,
    modules,
    stats: {
      total_plugins: plugins.length,
      total_modules: modules.length,
      categories: [...new Set(plugins.map((p) => p.category).filter(Boolean))].sort(),
      engine_version: '',
    },
  }
}

export function itemFromUsageFb(kind, slug) {
  const doc = getUsageDoc(kind, slug)
  if (!doc) return null
  const description = doc.noteCn || doc.noteEn || ''
  if (kind === 'plugin') {
    return {
      slug: doc.slug,
      name: doc.name || doc.slug,
      category: doc.category || '',
      version: '',
      version_name: '',
      author: '',
      engine_version: '',
      description,
      path: `plugins/${doc.slug}`,
      modules: [],
      usage_doc: hasAiUsage(doc),
      in_source: doc.inSource !== false,
    }
  }
  return {
    slug: doc.slug,
    name: doc.name || doc.slug,
    type: 'Runtime',
    path: `modules/${doc.slug}`,
    description,
    base: 'ModuleRules',
    public_deps: [],
    private_deps: [],
    platform: '',
    usage_doc: hasAiUsage(doc),
    in_source: doc.inSource !== false,
  }
}

/** 清掉内存与 sessionStorage 里的缓存（重建之后调用）。 */
export function resetUsageFb() {
  state.loaded = false
  state.index = null
  state.docs = 0
  state.generatedAt = ''
  state.error = ''
  state.source = ''
  sessionStorage.removeItem(SESSION_KEY)
  sessionStorage.removeItem(SESSION_URL)
}

export async function rebuildUsageFb() {
  const resp = await fetch('/api/usage-fb/rebuild', { method: 'POST' })
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`)
  resetUsageFb()
  await ensureUsageFb({ force: true })
  return resp.json()
}
