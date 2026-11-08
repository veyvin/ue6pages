---
layout: default
title: 自动化控制器 RPC 组件 / Automation Controller RPC Component
---

<h1>自动化控制器 RPC 组件 / Automation Controller RPC Component</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/AutomationControllerRpc/AutomationControllerRpc.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">测试</div><div class="lang-content">Testing</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">AutomationControllerRpc</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Automation Controller RPC Component</code>（模块 <code class="usage-code">AutomationControllerRpc</code>）。</li><li>在要远程跑测试的编辑器或游戏实例上加载该模块，使 <code class="usage-code">AutomationController</code> 能通过 RPC 接收“运行已注册测试”的请求。</li><li>用 <code class="usage-code">Tools &gt; Session Frontend</code> 连到该实例（或你的 RPC 客户端），列出并启动已注册的 Automation 用例。</li><li>确认请求走 RPC/消息通道到达 Controller，而不是在本地进程内直接点 Run；设备/从进程上应看到同样的测试开始。</li><li>这是测试编排通道，不要当 Enhanced Input 或 OpenXR 组件。游戏 Shipping 包不要依赖 <code class="usage-code">AutomationControllerRpc</code>。</li></ol><p class="usage-note">让 Automation Controller 经 RPC 远程跑已注册测试，不是输入或 XR 插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Automation Controller RPC Component</code> (module <code class="usage-code">AutomationControllerRpc</code>).</li><li>Load it on the editor or game instance that should run tests remotely so <code class="usage-code">AutomationController</code> can accept RPCs to execute registered tests.</li><li>Connect <code class="usage-code">Tools &gt; Session Frontend</code> (or your RPC client) to that instance, list registered automation cases, and start them.</li><li>Confirm the request reaches the controller over RPC/messaging, not a local in-process Run; the device/worker should start the same tests.</li><li>This is a test-orchestration channel, not Enhanced Input or OpenXR. Do not depend on <code class="usage-code">AutomationControllerRpc</code> in shipping games.</li></ol><p class="usage-note">Lets Automation Controller run registered tests over RPC; not an input or XR plugin.</p></div></div></div>
    </div>

