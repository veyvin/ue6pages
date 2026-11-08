---
layout: default
title: 美元核心 / USD Core
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">USD Core</div>
      <div class="hero-title-cn">美元核心 · 添加了对美元 SDK、UE 包装类和美元转换实用程序的支持</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/USDCore/USDCore.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">添加了对美元 SDK、UE 包装类和美元转换实用程序的支持</div><div class="lang-content">Adds support for USD SDK, UE wrapper classes and USD conversion utilities</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：UnrealUSDWrapper, USDUtilities, USDClasses。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: UnrealUSDWrapper, USDUtilities, USDClasses. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">USD Core</code>（模块 <code class="usage-code">UnrealUSDWrapper</code>、<code class="usage-code">USDUtilities</code>、<code class="usage-code">USDClasses</code>）。</li><li>它添加对 USD SDK、UE 包装类与 USD 转换实用程序的支持。</li><li>作为 USD 插件的底层依赖，提供 USD 类型与转换能力。</li><li>Game 模块依赖运行时模块；供 USD 导入/舞台使用。</li></ol><p class="usage-note">USD SDK/UE 包装类/转换实用程序支持。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">USD Core</code> (modules <code class="usage-code">UnrealUSDWrapper</code>, <code class="usage-code">USDUtilities</code>, <code class="usage-code">USDClasses</code>).</li><li>It adds support for the USD SDK, UE wrapper classes, and USD conversion utilities.</li><li>A low-level dependency for USD plugins, providing USD types and conversion.</li><li>Game modules depend on runtime modules; used by USD import/stage.</li></ol><p class="usage-note">USD SDK support, UE wrappers, and conversion utilities.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealUSDWrapper</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDUtilities</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDClasses</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/USDCore/USDCore.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
