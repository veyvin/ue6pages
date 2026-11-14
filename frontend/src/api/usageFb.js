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
  progress: {
    phase: 'idle',
    received: 0,
    total: 0,
    ratio: null,
    rate: 0,
    url: '',
  },
  cached: false,
  everLoaded: false,
}

/**
 * 首访体积预估：优先用响应头 Content-Length 的真实值；拿不到时按当前已知 docs 数
 * 线性外推（单条约 x KB），再退回全局默认值。实测全量 ≈1000 条约 3.6 MB，约 3.6 KB/条。
 */
const BYTES_PER_DOC = 3.6 * 1024 // ≈ 3.6 KB/条（含步骤文本）
export const ESTIMATED_BYTES = 3.6 * 1024 * 1024
export const ESTIMATED_BYTES_GZIP = 720 * 1024

/** 由已知 docs 数线性外推全量体积；docs 为 0 时返回全局默认估算。 */
export function estimateTotalBytes(docs = state.docs) {
  if (docs > 0) return Math.round(docs * BYTES_PER_DOC)
  return ESTIMATED_BYTES
}

const progressListeners = new Set()

function emitProgress() {
  for (const fn of progressListeners) {
    try {
      fn({ ...state.progress })
    } catch (e) {
      /* 监听器异常不影响主流程 */
    }
  }
}

function setProgress(patch) {
  Object.assign(state.progress, patch)
  emitProgress()
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

function parseToDocs(arrayBuffer) {
  const r = view(arrayBuffer)
  if (r.ident !== IDENT) throw new Error(`usage.fb 标识符异常：${r.ident || '(空)'}`)

  const root = r.u32(0)
  const versionOff = r.fieldOffset(root, 0)
  const version = versionOff ? r.i32(root + versionOff) : 0
  const generatedAt = r.readString(root, 1)

  const docs = []
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
    docs.push(doc)
  }
  return { version, generatedAt, docs }
}

function parse(arrayBuffer) {
  const { version, generatedAt, docs } = parseToDocs(arrayBuffer)
  const index = new Map()
  for (const doc of docs) index.set(`${doc.kind}:${doc.slug}`, doc)
  return { version, generatedAt, index, count: docs.length }
}

function applyParsed(parsed, source, etag) {
  state.index = parsed.index
  state.docs = parsed.count
  state.generatedAt = parsed.generatedAt
  state.loaded = true
  state.error = ''
  state.source = source
  state.cached = false
  state.everLoaded = true
  if (etag) sessionStorage.setItem(SESSION_KEY, etag)
  sessionStorage.setItem(SESSION_URL, source)
}

async function fetchOne(url, { force = false } = {}) {
  const headers = {}
  if (!force && sessionStorage.getItem(SESSION_URL) === url) {
    const etag = sessionStorage.getItem(SESSION_KEY)
    if (etag) headers['If-None-Match'] = etag
  }
  const result = await loadWithProgress(url, headers)
  if (result.status === 304 && state.index) return { kind: 'not-modified', url }
  const buf = result.buffer
  if (!buf || buf.byteLength < 12) throw new Error('usage.fb 太短')
  setProgress({ phase: 'parsing', received: buf.byteLength, total: buf.byteLength, ratio: 1 })
  return {
    kind: 'ok',
    url,
    parsed: parse(buf),
    etag: result.etag || '',
  }
}

/**
 * 流式下载 usage.fb：用 fetch + ReadableStream 边读边拼进度（比 XHR 更细、首字节更早、
 * 支持 AbortController 中止）。FlatBuffers 必须收齐完整 buffer 才能解析，所以这里只做
 * 下载阶段的流式进度；收满后再进入 parsing 阶段。
 */
async function loadWithProgress(url, headers = {}, { signal } = {}) {
  let controller = signal ? null : new AbortController()
  const abortSignal = signal || controller.signal
  const startedAt = performance.now()

  const resp = await fetch(url, {
    headers,
    signal: abortSignal,
    // 让 CDN / 代理返回压缩后的传输体积，进度更接近真实网络耗时
    cache: 'default',
  })

  if (resp.status === 304) {
    return { status: 304, buffer: null, etag: resp.headers.get('ETag') || '' }
  }
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`)

  const etag = resp.headers.get('ETag') || ''
  const total = Number(resp.headers.get('Content-Length')) || 0
  setProgress({ phase: 'downloading', url, received: 0, total, ratio: total ? 0 : null, rate: 0 })

  // 没有可读流（老浏览器 / 已被消费）：退化为一次性 arrayBuffer
  if (!resp.body || !resp.body.getReader) {
    const buffer = await resp.arrayBuffer()
    setProgress({ phase: 'downloading', received: buffer.byteLength, total: buffer.byteLength, ratio: 1, rate: buffer.byteLength / ((performance.now() - startedAt) / 1000 || 1) })
    return { status: resp.status, buffer, etag }
  }

  const reader = resp.body.getReader()
  const chunks = []
  let received = 0
  let lastEmit = 0

  try {
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      if (value) {
        chunks.push(value)
        received += value.byteLength
        const now = performance.now()
        // 节流到 ~50ms 一次，避免高频 setProgress 触发过多渲染
        if (now - lastEmit > 50 || (total && received >= total)) {
          lastEmit = now
          const elapsed = Math.max((now - startedAt) / 1000, 0.001)
          setProgress({
            phase: 'downloading',
            received,
            total: total || received,
            ratio: total ? Math.min(received / total, 1) : null,
            rate: received / elapsed,
          })
        }
      }
    }
  } finally {
    reader.releaseLock?.()
  }

  const buffer = concatChunks(chunks, received)
  setProgress({ phase: 'downloading', received, total: total || received, ratio: 1, rate: received / Math.max((performance.now() - startedAt) / 1000, 0.001) })
  return { status: resp.status, buffer, etag }
}

function concatChunks(chunks, totalLen) {
  if (chunks.length === 1) {
    const only = chunks[0]
    return only.byteOffset === 0 && only.byteLength === only.buffer.byteLength
      ? only.buffer
      : only.buffer.slice(only.byteOffset, only.byteOffset + only.byteLength)
  }
  const out = new Uint8Array(totalLen)
  let offset = 0
  for (const c of chunks) {
    out.set(c, offset)
    offset += c.byteLength
  }
  return out.buffer
}

/** 订阅下载/解析进度，返回取消订阅函数。 */
export function onUsageFbProgress(fn) {
  progressListeners.add(fn)
  fn({ ...state.progress })
  return () => progressListeners.delete(fn)
}

export function usageFbProgress() {
  return { ...state.progress }
}

export function usageFbState() {
  return {
    loaded: state.loaded,
    loading: Boolean(state.loading),
    docs: state.docs,
    generatedAt: state.generatedAt,
    error: state.error,
    source: state.source,
    cached: state.cached,
    everLoaded: state.everLoaded,
    progress: { ...state.progress },
  }
}

/**
 * 首屏预估提示文案：
 * - 已加载且走缓存命中 → “已走缓存，秒开”
 * - 正在下载且已知总大小 → 显示估算体积
 * - 默认首访 → 用常量估算“首次约 X，之后走缓存秒开”
 */
export function estimateHint() {
  const total = state.progress.total || 0
  // 已知真实总大小优先；否则按当前 docs 数线性外推；再退回全局默认
  const bytes = total > 0 ? total : estimateTotalBytes()
  const size = formatBytes(bytes)
  if (state.loaded && state.cached) return '已走缓存，秒开'
  if (state.loaded) return `本次约 ${size}，之后走缓存秒开`
  return `首次约 ${size}，之后走缓存秒开`
}

export function formatBytes(n) {
  if (!n) return '0 B'
  const units = ['B', 'KB', 'MB', 'GB']
  let i = 0
  let v = n
  while (v >= 1024 && i < units.length - 1) { v /= 1024; i += 1 }
  return `${v.toFixed(v >= 100 || i === 0 ? 0 : 1)} ${units[i]}`
}

/** 拉取并解析 usage.fb；并发调用共享同一个请求。失败时返回 null，不影响 Markdown 回退。 */
export function ensureUsageFb({ force = false } = {}) {
  if (state.loaded && !force) return Promise.resolve(state)
  if (state.loading && !force) return state.loading

  state.loading = (async () => {
    const errors = []

    async function tryUrl(url) {
      setProgress({ phase: 'connecting', url, received: 0, total: 0, ratio: null, rate: 0 })
      const result = await fetchOne(url, { force })
      if (result.kind === 'not-modified') {
        state.loaded = true
        state.source = url
        state.cached = true
        state.everLoaded = true
        setProgress({ phase: 'done', ratio: 1 })
        return state
      }
      applyParsed(result.parsed, result.url, result.etag)
      setProgress({ phase: 'done', ratio: 1 })
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
      || ((state.loaded = false),
        (state.error = errors.join(' · ') || 'usage.fb 读取失败'),
        setProgress({ phase: 'error' }),
        state)
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