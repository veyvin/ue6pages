---
layout: default
title: UMG 视图模型 / UMG Viewmodel
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">UMG Viewmodel</div>
      <div class="hero-title-cn">UMG 视图模型 · 支持 UMG 中的模型-视图-视图模型模式的插件。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>UI</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ModelViewViewModel/ModelViewViewModel.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持 UMG 中的模型-视图-视图模型模式的插件。</div><div class="lang-content">A plugin to support the Model-View-Viewmodel pattern in UMG.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>UMG（Unreal Motion Graphics）是运行时 UI 模块：Widget Blueprint、UUserWidget、槽与动画。游戏 HUD、菜单几乎都建立在 UMG + Slate 上。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ModelViewViewModel, ModelViewViewModelBlueprint, ModelViewViewModelEditor, ModelViewViewModelDebugger, ModelViewViewModelDebuggerEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>UMG (Unreal Motion Graphics) is the runtime UI module: Widget Blueprints, UUserWidget, slots, and widget animation. Most game HUDs and menus are UMG on top of Slate.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ModelViewViewModel, ModelViewViewModelBlueprint, ModelViewViewModelEditor, ModelViewViewModelDebugger, ModelViewViewModelDebuggerEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">UMG Viewmodel</code>（模块 <code class="usage-code">ModelViewViewModel</code>、<code class="usage-code">ModelViewViewModelBlueprint</code>、<code class="usage-code">ModelViewViewModelDebugger</code>，编辑器 <code class="usage-code">ModelViewViewModelEditor</code>、<code class="usage-code">ModelViewViewModelDebuggerEditor</code>）。</li><li>它支持 UMG 中的模型-视图-视图模型(MVVM)模式（数据驱动 UI）。</li><li>用 ViewModel 把 UI 与逻辑分离，在蓝图里绑定数据。</li><li>Game 模块依赖运行时模块；编辑器/调试器模块只进 Editor Target。</li></ol><p class="usage-note">UMG 的 MVVM（数据驱动 UI）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">UMG Viewmodel</code> (modules <code class="usage-code">ModelViewViewModel</code>, <code class="usage-code">ModelViewViewModelBlueprint</code>, <code class="usage-code">ModelViewViewModelDebugger</code>, editor <code class="usage-code">ModelViewViewModelEditor</code>, <code class="usage-code">ModelViewViewModelDebuggerEditor</code>).</li><li>It supports the Model-View-ViewModel (MVVM) pattern in UMG (data-driven UI).</li><li>Use ViewModels to separate UI from logic and bind data in Blueprint.</li><li>Game modules depend on runtime modules; editor/debugger modules go to Editor targets only.</li></ol><p class="usage-note">MVVM for UMG (data-driven UI).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">ModelViewViewModel</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelViewViewModelBlueprint</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelViewViewModelEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelViewViewModelDebugger</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelViewViewModelDebuggerEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ModelViewViewModel/ModelViewViewModel.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
