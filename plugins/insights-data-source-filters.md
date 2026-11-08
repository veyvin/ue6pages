---
layout: default
title: 见解数据源过滤器 / Insights Data Source Filters
---

<h1>见解数据源过滤器 / Insights Data Source Filters</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/TraceSourceFiltering/TraceSourceFilters.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">见解</div><div class="lang-content">Insights</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">SourceFilteringTrace, SourceFilteringCore, SourceFilteringEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">Insights Data Source Filters</code>（模块 <code class="usage-code">SourceFilteringTrace</code>、<code class="usage-code">SourceFilteringCore</code>、<code class="usage-code">SourceFilteringEditor</code>）。</li><li>在 Unreal Insights 的 trace 里按源数据过滤（如按 CPU 线程/对象/系统），聚焦关注的性能数据。</li><li>启动 trace 时启用源过滤，打开 Insights 应用过滤器分析。</li><li>这是编辑器/开发者分析工具，默认不进 Shipping。</li></ol><p class="usage-note">Unreal Insights 的源数据过滤，减少 trace 噪音。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">Insights Data Source Filters</code> (modules <code class="usage-code">SourceFilteringTrace</code>, <code class="usage-code">SourceFilteringCore</code>, <code class="usage-code">SourceFilteringEditor</code>).</li><li>In Unreal Insights traces, filter by source data (e.g. CPU thread/object/system) to focus on the perf data you care about.</li><li>Enable source filtering when starting a trace and apply the filters in Insights to analyze.</li><li>It is an editor/developer analysis tool that does not ship by default.</li></ol><p class="usage-note">Source data filtering for Unreal Insights to reduce trace noise.</p></div></div></div>
    </div>

