<script setup>
import { onMounted } from 'vue'
import Sidebar from './components/Sidebar.vue'
import Topbar from './components/Topbar.vue'
import { useItemsStore } from './stores/items.js'

const store = useItemsStore()

onMounted(() => store.loadAll())
</script>

<template>
  <div class="app">
    <Sidebar />
    <div class="main-wrap">
      <Topbar />
      <main class="content">
        <router-view v-slot="{ Component, route }">
          <transition name="page" mode="out-in">
            <div :key="route.fullPath" class="route-view">
              <component :is="Component" />
            </div>
          </transition>
        </router-view>
      </main>
    </div>
  </div>
</template>

<style>
.page-enter-active, .page-leave-active {
  transition: opacity var(--dur-base) var(--ease-spring);
}
.page-enter-from, .page-leave-to { opacity: 0; }
</style>
