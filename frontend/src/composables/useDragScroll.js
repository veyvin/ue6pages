import { nextTick, onBeforeUnmount, onMounted, ref } from 'vue'

/** 横向溢出容器：拖动平移、滚轮改横滚、左右边缘提示。 */
export function useDragScroll() {
  const el = ref(null)
  const canStart = ref(false)
  const canEnd = ref(false)

  let pointerId = null
  let originX = 0
  let originScroll = 0
  let dragged = false
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
    dragged = false
    node.classList.add('is-dragging')
    node.setPointerCapture?.(e.pointerId)
  }

  function onPointerMove(e) {
    const node = el.value
    if (!node || pointerId !== e.pointerId) return
    const dx = e.clientX - originX
    if (Math.abs(dx) > 4) dragged = true
    if (dragged) {
      node.scrollLeft = originScroll - dx
      e.preventDefault()
    }
  }

  function endDrag(e) {
    const node = el.value
    if (pointerId !== e.pointerId) return
    pointerId = null
    node?.classList.remove('is-dragging')
    node?.releasePointerCapture?.(e.pointerId)
  }

  function onClickCapture(e) {
    if (!dragged) return
    e.preventDefault()
    e.stopPropagation()
    dragged = false
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
