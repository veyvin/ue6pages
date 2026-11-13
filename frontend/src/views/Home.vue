<script setup>
import { computed, ref, watch } from 'vue'
import { useItemsStore } from '../stores/items.js'

const PAGE_SIZE = 60
const store = useItemsStore()

const pluginLimit = ref(PAGE_SIZE)
const moduleLimit = ref(PAGE_SIZE)

const visiblePlugins = computed(() => store.filteredPlugins.slice(0, pluginLimit.value))
const visibleModules = computed(() => store.filteredModules.slice(0, moduleLimit.value))

watch(() => [store.query, store.category], () => {
  pluginLimit.value = PAGE_SIZE
  moduleLimit.value = PAGE_SIZE
})

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

    <div v-if="!store.stats && store.loading" class="console-card console-skeleton" aria-busy="true">
      <div class="skeleton-line"></div>
      <div class="skeleton-line short"></div>
      <div class="skeleton-line"></div>
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
          <div class="note">
            目录来自 usage.fb{{ store.catalogSource ? ` · ${store.catalogSource}` : '' }}
            · 点击卡片进入详情
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
      <button v-if="store.category || store.query" class="filter-clear" @click="resetFilters">
        重置 ⟲
      </button>
    </div>

    <div v-if="store.loading && !store.plugins.length" class="empty">加载中…</div>
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
        :class="{ 'span-2': isWide(i) }"
        :to="{ name: 'plugin', params: { slug: p.slug } }"
      >
        <div class="plugin-card-top">
          <div class="plugin-badge">{{ initial(p.name) }}</div>
          <div class="plugin-meta">
            <span class="card-no">No.{{ cardNo(i) }}</span>
            <span v-if="p.usage_doc" class="doc-badge">FB</span>
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

    <div v-if="!store.filteredModules.length" class="empty-card">
      <span class="empty-glyph">[ — ]</span>
      <p class="empty-text">没有匹配的模块。试试清空搜索，或到设置里重新扫描 Engine/Source。</p>
    </div>
    <div v-else class="module-grid">
      <router-link
        v-for="(m, i) in visibleModules"
        :key="m.slug"
        class="module-card"
        :class="{ editor: m.type === 'Editor' }"
        :to="{ name: 'module', params: { slug: m.slug } }"
      >
        <div class="module-card-head">
          <span class="module-type-dot" :class="{ editor: m.type === 'Editor' }"></span>
          <span class="module-name" :title="m.name">{{ m.name }}</span>
        </div>
        <div class="module-path" :title="m.path">{{ m.path }}</div>
        <div class="module-card-foot">
          <span class="tag" :class="typeClass(m.type)">{{ m.type }}</span>
          <span class="module-index">M.{{ String(i + 1).padStart(3, '0') }}</span>
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