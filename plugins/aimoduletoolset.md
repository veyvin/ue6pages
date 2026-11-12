---
layout: default
title: AI模块工具集 / AIModuleToolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AIModuleToolset</div>
      <div class="hero-title-cn">AI模块工具集 · AIModule 系统工具集</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>AI</span><span class="chip">Epic Games</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/AIModuleToolset/AIModuleToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">AIModule 系统工具集</div><div class="lang-content">Toolset for AIModule Systems</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：AIModule 系统工具集</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：AIModuleToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Toolset for AIModule Systems</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: AIModuleToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">AIModuleToolset</code>（模块 <code class="usage-code">AIModuleToolset</code>），并同时打开 <code class="usage-code">AI Assistant</code>（以及需要时的 <code class="usage-code">All Toolsets</code>）。</li><li>打开编辑器 AI Assistant 面板，确认已注册面向 <code class="usage-code">AIModule</code> 的工具（行为树、黑板、AI 控制器等检查/改写），而不是关卡里的 <code class="usage-code">AIController</code> 组件。</li><li>在内容浏览器打开一份 <code class="usage-code">Behavior Tree</code> 或 <code class="usage-code">Blackboard</code>，让助手通过本 Toolset 读取节点/键，而不是你在 Details 里手改。</li><li>不要把 <code class="usage-code">AIModuleToolset</code> 加进游戏模块 <code class="usage-code">Build.cs</code> 或 Shipping；它只给编辑器助手用。</li><li>需要全套助手工具时改用聚合插件 <code class="usage-code">All Toolsets</code>，不要在 PIE 里找本插件的 Actor。</li></ol><p class="usage-note">编辑器 AI 助手的 `AIModule` 工具包，不是运行时导航或行为树运行时。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">AIModuleToolset</code> (module <code class="usage-code">AIModuleToolset</code>) together with <code class="usage-code">AI Assistant</code> (and <code class="usage-code">All Toolsets</code> if you want every toolset).</li><li>Open the in-editor AI Assistant and confirm tools targeting <code class="usage-code">AIModule</code> (Behavior Tree, Blackboard, AI controller inspect/edit) — not an <code class="usage-code">AIController</code> you add to a pawn.</li><li>Open a <code class="usage-code">Behavior Tree</code> or <code class="usage-code">Blackboard</code> and let the assistant read nodes/keys through this toolset instead of editing Details by hand.</li><li>Do not add <code class="usage-code">AIModuleToolset</code> to a game <code class="usage-code">Build.cs</code> or Shipping; it is editor-assistant only.</li><li>Use aggregator <code class="usage-code">All Toolsets</code> for every assistant tool; do not look for an actor from this plugin in PIE.</li></ol><p class="usage-note">Editor-assistant tooling over `AIModule`, not runtime navigation or Behavior Tree execution.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AIModuleToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/AIModuleToolset/AIModuleToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
