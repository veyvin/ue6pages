---
layout: default
title: 音乐会同步核心 / Concert Sync Core
---

<h1>音乐会同步核心 / Concert Sync Core</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/Concert/ConcertSync/ConcertSyncCore/ConcertSyncCore.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.2</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">联网</div><div class="lang-content">Networking</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ConcertSyncCore</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Concert Sync Core</code>（模块 <code class="usage-code">ConcertSyncCore</code>）。它是客户端/服务器共享的会话、事务、活动和包协议，没有自己的浏览器窗口。</li><li>真正进会话仍靠 <code class="usage-code">Concert Sync - Client</code> Join 和 <code class="usage-code">Concert Sync - Server</code> 宿主；Core 被它们加载。</li><li>写自定义 Concert 桥时，Editor 模块依赖 <code class="usage-code">ConcertSyncCore</code>，用其会话事件、工作区与活动结构，而不是直接解析网络字节。</li><li>不要在游戏模块里 <code class="usage-code">#include</code> 这些头文件，也不要单独启用 Core 却关掉 Client/Server 还指望能同步关卡。</li><li>保持与 Client/Server 同一引擎版本，协议不兼容时会话会直接拒绝连接。</li></ol><p class="usage-note">共享数据层，不是可点击的多人编辑入口。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Concert Sync Core</code> (module <code class="usage-code">ConcertSyncCore</code>). It is the shared session, transaction, activity, and package protocol — no browser window of its own.</li><li>Actual sessions still need <code class="usage-code">Concert Sync - Client</code> Join and a <code class="usage-code">Concert Sync - Server</code> host; they load Core.</li><li>For a custom Concert bridge, depend on <code class="usage-code">ConcertSyncCore</code> in an Editor module and use its session events, workspace, and activity types instead of parsing packets.</li><li>Do not include these headers from a game module, and do not enable Core alone with Client/Server off expecting map sync.</li><li>Keep Core on the same engine version as Client/Server; protocol mismatch refuses the session.</li></ol><p class="usage-note">Shared data layer, not the clickable multi-user entry point.</p></div></div></div>
    </div>

