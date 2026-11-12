---
layout: default
title: Electra 的 AV1 软件解码器 / AV1 software decoder for Electra
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AV1 software decoder for Electra</div>
      <div class="hero-title-cn">Electra 的 AV1 软件解码器 · 允许使用 Electra 媒体播放器解码 AV1 编码的视频。仅</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AV1DecoderElectra/AV1DecoderElectra.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">允许使用 Electra 媒体播放器解码 AV1 编码的视频。仅软件解决方案，性能会因平台而异。</div><div class="lang-content">Enables decoding of AV1 encoded videos with the Electra media player. Software solution only, performance will vary per platform.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：允许使用 Electra 媒体播放器解码 AV1 编码的视频。仅软件解决方案，性能会因平台而异。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AV1DecoderElectra。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Enables decoding of AV1 encoded videos with the Electra media player. Software solution only, performance will vary per platform.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AV1DecoderElectra. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 的 Media Players 中启用 <code class="usage-code">AV1 software decoder for Electra</code>（<code class="usage-code">AV1DecoderElectra.uplugin</code>），并同时保持 <code class="usage-code">Electra Player</code> 可用，然后重启编辑器。</li><li>把 AV1 片源（常见为 <code class="usage-code">av01</code> 的 <code class="usage-code">.mp4</code> / <code class="usage-code">.webm</code>，或 IVF）放进项目可访问路径；该模块是 dav1d 一类的 CPU 软解，不会在内容浏览器里生成独立「解码器资产」。</li><li>新建 <code class="usage-code">File Media Source</code>（或 URL/<code class="usage-code">Stream Media Source</code>），指向上述 AV1 文件；在 <code class="usage-code">Media Player</code> 资产上把首选播放器设为 Electra，不要用 WMF/AVF 去解 AV1。</li><li>创建 <code class="usage-code">Media Texture</code> 绑定该 <code class="usage-code">Media Player</code>，赋给材质采样器或 <code class="usage-code">Media Plate</code>；蓝图里对播放器 <code class="usage-code">Open Source</code> / <code class="usage-code">Play</code>。Electra 会按四字符码自动选用 <code class="usage-code">AV1DecoderElectra</code>。</li><li>在目标平台用 <code class="usage-code">stat unit</code> / 媒体日志确认解码线程 CPU 占用；软解性能随分辨率与平台变化，Shipping 包需把该插件打进对应平台，不要只在编辑器启用。</li><li>游戏模块一般不必把 <code class="usage-code">AV1DecoderElectra</code> 写进 <code class="usage-code">Build.cs</code>：解码器由 Electra 工厂在运行时注册。只有写自定义 Electra 解码管线时才依赖该模块头文件。</li></ol><p class="usage-note">这是 Electra 的 AV1 软解插件，不是通用 Media Player。没有独立组件；片源必须是 AV1，播放器必须走 Electra。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AV1 software decoder for Electra</code> (<code class="usage-code">AV1DecoderElectra.uplugin</code>) under <code class="usage-code">Edit &gt; Plugins</code> &gt; Media Players, keep <code class="usage-code">Electra Player</code> enabled, then restart the editor.</li><li>Place AV1 bitstreams (typically <code class="usage-code">av01</code> in <code class="usage-code">.mp4</code> / <code class="usage-code">.webm</code>, or IVF) where the project can read them. This module is a CPU software decoder (dav1d-style); it does not create a decoder asset in the Content Browser.</li><li>Create a <code class="usage-code">File Media Source</code> (or URL/<code class="usage-code">Stream Media Source</code>) that points at the AV1 file. On the <code class="usage-code">Media Player</code> asset, prefer Electra — do not expect WMF/AVF to decode AV1.</li><li>Create a <code class="usage-code">Media Texture</code> bound to that <code class="usage-code">Media Player</code> and sample it in a material or <code class="usage-code">Media Plate</code>. From Blueprint, <code class="usage-code">Open Source</code> / <code class="usage-code">Play</code>. Electra selects <code class="usage-code">AV1DecoderElectra</code> from the codec fourCC.</li><li>On the target device, watch <code class="usage-code">stat unit</code> and media logs for decode-thread CPU. Software AV1 cost varies by resolution and platform; include the plugin in the cooked platform, not editor-only.</li><li>Gameplay <code class="usage-code">Build.cs</code> files usually omit <code class="usage-code">AV1DecoderElectra</code> because Electra’s factory registers the decoder at runtime. Depend on the module only if you are extending Electra’s decoder pipeline in C++.</li></ol><p class="usage-note">This is Electra’s AV1 software decoder, not a generic Media Player. There is no component to add; the bitstream must be AV1 and playback must go through Electra.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AV1DecoderElectra</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AV1DecoderElectra/AV1DecoderElectra.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
