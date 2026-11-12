---
layout: default
title: 实体框架测试 / EntityFrameworkTests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">EntityFrameworkTests</div>
      <div class="hero-title-cn">实体框架测试 · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Verse</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">4</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/EntityFrameworkTests/EntityFrameworkTests.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">（无描述）</div><div class="lang-content">(no description)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>Verse 语言/运行时的一块：编译、VM、设备或编辑器支持，服务 UEFN 体验。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：EntityTestSuite, ExecutionTestSuite, ComponentTestSuite, EntityRegistryTestSuite。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>A slice of the Verse language/runtime: compiler, VM, devices, or editor support for UEFN.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: EntityTestSuite, ExecutionTestSuite, ComponentTestSuite, EntityRegistryTestSuite. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>这是 <code class="usage-code">EntityFramework</code> 的运行时测试套件插件，含 <code class="usage-code">EntityTestSuite</code>、<code class="usage-code">ExecutionTestSuite</code>、<code class="usage-code">ComponentTestSuite</code>、<code class="usage-code">EntityRegistryTestSuite</code>。</li><li>在启用 <code class="usage-code">EntityFramework</code> 的构建里启用它，让测试模块被编译进来。</li><li>在 <code class="usage-code">Session Frontend &gt; Automation</code> 按套件名（如 <code class="usage-code">EntityTestSuite</code>）过滤用例。</li><li>勾选后 <code class="usage-code">Start Tests</code>，关注实体创建、组件注册、执行调度是否全绿。</li><li>命令行用 <code class="usage-code">-ExecCmds=&quot;Automation RunTests EntityTestSuite&quot;</code> 批跑，投产前确保测试模块不随游戏打包。</li></ol><p class="usage-note">这些测试覆盖实体/组件的核心行为，读测试源码是理解 EntityFramework 数据流的好材料，但它不提供业务 API。</p></div><div class="lang-content"><ol class="usage-steps"><li>This is the runtime test-suite plugin for <code class="usage-code">EntityFramework</code>, bundling <code class="usage-code">EntityTestSuite</code>, <code class="usage-code">ExecutionTestSuite</code>, <code class="usage-code">ComponentTestSuite</code>, <code class="usage-code">EntityRegistryTestSuite</code>.</li><li>Enable it in a build that has <code class="usage-code">EntityFramework</code> so the test modules compile in.</li><li>In <code class="usage-code">Session Frontend &gt; Automation</code>, filter cases by suite name (e.g., <code class="usage-code">EntityTestSuite</code>).</li><li>Select and <code class="usage-code">Start Tests</code>, watching that entity creation, component registry, and execution scheduling all pass.</li><li>Batch-run from the command line with <code class="usage-code">-ExecCmds=&quot;Automation RunTests EntityTestSuite&quot;</code>; make sure the test modules aren&#x27;t packaged into the game.</li></ol><p class="usage-note">These suites cover core entity/component behavior — good reading to learn EntityFramework&#x27;s data flow — but they expose no business API.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (4)</div><div class="module-item"><span class="dot"></span><span class="name mono">EntityTestSuite</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ExecutionTestSuite</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ComponentTestSuite</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EntityRegistryTestSuite</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/EntityFrameworkTests/EntityFrameworkTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
