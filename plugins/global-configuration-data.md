---
layout: default
title: 全局配置数据 / Global Configuration Data
---

<h1>全局配置数据 / Global Configuration Data</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/GlobalConfigurationData/GlobalConfigurationData.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">杂项</div><div class="lang-content">Misc</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GlobalConfigurationData, GlobalConfigurationDataCore</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Global Configuration Data</code>（模块 <code class="usage-code">GlobalConfigurationData</code>、<code class="usage-code">GlobalConfigurationDataCore</code>）。</li><li>用它查询可能来自多个来源的配置数据，而无需知道具体是哪个来源。</li><li>注册配置提供者/数据源，再通过统一接口查询取值。</li><li>Experimental：接口可能随夜构建变化，别写死未文档化的来源类型。</li></ol><p class="usage-note">多来源配置查询系统，不是引擎的 ini/Config 缓存本身。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Global Configuration Data</code> (modules <code class="usage-code">GlobalConfigurationData</code>, <code class="usage-code">GlobalConfigurationDataCore</code>).</li><li>Use it to query configuration data that may come from many sources without knowing which one.</li><li>Register config providers/data sources, then query values through the unified interface.</li><li>Experimental: contract may change on nightlies; do not freeze undocumented source types.</li></ol><p class="usage-note">A multi-source config query system, not the engine&#x27;s ini/Config cache itself.</p></div></div></div>
    </div>

