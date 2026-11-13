---
layout: default
title: Storm Sync 运动设计桥 / Storm Sync Motion Design Bridge
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Storm Sync Motion Design Bridge</div>
      <div class="hero-title-cn">Storm Sync 运动设计桥 · Motion Design Plugin 和 Storm Syn</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/StormSyncAvalancheBridge/StormSyncAvalancheBridge.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Motion Design Plugin 和 Storm Sync 之间的插件桥梁，提供编辑器内集成以同步资源</div><div class="lang-content">Plugin bridge between Motion Design Plugin and Storm Sync to provide in-editor integration to synchronize assets</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Motion Design Plugin 和 Storm Sync 之间的插件桥梁，提供编辑器内集成以同步资源</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：StormSyncAvaBridgeEditor, StormSyncAvaBridge。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Plugin bridge between Motion Design Plugin and Storm Sync to provide in-editor integration to synchronize assets</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: StormSyncAvaBridgeEditor, StormSyncAvaBridge. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Storm Sync Motion Design Bridge</code>（运行时 <code class="usage-code">StormSyncAvaBridge</code>，编辑器 <code class="usage-code">StormSyncAvaBridgeEditor</code>），属 Virtual Production。</li><li>它是 Motion Design 插件与 Storm Sync 之间的桥，提供编辑器内集成以同步资产。</li><li>在 Motion Design 工作流里用它在编辑器间同步资产。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">Motion Design 与 Storm Sync 之间的资产同步桥。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Storm Sync Motion Design Bridge</code> (runtime <code class="usage-code">StormSyncAvaBridge</code>, editor <code class="usage-code">StormSyncAvaBridgeEditor</code>), part of Virtual Production.</li><li>It bridges the Motion Design plugin and Storm Sync, providing in-editor integration to sync assets.</li><li>In a Motion Design workflow, use it to sync assets across editors.</li><li>Game modules depend on runtime modules; editor modules go to Editor targets only.</li></ol><p class="usage-note">A bridge between Motion Design and Storm Sync for asset sync.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">StormSyncAvaBridgeEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">StormSyncAvaBridge</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/StormSyncAvalancheBridge/StormSyncAvalancheBridge.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
