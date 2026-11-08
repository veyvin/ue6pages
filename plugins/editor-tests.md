---
layout: default
title: 编辑器测试 / Editor Tests
---

<h1>编辑器测试 / Editor Tests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Tests/EditorTests/EditorTests.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">测试</div><div class="lang-content">Testing</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">EditorTests</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Editor Tests</code> 插件并重启。</li><li>打开 <code class="usage-code">Tools &gt; Session Frontend</code>（或 <code class="usage-code">Window &gt; Developer Tools &gt; Session Frontend</code>）的 Automation 标签。</li><li>勾选 <code class="usage-code">Editor</code> 相关测试集，点 <code class="usage-code">Start Tests</code>。</li><li>查看结果面板，定位失败用例并对照日志排查。</li><li>CI 场景改用命令行：<code class="usage-code">UnrealEditor-Cmd.exe YourProject.uproject -ExecCmds=&quot;Automation RunTests Editor; Quit&quot;</code>。</li></ol><p class="usage-note">这是自动化测试插件，价值在于跑 `Editor` 测试集并看报告，而不是拖进关卡；在 Session Frontend / 命令行里执行。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Editor Tests</code> and restart.</li><li>Open the Automation tab in <code class="usage-code">Tools &gt; Session Frontend</code> (or <code class="usage-code">Window &gt; Developer Tools &gt; Session Frontend</code>).</li><li>Tick the <code class="usage-code">Editor</code> test set and click <code class="usage-code">Start Tests</code>.</li><li>Review the results panel, locate failing cases, and inspect the logs.</li><li>For CI, run the command line instead: <code class="usage-code">UnrealEditor-Cmd.exe YourProject.uproject -ExecCmds=&quot;Automation RunTests Editor; Quit&quot;</code>.</li></ol><p class="usage-note">It is an automation-testing plugin — its value is running the `Editor` test set and reading the report, not dragging into a level; execute via Session Frontend or the command line.</p></div></div></div>
    </div>

