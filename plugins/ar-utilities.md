---
layout: default
title: 增强现实实用工具 / AR Utilities
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AR Utilities</div>
      <div class="hero-title-cn">增强现实实用工具 · AR 系统的实用程序代码和内容</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Augmented Reality</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AR/ARUtilities/ARUtilities.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">AR 系统的实用程序代码和内容</div><div class="lang-content">Utility code and content for AR systems</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：AR 系统的实用程序代码和内容</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ARUtilities。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Utility code and content for AR systems</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ARUtilities. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在已有 AR 会话（<code class="usage-code">Apple ARKit</code>、ARCore 等）的项目中启用 <code class="usage-code">AR Utilities</code>（模块 <code class="usage-code">ARUtilities</code>）。它提供透视材质与辅助内容，不替代 <code class="usage-code">ARSessionConfig</code>。</li><li>给要显示相机透视的网格加上 <code class="usage-code">UPassthroughMaterialUpdateComponent</code>，指定材质槽与纹理参数名；组件每帧把 AR 相机画面写入该参数。</li><li>使用插件 Content 里的透视/平面调试材质（路径以 <code class="usage-code">/ARUtilities/</code> 为前缀），把平面可视化 Actor 钉到 <code class="usage-code">UARTrackedGeometry</code>，而不是手写一张未更新的相机贴图。</li><li>身体/人脸 Live Link 重定向用 <code class="usage-code">UARLiveLinkRetargetAsset</code> 接到角色 <code class="usage-code">AnimBP</code>，与具体厂商的 Face/Pose 插件配合。</li><li>游戏 <code class="usage-code">Build.cs</code> 加 <code class="usage-code">ARUtilities</code>。先 <code class="usage-code">Start AR Session</code> 再验证透视是否刷新；Win 编辑器无相机帧时组件只会停在占位纹理。</li></ol><p class="usage-note">AR 透视与 Live Link 重定向工具层，不是 ARKit 会话本身。世界追踪仍在 `Apple ARKit`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AR Utilities</code> (module <code class="usage-code">ARUtilities</code>) in a project that already has an AR session (<code class="usage-code">Apple ARKit</code>, ARCore, …). It supplies passthrough materials and helpers; it does not replace <code class="usage-code">ARSessionConfig</code>.</li><li>Add <code class="usage-code">UPassthroughMaterialUpdateComponent</code> to the mesh that should show camera passthrough, set the material slot and texture parameter name, and let it write the AR camera image each frame.</li><li>Use the plugin Content passthrough/plane-debug materials (paths under <code class="usage-code">/ARUtilities/</code>) and pin visualizers to <code class="usage-code">UARTrackedGeometry</code> instead of a stale camera texture.</li><li>For body/face Live Link retargeting, assign <code class="usage-code">UARLiveLinkRetargetAsset</code> on the character <code class="usage-code">AnimBP</code> alongside the vendor Face/Pose plugin.</li><li>Depend on <code class="usage-code">ARUtilities</code> in game <code class="usage-code">Build.cs</code>. <code class="usage-code">Start AR Session</code> before judging passthrough. On a Win editor with no camera frames the component stays on a placeholder.</li></ol><p class="usage-note">Passthrough and Live Link retarget helpers, not the ARKit session. World tracking stays in `Apple ARKit`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ARUtilities</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AR/ARUtilities/ARUtilities.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
