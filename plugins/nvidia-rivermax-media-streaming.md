---
layout: default
title: NVIDIA Rivermax 媒体流 / NVIDIA Rivermax Media Streaming
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">N</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">NVIDIA Rivermax Media Streaming</div>
      <div class="hero-title-cn">NVIDIA Rivermax 媒体流 · 为媒体捕获和媒体播放器添加 NVIDIA Rivermax 功能</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/Rivermax/RivermaxMedia/RivermaxMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">为媒体捕获和媒体播放器添加 NVIDIA Rivermax 功能</div><div class="lang-content">Adding NVIDIA Rivermax capabilities for Media Captures and Media Players</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：为媒体捕获和媒体播放器添加 NVIDIA Rivermax 功能</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：RivermaxMedia, RivermaxMediaEditor, RivermaxMediaFactory。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adding NVIDIA Rivermax capabilities for Media Captures and Media Players</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: RivermaxMedia, RivermaxMediaEditor, RivermaxMediaFactory. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">NVIDIA Rivermax Media Streaming</code>（运行时 <code class="usage-code">RivermaxMedia</code>，编辑器 <code class="usage-code">RivermaxMediaEditor</code>，工厂 <code class="usage-code">RivermaxMediaFactory</code>），属 Virtual Production。</li><li>它为媒体捕获与媒体播放器添加 NVIDIA Rivermax 功能（低延迟 SMPTE ST 2110 网络视频）。</li><li>在 Media IO/Media Player 里选 Rivermax 源/输出，接入专业网络视频流。</li><li>Game 模块依赖 <code class="usage-code">RivermaxMedia</code>；编辑器/工厂模块只进 Editor Target。</li></ol><p class="usage-note">NVIDIA Rivermax 的专业网络视频（ST 2110）媒体 IO。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">NVIDIA Rivermax Media Streaming</code> (runtime <code class="usage-code">RivermaxMedia</code>, editor <code class="usage-code">RivermaxMediaEditor</code>, factory <code class="usage-code">RivermaxMediaFactory</code>), part of Virtual Production.</li><li>It adds NVIDIA Rivermax to media capture and media players (low-latency SMPTE ST 2110 networked video).</li><li>Select a Rivermax source/output in Media IO/Media Player to tap professional networked video.</li><li>Game modules depend on <code class="usage-code">RivermaxMedia</code>; editor/factory modules go to Editor targets only.</li></ol><p class="usage-note">NVIDIA Rivermax professional networked-video (ST 2110) media IO.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">RivermaxMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RivermaxMediaEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RivermaxMediaFactory</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/Rivermax/RivermaxMedia/RivermaxMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
