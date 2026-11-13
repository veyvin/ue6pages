---
layout: default
title: 增强的输入代码质量虚幻测试插件 / Enhanced Input Code Quality Unreal Test Plugin
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Enhanced Input Code Quality Unreal Test Plugin</div>
      <div class="hero-title-cn">增强的输入代码质量虚幻测试插件 · 虚幻引擎增强输入的简化测试</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/CQTestEnhancedInput/CQTestEnhancedInput.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">虚幻引擎增强输入的简化测试</div><div class="lang-content">Simplified testing of the Enhanced Input for Unreal Engine</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Enhanced Input 替代旧的轴/动作映射：Input Action + Input Mapping Context，支持触发器、修饰符、按键和弦，以及运行时切换上下文（步行/开车/UI）。新项目应优先用它而不是 DefaultInput.ini 里的老绑定。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CQTestEnhancedInput, CQTestEnhancedInputTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine</a></p></div><div class="lang-content"><p>Enhanced Input replaces old axis/action mappings with Input Actions and Mapping Contexts, plus triggers, modifiers, chords, and runtime context swaps (walk / drive / UI). New projects should use it instead of legacy DefaultInput.ini bindings.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CQTestEnhancedInput, CQTestEnhancedInputTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>这是 Enhanced Input 的自动化测试插件（模块 <code class="usage-code">CQTestEnhancedInput</code> / <code class="usage-code">CQTestEnhancedInputTests</code>），服务引擎 QA/CI 回归，不是游戏玩法功能。</li><li>在编辑器或命令行构建里把 <code class="usage-code">CQTestEnhancedInput</code> 编译进来（不要放进对外发布的游戏目标）。</li><li>打开 <code class="usage-code">Session Frontend &gt; Automation</code>，在过滤器里搜 <code class="usage-code">CQTestEnhancedInput</code> 找到用例。</li><li>勾选后点 <code class="usage-code">Start Tests</code> 运行，查看通过/失败与日志。</li><li>批量跑用命令行 <code class="usage-code">-ExecCmds=&quot;Automation RunTests CQTestEnhancedInput&quot;</code>。</li></ol><p class="usage-note">它验证 Enhanced Input 的行为，不提供你在项目里调用的 API；读它的测试源码能学到 EI 的正确用法。</p></div><div class="lang-content"><ol class="usage-steps"><li>This is an Enhanced Input automation-test plugin (<code class="usage-code">CQTestEnhancedInput</code> / <code class="usage-code">CQTestEnhancedInputTests</code>) for engine QA/CI regression, not a gameplay feature.</li><li>Compile <code class="usage-code">CQTestEnhancedInput</code> into an editor or command-line build (never into a shipping game target).</li><li>Open <code class="usage-code">Session Frontend &gt; Automation</code> and filter for <code class="usage-code">CQTestEnhancedInput</code> to locate the cases.</li><li>Select them and click <code class="usage-code">Start Tests</code>, then read pass/fail and logs.</li><li>Batch-run from the command line with <code class="usage-code">-ExecCmds=&quot;Automation RunTests CQTestEnhancedInput&quot;</code>.</li></ol><p class="usage-note">It validates Enhanced Input behavior and exposes no API you call in a project; its test sources are a good reference for correct EI usage.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">CQTestEnhancedInput</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CQTestEnhancedInputTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/CQTestEnhancedInput/CQTestEnhancedInput.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
