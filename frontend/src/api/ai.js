/** SSE 流式调用 AI —— Fetch + ReadableStream，事件回调驱动。 */
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
      buf += decoder.decode(value, { stream: true })

      // 按 SSE 的 \n\n 切 frame
      let sepIdx
      while ((sepIdx = buf.indexOf('\n\n')) !== -1) {
        const frame = buf.slice(0, sepIdx)
        buf = buf.slice(sepIdx + 2)

        const lines = frame.split('\n')
        for (const line of lines) {
          if (!line.startsWith('data:')) continue
          const data = line.slice(5).trim()
          if (data === '[DONE]') {
            onDone?.()
            return
          }
          // 把后端转义的 \n 还原
          const piece = data.replace(/\\n/g, '\n')
          onChunk?.(piece)
        }
      }
    }
    onDone?.()
  } catch (err) {
    onError?.(err)
  }
}
