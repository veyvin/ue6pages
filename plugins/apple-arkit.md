---
layout: default
title: 苹果 ARKit / Apple ARKit
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Apple ARKit</div>
      <div class="hero-title-cn">苹果 ARKit · 支持苹果ARKit增强现实系统</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Augmented Reality</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AR/AppleAR/AppleARKit/AppleARKit.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持苹果ARKit增强现实系统</div><div class="lang-content">Support for Apple's ARKit augmented reality system</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持苹果ARKit增强现实系统</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AppleARKit, AppleARKitPoseTrackingLiveLink。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Support for Apple's ARKit augmented reality system</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AppleARKit, AppleARKitPoseTrackingLiveLink. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>仅为 iOS/iPadOS 工程启用 <code class="usage-code">Apple ARKit</code>（运行时 <code class="usage-code">AppleARKit</code>，身体 Pose 转发 <code class="usage-code">AppleARKitPoseTrackingLiveLink</code>）。它是 XR/AR 会话后端，不是可拖进关卡的网格组件。</li><li>创建 <code class="usage-code">ARSessionConfig</code>：打开平面检测、图像追踪、环境光估计或身体追踪等所需特性；默认 Pawn 使用 AR 游戏模式并在 BeginPlay <code class="usage-code">Start AR Session</code>。</li><li>相机背景由 ARKit 合成；用 <code class="usage-code">ARTrace</code> / 命中测试把 Actor 钉到平面或图像锚点。图像库用 <code class="usage-code">ARCandidateImage</code> 数据资产，不要当普通 <code class="usage-code">Texture</code> 去「追踪」。</li><li>身体骨骼走 <code class="usage-code">AppleARKitPoseTrackingLiveLink</code>：在 Live Link 客户端接 ARKit Pose 主题，再驱动角色 <code class="usage-code">AnimBP</code>。脸部几何另开 <code class="usage-code">Apple ARKit Face Support</code>。</li><li>在 <code class="usage-code">DefaultEngine.ini</code> 的 <code class="usage-code">[/Script/AppleARKit.AppleARKitSettings]</code> 调日志与会话选项；<code class="usage-code">Info.plist</code> 声明相机。游戏 <code class="usage-code">Build.cs</code> 加 <code class="usage-code">AppleARKit</code>，需要 Pose 再加 <code class="usage-code">AppleARKitPoseTrackingLiveLink</code>。</li><li>用 Launch on Device 验证；Win64 PIE 没有 ARKit 世界。</li></ol><p class="usage-note">Apple 世界追踪/锚点/身体 Pose 后端。人脸请用 Face Support；启动片请用 `Apple Movie Player`，不要混。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Apple ARKit</code> only for iOS/iPadOS (<code class="usage-code">AppleARKit</code> runtime, body pose via <code class="usage-code">AppleARKitPoseTrackingLiveLink</code>). It is the XR/AR session backend, not a mesh component you drop in a level.</li><li>Author an <code class="usage-code">ARSessionConfig</code> (plane detection, image tracking, light estimation, body tracking as needed). Use an AR game mode / pawn and <code class="usage-code">Start AR Session</code> on BeginPlay.</li><li>ARKit composites the camera feed. Pin actors with <code class="usage-code">ARTrace</code> / hit tests against planes or image anchors. Image libraries are <code class="usage-code">ARCandidateImage</code> assets, not plain <code class="usage-code">Texture</code> objects.</li><li>Body skeletons go through <code class="usage-code">AppleARKitPoseTrackingLiveLink</code> into a Live Link subject and then the character <code class="usage-code">AnimBP</code>. Face mesh/blendshapes are the separate <code class="usage-code">Apple ARKit Face Support</code> plugin.</li><li>Tune <code class="usage-code">[/Script/AppleARKit.AppleARKitSettings]</code> in <code class="usage-code">DefaultEngine.ini</code> and declare the camera in <code class="usage-code">Info.plist</code>. Game <code class="usage-code">Build.cs</code> adds <code class="usage-code">AppleARKit</code>, plus <code class="usage-code">AppleARKitPoseTrackingLiveLink</code> if you consume pose.</li><li>Prove with Launch on Device; Win64 PIE has no ARKit world.</li></ol><p class="usage-note">Apple world-tracking / anchors / body-pose backend. Faces are Face Support; startup movies are `Apple Movie Player`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AppleARKit</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AppleARKitPoseTrackingLiveLink</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AR/AppleAR/AppleARKit/AppleARKit.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
