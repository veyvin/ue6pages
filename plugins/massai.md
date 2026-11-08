---
layout: default
title: 马萨诸塞州人工智能 / MassAI
---

<h1>马萨诸塞州人工智能 / MassAI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/AI/MassAI/MassAI.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.4</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">人工智能</div><div class="lang-content">AI</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MassNavigation, MassNavMeshNavigation, MassZoneGraphNavigation, MassNavigationEditor, MassAIBehavior, MassAIBehaviorEditor, MassAIReplication, MassAIDebug, MassAITestSuite</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MassAI</code>（模块 <code class="usage-code">MassNavigation</code>、<code class="usage-code">MassNavMeshNavigation</code>、<code class="usage-code">MassZoneGraphNavigation</code>、<code class="usage-code">MassAIBehavior</code>、<code class="usage-code">MassAIReplication</code>、<code class="usage-code">MassAIDebug</code> 等）。</li><li>把 Mass Entity（ECS）用到大规模 AI：用碎片、处理器与 StateTree 驱动成千上万代理，而非每代理一个行为树。</li><li>用 Mass Spawner 生成代理，配导航（NavMesh/ZoneGraph）与行为，适合人群、兵团。</li><li>Game 模块依赖运行时模块；编辑器/调试模块只进 Editor Target。</li></ol><p class="usage-note">Mass Entity(ECS) 的大规模 AI，适合人群/兵团，不是逐 Actor 行为树。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MassAI</code> (modules <code class="usage-code">MassNavigation</code>, <code class="usage-code">MassNavMeshNavigation</code>, <code class="usage-code">MassZoneGraphNavigation</code>, <code class="usage-code">MassAIBehavior</code>, <code class="usage-code">MassAIReplication</code>, <code class="usage-code">MassAIDebug</code>, etc.).</li><li>Apply Mass Entity (ECS) to large-scale AI: drive thousands of agents with fragments, processors, and StateTree instead of a Behavior Tree per actor.</li><li>Spawn agents with Mass Spawner, add navigation (NavMesh/ZoneGraph) and behavior; ideal for crowds and armies.</li><li>Game modules depend on runtime modules; editor/debug modules go to Editor targets only.</li></ol><p class="usage-note">Large-scale AI on Mass Entity (ECS) for crowds/armies, not per-actor Behavior Trees.</p></div></div></div>
    </div>

