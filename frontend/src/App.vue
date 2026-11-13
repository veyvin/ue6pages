<script setup>
import { onMounted } from 'vue'
import Topbar from './components/Topbar.vue'
import { useItemsStore } from './stores/items.js'

const store = useItemsStore()

onMounted(() => store.loadAll())
</script>

<template>
  <div class="app">
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
</style>
