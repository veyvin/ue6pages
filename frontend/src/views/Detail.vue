<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { ItemsAPI, UsageDocAPI, errMsg } from '../api/client.js'
import { streamAiChat, streamUsageBatch } from '../api/ai.js'
import { ensureUsageFb, getUsageDoc, itemFromUsageFb, itemStatus, onUsageFbProgress, toUsageDoc } from '../api/usageFb.js'
import { renderMarkdown } from '../utils/markdown.js'
import { useItemsStore } from '../stores/items.js'

const props = defineProps({
  kind: { type: String, required: true },
  slug: { type: String, required: true },
})

const router = useRouter()
const known = useItemsStore()

const item = ref(null)
const loading = ref(false)
const error = ref('')
let requestId = 0

const progress = ref({ phase: 'idle', received: 0, total: 0, ratio: null, rate: 0, url: '' })
let stopProgress = null
onMounted(() => { stopProgress = onUsageFbProgress((p) => { progress.value = p }) })
onBeforeUnmount(() => { stopProgress?.() })

const phaseMap = {
  idle: { title: '准备打开条目', sub: 'resolving entry' },
  connecting: { title: '正在连接数据源', sub: 'handshake · usage.fb' },
  downloading: { title: '正在下载 usage.fb', sub: 'streaming flatbuffer bundle' },
  parsing: { title: '正在解析索引', sub: 'decoding flatbuffers tables' },
  done: { title: '索引就绪', sub: 'index ready' },
  error: { title: '数据包加载失败', sub: 'fallback to backend api' },
}
const phaseTitle = computed(() => phaseMap[progress.value.phase]?.title || '加载中')
const phaseSub = computed(() => phaseMap[progress.value.phase]?.sub || '')
const percentLabel = computed(() => {
  if (progress.value.phase === 'parsing' || progress.value.phase === 'done') return '100%'
  if (progress.value.ratio == null) return ''
  return `${Math.round(progress.value.ratio * 100)}%`
})
function byteLabel(n) {
  if (!n) return '0 B'
  const units = ['B', 'KB', 'MB', 'GB']
  let i = 0
  let v = n
  while (v >= 1024 && i < units.length - 1) { v /= 1024; i += 1 }
  return `${v.toFixed(v >= 100 || i === 0 ? 0 : 1)} ${units[i]}`
}

const aiOpen = ref(false)
const messages = ref([])
const input = ref('')
const sending = ref(false)
const messagesEl = ref(null)

const usage = ref({ found: false, content: '', mtime: 0 })
const usageBusy = ref(false)
const usageLoading = ref(false)
const usageError = ref('')

const isPlugin = computed(() => props.kind === 'plugin')
const kindLabel = computed(() => (isPlugin.value ? '插件' : '模块'))
const status = computed(() => itemStatus(item.value))

const quickPrompts = computed(() => (isPlugin.value
  ? [
      '这个插件是做什么的？怎么在项目里启用？',
      '给出一个最小 C++ 或蓝图使用示例',
      '使用时有哪些常见坑和注意事项？',
    ]
  : [
      '这个模块在引擎里承担什么角色？',
      '如何在 Build.cs 里依赖它？给出示例',
      '典型使用场景有哪些？',
    ]))

const descriptionParagraphs = computed(() =>
  (item.value?.description || '').split(/\n+/).map(s => s.trim()).filter(Boolean))

const usageMtime = computed(() => (
  usage.value.found && usage.value.mtime
    ? new Date(usage.value.mtime * 1000).toLocaleString('zh-CN', { hour12: false })
    : ''
))

async function loadUsage() {
  usageError.value = ''
  usageLoading.value = true
  try {
    await ensureUsageFb()
    const fromFb = toUsageDoc(getUsageDoc(props.kind, props.slug))
    if (fromFb?.found) {
      usage.value = fromFb
      return
    }
    usage.value = await UsageDocAPI.get(props.kind, props.slug)
  } catch (err) {
    usageError.value = errMsg(err)
  } finally {
    usageLoading.value = false
  }
}

async function generateUsage() {
  if (usageBusy.value || !item.value) return
  usageBusy.value = true
  usageError.value = ''
  await streamUsageBatch(
    { kind: props.kind, slugs: [props.slug], overwrite: true },
    {
      onFrame: (frame) => {
        if (frame.type !== 'item') return
        if (frame.status === 'ok') {
          UsageDocAPI.get(props.kind, props.slug)
            .then((doc) => { usage.value = doc })
            .catch(() => loadUsage())
        } else usageError.value = frame.error || '生成失败'
      },
      onError: (err) => {
        usageError.value = '连接中断：' + errMsg(err)
      },
    },
  )
  usageBusy.value = false
}

async function load() {
  const id = ++requestId
  loading.value = true
  error.value = ''
  item.value = null
  messages.value = []
  aiOpen.value = false
  usageBusy.value = false
  usageLoading.value = true
  usageError.value = ''
  try {
    await ensureUsageFb()
    const fromFb = itemFromUsageFb(props.kind, props.slug)
    if (fromFb && id === requestId) {
      item.value = fromFb
      loadUsage()
      const overlay = isPlugin.value
        ? ItemsAPI.getPlugin(props.slug)
        : ItemsAPI.getModule(props.slug)
      overlay.then((apiItem) => {
        if (id !== requestId) return
        item.value = {
          ...fromFb,
          ...apiItem,
          usage_doc: Boolean(fromFb.usage_doc) || Boolean(apiItem.usage_doc),
          in_source: true,
        }
      }).catch(() => {})
      return
    }
    const data = isPlugin.value
      ? await ItemsAPI.getPlugin(props.slug)
      : await ItemsAPI.getModule(props.slug)
    if (id === requestId) {
      if (!data) throw new Error('未找到该条目')
      item.value = data
      loadUsage()
    }
  } catch (err) {
    if (id === requestId) error.value = errMsg(err)
  } finally {
    if (id === requestId) loading.value = false
  }
}

watch(() => [props.kind, props.slug], load, { immediate: true })

function scrollToBottom() {
  nextTick(() => {
    if (messagesEl.value) messagesEl.value.scrollTop = messagesEl.value.scrollHeight
  })
}

async function send(text) {
  const message = (text ?? input.value).trim()
  if (!message || sending.value || !item.value) return

  const history = messages.value
    .filter(m => !m.streaming && m.content)
    .map(m => [m.role, m.content])

  input.value = ''
  messages.value.push({ role: 'user', content: message })
  const index = messages.value.push({ role: 'assistant', content: '', streaming: true }) - 1
  sending.value = true
  scrollToBottom()

  await streamAiChat(
    { kind: props.kind, slug: props.slug, message, history },
    {
      onChunk: (piece) => {
        messages.value[index].content += piece
        scrollToBottom()
      },
      onError: (err) => {
        messages.value[index].content += `\n\n⚠ ${err.message}`
      },
    },
  )

  messages.value[index].streaming = false
  if (!messages.value[index].content) {
    messages.value[index].content = '（没有收到回复）'
  }
  sending.value = false
  scrollToBottom()
}

function openAi(prompt) {
  aiOpen.value = true
  if (prompt) send(prompt)
}

function clearChat() {
  if (sending.value) return
  messages.value = []
}

function goRelated(kind, slug) {
  if (!slug) return
  router.push({ name: kind === 'module' ? 'module' : 'plugin', params: { slug } })
}

function slugTitle(s) {
  return (s || '').replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

function tagClass(type) {
  if (type === 'Editor') return 'editor'
  if (type === 'Runtime') return 'runtime'
  return ''
}
</script>

<template>
  <div v-if="loading" class="detail-skeleton" aria-busy="true" aria-live="polite">
    <div class="load-card is-compact" :data-phase="progress.phase">
      <div class="load-head">
        <span class="load-spinner" aria-hidden="true"></span>
        <div class="load-text">
          <div class="load-title">{{ phaseTitle }}</div>
          <div class="load-sub">{{ phaseSub }}</div>
        </div>
        <span v-if="percentLabel" class="load-pct">{{ percentLabel }}</span>
      </div>
      <div class="load-track">
        <div
          class="load-fill"
          :class="{ indeterminate: progress.ratio == null }"
          :style="{ width: progress.ratio != null ? (progress.ratio * 100).toFixed(1) + '%' : '' }"
        ></div>
      </div>
      <div class="load-meta">
        <span>已接收 <b>{{ byteLabel(progress.received) }}</b><template v-if="progress.total"> / {{ byteLabel(progress.total) }}</template></span>
        <span v-if="progress.rate">速率 <b>{{ byteLabel(progress.rate) }}/s</b></span>
      </div>
    </div>
    <div class="sk-block sk-title"></div>
    <div class="sk-block sk-meta"></div>
    <div class="sk-block sk-body"></div>
  </div>

  <div v-else-if="error" class="banner banner-error">加载失败：{{ error }}</div>

  <div v-else-if="item" class="detail">
    <nav class="crumb">
      <router-link :to="{ name: 'home' }">Index</router-link>
      <span class="sep">//</span>
      <router-link class="crumb-kind" :to="{ name: 'home', hash: isPlugin ? '#plugins' : '#modules' }">
        {{ isPlugin ? 'Plugins' : 'Modules' }}
      </router-link>
      <span class="sep">//</span>
      <span class="current">{{ item.name }}</span>
    </nav>

    <section class="detail-head">
      <div class="detail-head-main">
        <div class="kicker">
          <span class="kicker-dot"></span>
          {{ isPlugin ? 'Plugin / 插件' : 'Module / 模块' }}
          <span class="kicker-dim">/ Source Entry</span>
        </div>

        <h1 class="detail-title">{{ item.name }}</h1>

        <div class="hero-tags">
          <span v-if="item.category" class="chip chip-light chip-lime">{{ item.category }}</span>
          <span v-if="!isPlugin" class="chip chip-light">
            <span class="module-type-dot" :class="{ editor: item.type === 'Editor' }" style="margin-right: 6px;"></span>
            {{ item.type }}
          </span>
          <span v-if="isPlugin && item.version_name" class="chip chip-light mono">v{{ item.version_name }}</span>
          <span v-if="isPlugin && item.author" class="chip chip-light">{{ item.author }}</span>
          <span v-if="!isPlugin && item.platform" class="chip chip-light">{{ item.platform }}</span>
          <span class="chip chip-light mono">SLUG / {{ props.slug }}</span>
          <span v-if="status === 'gone'" class="chip chip-light chip-rose">源码已删</span>
          <span v-else-if="status === 'missing'" class="chip chip-light chip-warning">未生成用法</span>
          <span v-else class="chip chip-light chip-success">已生成用法</span>
        </div>
      </div>

        <div class="detail-actions">
          <button class="btn" :disabled="usageBusy" @click="generateUsage">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z" />
            </svg>
            {{ usageBusy ? '生成中…' : (usage.found ? '重新生成用法' : 'AI 生成用法') }}
          </button>
          <button class="btn btn-lime" @click="openAi(quickPrompts[0])">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z" />
              <path d="M19 17l.8 2.2L22 20l-2.2.8L19 23l-.8-2.2L16 20l2.2-.8z" />
            </svg>
            AI 讲解用法
          </button>
        </div>
    </section>

    <div v-if="status === 'gone'" class="banner banner-gone">
      当前 UE 源码里已经找不到这个{{ kindLabel }}，目录里仍保留历史条目，用法仅供参考。
    </div>
    <div v-else-if="status === 'missing'" class="banner banner-warn is-missing">
      还没有 AI 生成的《使用方法》。可以在本页或设置里批量补全。
    </div>

    <section class="meta-console" aria-label="元数据">
      <div class="meta-grid">
        <template v-if="isPlugin">
          <div class="meta-item">
            <div class="meta-label">Version</div>
            <div class="meta-value mono">{{ item.version_name || item.version || '—' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Author</div>
            <div class="meta-value">{{ item.author || '—' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Engine</div>
            <div class="meta-value mono orange">{{ item.engine_version || '—' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Modules</div>
            <div class="meta-value mono">{{ item.modules.length }}</div>
          </div>
        </template>
        <template v-else>
          <div class="meta-item">
            <div class="meta-label">Type</div>
            <div class="meta-value">{{ item.type }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Base rules</div>
            <div class="meta-value mono">{{ item.base }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Platform</div>
            <div class="meta-value">{{ item.platform || '通用' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Dependencies</div>
            <div class="meta-value mono">{{ item.public_deps.length + item.private_deps.length }}</div>
          </div>
        </template>
      </div>

      <div class="meta-source">
        <span class="label">{{ isPlugin ? 'Plugin file' : 'Build file' }}</span>
        <span class="file-path">{{ item.path }}</span>
      </div>
    </section>

    <div class="content-grid">
      <div class="content-main">
        <section class="paper-card">
          <div class="card-title">
            <span class="card-title-sep">01</span>
            描述 <span class="serif">Description</span>
          </div>
          <div class="desc-body">
            <p v-for="(para, i) in descriptionParagraphs" :key="i">{{ para }}</p>
            <p v-if="!descriptionParagraphs.length" class="muted">
              源码中没有提供描述。点击右上角「AI 讲解用法」，由 AI 根据元数据给出说明。
            </p>
          </div>
        </section>

        <section class="paper-card">
          <div class="card-title">
            <span class="card-title-sep">02</span>
            使用方法 <span class="serif">Usage</span>
            <span v-if="status === 'gone'" class="chip chip-light chip-rose" style="margin-left: auto;">
              源码已删
            </span>
            <span v-else-if="usage.found" class="chip chip-light chip-success" style="margin-left: auto;">
              已生成 · {{ usageMtime }}
            </span>
            <span v-else class="chip chip-light chip-warning" style="margin-left: auto;">
              未生成用法
            </span>
          </div>
          <div v-if="usageLoading && !usage.found" class="usage-loading" aria-busy="true">
            <div class="load-track"><div class="load-fill indeterminate"></div></div>
            <p class="muted" style="margin-top: 10px;">正在从 usage.fb 载入该条目的用法…</p>
          </div>
          <div v-else-if="usageBusy && !usage.found" class="usage-loading" aria-busy="true">
            <div class="load-track"><div class="load-fill indeterminate"></div></div>
            <p class="muted" style="margin-top: 10px;">AI 正在撰写《使用方法》… 生成完成后会自动刷新。</p>
          </div>
          <div v-else-if="usageError" class="banner banner-error" style="margin-top: var(--space-3);">
            {{ usageError }}
          </div>
          <div v-else-if="usage.found" class="md usage-body" v-html="renderMarkdown(usage.content)"></div>
          <div v-else class="desc-body usage-empty">
            <p class="muted">
              还没有《使用方法》文档。点击下方按钮，AI 会结合源码元数据写一份可直接上手的说明，
              并写入后端 <span class="mono">usage_docs_root</span> 目录（
              <span class="mono">{{ isPlugin ? 'plugins' : 'modules' }}/{{ props.slug }}.md</span>）。
            </p>
            <button class="btn btn-lime" :disabled="usageBusy" @click="generateUsage">
              {{ usageBusy ? '生成中…' : 'AI 生成使用方法' }}
            </button>
          </div>
        </section>

        <section class="paper-card">
          <div class="card-title">
            <span class="card-title-sep">03</span>
            AI 使用指南 <span class="serif">Guide</span>
            <span class="card-title-cn" style="margin-left: auto;">由 AI 生成，请以官方文档为准</span>
          </div>
          <div class="ai-quick-list">
            <span class="quick-label">Suggested</span>
            <button v-for="q in quickPrompts" :key="q" class="prompt-btn" @click="openAi(q)">
              <span class="prompt-text">{{ q }}</span>
            </button>
          </div>
        </section>
      </div>

      <aside class="detail-side">
        <div class="side-console usage-console">
          <div class="side-title">
            <span>Usage doc</span>
            <span class="count">{{ usage.found ? 'READY' : 'EMPTY' }}</span>
          </div>
          <div class="side-deps">
            <span class="usage-chip" :class="{ 'is-missing': !usage.found }">
              {{ usage.found ? '已生成使用方法' : '尚未生成' }}
            </span>
          </div>
          <div class="side-usage-meta">
            <span>{{ usage.found ? '最后更新' : '建议操作' }}</span>
            <b>{{ usage.found ? usageMtime : 'AI 生成' }}</b>
          </div>
          <div v-if="!usage.found" class="side-note" style="margin-top: 10px;">
            点击下方按钮，AI 会结合源码元数据写一份可直接上手的说明，并保存到
            <span class="mono">{{ isPlugin ? 'plugins' : 'modules' }}/{{ props.slug }}.md</span>。
          </div>
        </div>

        <div v-if="isPlugin" class="side-console">
          <div class="side-title">
            <span>Modules</span>
            <span class="count">{{ item.modules.length }}</span>
          </div>
          <div v-if="!item.modules.length" class="side-empty">无模块</div>
          <div v-for="m in item.modules" :key="m.name" class="side-row">
            <span class="dot" :class="{ editor: m.type === 'Editor' }"></span>
            <span class="name" :title="m.name">{{ m.name }}</span>
            <span class="tag" :class="tagClass(m.type)">{{ m.type }}</span>
          </div>
        </div>

        <template v-else>
          <div class="side-console">
            <div class="side-title">
              <span>Public deps</span>
              <span class="count">{{ item.public_deps.length }}</span>
            </div>
            <div class="side-deps">
              <span
                v-for="d in item.public_deps"
                :key="d"
                class="chip chip-lime mono is-link"
                role="link"
                tabindex="0"
                :title="`打开模块 ${d}`"
                @click="openRelated(d)"
                @keydown.enter="openRelated(d)"
              >{{ d }}</span>
              <span v-if="!item.public_deps.length" class="chip is-empty">无</span>
            </div>
          </div>
          <div class="side-console">
            <div class="side-title">
              <span>Private deps</span>
              <span class="count">{{ item.private_deps.length }}</span>
            </div>
            <div class="side-deps">
              <span
                v-for="d in item.private_deps"
                :key="d"
                class="chip chip-lime mono is-link"
                role="link"
                tabindex="0"
                :title="`打开模块 ${d}`"
                @click="openRelated(d)"
                @keydown.enter="openRelated(d)"
              >{{ d }}</span>
              <span v-if="!item.private_deps.length" class="chip is-empty">无</span>
            </div>
          </div>
        </template>

        <div class="side-console">
          <div class="side-title">
            <span>Source</span>
            <span class="count">PATH</span>
          </div>
          <div class="side-note">
            由后端扫描 <span class="mono">{{ item.path }}</span> 生成，路径相对于设置中的 engine_root。
          </div>
        </div>
      </aside>
    </div>
  </div>

  <button v-if="item && !aiOpen" class="ai-trigger" aria-label="AI 助手" @click="aiOpen = true">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z" />
      <path d="M19 17l.8 2.2L22 20l-2.2.8L19 23l-.8-2.2L16 20l2.2-.8z" />
    </svg>
  </button>

  <div v-if="item && aiOpen" class="ai-panel">
    <div class="ai-header">
      <span class="mini-dot" aria-hidden="true"></span>
      <div style="min-width: 0; flex: 1;">
        <div class="ai-header-title">AI 使用助手</div>
        <div class="ai-header-sub" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          {{ isPlugin ? 'PLUGIN' : 'MODULE' }} · {{ item.name }}
        </div>
      </div>
      <button class="ai-icon-btn" title="清空对话" :disabled="sending" @click="clearChat">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6" /><path d="M19 6l-1 14H6L5 6" /><path d="M10 11v6M14 11v6" /></svg>
      </button>
      <button class="ai-icon-btn" title="收起" @click="aiOpen = false">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" /></svg>
      </button>
    </div>

    <div ref="messagesEl" class="ai-messages">
      <div v-if="!messages.length" class="ai-msg assistant empty">
        问我关于这个{{ kindLabel }}的用途、依赖、示例或常见坑。
      </div>
      <div
        v-for="(m, i) in messages"
        :key="i"
        class="ai-msg"
        :class="[m.role, { md: m.role === 'assistant', 'ai-typing': m.streaming && m.content }]"
      >
        <template v-if="m.role === 'assistant'">
          <span v-if="!m.content && m.streaming" class="ai-thinking"><span></span><span></span><span></span></span>
          <div v-else v-html="renderMarkdown(m.content)"></div>
        </template>
        <template v-else>{{ m.content }}</template>
      </div>
    </div>

    <div v-if="!messages.length" class="ai-quick-list ai-quick-panel">
      <button v-for="q in quickPrompts" :key="q" class="prompt-btn" @click="send(q)">{{ q }}</button>
    </div>

    <div class="ai-input-wrap">
      <input
        v-model="input"
        class="ai-input"
        placeholder="输入问题，回车发送"
        @keydown.enter.prevent="send()"
      />
      <button class="ai-send" :disabled="sending || !input.trim()" aria-label="发送" @click="send()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13" /><polygon points="22 2 15 22 11 13 2 9 22 2" /></svg>
      </button>
    </div>
  </div>
</template>