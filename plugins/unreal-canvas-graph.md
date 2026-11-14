---
layout: default
title: 虚幻画布图 / Unreal Canvas Graph
---



<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Unreal Canvas Graph</div>
      <div class="hero-title-cn">虚幻画布图 · Unreal Canvas 画布的原生 Slate 编辑器。 U</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Epic Internal</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Developer/UnrealCanvas/UnrealCanvasGraph/UnrealCanvasGraph.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Unreal Canvas 画布的原生 Slate 编辑器。 UnrealCanvasClient拥有canvas文档模型和服务器客户端； UnrealCanvasAssetCache 将结果 Blob 转换为导入的 Uassets，每个（内容哈希、配方）一次； UnrealCanvasViewers 注册功能键控预览小部件； UnrealCanvasGraphEditor 是基于 EdGraph 的画布编辑器。服务器仍然是执行和存储的所有者，并且画布文档与 Web UI 保持字节兼容。</div><div class="lang-content">Native Slate editor for Unreal Canvas canvases. UnrealCanvasClient owns the canvas document model and the server client; UnrealCanvasAssetCache turns result blobs into imported uassets, once per (content hash, recipe); UnrealCanvasViewers registers capability-keyed preview widgets; UnrealCanvasGraphEditor is the EdGraph-based canvas editor. The server remains the owner of execution and storage, and canvas documents stay byte-compatible with the web UI.</div></div></div>
    </div>
    <div class="card usage-card" id="usage" data-usage-source="pending">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Unreal Canvas Graph</code> 的使用方法还没按这一份插件单独写完。这里故意不再套「编辑 > 插件启用 / 在 Build.cs 加依赖」的通用模板。</li></ol><p class="usage-note">正在逐条用 AI 按该条目的真实工作流补全。</p></div><div class="lang-content"><ol class="usage-steps"><li>Per-item how-to for <code class="usage-code">Unreal Canvas Graph</code> is not written yet. A generic enable-plugin / Build.cs template is intentionally omitted.</li></ol><p class="usage-note">Being filled one item at a time from that item’s real workflow.</p></div></div></div>
    </div>

    
  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealCanvasClient</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealCanvasAssetCache</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealCanvasRender</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealCanvasViewers</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealCanvasGraphEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Developer/UnrealCanvas/UnrealCanvasGraph/UnrealCanvasGraph.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
