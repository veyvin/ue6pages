---
layout: default
title: 状态树 / StateTree
---

<h1>状态树 / StateTree</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/StateTree/StateTree.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">StateTreeModule, StateTreeTestSuite, StateTreeDeveloper, StateTreeEditorModule</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">StateTree</code>（运行时 <code class="usage-code">StateTreeModule</code>，编辑器 <code class="usage-code">StateTreeEditorModule</code>，测试 <code class="usage-code">StateTreeTestSuite</code>、<code class="usage-code">StateTreeDeveloper</code>）。</li><li>它是通用分层状态机运行时（状态树：状态、任务、条件、评估器）。</li><li>用 StateTree 资产搭建 AI/玩法逻辑，运行时按条件在状态间切换。</li><li>Game 模块依赖运行时模块；编辑器/测试模块只进 Editor Target。</li></ol><p class="usage-note">通用分层状态机运行时（StateTree）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">StateTree</code> (runtime <code class="usage-code">StateTreeModule</code>, editor <code class="usage-code">StateTreeEditorModule</code>, tests <code class="usage-code">StateTreeTestSuite</code>, <code class="usage-code">StateTreeDeveloper</code>).</li><li>It is a general hierarchical state-machine runtime (state tree: states, tasks, conditions, evaluators).</li><li>Build AI/gameplay logic in StateTree assets that switch states by conditions at runtime.</li><li>Game modules depend on runtime modules; editor/test modules go to Editor targets only.</li></ol><p class="usage-note">A general hierarchical state-machine runtime (StateTree).</p></div></div></div>
    </div>

