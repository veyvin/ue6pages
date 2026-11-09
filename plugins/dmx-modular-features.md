---
layout: default
title: DMX 模块化功能 / DMX Modular Features
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DMX Modular Features</div>
      <div class="hero-title-cn">DMX 模块化功能 · DMX 的模块化功能</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Misc</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DMXModularFeatures/DMXModularFeatures.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">DMX 的模块化功能</div><div class="lang-content">Modular Features for DMX</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：DMX 的模块化功能</p><p>DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DMXFixtureActorInterface。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Modular Features for DMX</p><p>DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DMXFixtureActorInterface. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">DMX Modular Features</code>（唯一模块 <code class="usage-code">DMXFixtureActorInterface</code>）。它只提供灯具 Actor 接口，没有灯具网格或控制台 UI。</li><li>在自定义游戏/功能模块的 <code class="usage-code">Build.cs</code> 依赖 <code class="usage-code">DMXFixtureActorInterface</code>，让灯具类实现 <code class="usage-code">IDMXFixtureActorInterface</code>（或引擎暴露的同名 Fixture Actor 接口）。</li><li>把该 Actor 注册为 Modular Feature，使 <code class="usage-code">DMX Engine</code> / Pixel Mapping 能按接口枚举场景灯具，而不必依赖 <code class="usage-code">DMXFixtures</code> 插件内容。</li><li>实现接口要求的 Patch 绑定与属性应用函数；PIE 里用 Library 改通道，确认自定义 Actor 有响应。</li><li>不要在 <code class="usage-code">Window &gt; DMX</code> 里找本插件的独立面板——没有。</li><li>可与 <code class="usage-code">DMX Fixtures</code> 并存：商店灯具走官方蓝图，项目自研灯具走此接口。</li></ol><p class="usage-note">给自研灯具用的 Modular Feature 接口，不是又一套灯具资产包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">DMX Modular Features</code> (module <code class="usage-code">DMXFixtureActorInterface</code>). It is the fixture-actor interface only — no meshes or console UI.</li><li>Depend on <code class="usage-code">DMXFixtureActorInterface</code> in your game/feature <code class="usage-code">Build.cs</code> and implement <code class="usage-code">IDMXFixtureActorInterface</code> (the fixture actor interface) on your class.</li><li>Register the actor as a Modular Feature so <code class="usage-code">DMX Engine</code> / Pixel Mapping can enumerate fixtures without depending on <code class="usage-code">DMXFixtures</code> content.</li><li>Implement patch binding and attribute application; change Library channels in PIE and confirm the custom actor responds.</li><li>Do not look for a <code class="usage-code">Window &gt; DMX</code> panel owned by this plugin — there is none.</li><li>Can coexist with <code class="usage-code">DMX Fixtures</code>: stock Blueprints vs. project-owned fixtures on this interface.</li></ol><p class="usage-note">A Modular Feature interface for custom fixtures, not another fixture content pack.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">DMXFixtureActorInterface</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DMXModularFeatures/DMXModularFeatures.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
