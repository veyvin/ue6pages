---
layout: default
title: 混合现实捕捉框架 / Mixed Reality Capture Framework
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Mixed Reality Capture Framework</div>
      <div class="hero-title-cn">混合现实捕捉框架 · 一个简单的框架，为用户提供了一种将混合现实捕获集成到其 VR 项</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Reality</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/MixedRealityCaptureFramework/MixedRealityCaptureFramework.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">一个简单的框架，为用户提供了一种将混合现实捕获集成到其 VR 项目中的方法。</div><div class="lang-content">A simple framework that provides users a way to integrate mixed reality capture into their VR projects.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：一个简单的框架，为用户提供了一种将混合现实捕获集成到其 VR 项目中的方法。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：MixedRealityCaptureFramework。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A simple framework that provides users a way to integrate mixed reality capture into their VR projects.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: MixedRealityCaptureFramework. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Mixed Reality Capture Framework</code>（模块 <code class="usage-code">MixedRealityCaptureFramework</code>），面向 VR。</li><li>它提供一个简单框架，把混合现实捕获（MRC）集成到 VR 项目。</li><li>配置捕获相机/合成，把真实与虚拟画面合成输出。</li><li>运行时模块；需 VR + 捕获硬件配合。</li></ol><p class="usage-note">把混合现实捕获(MRC)集成到 VR 项目的框架。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Mixed Reality Capture Framework</code> (module <code class="usage-code">MixedRealityCaptureFramework</code>) for VR.</li><li>It provides a simple framework to integrate mixed reality capture (MRC) into VR projects.</li><li>Configure the capture camera/compositing to combine real and virtual footage.</li><li>A runtime module; requires VR plus capture hardware.</li></ol><p class="usage-note">A framework to integrate mixed reality capture (MRC) into VR projects.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">MixedRealityCaptureFramework</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/MixedRealityCaptureFramework/MixedRealityCaptureFramework.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
