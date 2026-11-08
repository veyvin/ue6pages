---
layout: default
title: 踏频测试 / Cadence Tests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence Tests</div>
      <div class="hero-title-cn">踏频测试 · Cadence 的自动化规范和客户端/服务器测试装置：Caden</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Physics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/CadenceTests/CadenceTests.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Cadence 的自动化规范和客户端/服务器测试装置：Cadence 下的服务器和客户端世界，逐帧勾选种子帧时间和数据包延迟或丢失。</div><div class="lang-content">Automation specs and a client/server test fixture for Cadence: server and client worlds under Cadence, ticked frame by frame with seeded frame times and packet delay or loss.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Cadence 的自动化规范和客户端/服务器测试装置：Cadence 下的服务器和客户端世界，逐帧勾选种子帧时间和数据包延迟或丢失。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CadenceTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Automation specs and a client/server test fixture for Cadence: server and client worlds under Cadence, ticked frame by frame with seeded frame times and packet delay or loss.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CadenceTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Cadence</code> 与 <code class="usage-code">Cadence Tests</code>（模块 <code class="usage-code">CadenceTests</code>）；这是进程内 client/server 测试夹具，不是游戏功能。</li><li>打开 <code class="usage-code">Window &gt; Developer Tools &gt; Session Frontend &gt; Automation</code>，筛选 <code class="usage-code">Cadence</code> 自动化 specs。</li><li>夹具会在 Cadence 下同时构造 server world 与 client world，按种子化的帧时间逐帧 <code class="usage-code">Tick</code>。</li><li>带数据包延迟或丢包的用例用来验证固定子 tick、输入复制和 resim 在劣网下仍收敛。</li><li>失败时对照夹具的 seeded frame time 与 delay/loss 参数复现，而不是只开 PIE 肉眼看。</li><li>需要自己加 spec 时依赖 <code class="usage-code">CadenceTests</code> 模块并沿用其 client/server fixture；不要把该模块打进 Shipping。</li></ol><p class="usage-note">进程内、可种子化帧时间和丢包的 Cadence 夹具；多进程场景请用 `Cadence Modular Tests`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cadence</code> and <code class="usage-code">Cadence Tests</code> (module <code class="usage-code">CadenceTests</code>). This is an in-process client/server fixture, not gameplay.</li><li>Open <code class="usage-code">Window &gt; Developer Tools &gt; Session Frontend &gt; Automation</code> and filter <code class="usage-code">Cadence</code> specs.</li><li>The fixture builds server and client worlds under Cadence and <code class="usage-code">Tick</code>s them frame-by-frame with seeded frame times.</li><li>Cases that inject packet delay or loss check that fixed sub-ticks, input replication, and resim still converge.</li><li>On failure, replay with the fixture’s seeded frame time and delay/loss knobs rather than a manual PIE session.</li><li>New specs should depend on <code class="usage-code">CadenceTests</code> and reuse its fixture. Do not ship the module.</li></ol><p class="usage-note">In-process Cadence fixture with seeded frame times and packet delay/loss. Use `Cadence Modular Tests` for separate processes.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CadenceTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/CadenceTests/CadenceTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
