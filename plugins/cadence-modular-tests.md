---
layout: default
title: Cadence 模块化测试 / Cadence Modular Tests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence Modular Tests</div>
      <div class="hero-title-cn">Cadence 模块化测试 · 针对 Cadence 的模块化测试框架测试：服务器和客户端在单独</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/CadenceModularTests/CadenceModularTests.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">针对 Cadence 的模块化测试框架测试：服务器和客户端在单独的进程中，通过 Cadence 的校正和重新模拟报告进行检查。</div><div class="lang-content">Modular Test Framework tests for Cadence: a server and clients in separate processes, checked through Cadence's correction and resim reports.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：针对 Cadence 的模块化测试框架测试：服务器和客户端在单独的进程中，通过 Cadence 的校正和重新模拟报告进行检查。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CadenceModularTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Modular Test Framework tests for Cadence: a server and clients in separate processes, checked through Cadence's correction and resim reports.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CadenceModularTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在源码版引擎启用 <code class="usage-code">Cadence</code>、<code class="usage-code">Cadence Input System</code> 与 <code class="usage-code">Cadence Modular Tests</code>（模块 <code class="usage-code">CadenceModularTests</code>）。</li><li>打开 <code class="usage-code">Window &gt; Developer Tools &gt; Session Frontend</code>，切到 <code class="usage-code">Automation</code> 页。</li><li>过滤器输入 <code class="usage-code">Cadence</code> / Modular，勾选 Cadence 的 Modular Test Framework 用例（独立进程里拉起 server + clients）。</li><li>运行后不要只看 Pass/Fail：打开 Cadence 的 correction 与 resim report，确认客户端预测偏差被重模拟纠正。</li><li>也可从命令行跑对应 Modular Test / Gauntlet 目标，便于 CI；失败时保留多进程日志而不是只看编辑器 Output Log。</li><li>这是引擎测试插件，不要写进游戏 <code class="usage-code">Build.cs</code> 或 Shipping。</li></ol><p class="usage-note">与同目录下的 `Cadence Tests` 不同：这里是多进程 Modular Test Framework，靠 correction/resim 报告验收。</p></div><div class="lang-content"><ol class="usage-steps"><li>On a source engine, enable <code class="usage-code">Cadence</code>, <code class="usage-code">Cadence Input System</code>, and <code class="usage-code">Cadence Modular Tests</code> (module <code class="usage-code">CadenceModularTests</code>).</li><li>Open <code class="usage-code">Window &gt; Developer Tools &gt; Session Frontend</code> → <code class="usage-code">Automation</code>.</li><li>Filter <code class="usage-code">Cadence</code> / Modular and run the Modular Test Framework cases (server + clients in separate processes).</li><li>Inspect Cadence correction and resim reports, not only Pass/Fail, to confirm prediction error is fixed by resimulation.</li><li>From CI, launch the matching Modular Test / Gauntlet target and keep per-process logs.</li><li>Engine test plugin only — do not add <code class="usage-code">CadenceModularTests</code> to a game <code class="usage-code">Build.cs</code> or Shipping build.</li></ol><p class="usage-note">Unlike in-process `Cadence Tests`, this is multi-process Modular Test Framework gated on correction/resim reports.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CadenceModularTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/CadenceModularTests/CadenceModularTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
