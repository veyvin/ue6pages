---
layout: default
title: 发现信标接收器 / Discovery Beacon Receiver
---

<h1>发现信标接收器 / Discovery Beacon Receiver</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/DiscoveryBeaconReceiver/DiscoveryBeaconReceiver.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">消息传递</div><div class="lang-content">Messaging</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DiscoveryBeaconReceiver</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Discovery Beacon Receiver</code> 在 UDP 多播套接字上监听查询报文，并用引擎信息（版本、项目名、端口）回应，供局域网发现工具定位本实例。</li><li>启用插件，并在 <code class="usage-code">DefaultEngine.ini</code> 的对应分区里配置多播组地址与端口。</li><li>让局域网里的发现客户端（如 Pixel Streaming / 远程工具）向该多播组发送查询包，插件会用单播回复。</li><li>在防火墙与交换机的组播策略上放行对应 UDP 端口，否则回复到不了发现端。</li><li>用 Wireshark 过滤该多播地址抓包，确认查询与回复流量，并核对回复里的引擎版本/端口字段。</li></ol><p class="usage-note">多播默认不跨网段；跨子网发现需要交换机开 IGMP 侦听或配置多播路由。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Discovery Beacon Receiver</code> listens for query packets on a UDP multicast socket and replies with engine info (version, project name, port) so LAN discovery tools can locate this instance.</li><li>Enable the plugin and set the multicast group address and port in the matching section of <code class="usage-code">DefaultEngine.ini</code>.</li><li>Have a LAN discovery client (Pixel Streaming / remote tooling) send a query to that multicast group; the plugin answers via unicast.</li><li>Allow the corresponding UDP port through firewall and switch multicast policy, or replies never reach the discovering end.</li><li>Capture with Wireshark filtered on that multicast address to confirm query/reply traffic and check the engine-version/port fields in the reply.</li></ol><p class="usage-note">Multicast does not cross subnets by default; cross-subnet discovery needs IGMP snooping or multicast routing on the switch.</p></div></div></div>
    </div>

