<script setup>
import { computed, nextTick, ref, watch } from 'vue'
import { ItemsAPI, UsageDocAPI, errMsg } from '../api/client.js'
import { streamAiChat, streamUsageBatch } from '../api/ai.js'
import { renderMarkdown } from '../utils/markdown.js'

const props = defineProps({
  kind: { type: String, required: true },
  slug: { type: String, required: true },
})

const item = ref(null)
const loading = ref(false)
const error = ref('')
let requestId = 0

const aiOpen = ref(false)
const messages = ref([])
const input = ref('')
const sending = ref(false)
const messagesEl = ref(null)

const usage = ref({ found: false, content: '', mtime: 0 })
const usageBusy = ref(false)
const usageError = ref('')

const isPlugin = computed(() => props.kind === 'plugin')
const kindLabel = computed(() => (isPlugin.value ? '插件' : '模块'))

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
  try {
    usage.value = await UsageDocAPI.get(props.kind, props.slug)
  } catch (err) {
    usageError.value = errMsg(err)
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
        if (frame.status === 'ok') loadUsage()
        else usageError.value = frame.error || '生成失败'
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
  usageError.value = ''
  try {
    const data = isPlugin.value
      ? await ItemsAPI.getPlugin(props.slug)
      : await ItemsAPI.getModule(props.slug)
    if (id === requestId) {
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

function tagClass(type) {
  if (type === 'Editor') return 'editor'
  if (type === 'Runtime') return 'runtime'
  return ''
}
</script>

<template>
  <div v-if="loading" class="empty">加载中…</div>

  <div v-else-if="error" class="banner banner-error">加载失败：{{ error }}</div>

  <div v-else-if="item" class="detail">
    <nav class="crumb">
      <router-link :to="{ name: 'home' }">Index</router-link>
      <span class="sep">//</span>
      <router-link :to="{ name: 'home', hash: isPlugin ? '#plugins' : '#modules' }">
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
          <span v-if="!isPlugin" class="chip chip-light">{{ item.type }}</span>
          <span v-if="isPlugin && item.version_name" class="chip chip-light mono">v{{ item.version_name }}</span>
          <span v-if="isPlugin && item.author" class="chip chip-light">{{ item.author }}</span>
          <span v-if="!isPlugin && item.platform" class="chip chip-light">{{ item.platform }}</span>
          <span class="chip chip-light">SLUG / {{ props.slug }}</span>
        </div>
      </div>

      <div class="detail-actions">
        <button class="btn" :disabled="usageBusy" @click="generateUsage">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z" />
          </svg>
          {{ usageBusy ? '生成中…' : (usage.found ? '重新生成使用方法' : 'AI 生成使用方法') }}
        </button>
        <button class="btn btn-lime" @click="openAi(quickPrompts[0])">
          ✦ AI 讲解用法
        </button>
      </div>
    </section>

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
            <span v-if="usage.found" class="chip chip-light chip-success" style="margin-left: auto;">
              已生成 · {{ usageMtime }}
            </span>
          </div>
          <div v-if="usageError" class="banner banner-error" style="margin-top: var(--space-3);">
            {{ usageError }}
          </div>
          <div v-else-if="usage.found" class="md usage-body" v-html="renderMarkdown(usage.content)"></div>
          <div v-else class="desc-body">
            <p class="muted">
              还没有《使用方法》文档。点击右上角「AI 生成使用方法」，文档会写入后端
              <span class="mono">usage_docs_root</span> 目录（<span class="mono">{{ isPlugin ? 'plugins' : 'modules' }}/{{ props.slug }}.md</span>）。
            </p>
          </div>
        </section>

        <section class="paper-card">
          <div class="card-title">
            <span class="card-title-sep">03</span>
            AI 使用指南 <span class="serif">Guide</span>
            <span class="card-title-cn" style="margin-left: auto;">由 AI 生成，请以官方文档为准</span>
          </div>
          <div class="ai-quick-list">
            <button v-for="q in quickPrompts" :key="q" class="prompt-btn" @click="openAi(q)">
              {{ q }}
            </button>
          </div>
        </section>
      </div>

      <aside class="detail-side">
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
            <div v-if="!item.public_deps.length" class="side-empty">无</div>
            <div v-else class="dep-list">
              <span v-for="d in item.public_deps" :key="d" class="chip chip-lime mono">{{ d }}</span>
            </div>
          </div>
          <div class="side-console">
            <div class="side-title">
              <span>Private deps</span>
              <span class="count">{{ item.private_deps.length }}</span>
            </div>
            <div v-if="!item.private_deps.length" class="side-empty">无</div>
            <div v-else class="dep-list">
              <span v-for="d in item.private_deps" :key="d" class="chip chip-lime mono">{{ d }}</span>
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
          <span v-if="!m.content && m.streaming">正在思考…</span>
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
