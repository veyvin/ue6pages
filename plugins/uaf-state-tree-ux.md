---
layout: default
title: UAF 状态树 UX / UAF State Tree UX
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">UAF State Tree UX</div>
      <div class="hero-title-cn">UAF 状态树 UX · UAF 工作区中的 uaf-web-ux 状态树设计原型：添加由</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/UAF/UAFSandbox/UAFSandboxStateTreeUX/UAFSandboxStateTreeUX.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">UAF 工作区中的 uaf-web-ux 状态树设计原型：添加由共享状态树视图模型驱动的以状态为中心的视图 (UX) 选项卡。</div><div class="lang-content">Prototype of the uaf-web-ux State Tree design inside the UAF workspace: adds a State Centric View (UX) tab driven by the shared State Tree view model.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：UAF 工作区中的 uaf-web-ux 状态树设计原型：添加由共享状态树视图模型驱动的以状态为中心的视图 (UX) 选项卡。</p><p>UAF 家族：新动画图框架上的一层（状态、层、Pose Search、Control Rig 桥）。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：UAFSandboxStateTreeUXEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Prototype of the uaf-web-ux State Tree design inside the UAF workspace: adds a State Centric View (UX) tab driven by the shared State Tree view model.</p><p>UAF family: a layer on the Unreal Animation Framework (state, layering, Pose Search, Control Rig bridge).</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: UAFSandboxStateTreeUXEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">UAF State Tree UX</code>（模块 <code class="usage-code">UAFSandboxStateTreeUXEditor</code>）。</li><li>它是 uaf-web-ux 状态树设计原型：添加由共享状态树视图模型驱动的、以状态为中心的视图(UX)选项卡。</li><li>在 UAF 工作区里体验新的状态树 UX 选项卡。</li><li>这是编辑器原型工具，只进 Editor Target。</li></ol><p class="usage-note">uaf-web-ux 状态树 UX 设计原型（状态中心选项卡）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">UAF State Tree UX</code> (module <code class="usage-code">UAFSandboxStateTreeUXEditor</code>).</li><li>It is the uaf-web-ux state-tree design prototype: adds a state-centric view (UX) tab driven by a shared state-tree view model.</li><li>Try the new state-tree UX tab in the UAF workspace.</li><li>It is an editor prototype tool for Editor targets only.</li></ol><p class="usage-note">The uaf-web-ux state-tree UX prototype (state-centric tab).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">UAFSandboxStateTreeUXEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/UAF/UAFSandbox/UAFSandboxStateTreeUX/UAFSandboxStateTreeUX.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
