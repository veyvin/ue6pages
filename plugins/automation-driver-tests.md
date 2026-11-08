---
layout: default
title: 自动化驱动程序测试 / Automation Driver Tests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Automation Driver Tests</div>
      <div class="hero-title-cn">自动化驱动程序测试 · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/AutomationDriverTests/AutomationDriverTests.uplugin</div></div></div>
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
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：AutomationDriverTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: AutomationDriverTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在编辑器测试环境启用 <code class="usage-code">Automation Driver Tests</code>（模块 <code class="usage-code">AutomationDriverTests</code>，<code class="usage-code">Plugins/Tests/AutomationDriverTests</code>）。</li><li>确保引擎模块 <code class="usage-code">AutomationDriver</code> 可用：它用 Slate 注入指针/按键，本插件是它的自动化用例包。</li><li>打开 <code class="usage-code">Tools &gt; Session Frontend &gt; Automation</code>，筛选 <code class="usage-code">AutomationDriver</code> 相关测试并全部运行。</li><li>失败时看用例是否在模拟点击/输入后断言控件状态，不要到关卡里找可放置 Actor。</li><li>不要把 <code class="usage-code">AutomationDriverTests</code> 加入游戏 <code class="usage-code">Build.cs</code> 或 Shipping。</li></ol><p class="usage-note">AutomationDriver 的 Slate UI 自动化测试集，不是游戏功能。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Automation Driver Tests</code> in an editor test environment (module <code class="usage-code">AutomationDriverTests</code>, <code class="usage-code">Plugins/Tests/AutomationDriverTests</code>).</li><li>Ensure the engine <code class="usage-code">AutomationDriver</code> module is available: it injects Slate pointer/key input; this plugin is its test suite.</li><li>Open <code class="usage-code">Tools &gt; Session Frontend &gt; Automation</code>, filter <code class="usage-code">AutomationDriver</code> tests, and run the set.</li><li>On failure, inspect whether simulated clicks/keys left the widget in the expected state; there is no placeable actor.</li><li>Do not add <code class="usage-code">AutomationDriverTests</code> to a game <code class="usage-code">Build.cs</code> or Shipping.</li></ol><p class="usage-note">Test suite for AutomationDriver Slate UI automation, not a game feature.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AutomationDriverTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/AutomationDriverTests/AutomationDriverTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
