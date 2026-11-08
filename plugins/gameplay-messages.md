---
layout: default
title: 游戏消息 / Gameplay Messages
---

<h1>游戏消息 / Gameplay Messages</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/GameplayMessages/GameplayMessages.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GameplayMessages, GameplayMessagesEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Gameplay Messages</code>（运行时 <code class="usage-code">GameplayMessages</code>，编辑器 <code class="usage-code">GameplayMessagesEditor</code>）。</li><li>用它在系统之间做解耦的消息传递：定义消息并在合适时机广播，其他系统订阅处理。</li><li>编辑器里用 <code class="usage-code">GameplayMessagesEditor</code> 调试/查看消息；Game 模块只依赖 <code class="usage-code">GameplayMessages</code>。</li><li>它是轻量消息总线，不替代复制型网络 RPC；联网逻辑仍走正常的复制通道。</li></ol><p class="usage-note">轻量玩法消息总线，用于解耦，不是网络 RPC。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Gameplay Messages</code> (runtime <code class="usage-code">GameplayMessages</code>, editor <code class="usage-code">GameplayMessagesEditor</code>).</li><li>Use it to decouple systems: define messages, broadcast at the right moment, and let other systems subscribe.</li><li>Use <code class="usage-code">GameplayMessagesEditor</code> for editor-side debugging/viewing; game modules depend on <code class="usage-code">GameplayMessages</code> only.</li><li>It is a lightweight message bus, not a replication RPC layer; networking still uses normal replication.</li></ol><p class="usage-note">A lightweight gameplay message bus for decoupling, not a network RPC layer.</p></div></div></div>
    </div>

