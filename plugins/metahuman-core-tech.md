---
layout: default
title: 超人类核心技术 / MetaHuman Core Tech
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">MetaHuman Core Tech</div>
      <div class="hero-title-cn">超人类核心技术 · MetaHuman Creator 和 MetaHuman An</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>MetaHuman</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">6</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MetaHuman/MetaHumanCoreTechLib/MetaHumanCoreTech.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">MetaHuman Creator 和 MetaHuman Animator 插件背后的核心技术。</div><div class="lang-content">The core technology behind the MetaHuman Creator and MetaHuman Animator plugins.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：MetaHumanCoreTechLib, MetaHumanCoreTech, MetaHumanImageViewer, MetaHumanCaptureData, MetaHumanPipelineCore, MetaHumanBodyTrackerInterface。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: MetaHumanCoreTechLib, MetaHumanCoreTech, MetaHumanImageViewer, MetaHumanCaptureData, MetaHumanPipelineCore, MetaHumanBodyTrackerInterface. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MetaHuman Core Tech</code>（模块 <code class="usage-code">MetaHumanCoreTech</code>、<code class="usage-code">MetaHumanCoreTechLib</code>、<code class="usage-code">MetaHumanImageViewer</code>、<code class="usage-code">MetaHumanCaptureData</code>、<code class="usage-code">MetaHumanPipelineCore</code>、<code class="usage-code">MetaHumanBodyTrackerInterface</code> 等）。</li><li>它是 MetaHuman Creator 与 MetaHuman Animator 背后的核心技术层。</li><li>通常作为底层依赖随上层 MetaHuman 插件启用，不直接面向最终用户操作。</li><li>写自定义 MetaHuman 管线/处理时才直接依赖这些模块。</li></ol><p class="usage-note">MetaHuman Creator/Animator 背后的底层核心技术。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MetaHuman Core Tech</code> (modules <code class="usage-code">MetaHumanCoreTech</code>, <code class="usage-code">MetaHumanCoreTechLib</code>, <code class="usage-code">MetaHumanImageViewer</code>, <code class="usage-code">MetaHumanCaptureData</code>, <code class="usage-code">MetaHumanPipelineCore</code>, <code class="usage-code">MetaHumanBodyTrackerInterface</code>, etc.).</li><li>It is the core technology layer behind MetaHuman Creator and MetaHuman Animator.</li><li>Usually enabled as a low-level dependency with the upper MetaHuman plugins; not directly operated by end users.</li><li>Depend on these modules directly only when writing custom MetaHuman pipelines/processing.</li></ol><p class="usage-note">The low-level core tech behind MetaHuman Creator/Animator.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (6)</div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanCoreTechLib</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanCoreTech</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanImageViewer</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanCaptureData</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanPipelineCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanBodyTrackerInterface</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MetaHuman/MetaHumanCoreTechLib/MetaHumanCoreTech.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
