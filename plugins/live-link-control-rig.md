---
layout: default
title: 实时链接控制装置 / Live Link Control Rig
---

<h1>实时链接控制装置 / Live Link Control Rig</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/LiveLinkControlRig/LiveLinkControlRig.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LiveLinkControlRig</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Live Link Control Rig</code>（模块 <code class="usage-code">LiveLinkControlRig</code>）。</li><li>把 Live Link 的实时数据接到 Control Rig，驱动绑定图里的 FK/IK 与空间切换。</li><li>在 Sequencer 或运行时用 Control Rig 节点消费 Live Link 主体数据（如动捕/面捕）。</li><li>Experimental：接口可能变动；依赖 Control Rig 与 Live Link 已启用。</li></ol><p class="usage-note">把 Live Link 实时数据驱动到 Control Rig，实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Live Link Control Rig</code> (module <code class="usage-code">LiveLinkControlRig</code>).</li><li>Feed Live Link real-time data into a Control Rig to drive FK/IK and space switching in the rig graph.</li><li>Consume Live Link subject data (mocap/facial) via Control Rig nodes in Sequencer or at runtime.</li><li>Experimental: contract may change; relies on Control Rig and Live Link being enabled.</li></ol><p class="usage-note">Drives Control Rig from Live Link data, experimental.</p></div></div></div>
    </div>

