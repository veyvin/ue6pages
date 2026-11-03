<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useTheme } from '../composables/useTheme.js'
import { useItemsStore } from '../stores/items.js'
import { errMsg } from '../api/client.js'

const route = useRoute()
const router = useRouter()
const store = useItemsStore()
const { theme, toggle } = useTheme()

const title = computed(() => {
  if (route.name === 'home') return 'Unreal Engine 插件与模块'
  if (route.name === 'plugin') {
    return store.plugins.find(p => p.slug === route.params.slug)?.name || route.params.slug
  }
  if (route.name === 'module') {
    return store.modules.find(m => m.slug === route.params.slug)?.name || route.params.slug
  }
  if (route.name === 'settings') return '设置'
  return ''
})

// 搜索在任意页面可输入；不在首页时自动跳到首页查看结果
function onSearch(e) {
  store.query = e.target.value
  if (route.name !== 'home') router.push({ name: 'home', hash: '#plugins' })
}

async function onRescan() {
  try {
    const r = await store.reload()
    alert(`✅ 已重扫：${r.plugins} 插件，${r.modules} 模块`)
  } catch (err) {
    alert('❌ 重扫失败：' + errMsg(err))
  }
}

function toggleSidebar() {
  document.getElementById('sidebar')?.classList.toggle('open')
}
</script>

<template>
  <header class="topbar">
    <button class="sidebar-toggle" aria-label="Menu" @click="toggleSidebar">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>

    <div class="topbar-title">{{ title }}</div>

    <div class="search">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--on-surface-variant)"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      <input :value="store.query" type="text" placeholder="Search plugins or modules…" @input="onSearch" />
    </div>

    <button class="icon-btn" @click="onRescan" title="重新扫描 UE 源码">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
    </button>

    <button class="icon-btn" @click="toggle" :title="theme === 'dark' ? 'Switch to light' : 'Switch to dark'">
      <!-- sun -->
      <svg v-if="theme === 'dark'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      <!-- moon -->
      <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
    </button>
  </header>
</template>
