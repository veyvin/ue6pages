---
layout: default
title: 缓动曲线工具 / Ease Curve Tool
---

<h1>缓动曲线工具 / Ease Curve Tool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/EaseCurveTool/EaseCurveTool.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">EaseCurveTool</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">编辑 &gt; 插件</code> 里启用 <code class="usage-code">Ease Curve Tool</code> 并重启编辑器。</li><li>打开一个带动画轨道的 <code class="usage-code">Sequencer</code>，选中骨骼或 Transform 轨道上的若干关键帧。</li><li>打开曲线编辑器 <code class="usage-code">Curve Editor</code>，用 Ease Curve Tool 的预设库给选中关键帧套用缓入/缓出，例如 <code class="usage-code">Ease In Out</code>。</li><li>切换不同预设对比曲线形状，并手动拖动切线手柄做微调。</li><li>把满意的一套切线设置存成自定义预设，供同项目其它镜头复用。</li><li>回到 Sequencer 播放，确认关键帧之间不再是线性插值而是自然缓动。</li></ol><p class="usage-note">Ease Curve Tool 是曲线编辑器里的切线预设工具，只作用于选中的关键帧；预设可在项目内复用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Ease Curve Tool</code> under <code class="usage-code">Edit &gt; Plugins</code> and restart the editor.</li><li>Open a <code class="usage-code">Sequencer</code> with an animation track and select several keys on a bone or Transform track.</li><li>Open the <code class="usage-code">Curve Editor</code> and apply an ease-in/ease-out preset from the Ease Curve Tool library, e.g. <code class="usage-code">Ease In Out</code>, to the selected keys.</li><li>Toggle between presets to compare curve shapes, then drag the tangent handles to fine-tune.</li><li>Save the tuned tangent setup as a custom preset so other shots in the project can reuse it.</li><li>Play back in Sequencer and confirm keys now ease between poses instead of interpolating linearly.</li></ol><p class="usage-note">Ease Curve Tool is a tangent-preset helper inside Curve Editor that acts on selected keys only; presets are reusable across the project.</p></div></div></div>
    </div>

