---
layout: default
title: Cadence SceneGraph 测试 / Cadence SceneGraph Tests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence SceneGraph Tests</div>
      <div class="hero-title-cn">Cadence SceneGraph 测试 · Cadence 下场景图的自动化规范和 Verse 探针：<pr</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Physics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/CadenceSceneGraphTests/CadenceSceneGraphTests.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Cadence 下场景图的自动化规范和 Verse 探针：<predicts> TickEvents 处理程序在客户端上运行，并在 Cadence 客户端/服务器装置上通过重新模拟进行重放。</div><div class="lang-content">Automation specs and Verse probes for Scene Graph under Cadence: <predicts> TickEvents handlers run on clients and replayed by resimulation, on the Cadence client/server fixture.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Cadence 下场景图的自动化规范和 Verse 探针： TickEvents 处理程序在客户端上运行，并在 Cadence 客户端/服务器装置上通过重新模拟进行重放。</p><p>Verse 语言/运行时的一块：编译、VM、设备或编辑器支持，服务 UEFN 体验。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CadenceSceneGraphTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Automation specs and Verse probes for Scene Graph under Cadence:  TickEvents handlers run on clients and replayed by resimulation, on the Cadence client/server fixture.</p><p>A slice of the Verse language/runtime: compiler, VM, devices, or editor support for UEFN.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CadenceSceneGraphTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Cadence</code>、<code class="usage-code">Cadence SceneGraph</code>、Scene Graph / Verse 支持以及 <code class="usage-code">Cadence SceneGraph Tests</code>（模块 <code class="usage-code">CadenceSceneGraphTests</code>）。</li><li>在 <code class="usage-code">Session Frontend &gt; Automation</code> 中筛选 <code class="usage-code">CadenceSceneGraph</code> 规范（specs）。</li><li>这些用例走 Cadence 的 client/server fixture：带 <code class="usage-code">&lt;predicts&gt;</code> 的 <code class="usage-code">TickEvents</code> 处理程序在客户端跑，再被 resimulation 重放。</li><li>Verse 探针会断言 Scene Graph 实体在预测帧与重放帧上的变换/输入一致；失败时对照 fixture 的帧时间与数据包设定。</li><li>改 Scene Graph 或 Verse 输入后重新编译 Verse，再跑同一组 specs，不要靠手工 PIE 代替。</li><li>测试模块不进游戏包；不要把 <code class="usage-code">CadenceSceneGraphTests</code> 加入运行时 <code class="usage-code">Build.cs</code>。</li></ol><p class="usage-note">专门覆盖 Cadence 下 Scene Graph 的 `&lt;predicts&gt;` TickEvents 与 Verse 探针，不是通用物理自动化。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cadence</code>, <code class="usage-code">Cadence SceneGraph</code>, Scene Graph / Verse support, and <code class="usage-code">Cadence SceneGraph Tests</code> (module <code class="usage-code">CadenceSceneGraphTests</code>).</li><li>In <code class="usage-code">Session Frontend &gt; Automation</code>, filter the <code class="usage-code">CadenceSceneGraph</code> specs.</li><li>Cases use the Cadence client/server fixture: <code class="usage-code">&lt;predicts&gt;</code> <code class="usage-code">TickEvents</code> handlers run on clients and are replayed by resimulation.</li><li>Verse probes assert Scene Graph transforms/input match between predicted and replayed frames; on failure compare fixture frame time and packet settings.</li><li>After Scene Graph or Verse input changes, compile Verse and rerun the same specs — do not substitute a manual PIE session.</li><li>Test-only; do not add <code class="usage-code">CadenceSceneGraphTests</code> to a runtime <code class="usage-code">Build.cs</code>.</li></ol><p class="usage-note">Covers Scene Graph `&lt;predicts&gt;` TickEvents and Verse probes under Cadence, not generic physics automation.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CadenceSceneGraphTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/CadenceSceneGraphTests/CadenceSceneGraphTests.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
