---
layout: default
title: 奥德网络 / Oodle Network
---

<h1>奥德网络 / Oodle Network</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Compression/OodleNetwork/OodleNetwork.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">压缩</div><div class="lang-content">Compression</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">OodleNetworkHandlerComponent</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Oodle Network</code>（模块 <code class="usage-code">OodleNetworkHandlerComponent</code>）。</li><li>它为网络数据包提供 Oodle 压缩（降低带宽）。</li><li>在网络的包处理器（PacketHandler）里启用 OodleNetwork 处理器。</li><li>属网络压缩扩展；需 Oodle 库随引擎提供。</li></ol><p class="usage-note">用 Oodle 压缩网络数据包（降带宽）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Oodle Network</code> (module <code class="usage-code">OodleNetworkHandlerComponent</code>).</li><li>It provides Oodle compression for network packets (lower bandwidth).</li><li>Enable the OodleNetwork handler in the network PacketHandler chain.</li><li>It is a network-compression extension; uses the Oodle library shipped with the engine.</li></ol><p class="usage-note">Oodle packet compression for networking (lower bandwidth).</p></div></div></div>
    </div>

