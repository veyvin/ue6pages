---
layout: default
title: 混沌可组合求解器 / Chaos Composable Solver
---

<h1>混沌可组合求解器 / Chaos Composable Solver</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/ChaosComposableSolver/ChaosComposableSolver.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosComposableSolver</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Chaos Composable Solver</code>。</li><li>在需要组合多种 Chaos 求解（刚体/布料/可变形）的关卡或系统里，按插件文档把 composable solver 接到现有 Chaos 场景，而不是再放一个独立 Physics Scene。</li><li>先在空关卡验证求解顺序与稳定性，再进正式内容。</li><li>接口可能随夜构建变化，不要写死未文档化的内部类型。</li></ol><p class="usage-note">Experimental 组合求解器，不是默认世界里的 Chaos 场景替换开关。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Chaos Composable Solver</code>.</li><li>Wire the composable solver into the existing Chaos scene when you must combine rigid/cloth/deformable solves; do not spawn a second physics scene.</li><li>Prove solver order and stability in an empty map before production content.</li><li>The contract can change on nightlies; do not freeze undocumented internal types.</li></ol><p class="usage-note">Experimental composable solver, not a drop-in replacement toggle for the default Chaos world.</p></div></div></div>
    </div>

