---
layout: default
title: 流程生产跟踪 / Flow Production Tracking
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Flow Production Tracking</div>
      <div class="hero-title-cn">流程生产跟踪 · 虚幻编辑器的流程生产跟踪（以前称为 Shotgun 和/或 Sh</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.10</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Shotgrid/Shotgrid.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">虚幻编辑器的流程生产跟踪（以前称为 Shotgun 和/或 ShotGrid）集成。</div><div class="lang-content">Flow Production Tracking (formerly known as Shotgun and/or ShotGrid) integration for the Unreal Editor.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：虚幻编辑器的流程生产跟踪（以前称为 Shotgun 和/或 ShotGrid）集成。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：Shotgrid。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Flow Production Tracking (formerly known as Shotgun and/or ShotGrid) integration for the Unreal Editor.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: Shotgrid. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">Flow Production Tracking</code>（模块 <code class="usage-code">Shotgrid</code>，描述符仍是 <code class="usage-code">Shotgrid.uplugin</code>）。这是 Autodesk Flow（原 Shotgun/ShotGrid）的编辑器集成，不是运行时在线子系统。</li><li>安装/配置 Flow Python Toolkit（<code class="usage-code">tk-unreal</code>）与站点 URL、脚本密钥或 SSO。编辑器启动后用插件登录 Flow 项目，而不是在关卡里放组件。</li><li>从 Flow 面板 Load 当前 Shot 对应的 Unreal 工程/关卡；完成镜头后 Publish 网格、关卡或 Sequencer 资产，任务状态应回到 Flow 网页。</li><li>核对 Publish 版本号、路径模板与 Toolkit schema 一致；失败先看 Output Log 里 Shotgun/Flow API 错误和 Python 引擎是否加载 <code class="usage-code">tk-unreal</code>。</li><li>只给制片管线用：<code class="usage-code">Shotgrid</code> 不要进游戏 Target。凭证放在本机 Toolkit 配置，不要写进要提交的 <code class="usage-code">DefaultEngine.ini</code>。</li></ol><p class="usage-note">ShotGrid/Flow 制片登录与 Publish，不是过场动画工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Flow Production Tracking</code> (module <code class="usage-code">Shotgrid</code>, descriptor still <code class="usage-code">Shotgrid.uplugin</code>). It is Autodesk Flow (formerly Shotgun/ShotGrid) for the editor, not a runtime online subsystem.</li><li>Install/configure the Flow Python Toolkit (<code class="usage-code">tk-unreal</code>) with site URL and script key or SSO. Log into the Flow project from the editor plugin — do not place a level component.</li><li>Load the Unreal map for the current shot from the Flow panel; after the shot, Publish meshes, levels, or Sequencer assets and confirm the version appears on the Flow web task.</li><li>Publish paths must match the Toolkit schema. On failure, read Shotgun/Flow API errors in the Output Log and confirm <code class="usage-code">tk-unreal</code> loaded in the Python engine.</li><li>Pipeline-only: keep <code class="usage-code">Shotgrid</code> off game targets. Store credentials in local Toolkit config, not in a committed <code class="usage-code">DefaultEngine.ini</code>.</li></ol><p class="usage-note">ShotGrid/Flow login and publish, not a cinematic authoring tool.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">Shotgrid</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Shotgrid/Shotgrid.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
