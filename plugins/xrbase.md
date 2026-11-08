---
layout: default
title: XR基地 / XRBase
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">X</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">XRBase</div>
      <div class="hero-title-cn">XR基地 · XR 基本功能实现。  （通常这个插件会被另一个需要它的插件自动</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Reality</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/XRBase/XRBase.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">XR 基本功能实现。  （通常这个插件会被另一个需要它的插件自动启用。）</div><div class="lang-content">XR Base Feature Implementations.  (Generally this plugin will be automatically enabled by another plugin that requires it.)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：XR 基本功能实现。  （通常这个插件会被另一个需要它的插件自动启用。）</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：XRBase, XRBaseEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: XR Base Feature Implementations.  (Generally this plugin will be automatically enabled by another plugin that requires it.)</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: XRBase, XRBaseEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">XRBase</code>（运行时 <code class="usage-code">XRBase</code>，编辑器 <code class="usage-code">XRBaseEditor</code>）。</li><li>它是 XR 基本功能实现（通常被需要它的其它插件自动启用）。</li><li>作为 XR 相关插件的底层依赖，一般无需手动启停。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">XR 基本功能实现（常被依赖插件自动启用）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">XRBase</code> (runtime <code class="usage-code">XRBase</code>, editor <code class="usage-code">XRBaseEditor</code>).</li><li>It is the XR base feature implementation (usually auto-enabled by another plugin that needs it).</li><li>A low-level dependency for XR-related plugins; generally no need to toggle manually.</li><li>Game modules depend on runtime modules; editor modules go to Editor targets only.</li></ol><p class="usage-note">XR base feature implementation (often auto-enabled by a dependent plugin).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">XRBase</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">XRBaseEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/XRBase/XRBase.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
