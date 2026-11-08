---
layout: default
title: 自动化性能测试工具 / AutomatedPerfTestTools
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AutomatedPerfTestTools</div>
      <div class="hero-title-cn">自动化性能测试工具 · 自动化性能测试框架工具</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Performance/AutomatedPerfTestTools/AutomatedPerfTestTools.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">自动化性能测试框架工具</div><div class="lang-content">Tools for Automated Perf Testing framework</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：自动化性能测试框架工具</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：AutomatedPerfTestLaunchExtension。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Tools for Automated Perf Testing framework</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: AutomatedPerfTestLaunchExtension. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>先启用 <code class="usage-code">AutomatedPerfTesting</code>，再启用配套的 <code class="usage-code">AutomatedPerfTestTools</code>（模块 <code class="usage-code">AutomatedPerfTestLaunchExtension</code>）。</li><li>打开 <code class="usage-code">Project Launcher</code> 或编辑器启动扩展，使用该模块注册的 Perf Test 启动项/参数，而不是手动拼一套 PIE 命令行。</li><li>从扩展里选目标地图、设备档和 Gauntlet 控制器，一键拉起与 CI 相同的性能测试。</li><li>跑完对照 <code class="usage-code">AutomatedPerfTesting</code> 产出的 Insights/CSV；本插件只提供启动/工具层。</li><li><code class="usage-code">AutomatedPerfTestLaunchExtension</code> 是编辑器启动扩展，不要写进 Game Target。</li></ol><p class="usage-note">为 AutomatedPerfTesting 提供编辑器启动扩展，本身不含 Gauntlet 控制器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AutomatedPerfTesting</code> first, then <code class="usage-code">AutomatedPerfTestTools</code> (module <code class="usage-code">AutomatedPerfTestLaunchExtension</code>).</li><li>Open <code class="usage-code">Project Launcher</code> or the editor launch extension this module registers, instead of hand-writing PIE command lines.</li><li>Pick the map, device profile, and Gauntlet controller from that extension so local runs match CI.</li><li>Judge results from the Insights/CSV produced by <code class="usage-code">AutomatedPerfTesting</code>; this plugin is the launch/tooling layer only.</li><li><code class="usage-code">AutomatedPerfTestLaunchExtension</code> is an editor launch extension — do not add it to a Game target.</li></ol><p class="usage-note">Editor launch tooling for AutomatedPerfTesting; it does not contain the Gauntlet controllers themselves.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AutomatedPerfTestLaunchExtension</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Performance/AutomatedPerfTestTools/AutomatedPerfTestTools.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
