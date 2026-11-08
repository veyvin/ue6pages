---
layout: default
title: MakeCookedEditorAsDLC / MakeCookedEditorAsDLC
---

<h1>MakeCookedEditorAsDLC / MakeCookedEditorAsDLC</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Editor/MakeCookedEditorAsDLC/MakeCookedEditorAsDLC.uplugin</code></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">MakeCookedEditorAsDLC</code> 与 <code class="usage-code">MakeCookedEditor</code> UAT 脚本配合，把熟编辑器生成为熟客户端的 DLC 附加组件。</li><li>它不需要手动启用；通过命令行/UAT 脚本使用。</li><li>在构建流水线里运行对应 UAT 命令生成编辑器 DLC 包。</li><li>这是构建工具辅助插件（无运行时模块），不进 Shipping。</li></ol><p class="usage-note">配合 MakeCookedEditor UAT 生成编辑器 DLC，构建期用、无需启用。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">MakeCookedEditorAsDLC</code> works with the <code class="usage-code">MakeCookedEditor</code> UAT script to generate a cooked editor as a DLC add-on to a cooked client.</li><li>It is not meant to be enabled by hand; use it through the command line/UAT script.</li><li>Run the corresponding UAT command in your build pipeline to produce the editor DLC package.</li><li>It is a build-tool helper plugin (no runtime modules) and does not ship.</li></ol><p class="usage-note">Works with the MakeCookedEditor UAT script to build an editor DLC; build-time, no need to enable.</p></div></div></div>
    </div>

