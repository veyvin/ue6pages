---
layout: default
title: 游戏捕获接口 / Gameplay Capture Interfaces
---

<h1>游戏捕获接口 / Gameplay Capture Interfaces</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/GameplayCaptureInterfaces/GameplayCaptureInterfaces.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GameplayCaptureInterfaces</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Gameplay Capture Interfaces</code>（模块 <code class="usage-code">GameplayCaptureInterfaces</code>）。</li><li>这是一个共享接口层：只有在编写 GameplayCapture 相关插件、需要与其互操作时才依赖它。</li><li>在模块 <code class="usage-code">Build.cs</code> 里依赖 <code class="usage-code">GameplayCaptureInterfaces</code>，实现/引用其中的接口，避免各 Capture 插件互相直接依赖。</li><li>普通玩法内容一般不直接用；Experimental，接口可能随夜构建变化。</li></ol><p class="usage-note">面向插件作者的共享接口，不是可放置的 Gameplay 组件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Gameplay Capture Interfaces</code> (module <code class="usage-code">GameplayCaptureInterfaces</code>).</li><li>This is a shared interface layer: depend on it only when writing GameplayCapture-related plugins that must interoperate.</li><li>Add <code class="usage-code">GameplayCaptureInterfaces</code> to your module <code class="usage-code">Build.cs</code> and implement/reference its interfaces so capture plugins avoid depending on each other directly.</li><li>Normal gameplay content rarely touches it; it is Experimental and may change on nightlies.</li></ol><p class="usage-note">A shared interface for plugin authors, not a placeable gameplay component.</p></div></div></div>
    </div>

