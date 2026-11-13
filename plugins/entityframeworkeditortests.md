---
layout: default
title: EntityFrameworkEditor测试 / EntityFrameworkEditorTests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">EntityFrameworkEditorTests</div>
      <div class="hero-title-cn">EntityFrameworkEditor测试 · EntityFramework 的编辑器工作流程测试</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Verse</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/EntityFrameworkEditorTests/EntityFrameworkEditorTests.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">EntityFramework 的编辑器工作流程测试</div><div class="lang-content">Editor workflow tests for EntityFramework</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：EntityFramework 的编辑器工作流程测试</p><p>Verse 语言/运行时的一块：编译、VM、设备或编辑器支持，服务 UEFN 体验。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：SceneGraphEditorWorkflows。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Editor workflow tests for EntityFramework</p><p>A slice of the Verse language/runtime: compiler, VM, devices, or editor support for UEFN.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: SceneGraphEditorWorkflows. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>这是 <code class="usage-code">EntityFramework</code> 的编辑器工作流自动化测试插件（模块 <code class="usage-code">SceneGraphEditorWorkflows</code>），验证编辑器内的场景图/实体操作。</li><li>在已启用 <code class="usage-code">EntityFramework</code> 的编辑器环境里启用该测试插件。</li><li>打开 <code class="usage-code">Session Frontend &gt; Automation</code>，在过滤器里搜 <code class="usage-code">SceneGraphEditorWorkflows</code> 或 <code class="usage-code">EntityFramework</code>。</li><li>选中用例点 <code class="usage-code">Start Tests</code> 运行，看结果与日志定位失败步骤。</li><li>它只在编辑器里跑自动化，不进游戏运行时，不要加入 Shipping。</li></ol><p class="usage-note">纯测试插件，提供的是编辑器自动化用例而非可用 API；CI 里用命令行 `Automation RunTests` 跑最省事。</p></div><div class="lang-content"><ol class="usage-steps"><li>This is the editor-workflow automation-test plugin for <code class="usage-code">EntityFramework</code> (module <code class="usage-code">SceneGraphEditorWorkflows</code>), validating in-editor scene-graph/entity operations.</li><li>Enable it in an editor that already has <code class="usage-code">EntityFramework</code> enabled.</li><li>Open <code class="usage-code">Session Frontend &gt; Automation</code> and filter for <code class="usage-code">SceneGraphEditorWorkflows</code> or <code class="usage-code">EntityFramework</code>.</li><li>Select the cases and click <code class="usage-code">Start Tests</code>, then read results and logs to find failing steps.</li><li>It runs editor automation only — never in a game runtime, never in Shipping.</li></ol><p class="usage-note">A pure test plugin that provides editor automation cases, not usable API; running `Automation RunTests` from the command line is the easiest CI path.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">SceneGraphEditorWorkflows</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/EntityFrameworkEditorTests/EntityFrameworkEditorTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
