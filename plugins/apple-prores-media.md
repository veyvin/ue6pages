---
layout: default
title: 苹果 ProRes 媒体 / Apple ProRes Media
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Apple ProRes Media</div>
      <div class="hero-title-cn">苹果 ProRes 媒体 · 实现视频播放和 Apple ProRes 编解码器的导出。  A</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AppleProResMedia/AppleProResMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">实现视频播放和 Apple ProRes 编解码器的导出。  Apple ProRes 是一种高品质、有损视频压缩格式。</div><div class="lang-content">Implements video playback and the export of the Apple ProRes Codec.  Apple ProRes is a high quality, lossy video compression format.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：实现视频播放和 Apple ProRes 编解码器的导出。  Apple ProRes 是一种高品质、有损视频压缩格式。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AppleProResMedia。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements video playback and the export of the Apple ProRes Codec.  Apple ProRes is a high quality, lossy video compression format.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AppleProResMedia. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Apple ProRes Media</code>（<code class="usage-code">AppleProResMedia.uplugin</code> / 模块 <code class="usage-code">AppleProResMedia</code>）并重启。这是 ProRes 导出（及 Media Framework 编解码）插件，不是 Electra 专用软解。</li><li>打开 <code class="usage-code">Window &gt; Cinematics &gt; Movie Render Queue</code>，加入 Level Sequence，在 Job Settings 里 <code class="usage-code">+ Setting</code> 增加 Apple ProRes 输出（标签随版本可能为 <code class="usage-code">Apple ProRes</code> / <code class="usage-code">ProRes</code>）。</li><li>容器一般为 <code class="usage-code">.mov</code>。在该设置里选档位（Proxy / LT / 422 / HQ / 4444 / 4444 XQ 等），并单独加音频输出（如 <code class="usage-code">WAV Audio</code> 或支持的音频轨），不要假设视频轨内嵌最终混音。</li><li>C++ 编码依赖 <code class="usage-code">AppleProResMedia</code> 的编码器 API（对照插件 Public 头），<code class="usage-code">Initialize</code> → 逐帧送像素 → <code class="usage-code">Finalize</code>。回放审查片可用 Media Framework 打开同容器，或改走 <code class="usage-code">Apple ProRes Decoder for Electra</code>。</li><li>按交付规格核对待机分辨率与帧率；渲染完成用 NLE 打开 <code class="usage-code">.mov</code>。Windows 上能否硬解取决于本机 ProRes 支持，不能用 Win PIE 当调色验收。</li></ol><p class="usage-note">MRQ / 编码器出 ProRes `.mov`。Electra 只播请用 `AppleProResDecoderElectra`。启动片不是这条管线。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Apple ProRes Media</code> (<code class="usage-code">AppleProResMedia.uplugin</code> / module <code class="usage-code">AppleProResMedia</code>) and restart. This is ProRes export (and Media Framework codec) support, not Electra’s dedicated software decoder.</li><li>Open <code class="usage-code">Window &gt; Cinematics &gt; Movie Render Queue</code>, add a Level Sequence, and in job Settings use <code class="usage-code">+ Setting</code> to add the Apple ProRes output (label may be <code class="usage-code">Apple ProRes</code> / <code class="usage-code">ProRes</code>).</li><li>The container is typically <code class="usage-code">.mov</code>. Pick a profile (Proxy / LT / 422 / HQ / 4444 / 4444 XQ, etc.) and add a separate audio output (<code class="usage-code">WAV Audio</code> or a supported track); do not assume a final mix is embedded.</li><li>C++ encoding depends on <code class="usage-code">AppleProResMedia</code> encoder APIs in the plugin Public headers: <code class="usage-code">Initialize</code>, submit frames, <code class="usage-code">Finalize</code>. Review playback can use Media Framework on the same container, or <code class="usage-code">Apple ProRes Decoder for Electra</code>.</li><li>Match delivery resolution and frame rate. Open the <code class="usage-code">.mov</code> in an NLE. Windows hardware decode depends on local ProRes support — Win PIE is not a color-finishing check.</li></ol><p class="usage-note">MRQ/encoder path to ProRes `.mov`. Electra-only playback is `AppleProResDecoderElectra`. Not the startup-movie pipeline.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AppleProResMedia</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AppleProResMedia/AppleProResMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
