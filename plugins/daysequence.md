---
layout: default
title: 日序 / DaySequence
---

<h1>日序 / DaySequence</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/DaySequence/DaySequence.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">其他</div><div class="lang-content">Other</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DaySequenceEditor, DaySequence</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">DaySequence</code> 用 Sequencer 驱动一整天的时间变化（太阳/月亮/天空），适合开放世界的昼夜系统。</li><li>启用后在关卡里放置 <code class="usage-code">DaySequenceActor</code>，把 Directional Light、Sky、SkyAtmosphere、Post Process 绑定到它的轨道。</li><li>打开 DaySequence 资产（Sequencer 时间轴），用关键帧或曲线定义 0–24 小时的太阳角度、色温和云量。</li><li>在关卡蓝图里用 <code class="usage-code">Set Time of Day</code> / <code class="usage-code">Play</code> 节点按游戏时钟推进，或把参数暴露给天气系统统一驱动。</li><li><code class="usage-code">DaySequenceEditor</code> 只提供编辑器 UI，打包只依赖运行时模块 <code class="usage-code">DaySequence</code>。</li></ol><p class="usage-note">它是 Experimental：与大世界时间同步时注意 Sequencer 帧率与确定性，避免昼夜跳变。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">DaySequence</code> drives a full day of time-of-day changes (sun/moon/sky) through Sequencer, ideal for open-world day-night systems.</li><li>After enabling, place a <code class="usage-code">DaySequenceActor</code> in the level and bind the Directional Light, Sky, SkyAtmosphere, and Post Process to its tracks.</li><li>Open the DaySequence asset (a Sequencer timeline) and key or curve the sun angle, color temperature, and cloud cover across 0–24 hours.</li><li>In the level Blueprint, drive it with <code class="usage-code">Set Time of Day</code> / <code class="usage-code">Play</code> nodes from the game clock, or expose the parameters to a weather system.</li><li><code class="usage-code">DaySequenceEditor</code> is the editor UI only; shipping depends solely on the runtime module <code class="usage-code">DaySequence</code>.</li></ol><p class="usage-note">Experimental: when syncing with a large-world clock, watch Sequencer framerate and determinism to avoid day-night jumps.</p></div></div></div>
    </div>

