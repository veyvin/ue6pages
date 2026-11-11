---
layout: default
title: 游戏功能工具集 / Game Features Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Game Features Toolset</div>
      <div class="hero-title-cn">游戏功能工具集 · 用于通过 AI 工具集注册表列出、检查和创建游戏功能插件的工具集</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/GameFeaturesToolset/GameFeaturesToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于通过 AI 工具集注册表列出、检查和创建游戏功能插件的工具集。</div><div class="lang-content">Toolset for listing, inspecting, and creating Game Feature Plugins via the AI Toolset Registry.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于通过 AI 工具集注册表列出、检查和创建游戏功能插件的工具集。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：GameFeaturesToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Toolset for listing, inspecting, and creating Game Feature Plugins via the AI Toolset Registry.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: GameFeaturesToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">Game Features Toolset</code>（模块 <code class="usage-code">GameFeaturesToolset</code>），并打开 <code class="usage-code">Toolset Registry</code> / 编辑器 AI；同时保持 <code class="usage-code">Game Features</code> 开启。</li><li>助手应出现列出、检查、创建 Game Feature Plugin 的工具。让它列出当前已注册 GFP，对照 <code class="usage-code">UGameFeaturesSubsystem</code> 或插件目录，而不是打开空白关卡。</li><li>用「创建」工具生成一个最小 GFP（含 <code class="usage-code">UGameFeatureData</code>）；内容浏览器/<code class="usage-code">Plugins</code> 目录应出现新插件，状态为 Registered 或可 Load。</li><li>再让助手 Inspect 该 GFP 的 Actions（加组件、数据包等）。创建失败时看路径是否落在允许的 Plugins 目录、以及 GameFeatures 是否启用。</li><li>不要把 <code class="usage-code">GameFeaturesToolset</code> 打进游戏包；它只替 AI 改工程插件树。</li></ol><p class="usage-note">AI 侧的 GFP 增删查，真正加载激活仍走 `GameFeatures` 子系统。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Game Features Toolset</code> (module <code class="usage-code">GameFeaturesToolset</code>) plus <code class="usage-code">Toolset Registry</code> / editor AI, and keep <code class="usage-code">Game Features</code> on.</li><li>The assistant should expose list/inspect/create Game Feature Plugin tools. Ask it to list registered GFPs and compare with <code class="usage-code">UGameFeaturesSubsystem</code> or the Plugins folder — not an empty map.</li><li>Use create to scaffold a minimal GFP (with <code class="usage-code">UGameFeatureData</code>). A new plugin should appear under <code class="usage-code">Plugins</code> and show Registered or loadable.</li><li>Inspect its Actions (add component, data packs). If create fails, check the target Plugins path and that GameFeatures is enabled.</li><li>Do not cook <code class="usage-code">GameFeaturesToolset</code> into the game; it only lets the AI mutate the project plugin tree.</li></ol><p class="usage-note">AI list/inspect/create for GFPs; load/activate still goes through the `GameFeatures` subsystem.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GameFeaturesToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/GameFeaturesToolset/GameFeaturesToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
