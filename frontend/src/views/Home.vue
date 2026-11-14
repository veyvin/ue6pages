<script setup>
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useItemsStore } from '../stores/items.js'
import { itemStatus, onUsageFbProgress, estimateHint } from '../api/usageFb.js'
import { useDragScroll } from '../composables/useDragScroll.js'

const PAGE_SIZE = 60
const store = useItemsStore()
const {
  el: catScroll,
  canStart: catCanStart,
  canEnd: catCanEnd,
  updateEdges: updateCatEdges,
  onPointerDown: onCatPointerDown,
  onPointerMove: onCatPointerMove,
  onPointerUp: onCatPointerUp,
  onPointerCancel: onCatPointerCancel,
  onClickCapture: onCatClickCapture,
  onScroll: onCatScroll,
} = useDragScroll()

const pluginLimit = ref(PAGE_SIZE)
const moduleLimit = ref(PAGE_SIZE)

const progress = ref({ phase: 'idle', received: 0, total: 0, ratio: null, rate: 0, url: '' })
let stopProgress = null
onMounted(() => { stopProgress = onUsageFbProgress((p) => { progress.value = p }) })
onBeforeUnmount(() => { stopProgress?.() })

const phaseMap = {
  idle: { title: '准备加载数据包', sub: 'connecting to usage.fb index' },
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

const stepOrder = ['connect', 'download', 'parse', 'ready']
const currentStep = computed(() => {
  switch (progress.value.phase) {
    case 'connecting': return 'connect'
    case 'downloading': return 'download'
    case 'parsing': return 'parse'
    case 'done': return 'ready'
    default: return 'connect'
  }
})
function stepClass(step) {
  const cur = currentStep.value
  if (step === cur) return 'is-active'
  return stepOrder.indexOf(step) < stepOrder.indexOf(cur) ? 'is-done' : ''
}

function byteLabel(n) {
  if (!n) return '0 B'
  const units = ['B', 'KB', 'MB', 'GB']
  let i = 0
  let v = n
  while (v >= 1024 && i < units.length - 1) { v /= 1024; i += 1 }
  return `${v.toFixed(v >= 100 || i === 0 ? 0 : 1)} ${units[i]}`
}
function shortHost(url) {
  try {
    const u = new URL(url, location.origin)
    const path = u.pathname.split('/').filter(Boolean).pop() || ''
    return `${u.host}${path ? ' / ' + path : ''}`
  } catch {
    return url
  }
}

const visiblePlugins = computed(() => store.filteredPlugins.slice(0, pluginLimit.value))
const visibleModules = computed(() => store.filteredModules.slice(0, moduleLimit.value))

watch(() => [store.query, store.category, store.status], () => {
  pluginLimit.value = PAGE_SIZE
  moduleLimit.value = PAGE_SIZE
})

watch(() => store.categories.length, () => updateCatEdges())

const totalItems = computed(() =>
  (store.stats?.total_plugins ?? 0) + (store.stats?.total_modules ?? 0))

const ratio = computed(() => {
  if (!totalItems.value) return 22
  const raw = ((store.stats?.total_plugins ?? 0) / totalItems.value) * 100
  return Math.max(20, Math.min(94, Math.round(raw)))
})

function initial(name) {
  return (name || '?').trim().charAt(0).toUpperCase()
}

function cardNo(index) {
  return String(index + 1).padStart(2, '0')
}

function isWide(index) {
  return index === 0 || index % 7 === 3
}

function resetFilters() {
  store.query = ''
  store.category = ''
  store.status = ''
}

function cardClass(item, index) {
  const status = itemStatus(item)
  return {
    'span-2': isWide(index),
    'is-missing': status === 'missing',
    'is-gone': status === 'gone',
  }
}

function moduleCardClass(item) {
  const status = itemStatus(item)
  return {
    editor: item.type === 'Editor',
    'is-missing': status === 'missing',
    'is-gone': status === 'gone',
  }
}

function statusLabel(item) {
  const status = itemStatus(item)
  if (status === 'gone') return '源码已删'
  if (status === 'missing') return '未生成用法'
  return '已生成用法'
}

function typeClass(type) {
  if (type === 'Editor') return 'editor'
  if (type === 'Runtime') return 'runtime'
  return ''
}
</script>

<template>
  <section class="hero">
    <div class="hero-copy">
      <div class="kicker">
        <span class="kicker-dot"></span>
        Live from source
        <span class="kicker-dim">/ {{ store.stats?.engine_version || 'UNREAL ENGINE' }}</span>
      </div>

      <h1 class="hero-title">
        <span class="line"><span>插件</span><span class="en">Plugins</span></span>
        <span class="line"><span>模块</span><span class="en">Modules</span></span>
      </h1>

      <p class="hero-lede">
        从 <span class="hl mono">.uplugin</span> 到 <span class="hl mono">*.Build.cs</span>，
        把引擎源码里的每一个插件与模块，整理成<span class="hl-lime">可检索、可讲解</span>的说明书。
        <em>Read it. Use it. Ship it.</em>
      </p>

      <div class="hero-annot">About / UE Docs</div>

      <div class="hero-actions">
        <a class="pill-play" href="#plugins">
          <span class="play" aria-hidden="true">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z" /></svg>
          </span>
          <span>浏览插件索引</span>
        </a>
        <router-link class="btn btn-dark" :to="{ name: 'settings' }">设置引擎路径</router-link>
      </div>
    </div>

    <div class="hero-object">
      <div class="keycap-scene" aria-hidden="true">
        <div class="keycap-aura"></div>
        <div class="keycap">
          <span class="keycap-legend">UE</span>
          <span class="keycap-sub">F1</span>
        </div>
      </div>

      <div class="object-caption">Tactile / Source / Docs</div>
    </div>
  </section>

  <section aria-label="扫描统计">
    <div v-if="store.error" class="banner banner-error" style="margin-bottom: 18px;">
      无法连接后端：{{ store.error }}。请确认后端已启动（backend 目录下
      <span class="mono">uvicorn backend.app:app --port 8001</span>），或到
      <router-link to="/settings">设置</router-link> 检查引擎路径。
    </div>

    <div
      v-if="!store.stats && store.loading"
      class="console-card load-card is-compact"
      :data-phase="progress.phase"
      aria-busy="true"
      aria-live="polite"
    >
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
        <span v-if="progress.url"><b>{{ shortHost(progress.url) }}</b></span>
      </div>
      <p class="load-hint">{{ estimateHint() }}</p>
      <div class="load-steps">
        <span class="load-step" :class="stepClass('connect')">连接</span>
        <span class="load-step" :class="stepClass('download')">下载 usage.fb</span>
        <span class="load-step" :class="stepClass('parse')">解析索引</span>
        <span class="load-step" :class="stepClass('ready')">合并数据</span>
      </div>
    </div>

    <div class="console-card">      <div class="console-top">
        <div class="stat-block">
          <div class="console-label">
            <span class="lb">01</span> Plugins / .uplugin
            <span class="live"><i></i>live</span>
          </div>
          <div class="stat-value">{{ store.stats?.total_plugins ?? '—' }}</div>
          <div class="stat-sub">已扫描的插件条目</div>
        </div>

        <div class="stat-block">
          <div class="console-label">
            <span class="lb">02</span> Modules / .Build.cs
            <span class="live"><i></i>live</span>
          </div>
          <div class="stat-value">{{ store.stats?.total_modules ?? '—' }}</div>
          <div class="stat-sub">已扫描的模块构建文件</div>
        </div>

        <div class="console-panel">
          <div class="console-row">
            <span class="label">Engine</span>
            <span class="value orange">{{ store.stats?.engine_version || 'UE5' }}</span>
          </div>
          <div class="divider"></div>
          <div class="console-row">
            <span class="label">Categories</span>
            <span class="value">{{ store.stats?.categories?.length ?? '—' }}</span>
          </div>
          <div class="console-row">
            <span class="label">Index status</span>
            <span class="value lime">{{ store.loading ? 'SCANNING' : 'READY' }}</span>
          </div>
          <div class="console-row">
            <span class="label">No usage</span>
            <span class="value orange">{{ store.statusCounts.missing }}</span>
          </div>
          <div class="console-row">
            <span class="label">Removed</span>
            <span class="value rose">{{ store.statusCounts.gone }}</span>
          </div>
          <div class="note">
            目录来自 usage.fb{{ store.catalogSource ? ` · ${store.catalogSource}` : '' }}
            · 橙：尚未 AI 生成使用方法 · 玫红：源码里已经删掉
          </div>
        </div>
      </div>

      <div class="console-foot">
        <div class="console-slider" :style="{ '--ratio': ratio }">
          <div class="slider-fill"></div>
          <div class="slider-thumb" aria-hidden="true">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="4" y1="12" x2="19" y2="12" />
              <polyline points="13 6 19 12 13 18" />
            </svg>
          </div>
        </div>
        <div class="console-ratio">
          <b>{{ totalItems }} Items</b>
          <span>P {{ store.stats?.total_plugins ?? 0 }} · M {{ store.stats?.total_modules ?? 0 }}</span>
        </div>
      </div>
    </div>
  </section>

  <section id="plugins">
    <div class="section-head">
      <div class="section-head-main">
        <div class="section-kicker"><span class="sk-num">02</span> <span class="sk-slash">/</span> Plugin Index</div>
        <h2 class="section-title">
          插件 <span class="serif">Plugins</span>
          <span class="title-cn-sub">{{ store.filteredPlugins.length }} 个</span>
        </h2>
      </div>
      <span class="count-pill">{{ visiblePlugins.length }} / {{ store.filteredPlugins.length }} Items</span>
    </div>

    <div class="filter-bar">
      <div
        ref="catScroll"
        class="filter-scroll"
        :class="{ 'has-start': catCanStart, 'has-end': catCanEnd }"
        @pointerdown="onCatPointerDown"
        @pointermove="onCatPointerMove"
        @pointerup="onCatPointerUp"
        @pointercancel="onCatPointerCancel"
        @click.capture="onCatClickCapture"
        @scroll="onCatScroll"
      >
        <div class="segmented" role="tablist" aria-label="插件分类">
          <button :class="{ active: !store.category }" @click="store.category = ''">全部</button>
          <button
            v-for="c in store.categories"
            :key="c"
            :class="{ active: store.category === c }"
            @click="store.category = c"
          >
            {{ c }}
          </button>
        </div>
      </div>
      <div class="filter-bar-meta">
        <div class="segmented status-seg" role="tablist" aria-label="条目状态">
          <button :class="{ active: !store.status }" @click="store.status = ''">全部</button>
          <button :class="{ active: store.status === 'missing' }" @click="store.status = 'missing'">
            未生成 {{ store.statusCounts.missing }}
          </button>
          <button :class="{ active: store.status === 'gone' }" @click="store.status = 'gone'">
            源码已删 {{ store.statusCounts.gone }}
          </button>
        </div>
        <button v-if="store.category || store.query || store.status" class="filter-clear" @click="resetFilters">
          重置 ⟲
        </button>
      </div>
    </div>

    <div v-if="store.loading && !store.plugins.length" class="list-skeleton" aria-hidden="true">
      <div v-for="n in 4" :key="n" class="list-skeleton-card">
        <div class="sk-row sk-dot"></div>
        <div class="sk-row sk-name"></div>
        <div class="sk-row sk-desc"></div>
        <div class="sk-row sk-tags"></div>
      </div>
    </div>
    <div v-else-if="!store.filteredPlugins.length" class="empty-card">
      <span class="empty-glyph">[ ∅ ]</span>
      <p class="empty-text">没有匹配的插件。清空搜索或切换分类，也可以到设置里更换 engine_root。</p>
      <button class="btn btn-dark" @click="resetFilters">重置检索条件</button>
    </div>
    <div v-else class="bento-grid">
      <router-link
        v-for="(p, i) in visiblePlugins"
        :key="p.slug"
        class="plugin-card"
        :class="cardClass(p, i)"
        :to="{ name: 'plugin', params: { slug: p.slug } }"
      >
        <div class="plugin-card-top">
          <div class="plugin-badge">{{ initial(p.name) }}</div>
          <div class="plugin-meta">
            <span class="card-no">No.{{ cardNo(i) }}</span>
            <span class="doc-badge" :class="'is-' + itemStatus(p)">{{ statusLabel(p) }}</span>
          </div>
        </div>

        <h3 class="plugin-name">{{ p.name }}</h3>
        <p class="plugin-desc">{{ p.description || '源码未提供描述，进入详情页可让 AI 讲解用法。' }}</p>

        <div class="plugin-foot">
          <span class="plugin-path" :title="p.path">{{ p.path }}</span>
          <span class="chip chip-lime">{{ p.category || 'General' }}</span>
        </div>

        <span class="card-sheen" aria-hidden="true"></span>
      </router-link>
    </div>

    <div v-if="store.filteredPlugins.length > pluginLimit" class="more">
      <button class="btn btn-dark" @click="pluginLimit += PAGE_SIZE">
        加载更多（剩余 {{ store.filteredPlugins.length - pluginLimit }}）
      </button>
    </div>
  </section>

  <section id="modules">
    <div class="section-head">
      <div class="section-head-main">
        <div class="section-kicker"><span class="sk-num">03</span> <span class="sk-slash">/</span> Module Index</div>
        <h2 class="section-title">
          模块 <span class="serif">Modules</span>
          <span class="title-cn-sub">{{ store.filteredModules.length }} 个</span>
        </h2>
      </div>
      <span class="count-pill">{{ visibleModules.length }} / {{ store.filteredModules.length }} Items</span>
    </div>

    <div class="filter-bar">
      <div class="segmented status-seg" role="tablist" aria-label="模块状态">
        <button :class="{ active: !store.status }" @click="store.status = ''">全部</button>
        <button :class="{ active: store.status === 'missing' }" @click="store.status = 'missing'">
          未生成 {{ store.statusCounts.missing }}
        </button>
        <button :class="{ active: store.status === 'gone' }" @click="store.status = 'gone'">
          源码已删 {{ store.statusCounts.gone }}
        </button>
      </div>
    </div>

    <div v-if="!store.filteredModules.length" class="empty-card">
      <span class="empty-glyph">[ — ]</span>
      <p class="empty-text">没有匹配的模块。试试清空搜索，或到设置里重新扫描 Engine/Source。</p>
    </div>
    <div v-else class="module-grid">
      <router-link
        v-for="(m, i) in visibleModules"
        :key="m.slug"
        class="module-card"
        :class="moduleCardClass(m)"
        :to="{ name: 'module', params: { slug: m.slug } }"
      >
        <div class="module-card-head">
          <span class="module-type-dot" :class="{ editor: m.type === 'Editor' }"></span>
          <span class="module-name" :title="m.name">{{ m.name }}</span>
        </div>
        <div class="module-path" :title="m.path">{{ m.path }}</div>
        <div class="module-card-foot">
          <span class="tag" :class="typeClass(m.type)">{{ m.type }}</span>
          <span class="doc-badge compact" :class="'is-' + itemStatus(m)">{{ statusLabel(m) }}</span>
        </div>
      </router-link>
    </div>

    <div v-if="store.filteredModules.length > moduleLimit" class="more">
      <button class="btn btn-dark" @click="moduleLimit += PAGE_SIZE">
        加载更多（剩余 {{ store.filteredModules.length - moduleLimit }}）
      </button>
    </div>
  </section>

  <footer class="home-footer">
    <section class="outro">
      <div class="outro-slogan">
        <span class="outro-paren" aria-hidden="true">(</span>
        <div class="outro-text">
          <span class="outro-cn">源码即说明书</span>
          <span class="outro-en">Read the source. Know the engine.</span>
          <div class="outro-meta">
            <em>{{ store.stats?.total_plugins ?? 0 }} Plugins</em>
            <i></i>
            <em>{{ store.stats?.total_modules ?? 0 }} Modules</em>
            <i></i>
            <span>{{ store.stats?.engine_version || 'UE5' }}</span>
          </div>
        </div>
        <span class="outro-paren" aria-hidden="true">)</span>
      </div>
      <svg class="outro-star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 0c1.1 8.2 3.8 10.9 12 12-8.2 1.1-10.9 3.8-12 12C10.9 15.8 8.2 13.1 0 12 8.2 10.9 10.9 8.2 12 0Z" />
      </svg>
    </section>

    <div class="site-foot">
      <span>UE Docs Lab — Generated from Unreal Engine source</span>
      <span class="site-foot-links">
        <router-link :to="{ name: 'home', hash: '#plugins' }">Plugins</router-link>
        <router-link :to="{ name: 'home', hash: '#modules' }">Modules</router-link>
        <router-link :to="{ name: 'settings' }">Settings</router-link>
      </span>
      <span>FastAPI · Vue · {{ store.stats?.engine_version || 'UE5' }}</span>
    </div>
  </footer>
</template>