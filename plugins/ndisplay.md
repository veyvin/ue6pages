---
layout: default
title: 显示器 / nDisplay
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">N</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">nDisplay</div>
      <div class="hero-title-cn">显示器 · 支持使用多台 PC 以单声道或立体声进行同步集群渲染</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Misc</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">26</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/nDisplay/nDisplay.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持使用多台 PC 以单声道或立体声进行同步集群渲染</div><div class="lang-content">Support for synchronized clustered rendering using multiple PCs in mono or stereo</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>nDisplay 把一台场景渲染到多台同步的机器/窗口上，用于 LED 墙、洞穴、集群视口。和 Switchboard、Live Link、摄像机跟踪一起做虚拟制片。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：DisplayCluster, DisplayClusterFillDerivedDataCache, DisplayClusterEditor, DisplayClusterProjection, DisplayClusterWarp, DisplayClusterShaders, DisplayClusterMessageInterception, DisplayClusterConfiguration 等。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine</a></p></div><div class="lang-content"><p>nDisplay renders one scene across synchronized machines or windows for LED walls, CAVE, and cluster viewports. It is used in virtual production with Switchboard, Live Link, and camera tracking.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: DisplayCluster, DisplayClusterFillDerivedDataCache, DisplayClusterEditor, DisplayClusterProjection, DisplayClusterWarp, DisplayClusterShaders, DisplayClusterMessageInterception, DisplayClusterConfiguration 等. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">nDisplay</code>（模块 <code class="usage-code">DisplayCluster</code>、<code class="usage-code">DisplayClusterProjection</code>、<code class="usage-code">DisplayClusterWarp</code>、<code class="usage-code">DisplayClusterShaders</code>、<code class="usage-code">DisplayClusterConfiguration</code> 等，编辑器 <code class="usage-code">DisplayClusterEditor</code>）。</li><li>它支持用多台 PC 以单声道或立体声进行同步集群渲染（LED 墙、CAVE、集群视口）。</li><li>配置 nDisplay 集群与投影/变形，配合 Switchboard 启动与摄像机跟踪做虚拟制片。</li><li>Game 模块依赖运行时模块；<code class="usage-code">DisplayClusterEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">多机同步集群渲染（nDisplay），LED 墙/CAVE 核心。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">nDisplay</code> (modules <code class="usage-code">DisplayCluster</code>, <code class="usage-code">DisplayClusterProjection</code>, <code class="usage-code">DisplayClusterWarp</code>, <code class="usage-code">DisplayClusterShaders</code>, <code class="usage-code">DisplayClusterConfiguration</code>, etc., editor <code class="usage-code">DisplayClusterEditor</code>).</li><li>It supports synchronized clustered rendering across multiple PCs in mono or stereo (LED walls, CAVE, cluster viewports).</li><li>Configure the nDisplay cluster and projection/warp, launch with Switchboard, and use camera tracking for virtual production.</li><li>Game modules depend on runtime modules; <code class="usage-code">DisplayClusterEditor</code> is Editor-target only.</li></ol><p class="usage-note">Synchronized clustered multi-PC rendering (nDisplay), the core for LED walls/CAVE.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (26)</div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayCluster</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterFillDerivedDataCache</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterProjection</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterWarp</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterShaders</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMessageInterception</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterConfiguration</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterOperator</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterConfigurator</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterLightCardEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterLightCardEditorShaders</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterScenePreview</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterColorGrading</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterDetails</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterStageMonitoring</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterRemoteControlInterceptor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMediaEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMonitor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMonitorEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMultiUser</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterTests</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMoviePipeline</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterMoviePipelineEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DisplayClusterReplication</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/nDisplay/nDisplay.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
