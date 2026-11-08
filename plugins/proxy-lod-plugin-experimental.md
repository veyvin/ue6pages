---
layout: default
title: 代理 LOD 插件（实验性） / Proxy LOD Plugin (Experimental)
---

<h1>代理 LOD 插件（实验性） / Proxy LOD Plugin (Experimental)</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Editor/ProxyLODPlugin/ProxyLODPlugin.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ProxyLODMeshReduction</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Proxy LOD Plugin (Experimental)</code>（模块 <code class="usage-code">ProxyLODMeshReduction</code>）。</li><li>它用于生成代理 LOD（把多网格合并简化成远景代理）。</li><li>在 HLOD/代理网格流程里用它生成远距离替代网格。</li><li>属实验性编辑器简化工具；默认不进 Shipping。</li></ol><p class="usage-note">生成代理 LOD（远景合并简化网格）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Proxy LOD Plugin (Experimental)</code> (module <code class="usage-code">ProxyLODMeshReduction</code>).</li><li>It generates Proxy LOD systems (merge/simplify meshes into a distant proxy).</li><li>Use it in HLOD/proxy-mesh flows to build far-distance stand-in meshes.</li><li>It is an experimental editor reduction tool; it does not ship by default.</li></ol><p class="usage-note">Generate Proxy LODs (merged/simplified distant meshes).</p></div></div></div>
    </div>

