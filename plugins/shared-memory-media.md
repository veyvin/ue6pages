---
layout: default
title: 共享存储介质 / Shared Memory Media
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Shared Memory Media</div>
      <div class="hero-title-cn">共享存储介质 · 实现在同一台机器上的进程之间共享 GPU 纹理的媒体输出和媒体源</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/SharedMemoryMedia/SharedMemoryMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">实现在同一台机器上的进程之间共享 GPU 纹理的媒体输出和媒体源。</div><div class="lang-content">Implements a media output and a media source that share GPU textures between processes on the same machine.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：实现在同一台机器上的进程之间共享 GPU 纹理的媒体输出和媒体源。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：SharedMemoryMediaVulkanPreInit, SharedMemoryMedia, SharedMemoryMediaEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements a media output and a media source that share GPU textures between processes on the same machine.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: SharedMemoryMediaVulkanPreInit, SharedMemoryMedia, SharedMemoryMediaEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Shared Memory Media</code>（运行时 <code class="usage-code">SharedMemoryMedia</code>、<code class="usage-code">SharedMemoryMediaVulkanPreInit</code>，编辑器 <code class="usage-code">SharedMemoryMediaEditor</code>）。</li><li>它在同一台机器的进程之间共享 GPU 纹理，提供媒体输出与媒体源。</li><li>把本进程画面作为 media source，或作为 media output 接收；用于多进程协作/外部工具。</li><li>Game 模块依赖运行时模块；<code class="usage-code">SharedMemoryMediaEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">同机进程间共享 GPU 纹理的媒体源/输出。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Shared Memory Media</code> (runtime <code class="usage-code">SharedMemoryMedia</code>, <code class="usage-code">SharedMemoryMediaVulkanPreInit</code>, editor <code class="usage-code">SharedMemoryMediaEditor</code>).</li><li>It shares GPU textures between processes on the same machine, providing a media output and media source.</li><li>Expose this process&#x27;s frames as a media source, or receive as a media output; for multi-process / external-tool collaboration.</li><li>Game modules depend on runtime modules; <code class="usage-code">SharedMemoryMediaEditor</code> is Editor-target only.</li></ol><p class="usage-note">Mechanism to share GPU textures between same-machine processes as media source/output.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">SharedMemoryMediaVulkanPreInit</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SharedMemoryMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SharedMemoryMediaEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/SharedMemoryMedia/SharedMemoryMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
