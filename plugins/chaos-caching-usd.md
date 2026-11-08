---
layout: default
title: 混沌缓存美元 / Chaos Caching USD
---

<h1>混沌缓存美元 / Chaos Caching USD</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/ChaosCachingUSD/ChaosCachingUSD.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">进口商</div><div class="lang-content">Importers</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosCachingUSD</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Chaos Caching USD</code>（模块 <code class="usage-code">ChaosCachingUSD</code>）。</li><li>关卡里先用 Chaos Cache Manager 录一段刚体/破坏缓存（Chaos Caching）。</li><li>通过 USD Stage / 导出管线把该 Chaos Cache 写成 USD，供外部 DCC 或再导入对拍。</li><li>不要把它当实时 Chaos 求解器本身；求解仍由 Chaos 运行时完成，本插件只管 USD 进出。</li></ol><p class="usage-note">Experimental：把已录制的 Chaos Cache 接到 USD，不是在 USD 里跑物理。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Chaos Caching USD</code> (module <code class="usage-code">ChaosCachingUSD</code>).</li><li>Record a rigid/destruction take with a Chaos Cache Manager first.</li><li>Export that cache through the USD stage/export path for DCC or round-trip.</li><li>This is not the Chaos solver; simulation stays in Chaos runtime, this plugin only does USD I/O.</li></ol><p class="usage-note">Experimental USD I/O for recorded Chaos caches, not physics inside USD.</p></div></div></div>
    </div>

