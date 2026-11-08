---
layout: default
title: 代码质量测试虚幻测试插件 / Code Quality Tests Unreal Test Plugin
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Code Quality Tests Unreal Test Plugin</div>
      <div class="hero-title-cn">代码质量测试虚幻测试插件 · CQTest 虚幻引擎模块的测试</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/CQTest/CQTest.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">CQTest 虚幻引擎模块的测试</div><div class="lang-content">Tests for the CQTest Unreal Engine module</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：CQTest 虚幻引擎模块的测试</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CQTestTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Tests for the CQTest Unreal Engine module</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CQTestTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用测试插件 <code class="usage-code">Code Quality Tests Unreal Test Plugin</code>（描述符 <code class="usage-code">CQTest.uplugin</code>，模块 <code class="usage-code">CQTestTests</code>）。它测的是引擎 <code class="usage-code">CQTest</code> 框架，不是给游戏加组件。</li><li>打开 <code class="usage-code">Tools &gt; Session Frontend</code> → <code class="usage-code">Automation</code>，筛选 <code class="usage-code">CQTest</code> / <code class="usage-code">CQTestTests</code>。</li><li>跑这组用例，确认断言、期望宏与测试夹具在编辑器自动化会话里通过。</li><li>命令行也可用 <code class="usage-code">UnrealEditor-Cmd</code> 的 <code class="usage-code">Automation RunTests</code> 指向 <code class="usage-code">CQTest</code> 过滤器，便于 CI。</li><li>不要把 <code class="usage-code">CQTestTests</code> 链进游戏模块或 Shipping 包。</li></ol><p class="usage-note">CQTest 框架的自测插件，不是质量门禁配置工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Code Quality Tests Unreal Test Plugin</code> (<code class="usage-code">CQTest.uplugin</code>, module <code class="usage-code">CQTestTests</code>). It tests the engine <code class="usage-code">CQTest</code> module; it is not a gameplay component.</li><li>Open <code class="usage-code">Tools &gt; Session Frontend</code> → <code class="usage-code">Automation</code> and filter <code class="usage-code">CQTest</code> / <code class="usage-code">CQTestTests</code>.</li><li>Run the suite and confirm asserts, expect macros, and fixtures pass in the editor automation session.</li><li>For CI, invoke <code class="usage-code">UnrealEditor-Cmd</code> <code class="usage-code">Automation RunTests</code> with a <code class="usage-code">CQTest</code> filter.</li><li>Do not link <code class="usage-code">CQTestTests</code> into a game module or Shipping package.</li></ol><p class="usage-note">Self-tests for the CQTest framework, not a quality-gate settings UI.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CQTestTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/CQTest/CQTest.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
