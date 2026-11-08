---
layout: default
title: 编辑表现 / Editor Performance
---

<h1>编辑表现 / Editor Performance</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/EditorPerformance/EditorPerformance.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">表现</div><div class="lang-content">Performance</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">EditorPerformance, StallLogSubsystem, CrashDiagnostics</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Editor Performance</code> 插件并重启（Experimental，先在测试项目里用）。</li><li>复现卡顿操作（大关卡 PIE、全量编译、自动保存），让插件记录编辑器 stall。</li><li>通过 <code class="usage-code">StallLogSubsystem</code> 的日志/控制台命令查看 stall 记录，检查 stall 时长与调用栈。</li><li>若触发崩溃，读取 <code class="usage-code">CrashDiagnostics</code> 生成的诊断信息定位崩溃上下文。</li><li>对照热点优化（关掉重型视口实时预览、拆关卡、削减编辑器 tick 负担）。</li><li>复跑同样操作，比较前后 stall 次数确认改善。</li></ol><p class="usage-note">该插件把编辑器性能反馈给开发者，靠 `StallLogSubsystem` 记录卡顿、`CrashDiagnostics` 记录崩溃；Experimental 接口可能变。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Editor Performance</code> and restart (Experimental — try it in a test project first).</li><li>Reproduce the hitch (large-map PIE, full compile, autosave) so the plugin records editor stalls.</li><li>Inspect stall records via <code class="usage-code">StallLogSubsystem</code> logs/console commands, checking stall duration and call stacks.</li><li>If it crashes, read the <code class="usage-code">CrashDiagnostics</code> output to locate the crash context.</li><li>Optimize the hot spots (disable heavy real-time viewport preview, split levels, trim editor tick load).</li><li>Re-run the same operations and compare stall counts before/after to confirm the win.</li></ol><p class="usage-note">It feeds editor performance back to developers via `StallLogSubsystem` for stalls and `CrashDiagnostics` for crashes; Experimental, so the API may change.</p></div></div></div>
    </div>

