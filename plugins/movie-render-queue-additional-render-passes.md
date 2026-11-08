---
layout: default
title: 影片渲染队列附加渲染通道 / Movie Render Queue Additional Render Passes
---

<h1>影片渲染队列附加渲染通道 / Movie Render Queue Additional Render Passes</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/MovieScene/MoviePipelineMaskRenderPass/MoviePipelineMaskRenderPass.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MoviePipelineMaskRenderPass</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Movie Render Queue Additional Render Passes</code>（模块 <code class="usage-code">MoviePipelineMaskRenderPass</code>）。</li><li>它为 MRQ 增加附加渲染通道：ObjectId 遮罩（Cryptomatte 规范，仅编辑器）以及 Sequencer 集成更好的全景通道。</li><li>在 MRQ 设置里启用 ObjectId/全景通道，渲染后用于合成/后期。</li><li>属 MRQ 渲染通道扩展；ObjectId 仅编辑器可用。</li></ol><p class="usage-note">MRQ 的附加渲染通道（ObjectId 遮罩/全景）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Movie Render Queue Additional Render Passes</code> (module <code class="usage-code">MoviePipelineMaskRenderPass</code>).</li><li>It adds extra render passes to MRQ: ObjectId pass (Cryptomatte spec, Editor-only) and a panoramic pass with better Sequencer integration.</li><li>Enable the ObjectId/panoramic passes in MRQ settings for compositing/post afterward.</li><li>It is an MRQ render-pass extension; ObjectId is Editor-only.</li></ol><p class="usage-note">Additional MRQ render passes (ObjectId mask/panoramic).</p></div></div></div>
    </div>

