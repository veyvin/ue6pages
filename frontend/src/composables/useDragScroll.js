import { nextTick, onBeforeUnmount, onMounted, ref } from 'vue'

const DRAG_PX = 8

/** 横向溢出容器：拖动平移、滚轮改横滚、左右边缘提示。点击子按钮不拦截。 */
export function useDragScroll() {
  const el = ref(null)
  const canStart = ref(false)
  const canEnd = ref(false)

  let pointerId = null
  let originX = 0
  let originScroll = 0
  let dragging = false
  let suppressClick = false
  let observer = null

  function updateEdges() {
    const node = el.value
    if (!node) {
      canStart.value = false
      canEnd.value = false
      return
    }
    const max = node.scrollWidth - node.clientWidth
    canStart.value = node.scrollLeft > 2
    canEnd.value = max > 2 && node.scrollLeft < max - 2
  }

  function onPointerDown(e) {
    const node = el.value
    if (!node || e.button !== 0) return
    pointerId = e.pointerId
    originX = e.clientX
    originScroll = node.scrollLeft
    dragging = false
    suppressClick = false
  }

  function onPointerMove(e) {
    const node = el.value
    if (!node || pointerId !== e.pointerId) return
    const dx = e.clientX - originX
    if (!dragging && Math.abs(dx) >= DRAG_PX) {
      dragging = true
      suppressClick = true
      node.classList.add('is-dragging')
      node.setPointerCapture?.(e.pointerId)
    }
    if (dragging) node.scrollLeft = originScroll - dx
  }

  function endDrag(e) {
    if (pointerId !== e.pointerId) return
    const node = el.value
    pointerId = null
    dragging = false
    node?.classList.remove('is-dragging')
    if (node?.hasPointerCapture?.(e.pointerId)) {
      node.releasePointerCapture(e.pointerId)
    }
  }

  function onClickCapture(e) {
    if (!suppressClick) return
    e.preventDefault()
    e.stopPropagation()
    suppressClick = false
  }

  function onWheel(e) {
    const node = el.value
    if (!node) return
    const max = node.scrollWidth - node.clientWidth
    if (max <= 0) return
    const delta = Math.abs(e.deltaY) > Math.abs(e.deltaX) ? e.deltaY : e.deltaX
    if (!delta) return
    node.scrollLeft += delta
    e.preventDefault()
  }

  onMounted(() => {
    const node = el.value
    if (!node) return
    node.addEventListener('wheel', onWheel, { passive: false })
    observer = new ResizeObserver(() => {
      nextTick(updateEdges)
    })
    observer.observe(node)
    nextTick(updateEdges)
  })

  onBeforeUnmount(() => {
    el.value?.removeEventListener('wheel', onWheel)
    observer?.disconnect()
  })

  return {
    el,
    canStart,
    canEnd,
    updateEdges,
    onPointerDown,
    onPointerMove,
    onPointerUp: endDrag,
    onPointerCancel: endDrag,
    onClickCapture,
    onScroll: updateEdges,
  }
}
