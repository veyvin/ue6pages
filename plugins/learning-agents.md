---
layout: default
title: 学习代理 / Learning Agents
---

<h1>学习代理 / Learning Agents</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/LearningAgents/LearningAgents.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.2</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">人工智能</div><div class="lang-content">AI</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LearningAgents, LearningAgentsTraining, LearningAgentsTrainingEditor, LearningAgentsReplay</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Learning Agents</code>（模块 <code class="usage-code">LearningAgents</code>、<code class="usage-code">LearningAgentsTraining</code>、<code class="usage-code">LearningAgentsReplay</code>，编辑器 <code class="usage-code">LearningAgentsTrainingEditor</code>）。</li><li>它用于游戏中 AI 角色控制的机器学习（强化学习/模仿学习）。</li><li>定义观察、动作、奖励，训练策略（可在编辑器里跑训练），再把学到的策略用于 NPC。</li><li>Experimental：接口可能变动；训练模块不进 Shipping，运行时用推理模块。</li></ol><p class="usage-note">面向 AI 角色的机器学习库（RL/模仿学习），实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Learning Agents</code> (modules <code class="usage-code">LearningAgents</code>, <code class="usage-code">LearningAgentsTraining</code>, <code class="usage-code">LearningAgentsReplay</code>, editor <code class="usage-code">LearningAgentsTrainingEditor</code>).</li><li>It provides machine learning for AI character control (reinforcement/imitation learning).</li><li>Define observations, actions, and rewards, train a policy (editor training), and use the learned policy on NPCs.</li><li>Experimental: contract may change; training modules do not ship, use the runtime inference modules.</li></ol><p class="usage-note">A machine-learning library for AI character control (RL/imitation), experimental.</p></div></div></div>
    </div>

