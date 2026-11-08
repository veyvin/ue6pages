---
layout: default
title: 数据驱动的控制台变量 / Data-Driven Console Variables
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Data-Driven Console Variables</div>
      <div class="hero-title-cn">数据驱动的控制台变量 · 在编辑器的数据资产中定义控制台变量（名称、类型、默认值）。新变量</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Programming</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/DataDrivenConsoleVariables/DataDrivenConsoleVariables.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">在编辑器的数据资产中定义控制台变量（名称、类型、默认值）。新变量在游戏启动时注册到控制台，并在编辑器中实时更新，无需重新启动。</div><div class="lang-content">Define console variables (name, type, default value) in Data Assets in the editor. New variables are registered with the console at game startup and live-update in the editor with no restart.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：在编辑器的数据资产中定义控制台变量（名称、类型、默认值）。新变量在游戏启动时注册到控制台，并在编辑器中实时更新，无需重新启动。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：DataDrivenConsoleVariables, DataDrivenConsoleVariablesEditor, DataDrivenConsoleVariablesTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Define console variables (name, type, default value) in Data Assets in the editor. New variables are registered with the console at game startup and live-update in the editor with no restart.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: DataDrivenConsoleVariables, DataDrivenConsoleVariablesEditor, DataDrivenConsoleVariablesTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Data-Driven Console Variables</code>（<code class="usage-code">DataDrivenConsoleVariables</code> + <code class="usage-code">DataDrivenConsoleVariablesEditor</code>）。</li><li>打开 <code class="usage-code">Project Settings</code> 里与 Data Driven CVars 相关的页（<code class="usage-code">UDataDrivenConsoleVariableSettings</code>），在数组中新增一项：<code class="usage-code">Name</code>（如 <code class="usage-code">ddc.Weapon.Recoil</code>）、<code class="usage-code">Type</code>（Bool/Int/Float/String）、Default、Tooltip。</li><li>不必重启编辑器：保存设置后按 `<code class="usage-code"> </code> `` 打开控制台，输入该名字应能自动完成并改值。</li><li>C++ 用 <code class="usage-code">IConsoleManager::Get().FindConsoleVariable(TEXT(&quot;ddc.Weapon.Recoil&quot;))</code> 读 <code class="usage-code">GetFloat</code>/<code class="usage-code">GetInt</code>/<code class="usage-code">GetBool</code>；蓝图可用 <code class="usage-code">Execute Console Command</code> 做调试，正式逻辑走 CVar 指针。</li><li>PIE 中改控制台值应立刻反映；把资产/设置一起提交，让其他机器启动时 <code class="usage-code">DataDrivenConsoleVariables</code> 重新注册同名变量。</li><li><code class="usage-code">DataDrivenConsoleVariablesEditor</code> 和 <code class="usage-code">DataDrivenConsoleVariablesTests</code> 不要进 Game Target；自动化可在 Session Frontend 筛 <code class="usage-code">DataDrivenConsoleVariables</code>。</li></ol><p class="usage-note">用数据资产注册 CVar，免改 C++ 再编译；游戏启动时注册，编辑器可热更新。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Data-Driven Console Variables</code> (<code class="usage-code">DataDrivenConsoleVariables</code> + <code class="usage-code">DataDrivenConsoleVariablesEditor</code>).</li><li>Open the Data Driven CVars page in <code class="usage-code">Project Settings</code> (<code class="usage-code">UDataDrivenConsoleVariableSettings</code>) and add a row: <code class="usage-code">Name</code> (e.g. <code class="usage-code">ddc.Weapon.Recoil</code>), <code class="usage-code">Type</code> (Bool/Int/Float/String), default, tooltip.</li><li>No editor restart: after saving, open the console with `<code class="usage-code"> </code> `` — the name should autocomplete and accept new values.</li><li>In C++ read <code class="usage-code">IConsoleManager::Get().FindConsoleVariable(TEXT(&quot;ddc.Weapon.Recoil&quot;))</code> via <code class="usage-code">GetFloat</code>/<code class="usage-code">GetInt</code>/<code class="usage-code">GetBool</code>. Blueprints may <code class="usage-code">Execute Console Command</code> for debug; shipping logic should use the CVar pointer.</li><li>Changing the value in PIE should apply immediately. Check in the settings asset so other machines re-register the same names at startup.</li><li>Keep <code class="usage-code">DataDrivenConsoleVariablesEditor</code> and <code class="usage-code">DataDrivenConsoleVariablesTests</code> off Game targets; run tests from Session Frontend filtered to <code class="usage-code">DataDrivenConsoleVariables</code>.</li></ol><p class="usage-note">Register CVars from data, no C++ rebuild; registered at game start, live-updated in editor.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">DataDrivenConsoleVariables</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataDrivenConsoleVariablesEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataDrivenConsoleVariablesTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/DataDrivenConsoleVariables/DataDrivenConsoleVariables.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
