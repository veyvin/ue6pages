---
layout: default
title: GPU 重塑插件 / GPU Reshape Plugin
---

<h1>GPU 重塑插件 / GPU Reshape Plugin</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Editor/GPUReshapeEditor/GPUReshapeEditor.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GPUReshapeEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">GPU Reshape Plugin</code>（模块 <code class="usage-code">GPUReshapeEditor</code>）并重启。</li><li>在编辑器里打开 GPU Reshape 集成面板，对渲染管线做捕获/分析（配合外部 GPU Reshape 工具）。</li><li>用于渲染调试与验证，不参与游戏逻辑。</li><li>这是编辑器开发者工具，只进 Editor Target。</li></ol><p class="usage-note">渲染管线捕获/调试的编辑器集成，不是运行时渲染插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">GPU Reshape Plugin</code> (module <code class="usage-code">GPUReshapeEditor</code>) and restart.</li><li>Open the GPU Reshape integration panel in the editor to capture/analyze the render pipeline (with the external GPU Reshape tool).</li><li>Use it for render debugging and validation; it does not drive gameplay.</li><li>It is an editor developer tool for Editor targets only.</li></ol><p class="usage-note">Editor integration for render-pipeline capture/debug, not a runtime render plugin.</p></div></div></div>
    </div>

