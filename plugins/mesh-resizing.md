---
layout: default
title: 调整网格大小 / Mesh Resizing
---

<h1>调整网格大小 / Mesh Resizing</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/MeshResizing/MeshResizing.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MeshResizingCore, MeshResizingDataflowNodes, MeshResizingEditorTools</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Mesh Resizing</code>（模块 <code class="usage-code">MeshResizingCore</code>、<code class="usage-code">MeshResizingDataflowNodes</code>、<code class="usage-code">MeshResizingEditorTools</code>）。</li><li>它用于调整网格大小（非等比缩放/重构网格），含 Dataflow 节点与编辑器工具。</li><li>在 Dataflow 或建模工具里对网格做尺寸调整，输出新网格。</li><li>Experimental：接口可能变动；编辑器工具只进 Editor Target。</li></ol><p class="usage-note">调整网格尺寸（含 Dataflow 节点与编辑器工具），实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Mesh Resizing</code> (modules <code class="usage-code">MeshResizingCore</code>, <code class="usage-code">MeshResizingDataflowNodes</code>, <code class="usage-code">MeshResizingEditorTools</code>).</li><li>It resizes meshes (non-uniform scaling/mesh reconstruction) with Dataflow nodes and editor tools.</li><li>Resize meshes in Dataflow or the modeling tools and output the new mesh.</li><li>Experimental: contract may change; editor tools go to Editor targets only.</li></ol><p class="usage-note">Mesh resizing (with Dataflow nodes and editor tools), experimental.</p></div></div></div>
    </div>

