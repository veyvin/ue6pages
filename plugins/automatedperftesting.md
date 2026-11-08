---
layout: default
title: 自动化性能测试 / AutomatedPerfTesting
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AutomatedPerfTesting</div>
      <div class="hero-title-cn">自动化性能测试 · 该插件提供 Gauntlet 测试控制器以方便自动性能测试。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Performance/AutomatedPerfTesting/AutomatedPerfTesting.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该插件提供 Gauntlet 测试控制器以方便自动性能测试。</div><div class="lang-content">This plugin provides Gauntlet Test Controllers to facilitate automatic performance testing.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该插件提供 Gauntlet 测试控制器以方便自动性能测试。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：AutomatedPerfTesting。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This plugin provides Gauntlet Test Controllers to facilitate automatic performance testing.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: AutomatedPerfTesting. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">AutomatedPerfTesting</code>（模块同名，路径 <code class="usage-code">Plugins/Performance/AutomatedPerfTesting</code>）。</li><li>准备性能测试关卡或 Sequencer，在项目配置 / DefaultDeviceProfiles 中指定 Gauntlet 要用的地图与控制器（插件提供的 Gauntlet Test Controller，不是 Enhanced Input）。</li><li>用 <code class="usage-code">RunUAT</code> / Gauntlet 拉起带该控制器的客户端（可加 Insights 跟踪），让控制器自动跑相机扫描、静帧或序列。</li><li>收集 CSV / Unreal Insights 轨迹与 FPS 图表，对比基线；不要在 <code class="usage-code">Session Frontend</code> 里当普通功能测试点一下就当完成。</li><li>C++ 若扩展控制器，只依赖 <code class="usage-code">AutomatedPerfTesting</code>；此插件服务 CI 性能，不要打进玩家包。</li></ol><p class="usage-note">Gauntlet 性能测试控制器，用于无人值守扫图/序列并出 Insights，不是输入映射插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AutomatedPerfTesting</code> (same-named module under <code class="usage-code">Plugins/Performance/AutomatedPerfTesting</code>).</li><li>Author a perf map or Sequencer and point Gauntlet at the map plus this plugin’s Gauntlet Test Controllers in project/device config (not Enhanced Input).</li><li>Launch via <code class="usage-code">RunUAT</code> / Gauntlet with those controllers (optionally with Insights tracing) so the client runs camera sweeps, static views, or sequences unattended.</li><li>Collect CSV / Unreal Insights traces and FPS charts against a baseline; clicking a functional test in <code class="usage-code">Session Frontend</code> is not the same workflow.</li><li>If you subclass a controller, depend on <code class="usage-code">AutomatedPerfTesting</code> only; keep this out of player shipping builds.</li></ol><p class="usage-note">Gauntlet perf-test controllers for unattended map/sequence runs and Insights, not an input-mapping plugin.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AutomatedPerfTesting</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Performance/AutomatedPerfTesting/AutomatedPerfTesting.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
