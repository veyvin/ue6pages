---
layout: default
title: 属性动画核心 / Property Animator Core
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Property Animator Core</div>
      <div class="hero-title-cn">属性动画核心 · 在运行时和编辑器中控制属性的可重用行为</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/PropertyAnimatorCore/PropertyAnimatorCore.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">在运行时和编辑器中控制属性的可重用行为</div><div class="lang-content">Re-usable behaviors to control properties at runtime and in editor</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：PropertyAnimatorCore, PropertyAnimatorCoreEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: PropertyAnimatorCore, PropertyAnimatorCoreEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Property Animator Core</code>（运行时 <code class="usage-code">PropertyAnimatorCore</code>，编辑器 <code class="usage-code">PropertyAnimatorCoreEditor</code>）。</li><li>它提供在运行时和编辑器中控制属性的可复用行为（核心层）。</li><li>作为 <code class="usage-code">Property Animator</code> 的底层依赖，不要单独当最终动画工具。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">属性动画器的核心：可复用的属性控制行为。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Property Animator Core</code> (runtime <code class="usage-code">PropertyAnimatorCore</code>, editor <code class="usage-code">PropertyAnimatorCoreEditor</code>).</li><li>It provides reusable behaviors to control properties at runtime and in the editor (the core layer).</li><li>A low-level dependency for <code class="usage-code">Property Animator</code>; not the end-user animator by itself.</li><li>Game modules depend on runtime modules; editor modules are Editor-target only.</li></ol><p class="usage-note">Property Animator core: reusable property-control behaviors.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyAnimatorCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyAnimatorCoreEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/PropertyAnimatorCore/PropertyAnimatorCore.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
