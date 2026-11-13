import { defineStore } from 'pinia'
import { ItemsAPI, errMsg } from '../api/client.js'
import {
  catalogFromUsageFb,
  ensureUsageFb,
  getUsageDoc,
} from '../api/usageFb.js'

function mergeLists(fbList, apiList, kind) {
  const apiBySlug = new Map((apiList || []).map((item) => [item.slug, item]))
  const seen = new Set()
  const out = []
  for (const fb of fbList) {
    seen.add(fb.slug)
    out.push({
      ...fb,
      ...(apiBySlug.get(fb.slug) || {}),
      usage_doc: true,
    })
  }
  for (const item of apiList || []) {
    if (seen.has(item.slug)) continue
    out.push({
      ...item,
      usage_doc: Boolean(getUsageDoc(kind, item.slug)),
    })
  }
  return out
}

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
    recent: [],
    catalogSource: '',
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

    usageCoverage(state) {
      const total = state.plugins.length + state.modules.length
      const have =
        state.plugins.filter(p => p.usage_doc).length +
        state.modules.filter(m => m.usage_doc).length
      return { have, total, pct: total ? Math.round((have / total) * 100) : 0 }
    },
  },

  actions: {
    async loadAll(force = false) {
      if (this.loaded && !force) return
      this.loading = true
      this.error = ''
      try {
        const fbState = await ensureUsageFb({ force })
        const fb = catalogFromUsageFb()

        let apiPlugins = []
        let apiModules = []
        let apiStats = null
        try {
          const [stats, plugins, modules] = await Promise.all([
            ItemsAPI.getStats(),
            ItemsAPI.listPlugins(),
            ItemsAPI.listModules(),
          ])
          apiStats = stats
          apiPlugins = plugins
          apiModules = modules
        } catch (err) {
          if (!fb.plugins.length && !fb.modules.length) {
            this.error = errMsg(err)
          }
        }

        if (fb.plugins.length || fb.modules.length) {
          this.plugins = mergeLists(fb.plugins, apiPlugins, 'plugin')
          this.modules = mergeLists(fb.modules, apiModules, 'module')
          this.stats = {
            total_plugins: this.plugins.length,
            total_modules: this.modules.length,
            categories: [...new Set(this.plugins.map((p) => p.category).filter(Boolean))].sort(),
            engine_version: apiStats?.engine_version || '',
          }
          this.catalogSource = fbState.source || 'usage.fb'
        } else {
          this.plugins = apiPlugins.map((p) => ({
            ...p,
            usage_doc: Boolean(getUsageDoc('plugin', p.slug)),
          }))
          this.modules = apiModules.map((m) => ({
            ...m,
            usage_doc: Boolean(getUsageDoc('module', m.slug)),
          }))
          this.stats = apiStats
          this.catalogSource = 'api'
        }
        this.loaded = Boolean(this.plugins.length || this.modules.length || apiStats)
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

    remember(kind, slug, name) {
      this.recent = [
        { kind, slug, name, at: Date.now() },
        ...this.recent.filter(r => !(r.kind === kind && r.slug === slug)),
      ].slice(0, 5)
    },
  },
})
