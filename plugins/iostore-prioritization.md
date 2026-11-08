---
layout: default
title: IoStore 优先级 / IoStore Prioritization
---

<h1>IoStore 优先级 / IoStore Prioritization</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/IoStorePrioritization/IoStorePrioritization.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value">IO</span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">IoStorePrioritization</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">IoStore Prioritization</code>（模块 <code class="usage-code">IoStorePrioritization</code>），运行时插件。</li><li>在流式加载期间，用基于表达式的规则动态调整 IoStore I/O 请求的优先级。</li><li>为不同流送状态/玩法场景配置优先级表达式，让关键内容优先加载。</li><li>运行时模块可进游戏包；用于优化大世界的流送 I/O 调度。</li></ol><p class="usage-note">基于表达式动态排序 IoStore I/O 优先级，优化流送。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">IoStore Prioritization</code> (module <code class="usage-code">IoStorePrioritization</code>), a runtime plugin.</li><li>During streaming, dynamically prioritize IoStore I/O requests using expression-based rules.</li><li>Author priority expressions per streaming state/gameplay scenario so critical content loads first.</li><li>Runtime modules can ship; it optimizes large-world streaming I/O scheduling.</li></ol><p class="usage-note">Expression-based dynamic prioritization of IoStore I/O to optimize streaming.</p></div></div></div>
    </div>

