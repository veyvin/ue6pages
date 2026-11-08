---
layout: default
title: 编辑遥测 / Editor Telemetry
---

<h1>编辑遥测 / Editor Telemetry</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/EditorTelemetry/EditorTelemetry.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">遥测</div><div class="lang-content">Telemetry</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">EditorTelemetry</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Editor Telemetry</code>（<code class="usage-code">EditorTelemetry</code> 模块）并重启。</li><li>确认它只在编辑器进程里发出遥测，不进入游戏运行时。</li><li>操作编辑器触发事件，检查本地日志或后端确定上报内容。</li><li>按需在遥测设置里开关具体事件，避免收集敏感信息。</li></ol><p class="usage-note">这份条目是 `EditorTelemetry` 编辑器模块版本，与 `RuntimeTelemetry` 同名不同模块；Experimental。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Editor Telemetry</code> (the <code class="usage-code">EditorTelemetry</code> module) and restart.</li><li>Confirm it emits telemetry only in the editor process and stays out of the game runtime.</li><li>Drive editor actions to trigger events, then check local logs or the backend for what is reported.</li><li>Toggle specific events in telemetry settings as needed to avoid collecting sensitive data.</li></ol><p class="usage-note">This entry is the `EditorTelemetry` editor-module variant — same display name as, but a different module from, `RuntimeTelemetry`; Experimental.</p></div></div></div>
    </div>

