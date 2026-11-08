---
layout: default
title: 运动设计数据链路 / Motion Design Data Link
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Motion Design Data Link</div>
      <div class="hero-title-cn">运动设计数据链路 · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DataLink/DataLink.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">（无描述）</div><div class="lang-content">(no description)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DataLink, DataLinkEdGraph, DataLinkEditor, DataLinkHttp, DataLinkJson, DataLinkJsonEditor, DataLinkDataTable, DataLinkWebSocket。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DataLink, DataLinkEdGraph, DataLinkEditor, DataLinkHttp, DataLinkJson, DataLinkJsonEditor, DataLinkDataTable, DataLinkWebSocket. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Motion Design Data Link</code>（模块 <code class="usage-code">DataLink</code>、<code class="usage-code">DataLinkEdGraph</code>、<code class="usage-code">DataLinkHttp</code>、<code class="usage-code">DataLinkJson</code>、<code class="usage-code">DataLinkDataTable</code>、<code class="usage-code">DataLinkWebSocket</code>，编辑器 <code class="usage-code">DataLinkEditor</code> 等）。</li><li>它用数据链接图把外部数据源（HTTP/JSON/DataTable/WebSocket）接入 Motion Design。</li><li>在数据链接编辑器里搭建图，定义取数/推送逻辑。</li><li>Game 模块依赖运行时模块；<code class="usage-code">*Editor</code> 模块只进 Editor Target。</li></ol><p class="usage-note">Data Link 数据链接图（HTTP/JSON/DataTable/WebSocket 接入）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Motion Design Data Link</code> (modules <code class="usage-code">DataLink</code>, <code class="usage-code">DataLinkEdGraph</code>, <code class="usage-code">DataLinkHttp</code>, <code class="usage-code">DataLinkJson</code>, <code class="usage-code">DataLinkDataTable</code>, <code class="usage-code">DataLinkWebSocket</code>, editor <code class="usage-code">DataLinkEditor</code>, etc.).</li><li>It uses data-link graphs to bring external data sources (HTTP/JSON/DataTable/WebSocket) into Motion Design.</li><li>Build graphs in the Data Link editor to define fetch/push logic.</li><li>Game modules depend on runtime modules; <code class="usage-code">*Editor</code> modules go to Editor targets only.</li></ol><p class="usage-note">Data Link graphs (HTTP/JSON/DataTable/WebSocket hookup).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">DataLink</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkEdGraph</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkHttp</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkJson</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkJsonEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkDataTable</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataLinkWebSocket</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DataLink/DataLink.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
