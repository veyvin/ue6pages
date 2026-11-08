---
layout: default
title: 仅 Linux 编译器集成 / Linux Compiler-only Integration
---

<h1>仅 Linux 编译器集成 / Linux Compiler-only Integration</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/NullSourceCodeAccess/NullSourceCodeAccess.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编程</div><div class="lang-content">Programming</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">火蜥蜴</div><div class="lang-content">Salamanderrake</div></div></span></li><li><span class="label">模块</span><span class="value">NullSourceCodeAccess</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">Linux Compiler-only Integration</code>（模块 <code class="usage-code">NullSourceCodeAccess</code>）并重启。</li><li>它在 Linux 上只查找 clang++、不绑定具体 IDE，用于仅编译的源码访问场景。</li><li>在 <code class="usage-code">Project Settings &gt; Source Code Access</code> 里选择它，用外部命令/脚本编译。</li><li>这是编辑器开发者工具，只进 Editor Target。</li></ol><p class="usage-note">Linux 上只找 clang++ 的源码访问集成，无 IDE 绑定。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">Linux Compiler-only Integration</code> (module <code class="usage-code">NullSourceCodeAccess</code>) and restart.</li><li>On Linux it only looks for clang++ and binds no IDE, for compile-only source access.</li><li>Pick it in <code class="usage-code">Project Settings &gt; Source Code Access</code> and build via external commands/scripts.</li><li>It is an editor developer tool for Editor targets only.</li></ol><p class="usage-note">A compile-only source-access integration on Linux that only looks for clang++, no IDE binding.</p></div></div></div>
    </div>

