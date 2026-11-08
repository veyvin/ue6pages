---
layout: default
title: VEUV - 体积编码 UV 贴图 / VEUV - Volume Encoded UV Maps
---

<h1>VEUV - 体积编码 UV 贴图 / VEUV - Volume Encoded UV Maps</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/VEUV/VEUV.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">几何学</div><div class="lang-content">Geometry</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">VEUVCore, VEUVEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">VEUV - Volume Encoded UV Maps</code>（运行时 <code class="usage-code">VEUVCore</code>，编辑器 <code class="usage-code">VEUVEditor</code>）。</li><li>它提供体积编码 UV 参数化（把 UV 编码进体积/顶点数据，便于高密度网格采样）。</li><li>在高模/体积网格流程里用 VEUV 做参数化与贴图采样。</li><li>Experimental：接口可能变动；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">体积编码 UV 参数化（VEUV），实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">VEUV - Volume Encoded UV Maps</code> (runtime <code class="usage-code">VEUVCore</code>, editor <code class="usage-code">VEUVEditor</code>).</li><li>It provides volume-encoded UV parameterization (encodes UVs into volume/vertex data for dense-mesh sampling).</li><li>In high-poly/volumetric mesh flows, use VEUV for parameterization and texture sampling.</li><li>Experimental: contract may change; editor modules go to Editor targets only.</li></ol><p class="usage-note">Volume-encoded UV parameterization (VEUV), experimental.</p></div></div></div>
    </div>

