---
layout: default
title: FbxAutomationTestBuilder / FbxAutomationTestBuilder
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">FbxAutomationTestBuilder</div>
      <div class="hero-title-cn">FbxAutomationTestBuilder · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/FbxAutomationTestBuilder/FbxAutomationTestBuilder.uplugin</div></div></div>
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
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：FbxAutomationTestBuilder。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: FbxAutomationTestBuilder. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">FbxAutomationTestBuilder</code>（模块 <code class="usage-code">FbxAutomationTestBuilder</code>，测试类），它用于对 FBX 导入管线做自动化测试。</li><li>打开 <code class="usage-code">Session Frontend &gt; Automation</code>（或 <code class="usage-code">Tools &gt; Test Automation</code>），筛出该插件构建的 FBX 自动化用例。</li><li>运行用例，观察它如何用测试数据构建 FBX 导入场景，并对导入结果（网格、材质、骨骼）做断言。</li><li>把它当测试脚手架模板：复用其 builder 结构，为你自己的导入器写自动化导入测试。</li><li>在命令行/CI 里用 <code class="usage-code">-ExecCmds=&quot;Automation RunTests Fbx&quot;</code> 批量跑，把 FBX 导入回归并入流水线。</li><li>它是开发测试模块，只在开发流程里用，不参与游戏运行，不要作为运行时依赖打包。</li></ol><p class="usage-note">FBX 导入的自动化测试脚手架，学它在 Automation 里构建导入场景并断言；纯开发用途。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">FbxAutomationTestBuilder</code> (module <code class="usage-code">FbxAutomationTestBuilder</code>, a test plugin). It automates tests for the FBX import pipeline.</li><li>Open <code class="usage-code">Session Frontend &gt; Automation</code> (or <code class="usage-code">Tools &gt; Test Automation</code>) and filter for the FBX automation cases this plugin builds.</li><li>Run the cases and study how it constructs an FBX import scenario from test data and asserts on the result (meshes, materials, skeletons).</li><li>Use it as a test scaffolding template: reuse its builder structure to write automated import tests for your own importer.</li><li>Batch-run from the command line or CI with <code class="usage-code">-ExecCmds=&quot;Automation RunTests Fbx&quot;</code> and fold FBX-import regression into the pipeline.</li><li>It is a development test module for the dev workflow only and is not part of the game runtime; do not ship it as a runtime dependency.</li></ol><p class="usage-note">An automation-test scaffold for FBX import — learn to build import scenarios and assert in Automation; dev-only.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">FbxAutomationTestBuilder</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/FbxAutomationTestBuilder/FbxAutomationTestBuilder.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
