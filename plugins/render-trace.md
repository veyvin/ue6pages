---
layout: default
title: 渲染追踪 / Render Trace
---

<h1>渲染追踪 / Render Trace</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/RenderTrace/RenderTrace.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">RenderTrace</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Render Trace</code>（模块 <code class="usage-code">RenderTrace</code>）。</li><li>它提供对网格上物理材质的像素级采样（按屏幕像素打到物理材质）。</li><li>用于需要精确采样物理表面（轮胎、足迹、弹着点）的玩法。</li><li>属运行时采样；可进游戏包。</li></ol><p class="usage-note">对网格物理材质做像素级采样。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Render Trace</code> (module <code class="usage-code">RenderTrace</code>).</li><li>It provides pixel-perfect sampling of physical materials on meshes.</li><li>Use it for gameplay that must sample physical surfaces precisely (tires, footprints, impact points).</li><li>It is runtime sampling; can ship in a cooked game.</li></ol><p class="usage-note">Pixel-perfect sampling of physical materials on meshes.</p></div></div></div>
    </div>

