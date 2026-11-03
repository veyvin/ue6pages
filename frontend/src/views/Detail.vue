<script setup>
import { computed, nextTick, ref, watch } from 'vue'
import { ItemsAPI, errMsg } from '../api/client.js'
import { streamAiChat } from '../api/ai.js'
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

async function load() {
  const id = ++requestId
  loading.value = true
  error.value = ''
  item.value = null
  messages.value = []
  aiOpen.value = false
  try {
    const data = isPlugin.value
      ? await ItemsAPI.getPlugin(props.slug)
      : await ItemsAPI.getModule(props.slug)
    if (id === requestId) item.value = data
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
</script>

<template>
  <div v-if="loading" class="empty">加载中…</div>

  <div v-else-if="error" class="banner banner-error">加载失败：{{ error }}</div>

  <div v-else-if="item" class="detail">
    <nav class="crumb">
      <router-link :to="{ name: 'home', hash: isPlugin ? '#plugins' : '#modules' }">
        {{ isPlugin ? 'Plugins 插件' : 'Modules 模块' }}
      </router-link>
      <span class="sep">/</span>
      <span class="current mono">{{ item.name }}</span>
    </nav>

    <section class="hero" style="margin-top: var(--space-4);">
      <div class="hero-top">
        <div class="hero-badge">{{ item.name.charAt(0).toUpperCase() }}</div>
        <div class="hero-info">
          <div class="hero-subtitle">{{ isPlugin ? 'Plugin · 插件' : 'Module · 模块' }}</div>
          <div class="hero-title">{{ item.name }}</div>
          <div class="hero-tags">
            <span v-if="item.category" class="chip chip-primary">{{ item.category }}</span>
            <span v-if="!isPlugin" class="chip">{{ item.type }}</span>
            <span v-if="isPlugin && item.version_name" class="chip mono">v{{ item.version_name }}</span>
            <span v-if="isPlugin && item.author" class="chip">{{ item.author }}</span>
            <span v-if="!isPlugin && item.platform" class="chip">{{ item.platform }}</span>
          </div>
        </div>
        <div class="hero-actions">
          <button class="btn btn-primary" @click="openAi(quickPrompts[0])">
            ✦ AI 讲解用法
          </button>
        </div>
      </div>

      <div class="meta-grid">
        <template v-if="isPlugin">
          <div class="meta-item">
            <div class="meta-label">Version / 版本</div>
            <div class="meta-value mono">{{ item.version_name || item.version || '—' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Author / 作者</div>
            <div class="meta-value">{{ item.author || '—' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Engine / 引擎</div>
            <div class="meta-value mono">{{ item.engine_version || '—' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Modules / 模块数</div>
            <div class="meta-value mono">{{ item.modules.length }}</div>
          </div>
        </template>
        <template v-else>
          <div class="meta-item">
            <div class="meta-label">Type / 类型</div>
            <div class="meta-value">{{ item.type }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Base rules / 基类</div>
            <div class="meta-value mono">{{ item.base }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Platform / 平台</div>
            <div class="meta-value">{{ item.platform || '通用' }}</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Dependencies / 依赖</div>
            <div class="meta-value mono">{{ item.public_deps.length + item.private_deps.length }}</div>
          </div>
        </template>
        <div class="meta-item wide">
          <div class="meta-label">{{ isPlugin ? 'Plugin file / 插件文件' : 'Build file / 构建文件' }}</div>
          <div class="file-path mono" style="margin-top: 4px; font-size: 12px;">{{ item.path }}</div>
        </div>
      </div>
    </section>

    <div class="content-grid">
      <div>
        <section class="card">
          <div class="card-title">
            <span class="card-title-sep"></span>
            Description <span class="card-title-cn">描述</span>
          </div>
          <div class="desc-body">
            <p v-for="(para, i) in descriptionParagraphs" :key="i">{{ para }}</p>
            <p v-if="!descriptionParagraphs.length" style="color: var(--on-surface-muted);">
              源码中没有提供描述。点击右上角「AI 讲解用法」，由 AI 根据元数据给出说明。
            </p>
          </div>
        </section>

        <section class="card">
          <div class="card-title">
            <span class="card-title-sep"></span>
            AI 使用指南 <span class="card-title-cn">由 AI 生成，请以官方文档为准</span>
          </div>
          <div class="ai-quick-list">
            <button v-for="q in quickPrompts" :key="q" class="ai-quick-btn" @click="openAi(q)">
              {{ q }}
            </button>
          </div>
        </section>
      </div>

      <aside class="detail-sidebar">
        <div v-if="isPlugin" class="sidebar-card">
          <div class="sidebar-card-title">Modules ({{ item.modules.length }})</div>
          <div v-if="!item.modules.length" style="font-size: 13px; color: var(--on-surface-muted);">无模块</div>
          <div v-for="m in item.modules" :key="m.name" class="module-item">
            <span class="dot" :style="m.type === 'Editor' ? 'background: var(--warning)' : ''"></span>
            <span class="name mono">{{ m.name }}</span>
            <span class="tag" :class="m.type.toLowerCase()">{{ m.type }}</span>
          </div>
        </div>

        <template v-else>
          <div class="sidebar-card">
            <div class="sidebar-card-title">Public deps ({{ item.public_deps.length }})</div>
            <div v-if="!item.public_deps.length" style="font-size: 13px; color: var(--on-surface-muted);">无</div>
            <div v-else class="dep-list">
              <span v-for="d in item.public_deps" :key="d" class="chip mono">{{ d }}</span>
            </div>
          </div>
          <div class="sidebar-card">
            <div class="sidebar-card-title">Private deps ({{ item.private_deps.length }})</div>
            <div v-if="!item.private_deps.length" style="font-size: 13px; color: var(--on-surface-muted);">无</div>
            <div v-else class="dep-list">
              <span v-for="d in item.private_deps" :key="d" class="chip mono">{{ d }}</span>
            </div>
          </div>
        </template>

        <div class="sidebar-card">
          <div class="sidebar-card-title">Source / 来源</div>
          <div style="font-size: 12px; color: var(--on-surface-variant); line-height: 1.6;">
            由后端扫描 <span class="mono">{{ item.path }}</span> 生成，
            路径相对于设置中的 engine_root。
          </div>
        </div>
      </aside>
    </div>
  </div>

  <button v-if="item && !aiOpen" class="ai-trigger" aria-label="AI 助手" @click="aiOpen = true">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 17l.8 2.2L22 20l-2.2.8L19 23l-.8-2.2L16 20l2.2-.8z"/></svg>
  </button>

  <div v-if="item && aiOpen" class="ai-panel">
    <div class="ai-header">
      <div style="min-width: 0; flex: 1;">
        <div class="ai-header-title">AI 使用助手</div>
        <div class="ai-header-sub mono" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          {{ kindLabel }} · {{ item.name }}
        </div>
      </div>
      <button class="ai-icon-btn" title="清空对话" :disabled="sending" @click="clearChat">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6M14 11v6"/></svg>
      </button>
      <button class="ai-icon-btn" title="收起" @click="aiOpen = false">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
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
      <button v-for="q in quickPrompts" :key="q" class="ai-quick-btn" @click="send(q)">{{ q }}</button>
    </div>

    <div class="ai-input-wrap">
      <input
        v-model="input"
        class="ai-input"
        placeholder="输入问题，回车发送"
        @keydown.enter.prevent="send()"
      />
      <button class="ai-send" :disabled="sending || !input.trim()" aria-label="发送" @click="send()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
      </button>
    </div>
  </div>
</template>
