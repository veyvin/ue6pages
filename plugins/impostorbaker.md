---
layout: default
title: 冒充贝克 / ImpostorBaker
---

<h1>冒充贝克 / ImpostorBaker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/ImpostorBaker/ImpostorBaker.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">网</div><div class="lang-content">Mesh</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">ImpostorBaker</code> 插件（无独立运行时模块）。</li><li>选中网格，用 ImpostorBaker 生成各种 Impostor，作为远距离网格 LOD。</li><li>在 LOD 设置里把远景替换为生成的 Impostor，减少远处绘制开销。</li><li>这是制作期烘焙工具（实验性），输出资产给运行时 LOD 使用。</li></ol><p class="usage-note">生成远景 Impostor LOD 的烘焙工具，编辑器期使用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">ImpostorBaker</code> (no standalone runtime module).</li><li>Select a mesh and use ImpostorBaker to generate impostors for use as distant mesh LODs.</li><li>Swap distant LODs to the generated impostor to cut far-field draw cost.</li><li>It is an authoring-time bake tool (experimental) whose assets feed runtime LODs.</li></ol><p class="usage-note">A bake tool that generates distant impostor LODs, used at authoring time.</p></div></div></div>
    </div>

