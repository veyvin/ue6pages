<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useTheme } from '../composables/useTheme.js'
import { useItemsStore } from '../stores/items.js'
import { errMsg } from '../api/client.js'

const route = useRoute()
const router = useRouter()
const store = useItemsStore()
const { theme, toggle } = useTheme()

const searchInput = ref(null)
const toast = ref('')
let toastTimer = null
function flashToast(text) {
  toast.value = text
  clearTimeout(toastTimer)
  toastTimer = setTimeout(() => { toast.value = '' }, 2600)
}

function onGlobalKey(e) {
  if (e.key !== '/' || e.metaKey || e.ctrlKey || e.altKey) return
  const tag = (e.target?.tagName || '').toLowerCase()
  if (tag === 'input' || tag === 'textarea' || e.target?.isContentEditable) return
  e.preventDefault()
  searchInput.value?.focus()
}

onMounted(() => window.addEventListener('keydown', onGlobalKey))
onUnmounted(() => window.removeEventListener('keydown', onGlobalKey))

const active = computed(() => {
  if (route.name === 'settings') return 'settings'
  if (route.name === 'plugin') return 'plugins'
  if (route.name === 'module') return 'modules'
  if (route.name === 'home') return 'home'
  return ''
})

function goHome(hash) {
  router.push({ name: 'home', hash })
}

// 搜索在任意页面可输入；不在首页时自动跳到首页查看结果
function onSearch(e) {
  store.query = e.target.value
  if (route.name !== 'home') router.push({ name: 'home', hash: '#plugins' })
}

async function onRescan() {
  try {
    const r = await store.reload()
    flashToast(`已重扫：${r.plugins} 个插件 / ${r.modules} 个模块`)
  } catch (err) {
    flashToast('重扫失败：' + errMsg(err))
  }
}
</script>

<template>
  <header class="topbar">
    <router-link to="/" class="brand" aria-label="UE Docs Lab 首页">
      <span class="brand-dot" aria-hidden="true"></span>
      <span class="brand-pill">UE Docs Lab<span class="brand-pill-sub" v-if="store.stats?.engine_version">{{ store.stats.engine_version }}</span></span>
    </router-link>

    <nav class="topnav" aria-label="主导航">
      <span class="nav-slash" aria-hidden="true">//</span>
      <button :class="{ active: active === 'home' }" @click="goHome('')">Index</button>
      <button :class="{ active: active === 'plugins' }" @click="goHome('#plugins')">
        Plugins <span class="nav-count">{{ store.stats?.total_plugins ?? '—' }}</span>
      </button>
      <button :class="{ active: active === 'modules' }" @click="goHome('#modules')">
        Modules <span class="nav-count">{{ store.stats?.total_modules ?? '—' }}</span>
      </button>
      <button :class="{ active: active === 'settings' }" @click="router.push({ name: 'settings' })">
        Settings
      </button>
    </nav>

    <div class="nav-status" aria-live="polite">
      <i></i>
      {{ store.loading ? 'Scanning' : (store.error ? 'Offline' : 'Index Ready') }}
    </div>

    <div class="top-actions">      <label class="search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.3-4.3" />
        </svg>
        <input
          ref="searchInput"
          :value="store.query"
          type="text"
          placeholder="Search plugins or modules…"
          aria-label="搜索插件或模块"
          @input="onSearch"
        />
        <span class="kbd" aria-hidden="true">/</span>
      </label>
      <transition name="toast-pop">
        <span v-if="toast" class="topbar-toast" role="status">{{ toast }}</span>
      </transition>

      <button class="keycap-btn" title="重新扫描 UE 源码" aria-label="重新扫描 UE 源码" @click="onRescan">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <polyline points="23 4 23 10 17 10" />
          <polyline points="1 20 1 14 7 14" />
          <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15" />
        </svg>
      </button>

      <button
        class="keycap-btn"
        :title="theme === 'dark' ? '切换到浅色' : '切换到深色'"
        :aria-label="theme === 'dark' ? '切换到浅色' : '切换到深色'"
        @click="toggle"
      >
        <svg v-if="theme === 'dark'" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="12" cy="12" r="4" />
          <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41" />
        </svg>
        <svg v-else width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
        </svg>
      </button>
    </div>
  </header>
</template>