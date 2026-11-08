---
layout: default
title: 远程会话 / RemoteSession
---

<h1>远程会话 / RemoteSession</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/RemoteSession/RemoteSession.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">实验性的</div><div class="lang-content">Experimental</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">RemoteSession, RemoteSessionEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">RemoteSession</code>（运行时 <code class="usage-code">RemoteSession</code>，编辑器 <code class="usage-code">RemoteSessionEditor</code>）。</li><li>它让一个引擎实例充当第二个实例的瘦客户端（渲染画面 + 回传输入）。</li><li>一台跑完整游戏，另一台只显示/操作，用于远程预览或设备协同。</li><li>属实验性远程会话；接口可能随版本变化。</li></ol><p class="usage-note">一个实例当瘦客户端，显示并操作另一个实例。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">RemoteSession</code> (runtime <code class="usage-code">RemoteSession</code>, editor <code class="usage-code">RemoteSessionEditor</code>).</li><li>It lets one engine instance act as a thin client (rendering and input) to a second instance.</li><li>Run the full game on one machine and display/control from another for remote preview or device pairing.</li><li>It is an experimental remote-session plugin; the contract may change across versions.</li></ol><p class="usage-note">One instance as a thin client (video + input) to another.</p></div></div></div>
    </div>

