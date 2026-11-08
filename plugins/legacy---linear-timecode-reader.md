---
layout: default
title: 旧版 - 线性时间码读取器 / Legacy - Linear Timecode Reader
---

<h1>旧版 - 线性时间码读取器 / Legacy - Linear Timecode Reader</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Media/LinearTimecode/LinearTimecode.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">媒体播放器</div><div class="lang-content">Media Players</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LinearTimecode</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Legacy - Linear Timecode Reader</code>（模块 <code class="usage-code">LinearTimecode</code>）。</li><li>用它将线性时间码（LTC）从媒体源读成组件/时间码值，用于同步。</li><li>注意它不使用同步机制，只做读取；需要严格同步时要自行加上下游同步逻辑。</li><li>属 Media Framework；旧版命名，功能仍可用。</li></ol><p class="usage-note">读取线性时间码的组件，本身不做同步。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Legacy - Linear Timecode Reader</code> (module <code class="usage-code">LinearTimecode</code>).</li><li>Use it to read linear timecode (LTC) from a media source into a component/timecode value for sync.</li><li>Note it does not apply a synchronization mechanism, only reads; add downstream sync yourself for strict sync.</li><li>Part of Media Framework; legacy naming but still functional.</li></ol><p class="usage-note">A component that reads linear timecode; it does not sync by itself.</p></div></div></div>
    </div>

