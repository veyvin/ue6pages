<script setup>
import Sidebar from './components/Sidebar.vue'
import Topbar from './components/Topbar.vue'
</script>

<template>
  <div class="app">
    <Sidebar />
    <div class="main-wrap">
      <Topbar />
      <main class="content">
        <router-view v-slot="{ Component }">
          <transition name="page" mode="out-in">
            <component :is="Component" />
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
