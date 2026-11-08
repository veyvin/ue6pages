---
layout: default
title: 几何脚本 / Geometry Script
---

<h1>几何脚本 / Geometry Script</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/GeometryScripting/GeometryScripting.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">几何学</div><div class="lang-content">Geometry</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GeometryScriptingCore, GeometryScriptingEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Geometry Script</code>（运行时 <code class="usage-code">GeometryScriptingCore</code>，编辑器 <code class="usage-code">GeometryScriptingEditor</code>）。</li><li>在蓝图或 Python 里调用 Geometry Script 函数库，对 DynamicMesh 做生成与编辑（布尔、挤出、倒角等）。</li><li>把脚本结果转成 StaticMesh 资产或直接用于关卡；编辑器工具默认不进 Shipping。</li><li>运行时依赖 <code class="usage-code">GeometryScriptingCore</code>；<code class="usage-code">GeometryScriptingEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">蓝图/Python 的网格生成与编辑函数库，编辑器侧居多。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Geometry Script</code> (runtime <code class="usage-code">GeometryScriptingCore</code>, editor <code class="usage-code">GeometryScriptingEditor</code>).</li><li>Call the Geometry Script function library from Blueprint or Python to generate/edit a DynamicMesh (boolean, extrude, bevel, etc.).</li><li>Convert the script result to a StaticMesh asset or use it in-level; editor tools do not ship.</li><li>Runtime depends on <code class="usage-code">GeometryScriptingCore</code>; <code class="usage-code">GeometryScriptingEditor</code> is Editor-target only.</li></ol><p class="usage-note">A Blueprint/Python mesh generation and editing library, mostly editor-side.</p></div></div></div>
    </div>

