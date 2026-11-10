---
layout: default
title: 虚幻控制台运行时 / UnrealConsole Runtime
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">UnrealConsole Runtime</div>
      <div class="hero-title-cn">虚幻控制台运行时 · 共享 UnrealConsole 启动尾部和运行模式调度。运行时</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Programs</span><span class="chip">Epic Games</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/UnrealConsoleRuntime/UnrealConsoleRuntime.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">共享 UnrealConsole 启动尾部和运行模式调度。运行时由 UnrealEditor.exe -unrealconsole 加载并静态链接到 UnrealConsole.exe。</div><div class="lang-content">Shared UnrealConsole startup tail and run-mode dispatch. Runtime-loaded by UnrealEditor.exe -unrealconsole and statically linked into UnrealConsole.exe.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：共享 UnrealConsole 启动尾部和运行模式调度。运行时由 UnrealEditor.exe -unrealconsole 加载并静态链接到 UnrealConsole.exe。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：UnrealConsoleRuntime。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Shared UnrealConsole startup tail and run-mode dispatch. Runtime-loaded by UnrealEditor.exe -unrealconsole and statically linked into UnrealConsole.exe.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: UnrealConsoleRuntime. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">UnrealConsole Runtime</code>（模块 <code class="usage-code">UnrealConsoleRuntime</code>），属 Programs。</li><li>它提供共享的 UnrealConsole 启动尾部与运行模式调度；由 <code class="usage-code">UnrealEditor.exe -unrealconsole</code> 加载并静态链接到 <code class="usage-code">UnrealConsole.exe</code>。</li><li>通过 <code class="usage-code">-unrealconsole</code> 启动控制台运行模式。</li><li>属程序/工具运行时；配合 UnrealConsole 可执行文件。</li></ol><p class="usage-note">UnrealConsole 启动尾部与运行模式调度的运行时。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">UnrealConsole Runtime</code> (module <code class="usage-code">UnrealConsoleRuntime</code>), under Programs.</li><li>It provides the shared UnrealConsole launch tail and run-mode dispatch; loaded by <code class="usage-code">UnrealEditor.exe -unrealconsole</code> and statically linked into <code class="usage-code">UnrealConsole.exe</code>.</li><li>Launch console run-mode via <code class="usage-code">-unrealconsole</code>.</li><li>It is a program/tool runtime; used with the UnrealConsole executable.</li></ol><p class="usage-note">The runtime for UnrealConsole launch tail and run-mode dispatch.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealConsoleRuntime</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/UnrealConsoleRuntime/UnrealConsoleRuntime.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
