---
layout: default
title: 机器学习适配器 / ML Adapter
---

<h1>机器学习适配器 / ML Adapter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/AI/MLAdapter/MLAdapter.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">人工智能</div><div class="lang-content">AI</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MLAdapter, MLAdapterTestSuite</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ML Adapter</code>（模块 <code class="usage-code">MLAdapter</code>，测试 <code class="usage-code">MLAdapterTestSuite</code>）。</li><li>它是在游戏中训练和使用机器学习代理的框架：提供 RPC 接口，外部进程可查询游戏状态并控制 Actor。</li><li>训练后，代理可通过从 ONNX 模型加载的神经网络在引擎内运行。</li><li>Game 模块依赖 <code class="usage-code">MLAdapter</code>；测试模块不进游戏包。</li></ol><p class="usage-note">游戏内 ML 代理训练/使用框架（RPC + ONNX 推理）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ML Adapter</code> (module <code class="usage-code">MLAdapter</code>, tests <code class="usage-code">MLAdapterTestSuite</code>).</li><li>It is a framework for training and using ML agents in games: an RPC interface lets an external process query game state and control actors.</li><li>After training, agents can run in-engine via a neural network loaded from an ONNX model.</li><li>Game modules depend on <code class="usage-code">MLAdapter</code>; keep the test module out of the cooked game.</li></ol><p class="usage-note">A framework for training/using ML agents in games (RPC + ONNX inference).</p></div></div></div>
    </div>

