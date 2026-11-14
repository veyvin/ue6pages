<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import Topbar from './components/Topbar.vue'
import { useItemsStore } from './stores/items.js'
import { onUsageFbProgress } from './api/usageFb.js'

const store = useItemsStore()

const progress = ref({ phase: 'idle', ratio: null })
let stopProgress = null
onMounted(() => {
  stopProgress = onUsageFbProgress((p) => { progress.value = p })
  store.loadAll()
})
onBeforeUnmount(() => { stopProgress?.() })

const busy = computed(() =>
  ['connecting', 'downloading', 'parsing'].includes(progress.value.phase))
const barWidth = computed(() => (
  progress.value.ratio != null ? `${Math.min(progress.value.ratio, 1) * 100}%` : ''))
</script>

<template>
  <div class="app">
    <transition name="fade">
      <div v-if="busy" class="top-progress" aria-hidden="true">
        <i :class="{ pending: progress.ratio == null }" :style="{ width: barWidth }"></i>
      </div>
    </transition>
    <Topbar />
    <main class="main">
      <div class="shell">
        <router-view v-slot="{ Component, route }">
          <transition name="page" mode="out-in">
            <div :key="route.path" class="route-view">
              <component :is="Component" />
            </div>
          </transition>
        </router-view>
      </div>
    </main>
  </div>
</template>

<style>
.page-enter-active,
.page-leave-active {
  transition: opacity var(--dur-base) var(--ease-spring),
              transform var(--dur-base) var(--ease-spring);
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

.fade-enter-active,
.fade-leave-active { transition: opacity var(--dur-fast, 160ms) ease; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }
</style>