---
layout: default
title: 诗歌测试支持 / Verse Testing Support
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">V</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Verse Testing Support</div>
      <div class="hero-title-cn">诗歌测试支持 · ModularTestFramework 的测试支持和 VNI </div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/ModularTestVerse/ModularTestVerse.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">ModularTestFramework 的测试支持和 VNI 桥。启用 Verse 测试创作。</div><div class="lang-content">Test support and VNI bridge for ModularTestFramework. Enables Verse test authoring.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Verse 是面向 UEFN / Fortnite 体验的脚本语言与运行时。这组插件提供编译、虚拟机、设备 API 与编辑器集成，不是传统蓝图游戏的必选项。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：ModularTestVerse。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Verse is the scripting language and runtime for UEFN / Fortnite experiences. These plugins provide the compiler, VM, device APIs, and editor integration — not required for classic Blueprint games.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: ModularTestVerse. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Verse Testing Support</code>（模块 <code class="usage-code">ModularTestVerse</code>）。</li><li>它是 ModularTestFramework 的测试支持与 VNI 桥，启用 Verse 测试创作。</li><li>在 CI/自动化里用 Modular Test Framework 编写/运行 Verse 测试。</li><li>属测试支撑模块；配合 Modular Test Framework。</li></ol><p class="usage-note">ModularTestFramework 的 Verse 测试支持与 VNI 桥。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Verse Testing Support</code> (module <code class="usage-code">ModularTestVerse</code>).</li><li>It is the ModularTestFramework test support and VNI bridge, enabling Verse test authoring.</li><li>Write/run Verse tests with the Modular Test Framework in CI/automation.</li><li>It is a test-support module; used with the Modular Test Framework.</li></ol><p class="usage-note">Verse test support and VNI bridge for ModularTestFramework.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ModularTestVerse</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/ModularTestVerse/ModularTestVerse.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
