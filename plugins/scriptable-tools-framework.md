---
layout: default
title: 脚本化工具框架 / Scriptable Tools Framework
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Scriptable Tools Framework</div>
      <div class="hero-title-cn">脚本化工具框架 · 交互式工具框架的蓝图脚本扩展</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ScriptableToolsFramework/ScriptableToolsFramework.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">交互式工具框架的蓝图脚本扩展</div><div class="lang-content">Blueprint-Scriptable extension to the Interactive Tools Framework</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：交互式工具框架的蓝图脚本扩展</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ScriptableToolsFramework, EditorScriptableToolsFramework。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Blueprint-Scriptable extension to the Interactive Tools Framework</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ScriptableToolsFramework, EditorScriptableToolsFramework. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Scriptable Tools Framework</code>（模块 <code class="usage-code">ScriptableToolsFramework</code>、<code class="usage-code">EditorScriptableToolsFramework</code>）。</li><li>它是 Interactive Tools Framework 的蓝图可脚本扩展。</li><li>用蓝图编写交互工具，再在 Scriptable Tools 编辑器模式里运行。</li><li>运行时框架可进工具；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">Interactive Tools Framework 的蓝图可脚本扩展。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Scriptable Tools Framework</code> (modules <code class="usage-code">ScriptableToolsFramework</code>, <code class="usage-code">EditorScriptableToolsFramework</code>).</li><li>It is a Blueprint-scriptable extension of the Interactive Tools Framework.</li><li>Author interactive tools in Blueprint, then run them in Scriptable Tools editor mode.</li><li>The runtime framework can ship with tools; editor modules are Editor-target only.</li></ol><p class="usage-note">Blueprint-scriptable extension of the Interactive Tools Framework.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">ScriptableToolsFramework</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorScriptableToolsFramework</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ScriptableToolsFramework/ScriptableToolsFramework.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
