---
layout: default
title: 播放检查 / PlayCheck
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">PlayCheck</div>
      <div class="hero-title-cn">播放检查 · 让代理在实时游戏中检查自己的工作：从 PIE 或游戏中捕获图像、</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Developer</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">4</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Developer/PlayCheck/PlayCheck.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">让代理在实时游戏中检查自己的工作：从 PIE 或游戏中捕获图像、视频和每帧数据（PNG 帧连拍、联系表、mp4 和每帧清单），使用分阶段捕获摄像机和 pawn 驱动项目自己的增强输入操作。三种计时策略：slomo 扩张、固定时间步长（时间精确）和即时 NVENC（唯一一种捕获 GPU 时间效果的策略）。作为 PlayCheckToolset 工具向代理公开，并作为 capture.* 和camera.* 控制台命令向人们公开。</div><div class="lang-content">Lets agents check their own work in the live game: captures images, video and per-frame data (PNG frame bursts, contact sheets, mp4 and a per-frame manifest) from PIE or -game, with a staged capture camera and pawn driving through the project's own Enhanced Input actions. Three timing strategies: slomo dilation, fixed-timestep (temporally exact) and realtime NVENC off the present hook (the only one that captures GPU-temporal effects). Exposed to agents as PlayCheckToolset tools, and to people as capture.* and camera.* console commands.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：让代理在实时游戏中检查自己的工作：从 PIE 或游戏中捕获图像、视频和每帧数据（PNG 帧连拍、联系表、mp4 和每帧清单），使用分阶段捕获摄像机和 pawn 驱动项目自己的增强输入操作。三种计时策略：slomo 扩张、固定时间步长（时间精确）和即时 NVENC（唯一一种捕获 GPU 时间效果的策略）。作为 PlayCheckToolset 工具向代理公开，并作为 capture.* 和camera.* 控制台命令向人们公开。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>编辑器或开发者插件，服务制作流程，默认不进 Shipping。</p><p>它打包的模块包括：PlayCheck, PlayCheckToolset, PlayCheckScene, PlayCheckSceneToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Lets agents check their own work in the live game: captures images, video and per-frame data (PNG frame bursts, contact sheets, mp4 and a per-frame manifest) from PIE or -game, with a staged capture camera and pawn driving through the project's own Enhanced Input actions. Three timing strategies: slomo dilation, fixed-timestep (temporally exact) and realtime NVENC off the present hook (the only one that captures GPU-temporal effects). Exposed to agents as PlayCheckToolset tools, and to people as capture.* and camera.* console commands.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>An editor/developer plugin for the authoring pipeline; it does not ship by default.</p><p>It ships these modules: PlayCheck, PlayCheckToolset, PlayCheckScene, PlayCheckSceneToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">PlayCheck</code>（模块 <code class="usage-code">PlayCheck</code>、<code class="usage-code">PlayCheckToolset</code>、<code class="usage-code">PlayCheckScene</code>、<code class="usage-code">PlayCheckSceneToolset</code>）。</li><li>它让代理在实时游戏中检查自己的工作：从 PIE/<code class="usage-code">-game</code> 捕获图像、视频和每帧数据（PNG 连拍、联系表、mp4 与每帧清单）。</li><li>用分阶段捕捉相机和 pawn，驱动项目自己的 Enhanced Input；三种计时：slomo、固定时间步、即时 NVENC。</li><li>对代理暴露为 PlayCheckToolset；对人暴露为 <code class="usage-code">capture.*</code> / <code class="usage-code">camera.*</code> 控制台命令。</li></ol><p class="usage-note">在 PIE/游戏中给代理捕捉画面与每帧数据以自检。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">PlayCheck</code> (modules <code class="usage-code">PlayCheck</code>, <code class="usage-code">PlayCheckToolset</code>, <code class="usage-code">PlayCheckScene</code>, <code class="usage-code">PlayCheckSceneToolset</code>).</li><li>It lets agents check their own work in the live game: captures images, video, and per-frame data (PNG bursts, contact sheets, mp4, per-frame manifest) from PIE/<code class="usage-code">-game</code>.</li><li>Uses a staged capture camera and pawn driving the project&#x27;s own Enhanced Input; three timing strategies: slomo, fixed timestep, and instant NVENC.</li><li>Exposed to agents as PlayCheckToolset and to humans as <code class="usage-code">capture.*</code> / <code class="usage-code">camera.*</code> console commands.</li></ol><p class="usage-note">Lets agents capture frames/per-frame data in PIE/game to check their own work.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (4)</div><div class="module-item"><span class="dot"></span><span class="name mono">PlayCheck</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PlayCheckToolset</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PlayCheckScene</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PlayCheckSceneToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Developer/PlayCheck/PlayCheck.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
