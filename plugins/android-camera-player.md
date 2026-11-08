---
layout: default
title: 安卓相机播放器 / Android Camera Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Android Camera Player</div>
      <div class="hero-title-cn">安卓相机播放器 · 使用 Android Camera 库实现相机预览。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">2.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">4</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AndroidCamera/AndroidCamera.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 Android Camera 库实现相机预览。</div><div class="lang-content">Implements camera preview using the Android Camera library.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 Android Camera 库实现相机预览。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AndroidCamera, AndroidCameraEditor, AndroidCameraFactory, AndroidCameraFactory。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements camera preview using the Android Camera library.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AndroidCamera, AndroidCameraEditor, AndroidCameraFactory, AndroidCameraFactory. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Android Camera Player</code>（<code class="usage-code">AndroidCamera</code>、<code class="usage-code">AndroidCameraFactory</code>，编辑器 <code class="usage-code">AndroidCameraEditor</code>）。</li><li>内容浏览器创建 Camera 用的 Media Source（由 <code class="usage-code">AndroidCameraFactory</code> 注册），以及 <code class="usage-code">Media Player</code>、<code class="usage-code">Media Texture</code>。</li><li>蓝图 Open Source 后把 <code class="usage-code">Media Texture</code> 画到 UMG Image 或网格材质上，作为设备摄像头预览。</li><li>在 <code class="usage-code">Project Settings &gt; Platforms &gt; Android</code> 打开 Camera 权限；包装到真机测试预览（编辑器会用工厂资产，但不出真实摄像头画面）。</li><li><code class="usage-code">AndroidCameraEditor</code> 只进 Editor Target；这不是 AJA/SDI，也不是文件 <code class="usage-code">Android Media Player</code>。</li></ol><p class="usage-note">用 Android Camera 库做 Media Framework 摄像头预览，只在设备上有效。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Android Camera Player</code> (<code class="usage-code">AndroidCamera</code>, <code class="usage-code">AndroidCameraFactory</code>, editor <code class="usage-code">AndroidCameraEditor</code>).</li><li>Create a camera Media Source (registered by <code class="usage-code">AndroidCameraFactory</code>) plus a <code class="usage-code">Media Player</code> and <code class="usage-code">Media Texture</code>.</li><li>Open the source from Blueprint and draw the <code class="usage-code">Media Texture</code> on a UMG Image or mesh material for device camera preview.</li><li>Enable Camera permission under <code class="usage-code">Project Settings &gt; Platforms &gt; Android</code> and package to a device (the editor authors assets but will not show a real camera).</li><li>Keep <code class="usage-code">AndroidCameraEditor</code> on an Editor target; this is not AJA/SDI and not the file-oriented <code class="usage-code">Android Media Player</code>.</li></ol><p class="usage-note">Media Framework camera preview via the Android Camera library; device-only.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (4)</div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidCamera</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidCameraEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidCameraFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidCameraFactory</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AndroidCamera/AndroidCamera.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
