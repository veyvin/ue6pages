---
layout: default
title: 兑换开放美元 / Interchange OpenUSD
---

<h1>兑换开放美元 / Interchange OpenUSD</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Interchange/Extensions/OpenUSD/InterchangeOpenUSD.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">进口商</div><div class="lang-content">Importers</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">InterchangeOpenUSDImport, InterchangeOpenUSDEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Interchange OpenUSD</code>（模块 <code class="usage-code">InterchangeOpenUSDImport</code>，编辑器 <code class="usage-code">InterchangeOpenUSDEditor</code>）。</li><li>通过 Interchange 框架翻译 OpenUSD（.usd/.usda/.usdc）文件，导入为引擎网格/材质/关卡。</li><li>在导入时选 USD 管道，配置单位、坐标与材质映射。</li><li>导入用 <code class="usage-code">InterchangeOpenUSDImport</code>；<code class="usage-code">InterchangeOpenUSDEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">用 Interchange 导入 OpenUSD，与 USD Importer 路径不同。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Interchange OpenUSD</code> (module <code class="usage-code">InterchangeOpenUSDImport</code>, editor <code class="usage-code">InterchangeOpenUSDEditor</code>).</li><li>Translate OpenUSD (.usd/.usda/.usdc) files via the Interchange framework into engine meshes/materials/levels.</li><li>At import, choose the USD pipeline and configure units, axes, and material mapping.</li><li>Import uses <code class="usage-code">InterchangeOpenUSDImport</code>; <code class="usage-code">InterchangeOpenUSDEditor</code> is Editor-target only.</li></ol><p class="usage-note">Imports OpenUSD via Interchange, a different path from the USD Importer.</p></div></div></div>
    </div>

