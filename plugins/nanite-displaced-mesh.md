---
layout: default
title: 纳米位移网格 / Nanite Displaced Mesh
---

<h1>纳米位移网格 / Nanite Displaced Mesh</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/NaniteDisplacedMesh/NaniteDisplacedMesh.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NaniteDisplacedMesh, NaniteDisplacedMeshEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Nanite Displaced Mesh</code>（运行时 <code class="usage-code">NaniteDisplacedMesh</code>，编辑器 <code class="usage-code">NaniteDisplacedMeshEditor</code>）。</li><li>它提供为 Nanite 网格做基本预位移（pre-displacement）管线的资源与组件类型。</li><li>给 Nanite 网格配置位移，烘出带位移的网格。</li><li>Experimental：接口可能变动；<code class="usage-code">NaniteDisplacedMeshEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">Nanite 网格的预位移管线（资源/组件），实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Nanite Displaced Mesh</code> (runtime <code class="usage-code">NaniteDisplacedMesh</code>, editor <code class="usage-code">NaniteDisplacedMeshEditor</code>).</li><li>It provides asset and component types that give Nanite meshes a basic pre-displacement pipeline.</li><li>Configure displacement on Nanite meshes and bake the displaced mesh.</li><li>Experimental: contract may change; <code class="usage-code">NaniteDisplacedMeshEditor</code> is Editor-target only.</li></ol><p class="usage-note">A pre-displacement pipeline for Nanite meshes (asset/component), experimental.</p></div></div></div>
    </div>

