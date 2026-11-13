---
layout: default
title: 智能对象 / SmartObjects
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">SmartObjects</div>
      <div class="hero-title-cn">智能对象 · 支持游戏世界中的环境生活</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Gameplay</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/SmartObjects/SmartObjects.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持游戏世界中的环境生活</div><div class="lang-content">Support for ambient life populating the game world</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持游戏世界中的环境生活</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：SmartObjectsModule, SmartObjectsTestSuite, SmartObjectsEditorModule。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Support for ambient life populating the game world</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: SmartObjectsModule, SmartObjectsTestSuite, SmartObjectsEditorModule. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">SmartObjects</code>（运行时 <code class="usage-code">SmartObjectsModule</code>，测试 <code class="usage-code">SmartObjectsTestSuite</code>，编辑器 <code class="usage-code">SmartObjectsEditorModule</code>）。</li><li>它支持游戏世界中的“环境生活”交互（对象提供可占用的交互槽，AI 前往使用）。</li><li>在关卡布置 Smart Object（如座位、资源点），用其定义行为与占用规则。</li><li>Game 模块依赖运行时模块；编辑器/测试模块只进 Editor Target。</li></ol><p class="usage-note">支持世界“环境生活”交互的 Smart Objects。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">SmartObjects</code> (runtime <code class="usage-code">SmartObjectsModule</code>, tests <code class="usage-code">SmartObjectsTestSuite</code>, editor <code class="usage-code">SmartObjectsEditorModule</code>).</li><li>It supports ambient life in the game world (objects expose occupancy interaction slots that AI go use).</li><li>Place Smart Objects (seats, resource points) in the level and define behaviors/occupancy rules.</li><li>Game modules depend on runtime modules; editor/test modules go to Editor targets only.</li></ol><p class="usage-note">Smart Objects supporting ambient-life world interactions.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">SmartObjectsModule</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SmartObjectsTestSuite</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SmartObjectsEditorModule</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/SmartObjects/SmartObjects.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
