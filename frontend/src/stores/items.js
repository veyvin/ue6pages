import { defineStore } from 'pinia'
import { ItemsAPI, errMsg } from '../api/client.js'
import {
  catalogFromUsageFb,
  ensureUsageFb,
  getUsageDoc,
  hasAiUsage,
  itemStatus,
  onUsageFbIndex,
} from '../api/usageFb.js'

function hasUsage(kind, slug, fallback = false) {
  return Boolean(fallback) || hasAiUsage(getUsageDoc(kind, slug))
}

function mergeLists(fbList, apiList, kind, liveScan) {
  const apiBySlug = new Map((apiList || []).map((item) => [item.slug, item]))
  const seen = new Set()
  const out = []
  for (const fb of fbList) {
    seen.add(fb.slug)
    const api = apiBySlug.get(fb.slug)
    out.push({
      ...fb,
      ...(api || {}),
      usage_doc: hasUsage(kind, fb.slug, fb.usage_doc),
      in_source: liveScan ? Boolean(api) : fb.in_source !== false,
    })
  }
  for (const item of apiList || []) {
    if (seen.has(item.slug)) continue
    out.push({
      ...item,
      usage_doc: hasUsage(kind, item.slug, item.usage_doc),
      in_source: true,
    })
  }
  return out
}

function matchesQuery(item, q) {
  if (!q) return true
  return [item.name, item.description, item.category, item.path]
    .some((v) => (v || '').toLowerCase().includes(q))
}

function matchesStatus(item, status) {
  if (!status) return true
  return itemStatus(item) === status
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
    status: '',
    recent: [],
    catalogSource: '',
    liveScan: false,
    _apiPlugins: [],
    _apiModules: [],
    _apiStats: null,
    _indexSubscribed: false,
  }),

  getters: {
    categories(state) {
      return [...new Set(state.plugins.map(p => p.category).filter(Boolean))].sort()
    },

    filteredPlugins(state) {
      const q = state.query.trim().toLowerCase()
      return state.plugins.filter(p => {
        if (state.category && p.category !== state.category) return false
        if (!matchesStatus(p, state.status)) return false
        return matchesQuery(p, q)
      })
    },

    filteredModules(state) {
      const q = state.query.trim().toLowerCase()
      return state.modules.filter(m => {
        if (!matchesStatus(m, state.status)) return false
        return matchesQuery(m, q)
      })
    },

    usageCoverage(state) {
      const total = state.plugins.length + state.modules.length
      const have =
        state.plugins.filter(p => p.usage_doc).length +
        state.modules.filter(m => m.usage_doc).length
      return { have, total, pct: total ? Math.round((have / total) * 100) : 0 }
    },

    statusCounts(state) {
      const all = [...state.plugins, ...state.modules]
      let missing = 0
      let gone = 0
      for (const item of all) {
        const st = itemStatus(item)
        if (st === 'missing') missing += 1
        else if (st === 'gone') gone += 1
      }
      return { missing, gone, total: all.length }
    },
  },

  actions: {
    _rebuildFromFb(source = '') {
      const fb = catalogFromUsageFb()
      if (!fb.plugins.length && !fb.modules.length) return
      this.plugins = mergeLists(fb.plugins, this._apiPlugins, 'plugin', this.liveScan)
      this.modules = mergeLists(fb.modules, this._apiModules, 'module', this.liveScan)
      this.stats = {
        total_plugins: this.plugins.length,
        total_modules: this.modules.length,
        categories: [...new Set(this.plugins.map((p) => p.category).filter(Boolean))].sort(),
        engine_version: this._apiStats?.engine_version || '',
      }
      this.catalogSource = source || this.catalogSource || 'usage.fb'
    },

    async loadAll(force = false) {
      if (this.loaded && !force) return
      this.loading = true
      this.error = ''
      if (!this._indexSubscribed) {
        onUsageFbIndex(({ source }) => {
          this._rebuildFromFb(source)
        })
        this._indexSubscribed = true
      }
      try {
        const fbState = await ensureUsageFb({ force })
        const fb = catalogFromUsageFb()

        let apiPlugins = []
        let apiModules = []
        let apiStats = null
        let liveScan = false
        try {
          const [stats, plugins, modules] = await Promise.all([
            ItemsAPI.getStats(),
            ItemsAPI.listPlugins(),
            ItemsAPI.listModules(),
          ])
          apiStats = stats
          apiPlugins = plugins
          apiModules = modules
          this._apiPlugins = apiPlugins
          this._apiModules = apiModules
          this._apiStats = apiStats
          liveScan = apiPlugins.length + apiModules.length > 0
        } catch (err) {
          if (!fb.plugins.length && !fb.modules.length) {
            this.error = errMsg(err)
          }
        }

        this.liveScan = liveScan
        if (fb.plugins.length || fb.modules.length) {
          this._rebuildFromFb(fbState.source || 'usage.fb')
        } else {
          this.plugins = apiPlugins.map((p) => ({
            ...p,
            usage_doc: hasUsage('plugin', p.slug, p.usage_doc),
            in_source: true,
          }))
          this.modules = apiModules.map((m) => ({
            ...m,
            usage_doc: hasUsage('module', m.slug, m.usage_doc),
            in_source: true,
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
