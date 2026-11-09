---
layout: default
title: Verse 游戏调试 / Verse Gameplay Debug
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">V</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Verse Gameplay Debug</div>
      <div class="hero-title-cn">Verse 游戏调试 · Verse 游戏调试 API</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Verse</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Verse/VerseGameplayDebug/VerseGameplayDebug.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Verse 游戏调试 API</div><div class="lang-content">Verse Gameplay Debug API</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Verse 是面向 UEFN / Fortnite 体验的脚本语言与运行时。这组插件提供编译、虚拟机、设备 API 与编辑器集成，不是传统蓝图游戏的必选项。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：VerseGameplayDebug。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Verse is the scripting language and runtime for UEFN / Fortnite experiences. These plugins provide the compiler, VM, device APIs, and editor integration — not required for classic Blueprint games.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: VerseGameplayDebug. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Verse Gameplay Debug</code>（模块 <code class="usage-code">VerseGameplayDebug</code>）。</li><li>它提供 Verse 游戏调试 API（输出/可视化 Verse 游戏逻辑状态）。</li><li>在 Verse 项目里用其 API 调试游戏行为。</li><li>属 Verse 生态调试模块。</li></ol><p class="usage-note">Verse 游戏调试 API。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Verse Gameplay Debug</code> (module <code class="usage-code">VerseGameplayDebug</code>).</li><li>It provides a Verse gameplay debug API (output/visualize Verse gameplay logic state).</li><li>Use its API to debug gameplay behavior in Verse projects.</li><li>It is a Verse-ecosystem debug module.</li></ol><p class="usage-note">A Verse gameplay debug API.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">VerseGameplayDebug</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Verse/VerseGameplayDebug/VerseGameplayDebug.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
