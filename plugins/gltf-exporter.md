---
layout: default
title: glTF 导出器 / glTF Exporter
---

<h1>glTF 导出器 / glTF Exporter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Enterprise/GLTFExporter/GLTFExporter.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.3.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">出口商</div><div class="lang-content">Exporters</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GLTFExporter</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">glTF Exporter</code>（模块 <code class="usage-code">GLTFExporter</code>），类别 Exporters。</li><li>在内容浏览器或关卡里选中资产，通过导出菜单选择 glTF 2.0 导出。</li><li>用于把引擎内容交给外部 DCC/Web 渲染；导出后检查材质、单位与节点结构。</li><li>这是导出工具，通常编辑器侧使用；不要当游戏运行时依赖。</li></ol><p class="usage-note">Khronos glTF 2.0 导出器，方向是引擎→外部。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">glTF Exporter</code> (module <code class="usage-code">GLTFExporter</code>), category Exporters.</li><li>Select assets in the Content Browser or level and export via the glTF 2.0 export menu.</li><li>Use it to hand engine content to external DCCs/web renderers; check materials, units, and node structure after export.</li><li>It is an export tool used editor-side; do not treat it as a game runtime dependency.</li></ol><p class="usage-note">A Khronos glTF 2.0 exporter, engine-to-external direction.</p></div></div></div>
    </div>

