---
layout: default
title: 蓝图工具集 / Blueprint Toolsets
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">B</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Blueprint Toolsets</div>
      <div class="hero-title-cn">蓝图工具集 · 用于蓝图资产的 AI 助手工具集，包括 Blueprint Gr</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Experimental</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/BlueprintToolsets/BlueprintToolsets.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于蓝图资产的 AI 助手工具集，包括 Blueprint Graph DSL。</div><div class="lang-content">AI assistant toolsets for Blueprint assets, including the Blueprint Graph DSL.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于蓝图资产的 AI 助手工具集，包括 Blueprint Graph DSL。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：BlueprintToolsets。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: AI assistant toolsets for Blueprint assets, including the Blueprint Graph DSL.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: BlueprintToolsets. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 启用实验性 <code class="usage-code">Blueprint Toolsets</code>（模块 <code class="usage-code">BlueprintToolsets</code>），并同时启用编辑器 AI / Toolset Registry 相关插件后重启。</li><li>确认助手能看到蓝图工具集：它提供针对蓝图资产的只读/只写工具，核心是 <code class="usage-code">Blueprint Graph DSL</code>。</li><li>在编辑器 AI 会话里指定一张蓝图资产，让助手用 DSL 描述 Event Graph / 函数图上的节点与连线，而不是让它猜截图。</li><li>需要改图时，走工具集的写接口应用 DSL 补丁（添加节点、接线、设引脚），再在蓝图编辑器里打开该资产核对编译。</li><li>把 <code class="usage-code">Blueprint Graph Formatter</code> 的 toolset 模块当作排版补充，而不是替代本插件的 DSL 读写。</li><li>此插件只服务编辑器自动化/AI，切勿加入 Shipping 游戏模块。</li></ol><p class="usage-note">Experimental Toolset：给编辑器 AI 用的 Blueprint Graph DSL，不是运行时蓝图 API。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Blueprint Toolsets</code> in <code class="usage-code">Edit &gt; Plugins</code> (module <code class="usage-code">BlueprintToolsets</code>), plus the editor AI / Toolset Registry plugins, then restart.</li><li>Confirm the assistant lists Blueprint tools: read/write helpers for Blueprint assets, including the <code class="usage-code">Blueprint Graph DSL</code>.</li><li>In an editor AI session, point at one Blueprint asset and have the assistant describe Event/function graphs via the DSL instead of guessing from screenshots.</li><li>To mutate a graph, apply DSL patches through the write tools (add nodes, wires, pin values), then open the asset in the Blueprint editor and compile.</li><li>Treat <code class="usage-code">BlueprintGraphFormatterToolset</code> as layout-only; this plugin owns structural DSL read/write.</li><li>Editor automation/AI only — never add <code class="usage-code">BlueprintToolsets</code> to a Shipping game module.</li></ol><p class="usage-note">Experimental toolset: Blueprint Graph DSL for the in-editor AI, not a runtime Blueprint API.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">BlueprintToolsets</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/BlueprintToolsets/BlueprintToolsets.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
