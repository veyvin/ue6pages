---
layout: default
title: 后处理材质链图 / Post Process Material Chain Graph
---

<h1>后处理材质链图 / Post Process Material Chain Graph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/PostProcessMaterialChainGraph/PostProcessMaterialChainGraph.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">其他</div><div class="lang-content">Other</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏</div><div class="lang-content">Epic Games</div></div></span></li><li><span class="label">模块</span><span class="value">PPMChainGraph, PPMChainGraphEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Post Process Material Chain Graph</code>（运行时 <code class="usage-code">PPMChainGraph</code>，编辑器 <code class="usage-code">PPMChainGraphEditor</code>）。</li><li>它允许堆叠后期处理材质，并渲染到与 Scene Color 分开的 Render Target。</li><li>用它在不写回场景颜色的情况下，对其它纹理做后期处理链。</li><li>属实验性后期处理工具；Game 模块依赖运行时，编辑器模块只进 Editor Target。</li></ol><p class="usage-note">把后期处理材质链渲染到独立 RT（可不写 Scene Color）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Post Process Material Chain Graph</code> (runtime <code class="usage-code">PPMChainGraph</code>, editor <code class="usage-code">PPMChainGraphEditor</code>).</li><li>It lets you stack post-process materials and render them into render targets separate from Scene Color.</li><li>Use it to operate on textures other than scene color without writing them back to scene color.</li><li>It is an experimental post-process tool; game modules depend on runtime, editor modules are Editor-target only.</li></ol><p class="usage-note">Stack post-process materials into separate RTs (not Scene Color).</p></div></div></div>
    </div>

