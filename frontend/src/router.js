import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('./views/Home.vue') },
  {
    path: '/plugins/:slug',
    name: 'plugin',
    component: () => import('./views/Detail.vue'),
    props: route => ({ kind: 'plugin', slug: route.params.slug }),
  },
  {
    path: '/modules/:slug',
    name: 'module',
    component: () => import('./views/Detail.vue'),
    props: route => ({ kind: 'module', slug: route.params.slug }),
  },
  { path: '/settings', name: 'settings', component: () => import('./views/Settings.vue') },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() { return { top: 0 } },
})
