import axios from 'axios'

export const api = axios.create({
  baseURL: '/api',
  timeout: 15000,
})

export const ItemsAPI = {
  getStats:    ()          => api.get('/stats').then(r => r.data),
  listPlugins: (params)    => api.get('/plugins', { params }).then(r => r.data),
  getPlugin:   (slug)      => api.get(`/plugins/${slug}`).then(r => r.data),
  listModules: (params)    => api.get('/modules', { params }).then(r => r.data),
  getModule:   (slug)      => api.get(`/modules/${slug}`).then(r => r.data),
  rescan:      ()          => api.post('/rescan').then(r => r.data),
}
