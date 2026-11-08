---
layout: default
title: 碰撞诊断工具集 / CrashDiagnosticsToolset
---

<h1>碰撞诊断工具集 / CrashDiagnosticsToolset</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Toolsets/CrashDiagnosticsToolset/CrashDiagnosticsToolset.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">实验性的</div><div class="lang-content">Experimental</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">CrashDiagnosticsToolset</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">CrashDiagnosticsToolset</code>（模块 <code class="usage-code">CrashDiagnosticsToolset</code>），并确保引擎 <code class="usage-code">CrashDiagnostics</code> 正在记录编辑器崩溃会话。</li><li>复现一次可捕获的编辑器崩溃或读已有崩溃记录目录；没有记录时助手查无可查。</li><li>打开编辑器 AI 助手，询问「解释最近一次 CrashDiagnostics 记录」：Toolset 提供读记录、列调用栈/上下文的工具，而不是新的 Crash Reporter 窗口。</li><li>对照助手给出的模块与调用栈，回到自己的 C++/插件改代码；需要原始转储仍用 Crash Reporter / 本机 dump。</li><li>仅编辑器自动化依赖本模块，禁止打进 Shipping 游戏。</li></ol><p class="usage-note">让 AI 读 CrashDiagnostics 会话，不是替代 Crash Reporter。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">CrashDiagnosticsToolset</code> (module <code class="usage-code">CrashDiagnosticsToolset</code>) and confirm engine <code class="usage-code">CrashDiagnostics</code> is recording editor crash sessions.</li><li>Reproduce a capturable editor crash or point at an existing session folder; with no recordings the assistant has nothing to read.</li><li>Ask the in-editor AI to explain the latest CrashDiagnostics recording. The Toolset exposes read/list stack/context tools — it is not a new Crash Reporter window.</li><li>Use the named module/stack to fix your C++/plugin. Raw dumps still go through Crash Reporter / local dump files.</li><li>Editor automation only — never ship in a game build.</li></ol><p class="usage-note">Lets AI read CrashDiagnostics sessions; it does not replace Crash Reporter.</p></div></div></div>
    </div>

