---
layout: default
title: 代码编辑器 / Code Editor
---

<h1>代码编辑器 / Code Editor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/CodeEditor/CodeEditor.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编程</div><div class="lang-content">Programming</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">CodeEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental <code class="usage-code">Code Editor</code>（模块 <code class="usage-code">CodeEditor</code>）并重启；这是编辑器内嵌代码编辑，不是游戏组件。</li><li>从 <code class="usage-code">Window</code> / <code class="usage-code">Tools</code> 打开 <code class="usage-code">Code Editor</code> 面板（或从 C++ 类资产“在编辑器中打开”）。</li><li>在面板中打开项目 <code class="usage-code">.h</code> / <code class="usage-code">.cpp</code>，修改后保存到磁盘；不要指望它替代 Rider/VS 的调试与 IntelliSense。</li><li>保存后用 Live Coding 或编译按钮验证；语法错误仍走虚幻编译日志。</li><li>不要把 <code class="usage-code">CodeEditor</code> 写进 Game <code class="usage-code">Build.cs</code> 或 Shipping。</li></ol><p class="usage-note">实验性编辑器内代码编辑，接口可能变化；不能当正式 IDE。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Code Editor</code> (module <code class="usage-code">CodeEditor</code>) and restart. It edits source inside Unreal, not as a gameplay component.</li><li>Open the <code class="usage-code">Code Editor</code> panel from <code class="usage-code">Window</code> / <code class="usage-code">Tools</code> (or “open in editor” on a C++ class asset).</li><li>Load project <code class="usage-code">.h</code> / <code class="usage-code">.cpp</code> files, edit, and save to disk. It does not replace Rider/VS debugging or IntelliSense.</li><li>After save, Live Coding or compile and watch the Unreal build log for errors.</li><li>Do not add <code class="usage-code">CodeEditor</code> to a Game <code class="usage-code">Build.cs</code> or Shipping target.</li></ol><p class="usage-note">Experimental in-editor code editing; not a production IDE, API may change.</p></div></div></div>
    </div>

