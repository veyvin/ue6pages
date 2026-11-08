---
layout: default
title: 搬运工 / Mover
---

<h1>搬运工 / Mover</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Mover/Mover.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">Mover, MoverCVDData, MoverEditor, MoverCVDEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Mover</code>（运行时 <code class="usage-code">Mover</code>、<code class="usage-code">MoverCVDData</code>，编辑器 <code class="usage-code">MoverEditor</code>、<code class="usage-code">MoverCVDEditor</code>）。</li><li>它用于在回滚网络（rollback networking）下支持 Actor 的移动（类似预测/回滚的运动系统）。</li><li>用 Mover Component 配置移动模式，联网项目在预测/回滚下同步移动。</li><li>Experimental：接口可能变动；参考 README 了解概念与已知问题。</li></ol><p class="usage-note">回滚网络下的 Actor 移动系统（Mover），实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Mover</code> (runtime <code class="usage-code">Mover</code>, <code class="usage-code">MoverCVDData</code>, editor <code class="usage-code">MoverEditor</code>, <code class="usage-code">MoverCVDEditor</code>).</li><li>It supports actor movement with rollback networking (a prediction/rollback movement system).</li><li>Configure movement modes via the Mover Component; net projects sync movement under prediction/rollback.</li><li>Experimental: contract may change; see the README for concepts and known issues.</li></ol><p class="usage-note">An actor movement system with rollback networking (Mover), experimental.</p></div></div></div>
    </div>

