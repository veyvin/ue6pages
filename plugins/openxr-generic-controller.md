---
layout: default
title: OpenXR 通用控制器 / OpenXR Generic Controller
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">O</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">OpenXR Generic Controller</div>
      <div class="hero-title-cn">OpenXR 通用控制器 · Khronos 对 OpenXR 的通用控制器支持：启用 XR_</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Reality</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/OpenXRGenericController/OpenXRGenericController.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Khronos 对 OpenXR 的通用控制器支持：启用 XR_KHR_generic_controller 扩展并注册 /interaction_profiles/khr/generic_controller 交互配置文件。</div><div class="lang-content">Khronos generic controller support for OpenXR: enables the XR_KHR_generic_controller extension and registers the /interaction_profiles/khr/generic_controller interaction profile.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>OpenXR 插件让引擎走 Khronos OpenXR 运行时，对接 SteamVR、Oculus、Windows Mixed Reality 等头显，而不为每个厂商单独写插件。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：OpenXRGenericController。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine</a></p></div><div class="lang-content"><p>The OpenXR plugin talks to a Khronos OpenXR runtime so Unreal can target SteamVR, Meta, WMR, and others without a vendor-specific plugin per HMD.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: OpenXRGenericController. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">OpenXR Generic Controller</code>（模块 <code class="usage-code">OpenXRGenericController</code>）。</li><li>它启用 <code class="usage-code">XR_KHR_generic_controller</code> 扩展并注册 <code class="usage-code">/interaction_profiles/khr/generic_controller</code>。</li><li>在 OpenXR 项目里支持通用控制器输入与手势。</li><li>属 OpenXR 输入扩展；需 OpenXR 运行时。</li></ol><p class="usage-note">OpenXR 的 Khronos 通用控制器支持（XR_KHR_generic_controller）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">OpenXR Generic Controller</code> (module <code class="usage-code">OpenXRGenericController</code>).</li><li>It enables the <code class="usage-code">XR_KHR_generic_controller</code> extension and registers the <code class="usage-code">/interaction_profiles/khr/generic_controller</code> profile.</li><li>Supports generic controller input/gestures in OpenXR projects.</li><li>It is an OpenXR input extension; requires an OpenXR runtime.</li></ol><p class="usage-note">OpenXR Khronos generic controller support (XR_KHR_generic_controller).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">OpenXRGenericController</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/OpenXRGenericController/OpenXRGenericController.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
