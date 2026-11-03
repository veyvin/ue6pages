import axios from 'axios'

export const api = axios.create({
  baseURL: '/api',
  timeout: 60000,
})

/** 把 axios / FastAPI 的错误转成可读文本。 */
export function errMsg(err) {
  const detail = err?.response?.data?.detail
  if (typeof detail === 'string') return detail
  if (detail) return JSON.stringify(detail)
  return err?.message || String(err)
}

export const ItemsAPI = {
  getStats:    ()          => api.get('/stats').then(r => r.data),
  listPlugins: (params)    => api.get('/plugins', { params }).then(r => r.data),
  getPlugin:   (slug)      => api.get(`/plugins/${slug}`).then(r => r.data),
  listModules: (params)    => api.get('/modules', { params }).then(r => r.data),
  getModule:   (slug)      => api.get(`/modules/${slug}`).then(r => r.data),
  rescan:      ()          => api.post('/rescan').then(r => r.data),
}

export const ConfigAPI = {
  get:    ()        => api.get('/config').then(r => r.data),
  update: (config)  => api.put('/config', config).then(r => r.data),
  testAi: ()        => api.post('/ai/test').then(r => r.data),
}

export const UsageDocAPI = {
  get:   (kind, slug) => api.get(`/usage-docs/${kind}/${slug}`).then(r => r.data),
  stats: ()           => api.get('/usage-docs/stats').then(r => r.data),
}
