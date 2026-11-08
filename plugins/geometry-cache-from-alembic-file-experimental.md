---
layout: default
title: Alembic 文件中的几何缓存（实验） / Geometry Cache from Alembic File(Experimental)
---

<h1>Alembic 文件中的几何缓存（实验） / Geometry Cache from Alembic File(Experimental)</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/GeometryCacheAbcFile/GeometryCacheAbcFile.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GeometryCacheAbcFile</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Geometry Cache from Alembic File</code>（模块 <code class="usage-code">GeometryCacheAbcFile</code>）。</li><li>无需先导入：直接把 <code class="usage-code">.abc</code> Alembic 文件作为几何缓存引用/导入到关卡。</li><li>在 Sequencer 里播放或挂到组件上查看动画几何体，检查帧范围与单位。</li><li>Experimental：接口可能变动；稳定管线可先导成 Geometry Cache 资产。</li></ol><p class="usage-note">直接从 Alembic 读几何缓存（免导入），与标准 Geometry Cache 导入路径互补。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Geometry Cache from Alembic File</code> (module <code class="usage-code">GeometryCacheAbcFile</code>).</li><li>Skip the pre-import step: reference/import the <code class="usage-code">.abc</code> Alembic file directly as geometry cache.</li><li>Play it in Sequencer or attach it to a component; check frame range and units.</li><li>Experimental: contract may change; for stable pipelines you can bake to a Geometry Cache asset first.</li></ol><p class="usage-note">Reads geometry cache straight from Alembic without a pre-import; complements the standard Geometry Cache import path.</p></div></div></div>
    </div>

