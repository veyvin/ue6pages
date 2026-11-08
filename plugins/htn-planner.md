---
layout: default
title: HTN规划师 / HTN planner
---

<h1>HTN规划师 / HTN planner</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/AI/HTNPlanner/HTNPlanner.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.01</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">人工智能</div><div class="lang-content">AI</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">HTNPlanner, HTNTestSuite</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">HTN planner</code>（模块 <code class="usage-code">HTNPlanner</code>，测试 <code class="usage-code">HTNTestSuite</code>）。</li><li>用分层任务网络（HTN）描述 AI 任务分解，规划出可执行的任务序列。</li><li>把 HTNPlanner 接入 AI 行为/控制器，由它规划并驱动 NPC 行为。</li><li>Experimental：接口可能变动；测试模块不要进游戏包。</li></ol><p class="usage-note">分层任务网络规划器（实验性 AI），与行为树/StateTree 是不同范式。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">HTN planner</code> (module <code class="usage-code">HTNPlanner</code>; tests <code class="usage-code">HTNTestSuite</code>).</li><li>Describe AI task decomposition with Hierarchical Task Networks (HTN) to plan executable task sequences.</li><li>Wire HTNPlanner into AI behavior/controllers so it plans and drives NPC behavior.</li><li>Experimental: contract may change; keep the test module out of the cooked game.</li></ol><p class="usage-note">A Hierarchical Task Network planner (experimental AI), a different paradigm from Behavior Trees/StateTree.</p></div></div></div>
    </div>

