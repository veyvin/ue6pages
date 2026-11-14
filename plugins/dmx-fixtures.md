---
layout: default
title: DMX 灯具 / DMX Fixtures
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DMX Fixtures</div>
      <div class="hero-title-cn">DMX 灯具 · DMX 灯具蓝图</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DMXFixtures/DMXFixtures.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">DMX 灯具蓝图</div><div class="lang-content">DMX Light Fixtures Blueprints</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：DMX 灯具蓝图</p><p>DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DMXFixtures。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: DMX Light Fixtures Blueprints</p><p>DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DMXFixtures. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">DMX Engine</code> 后再启用 <code class="usage-code">DMX Fixtures</code>（模块 <code class="usage-code">DMXFixtures</code>），并在内容浏览器打开该插件的 Content。</li><li>把插件自带的灯具蓝图（如 Moving Head、Point Light、Par 等 <code class="usage-code">DMXFixtureActor</code> 子类）拖进舞台关卡。</li><li>在 Actor Details 指定 <code class="usage-code">DMX Library</code> 与 Fixture Patch，让属性（Pan/Tilt/Dimmer/Color）驱动组件灯光与骨骼。</li><li>用 Control Console 或外部灯台改通道，视口里确认头灯转动和亮度，而不是只看通道监视器。</li><li>自定义灯具应继承这些蓝图或实现灯具接口，不要从零复制一份不接 Patch 的静态网格。</li><li>可进包装；没有 Library Patch 时灯具只是普通网格，不会响应 DMX。</li></ol><p class="usage-note">提供可放置的灯具蓝图；通道语义仍由 DMX Library 的 Fixture Type 定义。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">DMX Engine</code>, then <code class="usage-code">DMX Fixtures</code> (module <code class="usage-code">DMXFixtures</code>), and show the plugin Content folder.</li><li>Drop stock fixture Blueprints (Moving Head, Point Light, Par, and other <code class="usage-code">DMXFixtureActor</code> subclasses) into the stage level.</li><li>In Details, assign a <code class="usage-code">DMX Library</code> Fixture Patch so attributes (Pan/Tilt/Dimmer/Color) drive lights and bones.</li><li>Move channels from the Control Console or an external desk and confirm head motion and intensity in the viewport, not only a channel monitor.</li><li>Subclass these Blueprints or the fixture interface for custom units; do not duplicate a static mesh that never binds a Patch.</li><li>Shippable; without a Library Patch the actor is just a mesh and will not respond to DMX.</li></ol><p class="usage-note">Placeable fixture Blueprints; channel meaning still comes from the DMX Library Fixture Type.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">DMXFixtures</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DMXFixtures/DMXFixtures.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
