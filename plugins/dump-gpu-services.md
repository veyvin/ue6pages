---
layout: default
title: 转储 GPU 服务 / Dump GPU Services
---

<h1>转储 GPU 服务 / Dump GPU Services</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/DumpGPUServices/DumpGPUServices.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DumpGPUServices</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用开发者插件 <code class="usage-code">Dump GPU Services</code>（模块 <code class="usage-code">DumpGPUServices</code>）。它给控制台命令 <code class="usage-code">DumpGPU</code> 提供自动上传，不是后期处理效果。</li><li>在 <code class="usage-code">DefaultEngine.ini</code> 或项目的 DumpGPU 服务配置里填写上传端点/令牌（插件注册的 upload service）。</li><li>复现渲染问题后，在控制台执行 <code class="usage-code">DumpGPU</code>（可带帧数/路径参数），本地会写出 GPU 转储。</li><li>确认 <code class="usage-code">DumpGPUServices</code> 把转储自动传到配置的服务，而不是只停在工程 Saved 目录。</li><li>这是制作/调试管线，不要写进 Game Target，也不要在 Shipping 包保留上传令牌。</li><li>不要在 Post Process Volume 或 Show Flag 里找它——没有画面开关。</li></ol><p class="usage-note">DumpGPU 的自动上传服务，编辑器/开发机使用，不进游戏运行时画面。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the developer plugin <code class="usage-code">Dump GPU Services</code> (module <code class="usage-code">DumpGPUServices</code>). It auto-uploads <code class="usage-code">DumpGPU</code> captures; it is not a post-process effect.</li><li>Set the upload endpoint/token in <code class="usage-code">DefaultEngine.ini</code> or the plugin’s DumpGPU service config.</li><li>After reproducing a rendering bug, run <code class="usage-code">DumpGPU</code> in the console (optional frame/path args) to write a local GPU dump.</li><li>Confirm <code class="usage-code">DumpGPUServices</code> uploads that dump to the configured service instead of leaving it only under Saved.</li><li>Authoring/debug only: keep it off Game targets and never ship upload tokens.</li><li>There is no Post Process Volume or Show Flag for this plugin.</li></ol><p class="usage-note">Automatic upload service for DumpGPU; editor/dev machines only, not a runtime picture setting.</p></div></div></div>
    </div>

