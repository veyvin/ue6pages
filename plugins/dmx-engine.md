---
layout: default
title: DMX 引擎 / DMX Engine
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DMX Engine</div>
      <div class="hero-title-cn">DMX 引擎 · 与支持 DigitalMultiplexer (DMX) 的设备</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DMXDMXEngine.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">与支持 DigitalMultiplexer (DMX) 的设备进行通信的功能和资产</div><div class="lang-content">Functionality and assets for communication with DigitalMultiplexer (DMX) enabled devices</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DMXBlueprintGraph, DMXEditor, DMXRuntime。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DMXBlueprintGraph, DMXEditor, DMXRuntime. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">DMX Engine</code>（<code class="usage-code">DMXRuntime</code>、<code class="usage-code">DMXEditor</code>、<code class="usage-code">DMXBlueprintGraph</code>）；协议进出还要启用 <code class="usage-code">DMX Protocol</code>。</li><li>内容浏览器右键新建 <code class="usage-code">DMX Library</code>，在其中创建 Fixture Type、Fixture Patch 和 Controller（Universe/地址）。</li><li>从 <code class="usage-code">Window &gt; DMX</code> 打开 Library 编辑器核对 Patch 表；关卡里放置灯具 Actor 后，在 Details 指定 Library + Patch。</li><li>蓝图用 <code class="usage-code">DMXRuntime</code> 节点读写属性（如 <code class="usage-code">Get DMX Fixture Attributes</code> / <code class="usage-code">Set DMX Attribute</code>），走 <code class="usage-code">DMXBlueprintGraph</code>，不要手写原始 512 通道除非必要。</li><li>PIE 或 On-Air 时看灯具 Actor 的光束/颜色是否跟输入端口或控制台一致。</li><li>游戏模块只依赖 <code class="usage-code">DMXRuntime</code>；<code class="usage-code">DMXEditor</code> 与图节点模块不要写进 Game Target。</li></ol><p class="usage-note">DMX 资产与运行时核心：Library/Patch/属性；端口协议在 `DMX Protocol`，灯具网格在 `DMX Fixtures`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">DMX Engine</code> (<code class="usage-code">DMXRuntime</code>, <code class="usage-code">DMXEditor</code>, <code class="usage-code">DMXBlueprintGraph</code>); also enable <code class="usage-code">DMX Protocol</code> if you need wire I/O.</li><li>Create a <code class="usage-code">DMX Library</code> asset and author Fixture Types, Fixture Patches, and Controllers (universe/address).</li><li>Open the Library editor from <code class="usage-code">Window &gt; DMX</code>, then place fixture actors and assign Library + Patch in Details.</li><li>Read/write attributes from Blueprint via <code class="usage-code">DMXRuntime</code> nodes (<code class="usage-code">Get DMX Fixture Attributes</code> / <code class="usage-code">Set DMX Attribute</code>) from <code class="usage-code">DMXBlueprintGraph</code>; avoid raw 512-slot buffers unless you must.</li><li>In PIE or on-air, confirm fixture beams/color match the input port or console.</li><li>Game modules depend on <code class="usage-code">DMXRuntime</code> only; keep <code class="usage-code">DMXEditor</code> off Game targets.</li></ol><p class="usage-note">Core Library/Patch/attribute runtime; wire ports live in `DMX Protocol`, fixture meshes in `DMX Fixtures`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">DMXBlueprintGraph</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXRuntime</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DMXDMXEngine.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
