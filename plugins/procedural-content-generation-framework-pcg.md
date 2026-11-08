---
layout: default
title: 程序内容生成框架 (PCG) / Procedural Content Generation Framework (PCG)
---

<h1>程序内容生成框架 (PCG) / Procedural Content Generation Framework (PCG)</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/PCG/PCG.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">PCG, PCGEditor, PCGCompute</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Procedural Content Generation Framework (PCG)</code>（模块 <code class="usage-code">PCG</code>、<code class="usage-code">PCGEditor</code>、<code class="usage-code">PCGCompute</code>）。</li><li>它用节点图在编辑器或运行时程序化生成关卡内容：点云、变换、网格、植被与生成规则，可和景观、HLOD、Nanite 配合。</li><li>创建 PCG Graph，放到体积/关卡里执行，再按需启用各 PCG Interop 插件。</li><li>Game 模块依赖 <code class="usage-code">PCG</code>/<code class="usage-code">PCGCompute</code>；<code class="usage-code">PCGEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">PCG 主插件：节点图程序化生成关卡内容。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Procedural Content Generation Framework (PCG)</code> (modules <code class="usage-code">PCG</code>, <code class="usage-code">PCGEditor</code>, <code class="usage-code">PCGCompute</code>).</li><li>It is a node graph for procedural level content in editor or at runtime: point clouds, transforms, meshes, foliage, and spawn rules, working with Landscape, HLOD, and Nanite.</li><li>Create a PCG Graph, execute it from a volume/level, then enable PCG Interop plugins as needed.</li><li>Game modules depend on <code class="usage-code">PCG</code>/<code class="usage-code">PCGCompute</code>; <code class="usage-code">PCGEditor</code> is Editor-target only.</li></ol><p class="usage-note">Main PCG plugin: node-graph procedural level content.</p></div></div></div>
    </div>

