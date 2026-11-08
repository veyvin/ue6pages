---
layout: default
title: 运动轨迹 / Motion Trajectory
---

<h1>运动轨迹 / Motion Trajectory</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Animation/MotionTrajectory/MotionTrajectory.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MotionTrajectory</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Motion Trajectory</code>（模块 <code class="usage-code">MotionTrajectory</code>）。</li><li>它生成角色运动的预测并跟踪运动历史（供动画/运动匹配/决策使用）。</li><li>在角色组件上启用轨迹采样，读取预测/历史轨迹数据。</li><li>Experimental：接口可能变动；属动画辅助，运行时模块可进包。</li></ol><p class="usage-note">生成角色运动预测与历史轨迹，实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Motion Trajectory</code> (module <code class="usage-code">MotionTrajectory</code>).</li><li>It generates predictions and tracks history of character motion (for animation/motion matching/decisions).</li><li>Enable trajectory sampling on the character component and read predicted/history trajectory data.</li><li>Experimental: contract may change; it is animation assist, runtime modules can ship.</li></ol><p class="usage-note">Predicts and tracks character motion history, experimental.</p></div></div></div>
    </div>

