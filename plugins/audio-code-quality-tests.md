---
layout: default
title: 音频代码质量测试 / Audio Code Quality Tests
---

<h1>音频代码质量测试 / Audio Code Quality Tests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Tests/AudioCQTests/AudioCQTests.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">测试</div><div class="lang-content">Testing</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">AudioCQTests</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Testing 插件 <code class="usage-code">Audio Code Quality Tests</code>（模块 <code class="usage-code">AudioCQTests</code>）并重启。</li><li>打开 <code class="usage-code">Tools &gt; Session Frontend</code> → <code class="usage-code">Automation</code>。</li><li>筛选 <code class="usage-code">AudioCQTests</code>（树里常见 <code class="usage-code">Product.Plugins.AudioCQTests</code>），勾选用例后点 Start Tests。</li><li>这些是音频引擎的 CQTest/自动化用例，不要去内容浏览器建 Sound Wave 来“使用”它。</li><li>不要把 <code class="usage-code">AudioCQTests</code> 写进游戏 <code class="usage-code">Build.cs</code> 或 Shipping；命令行可用 <code class="usage-code">Automation RunTests AudioCQTests</code>。</li></ol><p class="usage-note">音频代码质量自动化，不是可播放的音频资产包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the Testing plugin <code class="usage-code">Audio Code Quality Tests</code> (module <code class="usage-code">AudioCQTests</code>) and restart.</li><li>Open <code class="usage-code">Tools &gt; Session Frontend</code> → <code class="usage-code">Automation</code>.</li><li>Filter <code class="usage-code">AudioCQTests</code> (often <code class="usage-code">Product.Plugins.AudioCQTests</code>), tick cases, and Start Tests.</li><li>These are CQTest/automation cases for the audio engine — do not create Sound Waves to “use” the plugin.</li><li>Do not add <code class="usage-code">AudioCQTests</code> to a game <code class="usage-code">Build.cs</code> or Shipping; CI can <code class="usage-code">Automation RunTests AudioCQTests</code>.</li></ol><p class="usage-note">Audio engine code-quality automation, not a playable audio content pack.</p></div></div></div>
    </div>

