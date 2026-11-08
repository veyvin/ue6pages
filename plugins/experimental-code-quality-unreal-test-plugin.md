---
layout: default
title: 实验代码质量虚幻测试插件 / Experimental Code Quality Unreal Test Plugin
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Experimental Code Quality Unreal Test Plugin</div>
      <div class="hero-title-cn">实验代码质量虚幻测试插件 · 虚幻引擎实验功能的简化测试</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/CQTestExperimental/CQTestExperimental.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">虚幻引擎实验功能的简化测试</div><div class="lang-content">Simplified testing of experimental features for Unreal Engine</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：虚幻引擎实验功能的简化测试</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：CQTestExperimentalTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Simplified testing of experimental features for Unreal Engine</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: CQTestExperimentalTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>这是 CQTest 框架的实验测试插件（模块 <code class="usage-code">CQTestExperimentalTests</code>）。启用后到源码里找该模块，看它如何用 <code class="usage-code">TEST_CLASS</code>、<code class="usage-code">TEST_METHOD</code> 等 CQTest 宏组织用例。</li><li>打开 <code class="usage-code">Session Frontend &gt; Automation</code>（新版为 <code class="usage-code">Tools &gt; Test Automation</code>），用过滤器筛出 CQTest 前缀的实验测试并运行。</li><li>命令行或 CI 里用 <code class="usage-code">-ExecCmds=&quot;Automation RunTests CQTest&quot;</code> 批量跑，把结果并入回归流水线。</li><li>把它当 CQTest 写法参考：复制其中的 <code class="usage-code">TEST_CLASS</code> / <code class="usage-code">TEST_METHOD</code> 结构，给你自己的代码质量检查写自动化测试。</li><li>若测试因 Experimental 接口变动而失败，对照当前引擎版本更新断言，不要为了变绿而删掉用例。</li><li>这类测试模块只服务开发流程，默认不参与游戏运行；打包时不必也不应作为运行时依赖。</li></ol><p class="usage-note">CQTest 实验用例，重点是学它的宏写法与在 Automation 里跑，不是拿来运行时用。</p></div><div class="lang-content"><ol class="usage-steps"><li>This is the CQTest framework&#x27;s experimental test plugin (module <code class="usage-code">CQTestExperimentalTests</code>). Enable it, then find the module in source to see how it organizes cases with <code class="usage-code">TEST_CLASS</code>, <code class="usage-code">TEST_METHOD</code>, and other CQTest macros.</li><li>Open <code class="usage-code">Session Frontend &gt; Automation</code> (or <code class="usage-code">Tools &gt; Test Automation</code>), filter for the CQTest-prefixed experimental tests, and run them.</li><li>From the command line or CI, batch-run with <code class="usage-code">-ExecCmds=&quot;Automation RunTests CQTest&quot;</code> and fold the results into your regression pipeline.</li><li>Use it as a CQTest style reference: copy the <code class="usage-code">TEST_CLASS</code> / <code class="usage-code">TEST_METHOD</code> structure to write automation tests for your own code-quality checks.</li><li>If a test fails because an Experimental interface changed, update the assertion to the current engine version — do not delete cases just to make it green.</li><li>These test modules serve the development workflow only and are not part of the game runtime; do not make them a runtime dependency when packaging.</li></ol><p class="usage-note">Experimental CQTest cases — the value is learning its macro style and running via Automation, not shipping it.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CQTestExperimentalTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/CQTestExperimental/CQTestExperimental.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
