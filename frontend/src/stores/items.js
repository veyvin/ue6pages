import { defineStore } from 'pinia'
import { ItemsAPI, errMsg } from '../api/client.js'

export const useItemsStore = defineStore('items', {
  state: () => ({
    stats: null,
    plugins: [],
    modules: [],
    loading: false,
    loaded: false,
    error: '',
    query: '',
    category: '',
  }),

  getters: {
    categories(state) {
      return [...new Set(state.plugins.map(p => p.category).filter(Boolean))].sort()
    },

    filteredPlugins(state) {
      const q = state.query.trim().toLowerCase()
      return state.plugins.filter(p => {
        if (state.category && p.category !== state.category) return false
        if (!q) return true
        return [p.name, p.description, p.category].some(v => (v || '').toLowerCase().includes(q))
      })
    },

    filteredModules(state) {
      const q = state.query.trim().toLowerCase()
      if (!q) return state.modules
      return state.modules.filter(m =>
        m.name.toLowerCase().includes(q) || m.path.toLowerCase().includes(q))
    },
  },

  actions: {
    async loadAll(force = false) {
      if (this.loaded && !force) return
      this.loading = true
      this.error = ''
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
      } catch (err) {
        this.error = errMsg(err)
      } finally {
        this.loading = false
      }
    },

    async reload() {
      const result = await ItemsAPI.rescan()
      this.loaded = false
      await this.loadAll(true)
      return result
    },
  },
})
