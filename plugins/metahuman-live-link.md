---
layout: default
title: 超人类实时链接 / MetaHuman Live Link
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">MetaHuman Live Link</div>
      <div class="hero-title-cn">超人类实时链接 · 用于流式传输实时 MetaHuman 动画数据的 Live Li</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>MetaHuman</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">7</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MetaHuman/MetaHumanLiveLink/MetaHumanLiveLink.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于流式传输实时 MetaHuman 动画数据的 Live Link 源和相关实用程序。</div><div class="lang-content">Live Link sources and associated utilities for streaming real time MetaHuman animation data.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Live Link 把外部设备的实时数据（动捕、摄像机、灯光、面捕）流进编辑器或运行时，驱动骨骼、摄像机、Control Rig。虚拟制片和 MetaHuman 面捕的主干。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：MetaHumanLiveLinkSource, MetaHumanLiveLinkSourceEditor, LiveLinkFaceSource, LiveLinkFaceSourceEditor, LiveLinkFaceDiscovery, MetaHumanLocalLiveLinkSource, MetaHumanLocalLiveLinkSourceEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine</a></p></div><div class="lang-content"><p>Live Link streams live data from mocap, cameras, lights, and facial capture into the editor or runtime to drive skeletons, cameras, and Control Rig. It is the backbone of virtual production and MetaHuman face capture.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: MetaHumanLiveLinkSource, MetaHumanLiveLinkSourceEditor, LiveLinkFaceSource, LiveLinkFaceSourceEditor, LiveLinkFaceDiscovery, MetaHumanLocalLiveLinkSource, MetaHumanLocalLiveLinkSourceEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MetaHuman Live Link</code>（模块 <code class="usage-code">MetaHumanLiveLinkSource</code>、<code class="usage-code">LiveLinkFaceSource</code>、<code class="usage-code">LiveLinkFaceDiscovery</code>、<code class="usage-code">MetaHumanLocalLiveLinkSource</code> 等，含 Editor 版）。</li><li>它提供用于流式传输实时 MetaHuman 动画数据的 Live Link 源。</li><li>把面捕/Live Link Face 数据流进 MetaHuman，实时驱动面部动画。</li><li>Game 模块依赖运行时模块；<code class="usage-code">*Editor</code> 模块只进 Editor Target。</li></ol><p class="usage-note">流式传输实时 MetaHuman 动画数据的 Live Link 源（面捕驱动）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MetaHuman Live Link</code> (modules <code class="usage-code">MetaHumanLiveLinkSource</code>, <code class="usage-code">LiveLinkFaceSource</code>, <code class="usage-code">LiveLinkFaceDiscovery</code>, <code class="usage-code">MetaHumanLocalLiveLinkSource</code>, etc., with Editor variants).</li><li>It provides Live Link sources for streaming real-time MetaHuman animation data.</li><li>Stream face capture / Live Link Face data into a MetaHuman to drive facial animation live.</li><li>Game modules depend on runtime modules; <code class="usage-code">*Editor</code> modules go to Editor targets only.</li></ol><p class="usage-note">Live Link sources streaming real-time MetaHuman animation data (face-capture driven).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (7)</div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanLiveLinkSource</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanLiveLinkSourceEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkFaceSource</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkFaceSourceEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkFaceDiscovery</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanLocalLiveLinkSource</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanLocalLiveLinkSourceEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MetaHuman/MetaHumanLiveLink/MetaHumanLiveLink.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
