---
layout: default
title: 功能测试编辑器 / Functional Testing Editor
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Functional Testing Editor</div>
      <div class="hero-title-cn">功能测试编辑器 · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/FunctionalTestingEditor/FunctionalTestingEditor.uplugin</div></div></div>
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
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：FunctionalTestingEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: FunctionalTestingEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Functional Testing Editor</code>（模块 <code class="usage-code">FunctionalTestingEditor</code>）。它给 <code class="usage-code">AFunctionalTest</code> / Screenshot 等功能测试补编辑器放置、细节定制与会话集成，运行时测试框架仍是 <code class="usage-code">FunctionalTesting</code>。</li><li>在测试关卡放置 <code class="usage-code">Functional Test</code> Actor（或派生），填 <code class="usage-code">Test Label</code>、准备/完成延迟、成功条件（例如 Actor 到达、查询通过）。</li><li>用编辑器扩展设截图对比基准、选中测试 Actor 的细节定制；不要把测试逻辑写在普通关卡蓝图 Event BeginPlay 里却从不 <code class="usage-code">Finish Test</code>。</li><li>打开 Session Frontend → Automation，过滤 <code class="usage-code">Functional</code> 或你的测试名，PIE/编辑器会话跑用例。失败看 Message Log 与截图 diff，而不是游戏 HUD。</li><li><code class="usage-code">FunctionalTestingEditor</code> 只进 Editor Target；CI 用 <code class="usage-code">-ExecCmds=&quot;Automation RunTests ...&quot;</code>。Shipping 客户端不要依赖本插件。</li></ol><p class="usage-note">功能测试的编辑器壳，真正的 `AFunctionalTest` API 在 `FunctionalTesting`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Functional Testing Editor</code> (module <code class="usage-code">FunctionalTestingEditor</code>). It adds placement, Details customization, and session integration for <code class="usage-code">AFunctionalTest</code> / screenshot tests; the runtime harness remains <code class="usage-code">FunctionalTesting</code>.</li><li>Place a <code class="usage-code">Functional Test</code> actor (or subclass) in a test map. Set <code class="usage-code">Test Label</code>, prepare/finish delays, and success conditions (actor reached, query passed).</li><li>Use the editor extras for screenshot baselines and test-actor Details. Do not put test logic only in level BeginPlay without ever calling <code class="usage-code">Finish Test</code>.</li><li>In Session Frontend → Automation, filter <code class="usage-code">Functional</code> or your test name and run in PIE/editor. Failures show in Message Log and screenshot diffs, not the game HUD.</li><li><code class="usage-code">FunctionalTestingEditor</code> is Editor-target only. CI uses <code class="usage-code">-ExecCmds=&quot;Automation RunTests ...&quot;</code>. Do not depend on this plugin in a shipping client.</li></ol><p class="usage-note">Editor shell for functional tests; `AFunctionalTest` APIs live in `FunctionalTesting`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">FunctionalTestingEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/FunctionalTestingEditor/FunctionalTestingEditor.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
