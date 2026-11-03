import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './styles/tokens.css'
import './styles/components.css'
import './styles/pages.css'
import App from './App.vue'
import { router } from './router.js'

createApp(App).use(createPinia()).use(router).mount('#app')
