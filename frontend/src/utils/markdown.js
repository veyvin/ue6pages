/**
 * 极简 Markdown 渲染，用于 AI 回复。
 * 先整体转义 HTML，再解析代码块 / 标题 / 列表 / 段落 / 行内代码 / 粗体 / 链接，
 * 因此模型输出里的任何标签都只会以文本形式显示。
 */

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

function inline(text) {
  return text
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
}

export function renderMarkdown(source = '') {
  const lines = escapeHtml(source).split('\n')
  const out = []
  let para = []
  let list = null
  let code = null

  const flushPara = () => {
    if (para.length) {
      out.push(`<p>${para.map(inline).join('<br>')}</p>`)
      para = []
    }
  }
  const flushList = () => {
    if (list) {
      const items = list.items.map(i => `<li>${inline(i)}</li>`).join('')
      out.push(`<${list.tag}>${items}</${list.tag}>`)
      list = null
    }
  }
  const flushAll = () => { flushPara(); flushList() }

  for (const line of lines) {
    if (line.trim().startsWith('```')) {
      if (code) {
        out.push(`<pre><code>${code.join('\n')}</code></pre>`)
        code = null
      } else {
        flushAll()
        code = []
      }
      continue
    }
    if (code) {
      code.push(line)
      continue
    }

    if (!line.trim()) {
      flushAll()
      continue
    }

    const heading = line.match(/^(#{1,4})\s+(.*)$/)
    if (heading) {
      flushAll()
      const level = Math.min(heading[1].length + 2, 6)
      out.push(`<h${level}>${inline(heading[2])}</h${level}>`)
      continue
    }

    const bullet = line.match(/^\s*[-*]\s+(.*)$/)
    const numbered = line.match(/^\s*\d+[.)]\s+(.*)$/)
    if (bullet || numbered) {
      flushPara()
      const tag = bullet ? 'ul' : 'ol'
      if (!list || list.tag !== tag) {
        flushList()
        list = { tag, items: [] }
      }
      list.items.push((bullet || numbered)[1])
      continue
    }

    flushList()
    para.push(line)
  }

  if (code) out.push(`<pre><code>${code.join('\n')}</code></pre>`)
  flushAll()
  return out.join('')
}
