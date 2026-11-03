/** 主题 composable — localStorage 持久化 + 跟随系统。 */
import { ref, watchEffect } from 'vue'

const THEME_KEY = 'ue-docs-theme'

function init() {
  const stored = localStorage.getItem(THEME_KEY)
  if (stored === 'light' || stored === 'dark') return stored
  return window.matchMedia?.('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

export const theme = ref(init())

export function useTheme() {
  watchEffect(() => {
    document.documentElement.setAttribute('data-theme', theme.value)
    localStorage.setItem(THEME_KEY, theme.value)
  })
  return {
    theme,
    toggle: () => (theme.value = theme.value === 'dark' ? 'light' : 'dark'),
    set: (t) => (theme.value = t),
  }
}
