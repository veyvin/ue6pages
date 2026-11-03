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

const BADGE_CLASSES = ['', 'purple', 'green', 'amber']

function badgeClass(index) {
  return BADGE_CLASSES[index % BADGE_CLASSES.length]
}

function initial(name) {
  return (name || '?').trim().charAt(0).toUpperCase()
}
</script>

<template>
  <div class="page-title-wrap">
    <h1>插件与模块总览</h1>
    <p>来自 UE 源码树的 .uplugin 与 *.Build.cs · 点击卡片查看详情，详情页可让 AI 讲解用法</p>
  </div>

  <div v-if="store.error" class="banner banner-error">
    无法连接后端：{{ store.error }}。请确认后端已启动（backend 目录下 uvicorn backend.app:app --port 8001），
    或到 <router-link to="/settings">设置</router-link> 检查引擎路径。
  </div>

  <section class="stats">
    <div class="stat-card plugins">
      <div class="stat-card-accent-bar"></div>
      <div class="stat-card-label">插件 Plugins</div>
      <div class="stat-card-value mono">{{ store.stats?.total_plugins ?? '—' }}</div>
      <div class="stat-card-sub">已扫描的 .uplugin</div>
    </div>
    <div class="stat-card modules">
      <div class="stat-card-accent-bar"></div>
      <div class="stat-card-label">模块 Modules</div>
      <div class="stat-card-value mono">{{ store.stats?.total_modules ?? '—' }}</div>
      <div class="stat-card-sub">已扫描的 *.Build.cs</div>
    </div>
    <div class="stat-card categories">
      <div class="stat-card-accent-bar"></div>
      <div class="stat-card-label">分类 Categories</div>
      <div class="stat-card-value mono">{{ store.stats?.categories?.length ?? '—' }}</div>
      <div class="stat-card-sub">插件分类数</div>
    </div>
    <div class="stat-card engine">
      <div class="stat-card-accent-bar"></div>
      <div class="stat-card-label">引擎版本 Engine</div>
      <div class="stat-card-value mono" style="font-size: 26px;">{{ store.stats?.engine_version || '—' }}</div>
      <div class="stat-card-sub">读取自插件 EngineVersion</div>
    </div>
  </section>

  <section id="plugins">
    <div class="filters-row">
      <h2 class="section-title" style="margin: 0;">Plugins 插件</h2>
      <div class="segmented">
        <button :class="{ active: !store.category }" @click="store.category = ''">全部</button>
        <button
          v-for="c in store.categories"
          :key="c"
          :class="{ active: store.category === c }"
          @click="store.category = c"
        >{{ c }}</button>
      </div>
    </div>

    <div v-if="store.loading && !store.plugins.length" class="empty">加载中…</div>
    <div v-else-if="!store.filteredPlugins.length" class="empty">没有匹配的插件</div>
    <div v-else class="card-grid" style="margin-top: var(--space-4);">
      <router-link
        v-for="(p, i) in visiblePlugins"
        :key="p.slug"
        class="grid-card"
        :to="{ name: 'plugin', params: { slug: p.slug } }"
      >
        <div class="grid-card-head">
          <div class="grid-card-badge" :class="badgeClass(i)">{{ initial(p.name) }}</div>
          <div class="grid-card-title">{{ p.name }}</div>
        </div>
        <div class="grid-card-desc">{{ p.description || '暂无描述' }}</div>
        <div class="grid-card-foot">
          <span class="grid-card-path mono">{{ p.path }}</span>
          <span v-if="p.category" class="chip chip-primary">{{ p.category }}</span>
        </div>
      </router-link>
    </div>

    <div v-if="store.filteredPlugins.length > pluginLimit" class="more" style="margin-top: var(--space-5);">
      <button class="btn" @click="pluginLimit += PAGE_SIZE">
        加载更多（剩余 {{ store.filteredPlugins.length - pluginLimit }}）
      </button>
    </div>
  </section>

  <section id="modules" style="margin-top: var(--space-8);">
    <div class="filters-row">
      <h2 class="section-title" style="margin: 0;">Modules 模块</h2>
      <span class="chip">{{ store.filteredModules.length }} / {{ store.modules.length }}</span>
    </div>

    <div v-if="!store.filteredModules.length" class="empty">没有匹配的模块</div>
    <div v-else class="module-grid" style="margin-top: var(--space-4);">
      <router-link
        v-for="m in visibleModules"
        :key="m.slug"
        class="module-item"
        :to="{ name: 'module', params: { slug: m.slug } }"
      >
        <span class="dot"></span>
        <span class="name mono">{{ m.name }}</span>
        <span class="tag" :class="m.type.toLowerCase()">{{ m.type }}</span>
      </router-link>
    </div>

    <div v-if="store.filteredModules.length > moduleLimit" class="more" style="margin-top: var(--space-5);">
      <button class="btn" @click="moduleLimit += PAGE_SIZE">
        加载更多（剩余 {{ store.filteredModules.length - moduleLimit }}）
      </button>
    </div>
  </section>
</template>
