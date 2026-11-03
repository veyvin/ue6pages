/**
 * SSE 流式调用 AI —— Fetch + ReadableStream，事件回调驱动。
 * 后端每帧为 `data: <JSON 字符串>`，结束帧为 `data: [DONE]`。
 */
export async function streamAiChat({ kind, slug, message, history = [] }, callbacks = {}) {
  const { onChunk, onDone, onError } = callbacks

  try {
    const resp = await fetch('/api/ai/stream', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ kind, slug, message, history }),
    })

    if (!resp.ok || !resp.body) {
      const body = await resp.text()
      throw new Error(`HTTP ${resp.status}: ${body.slice(0, 300)}`)
    }

    const reader = resp.body.getReader()
    const decoder = new TextDecoder('utf-8')
    let buf = ''

    while (true) {
      const { value, done } = await reader.read()
      if (done) break
      buf += decoder.decode(value, { stream: true }).replace(/\r\n/g, '\n')

      let sepIdx
      while ((sepIdx = buf.indexOf('\n\n')) !== -1) {
        const frame = buf.slice(0, sepIdx)
        buf = buf.slice(sepIdx + 2)

        for (const line of frame.split('\n')) {
          if (!line.startsWith('data:')) continue
          const data = line.slice(5).replace(/^ /, '')
          if (data === '[DONE]') {
            onDone?.()
            return
          }
          onChunk?.(JSON.parse(data))
        }
      }
    }
    onDone?.()
  } catch (err) {
    onError?.(err)
  }
}

/**
 * SSE 流式批量生成《使用方法》—— 与 chat 同样的事件协议，每帧是 JSON 对象：
 *   {type:'start'|'item'|'summary', ...}，结束帧 data: [DONE]。
 * fetchOptions 里可传 signal（AbortController）用于取消。
 */
export async function streamUsageBatch(payload, callbacks = {}, fetchOptions = {}) {
  const { onFrame, onDone, onError } = callbacks

  try {
    const resp = await fetch('/api/ai/batch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      ...fetchOptions,
    })

    if (!resp.ok || !resp.body) {
      const body = await resp.text()
      throw new Error(`HTTP ${resp.status}: ${body.slice(0, 300)}`)
    }

    const reader = resp.body.getReader()
    const decoder = new TextDecoder('utf-8')
    let buf = ''

    while (true) {
      const { value, done } = await reader.read()
      if (done) break
      buf += decoder.decode(value, { stream: true }).replace(/\r\n/g, '\n')

      let sepIdx
      while ((sepIdx = buf.indexOf('\n\n')) !== -1) {
        const frame = buf.slice(0, sepIdx)
        buf = buf.slice(sepIdx + 2)

        for (const line of frame.split('\n')) {
          if (!line.startsWith('data:')) continue
          const data = line.slice(5).replace(/^ /, '')
          if (data === '[DONE]') {
            onDone?.()
            return
          }
          onFrame?.(JSON.parse(data))
        }
      }
    }
    onDone?.()
  } catch (err) {
    onError?.(err)
  }
}
