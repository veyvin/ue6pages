import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: () => import('../views/Home.vue'), name: 'home' },
  { path: '/plugins/:slug', component: () => import('../views/Detail.vue'), name: 'plugin', props: route => ({ kind: 'plugin', slug: route.params.slug }) },
  { path: '/modules/:slug', component: () => import('../views/Detail.vue'), name: 'module', props: route => ({ kind: 'module', slug: route.params.slug }) },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() { return { top: 0 } },
})
