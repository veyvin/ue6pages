---
layout: default
title: 景观补丁 / Landscape Patch
---

<h1>景观补丁 / Landscape Patch</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Editor/LandscapePatch/LandscapePatch.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LandscapePatch, LandscapePatchEditorOnly</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">Landscape Patch</code>（模块 <code class="usage-code">LandscapePatch</code>、<code class="usage-code">LandscapePatchEditorOnly</code>）并重启。</li><li>把景观补丁组件附加到网格上，当网格移动/重新定位时影响景观。</li><li>用于让物件（如道路、水坑）随网格贴合并修改地形。</li><li>这是编辑器工具，服务制作流程，默认不进 Shipping。</li></ol><p class="usage-note">可附加到网格、随移动修改景观的补丁组件，编辑器向。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">Landscape Patch</code> (modules <code class="usage-code">LandscapePatch</code>, <code class="usage-code">LandscapePatchEditorOnly</code>) and restart.</li><li>Attach landscape patch components to meshes so the landscape is affected as the mesh is repositioned.</li><li>Use it to make objects (roads, puddles, etc.) conform and modify terrain as they move.</li><li>It is an editor tool for the authoring pipeline; it does not ship by default.</li></ol><p class="usage-note">Mesh-attachable patch components that modify landscape as they move, editor-oriented.</p></div></div></div>
    </div>

