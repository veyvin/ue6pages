<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useItemsStore } from '../stores/items.js'

const route = useRoute()
const router = useRouter()
const store = useItemsStore()

const active = computed(() => {
  if (route.name === 'home') return 'home'
  if (route.name === 'plugin') return 'plugins'
  if (route.name === 'module') return 'modules'
  return ''
})

function goHome(hash) {
  router.push({ name: 'home', hash })
}
</script>

<template>
  <aside class="sidebar" id="sidebar">
    <div class="brand">
      <div class="brand-logo">UE</div>
      <div>
        <div class="brand-text">UE Plugin Docs</div>
        <div class="brand-sub">ue.veyvin.com</div>
      </div>
    </div>

    <div class="nav-group-title">Browse 浏览</div>

    <button class="nav-item" :class="{ active: active === 'home' }" @click="goHome('')">
      <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      <span>Dashboard / 仪表盘</span>
    </button>

    <button class="nav-item" :class="{ active: active === 'plugins' }" @click="goHome('#plugins')">
      <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
      <span>Plugins <span class="nav-count mono">{{ store.stats?.total_plugins ?? '—' }}</span></span>
    </button>

    <button class="nav-item" :class="{ active: active === 'modules' }" @click="goHome('#modules')">
      <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7h-3V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v3H4a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/></svg>
      <span>Modules <span class="nav-count mono">{{ store.stats?.total_modules ?? '—' }}</span></span>
    </button>

    <div class="sidebar-footer">
      <div class="sidebar-footer-title">Backend</div>
      <div style="font-size:13px;color:var(--on-surface-variant);">
        <span class="mono" style="color:var(--on-surface); font-weight:var(--fw-semibold);">{{ store.stats?.engine_version || 'UE' }}</span>
        <span style="margin:0 6px;">·</span>
        <span class="mono">{{ store.stats?.total_plugins ?? 0 }} plugins</span>
        <span style="margin:0 6px;">·</span>
        <span class="mono">{{ store.stats?.total_modules ?? 0 }} modules</span>
      </div>
      <div class="sidebar-footer-sub">Powered by FastAPI · 可在 <code>backend/config.yaml</code> 中配置 engine_root 与 AI</div>
    </div>
  </aside>
</template>
