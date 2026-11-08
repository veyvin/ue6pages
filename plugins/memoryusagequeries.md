---
layout: default
title: 内存使用查询 / MemoryUsageQueries
---

<h1>内存使用查询 / MemoryUsageQueries</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/MemoryUsageQueries/MemoryUsageQueries.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">引擎</div><div class="lang-content">Engine</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MemoryUsageQueries</span></li>
  </ul>
</div>

    <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>MemoryUsageQueries 是引擎源码中的插件，具体职责以描述符和源码为准。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：MemoryUsageQueries。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>MemoryUsageQueries is an engine plugin whose job is defined by its descriptor and source.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: MemoryUsageQueries. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MemoryUsageQueries</code>（模块 <code class="usage-code">MemoryUsageQueries</code>）。</li><li>它提供内存使用查询能力，用于统计/定位内存占用。</li><li>在控制台/代码里调用其查询接口，输出内存使用报告辅助优化。</li><li>属引擎性能/内存分析辅助，具体 API 以源码为准。</li></ol><p class="usage-note">内存使用查询辅助插件，优化期用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MemoryUsageQueries</code> (module <code class="usage-code">MemoryUsageQueries</code>).</li><li>It provides memory-usage query capability to track/locate memory consumption.</li><li>Call its query interface from console/code to emit memory-usage reports for optimization.</li><li>It is an engine perf/memory-analysis aid; treat source as the API source of truth.</li></ol><p class="usage-note">A memory-usage query aid used during optimization.</p></div></div></div>
    </div>

