---
layout: default
title: 混沌布料资源编辑器（已弃用） / Chaos Cloth Asset Editor (Deprecated)
---

<h1>混沌布料资源编辑器（已弃用） / Chaos Cloth Asset Editor (Deprecated)</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/ChaosClothAssetEditor/ChaosClothAssetEditor.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在插件列表里找到 <code class="usage-code">Chaos Cloth Asset Editor (Deprecated)</code>，新项目不要启用。</li><li>已有工程若仍打开旧 Cloth Asset 编辑器，按引擎提示迁到 <code class="usage-code">Chaos Cloth Asset Editor Core</code>。</li><li>不要在 <code class="usage-code">Build.cs</code> 里新增对该过时描述符的依赖。</li><li>迁移完成后在 <code class="usage-code">Edit &gt; Plugins</code> 禁用本插件，避免两套编辑器抢同一资产。</li></ol><p class="usage-note">已废弃的 Cloth Asset 编辑器壳，没有可依赖的运行时模块列表。</p></div><div class="lang-content"><ol class="usage-steps"><li>Find <code class="usage-code">Chaos Cloth Asset Editor (Deprecated)</code> and do not enable it on new projects.</li><li>If an existing project still opens the old Cloth Asset editor, migrate to <code class="usage-code">Chaos Cloth Asset Editor Core</code>.</li><li>Do not add new <code class="usage-code">Build.cs</code> dependencies on this deprecated descriptor.</li><li>After migration, disable this plugin so two editors do not fight over the same asset.</li></ol><p class="usage-note">Deprecated editor shell; it ships no runtime module list to depend on.</p></div></div></div>
    </div>

