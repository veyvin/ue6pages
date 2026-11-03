import { defineStore } from 'pinia'
import { ItemsAPI } from '../api/client.js'

export const useItemsStore = defineStore('items', {
  state: () => ({
    stats: null,
    plugins: [],
    modules: [],
    loading: false,
    loaded: false,
  }),

  getters: {
    categories(state) {
      return [...new Set(state.plugins.map(p => p.category).filter(Boolean))].sort()
    },
  },

  actions: {
    async loadAll(force = false) {
      if (this.loaded && !force) return
      this.loading = true
      try {
        const [stats, plugins, modules] = await Promise.all([
          ItemsAPI.getStats(),
          ItemsAPI.listPlugins(),
          ItemsAPI.listModules(),
        ])
        this.stats = stats
        this.plugins = plugins
        this.modules = modules
        this.loaded = true
      } finally {
        this.loading = false
      }
    },

    async reload() {
      await ItemsAPI.rescan()
      this.loaded = false
      await this.loadAll(true)
    },
  },
})
