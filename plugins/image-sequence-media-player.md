---
layout: default
title: 图像序列媒体播放器 / Image Sequence Media Player
---

<h1>图像序列媒体播放器 / Image Sequence Media Player</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Media/ImgMedia/ImgMedia.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">媒体播放器</div><div class="lang-content">Media Players</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ImgMedia, ImgMediaEditor, ImgMediaEngine, ImgMediaFactory, ImgMediaFactory, OpenExrWrapper, ExrReaderGpu</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Image Sequence Media Player</code>（模块 <code class="usage-code">ImgMedia</code>、<code class="usage-code">ImgMediaEngine</code>、<code class="usage-code">ImgMediaEditor</code>、<code class="usage-code">ImgMediaFactory</code> 等）。</li><li>用 Media Player + ImgMediaSource 指向 EXR/PNG 等图像序列（目录或 <code class="usage-code">.exr</code> 序列）。</li><li>把 Media Texture 接到材质/Media Plate 播放，注意读取性能与预缓存。</li><li>Game 模块依赖 <code class="usage-code">ImgMedia</code> / <code class="usage-code">ImgMediaEngine</code>；Factory/Editor 模块只进 Editor Target。</li></ol><p class="usage-note">图像序列（EXR 等）媒体播放，非压缩视频文件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Image Sequence Media Player</code> (modules <code class="usage-code">ImgMedia</code>, <code class="usage-code">ImgMediaEngine</code>, <code class="usage-code">ImgMediaEditor</code>, <code class="usage-code">ImgMediaFactory</code>, etc.).</li><li>Use a Media Player + ImgMediaSource pointing at an EXR/PNG image sequence (a folder or <code class="usage-code">.exr</code> sequence).</li><li>Feed the Media Texture to a material/Media Plate; watch read performance and pre-caching.</li><li>Game modules depend on <code class="usage-code">ImgMedia</code> / <code class="usage-code">ImgMediaEngine</code>; factory/editor modules go to Editor targets only.</li></ol><p class="usage-note">Image-sequence (EXR etc.) media playback, not compressed video files.</p></div></div></div>
    </div>

