---
layout: default
title: 自动化测试工具集 / AutomationTestToolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AutomationTestToolset</div>
      <div class="hero-title-cn">自动化测试工具集 · 自动化测试发现和执行工具。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Uncategorized</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/AutomationTestToolset/AutomationTestToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">自动化测试发现和执行工具。</div><div class="lang-content">Automation test discovery and execution tools.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：自动化测试发现和执行工具。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：AutomationTestToolset, AutomationTestToolsetTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Automation test discovery and execution tools.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: AutomationTestToolset, AutomationTestToolsetTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental Toolset 插件 <code class="usage-code">AutomationTestToolset</code>（<code class="usage-code">AutomationTestToolset</code>、<code class="usage-code">AutomationTestToolsetTests</code>）。</li><li>在编辑器 AI 助手 / Toolset 面板中加载该工具集，用它发现已注册的 <code class="usage-code">FAutomationTestBase</code> 用例并请求执行。</li><li>执行结果应出现在 Automation 日志 / <code class="usage-code">Session Frontend</code>，与手动点测试列表一致。</li><li>用 <code class="usage-code">AutomationTestToolsetTests</code> 自测发现/执行路径；不要把工具集当关卡里的测试 Actor。</li><li>Toolset 只服务编辑器助手与自动化，不要打进 Shipping。</li></ol><p class="usage-note">给编辑器 AI/自动化用的测试发现与执行工具集，Experimental，非游戏功能。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the Experimental Toolset plugin <code class="usage-code">AutomationTestToolset</code> (<code class="usage-code">AutomationTestToolset</code>, <code class="usage-code">AutomationTestToolsetTests</code>).</li><li>Load it in the editor AI assistant / Toolset panel to discover registered <code class="usage-code">FAutomationTestBase</code> cases and request runs.</li><li>Results should show in the Automation log / <code class="usage-code">Session Frontend</code>, matching a manual run from the test list.</li><li>Use <code class="usage-code">AutomationTestToolsetTests</code> to verify discovery/execution; this is not a placeable test actor.</li><li>Toolsets serve the in-editor assistant and automation only — do not ship them.</li></ol><p class="usage-note">Experimental toolset for discovering and running automation tests from the editor assistant, not a game feature.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AutomationTestToolset</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AutomationTestToolsetTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/AutomationTestToolset/AutomationTestToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
