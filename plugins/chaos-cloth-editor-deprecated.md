---
layout: default
title: 混沌布料编辑器（已弃用） / Chaos Cloth Editor (Deprecated)
---

<h1>混沌布料编辑器（已弃用） / Chaos Cloth Editor (Deprecated)</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/ChaosClothEditor/ChaosClothEditor.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>插件名带 Deprecated：新项目改用 <code class="usage-code">Chaos Cloth</code> + <code class="usage-code">Chaos Cloth Asset</code> 编辑器。</li><li>旧工程若还靠本插件打开历史 Cloth 资产，按迁移提示另存为 Cloth Asset。</li><li>不要把已废弃编辑器模块写进新的 <code class="usage-code">*Editor.Build.cs</code>。</li><li>迁移后禁用本插件。</li></ol><p class="usage-note">旧 Chaos 布料编辑器，将随引擎移除。</p></div><div class="lang-content"><ol class="usage-steps"><li>This plugin is Deprecated; new work uses <code class="usage-code">Chaos Cloth</code> plus the <code class="usage-code">Chaos Cloth Asset</code> editor.</li><li>If a legacy project still opens old cloth assets here, resave them as Cloth Assets.</li><li>Do not add the deprecated editor modules to a new <code class="usage-code">*Editor.Build.cs</code>.</li><li>Disable the plugin after migration.</li></ol><p class="usage-note">Legacy Chaos cloth editor scheduled for removal.</p></div></div></div>
    </div>

