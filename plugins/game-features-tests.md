---
layout: default
title: 游戏功能测试 / Game Features Tests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Game Features Tests</div>
      <div class="hero-title-cn">游戏功能测试 · 测试 GameFeatures 插件。由 GameFeature</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/GameFeaturesTests/GameFeaturesTests.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">测试 GameFeatures 插件。由 GameFeatures 的 TestConfig 声明的同伴。</div><div class="lang-content">Tests for the GameFeatures plugin. Companion declared by GameFeatures' TestConfig.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：测试 GameFeatures 插件。由 GameFeatures 的 TestConfig 声明的同伴。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：GameFeaturesTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Tests for the GameFeatures plugin. Companion declared by GameFeatures' TestConfig.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: GameFeaturesTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>这是 <code class="usage-code">Game Features</code> 的 <code class="usage-code">TestConfig</code> 同伴插件（模块 <code class="usage-code">GameFeaturesTests</code>），用于跑 GFP 加载/激活自动化，不是给玩家开的功能包。</li><li>同时启用 <code class="usage-code">Game Features</code>。用 Session Frontend 或 <code class="usage-code">Automation RunTests</code> 过滤 <code class="usage-code">GameFeatures</code> / <code class="usage-code">GameFeaturesTests</code> 相关用例。</li><li>测试会装载临时 Game Feature 插件、检查 <code class="usage-code">UGameFeaturesSubsystem</code> 状态机（Registered → Loaded → Active）再卸载；失败时看哪一步 Status 卡住。</li><li>不要把本插件列进项目默认启用列表给 Shipping；仅 Editor/Program 测试目标加载。</li><li>写自己的 GFP 测试时参考这些用例如何创建 <code class="usage-code">UGameFeatureData</code> 与 Action，而不是复制到游戏模块。</li></ol><p class="usage-note">GameFeatures 的自动化同伴，不会给项目增加可玩功能。</p></div><div class="lang-content"><ol class="usage-steps"><li>This is the <code class="usage-code">TestConfig</code> companion for <code class="usage-code">Game Features</code> (module <code class="usage-code">GameFeaturesTests</code>): automation for GFP load/activate, not a player-facing feature pack.</li><li>Keep <code class="usage-code">Game Features</code> enabled. In Session Frontend or <code class="usage-code">Automation RunTests</code>, filter <code class="usage-code">GameFeatures</code> / <code class="usage-code">GameFeaturesTests</code>.</li><li>Tests mount a temporary Game Feature plugin, walk <code class="usage-code">UGameFeaturesSubsystem</code> (Registered → Loaded → Active), then unload. Failures usually stick on one of those states.</li><li>Do not enable this plugin by default in shipping projects; load it only on Editor/Program test targets.</li><li>When writing your own GFP tests, copy how these cases build <code class="usage-code">UGameFeatureData</code> and actions — do not ship the test module in the game.</li></ol><p class="usage-note">Automation companion for GameFeatures; it does not add playable features.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GameFeaturesTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/GameFeaturesTests/GameFeaturesTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
