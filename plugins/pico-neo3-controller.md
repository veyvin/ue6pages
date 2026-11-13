---
layout: default
title: PICO Neo3 控制器 / PICO Neo3 Controller
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">PICO Neo3 Controller</div>
      <div class="hero-title-cn">PICO Neo3 控制器 · PICO Neo3 控制器对 OpenXR 的支持：/inter</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Reality</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/PICONeo3Controller/PICONeo3Controller.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">PICO Neo3 控制器对 OpenXR 的支持：/interaction_profiles/bytedance/pico_neo3_controller 交互配置文件 (XR_BD_controller_interaction) 和控制器网格。</div><div class="lang-content">PICO Neo3 controller support for OpenXR: the /interaction_profiles/bytedance/pico_neo3_controller interaction profile (XR_BD_controller_interaction) and the controller meshes.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：PICO Neo3 控制器对 OpenXR 的支持：/interaction_profiles/bytedance/pico_neo3_controller 交互配置文件 (XR_BD_controller_interaction) 和控制器网格。</p><p>OpenXR 功能插件：在 OpenXR 运行时上实现手部、眼动、控制器或交互扩展。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：PICONeo3Controller。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: PICO Neo3 controller support for OpenXR: the /interaction_profiles/bytedance/pico_neo3_controller interaction profile (XR_BD_controller_interaction) and the controller meshes.</p><p>OpenXR feature plugin: hands, eye tracking, controllers, or interaction on top of the OpenXR runtime.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: PICONeo3Controller. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">PICO Neo3 Controller</code>（模块 <code class="usage-code">PICONeo3Controller</code>）。</li><li>它为 PICO Neo3 控制器提供 OpenXR 支持：<code class="usage-code">/interaction_profiles/bytedance/pico_neo3_controller</code>（<code class="usage-code">XR_BD_controller_interaction</code>）及控制器网格。</li><li>在 Neo3 手柄的 OpenXR 项目里使用对应交互配置与可视化模型。</li><li>属 OpenXR 输入扩展；需 OpenXR 运行时。</li></ol><p class="usage-note">OpenXR 的 PICO Neo3 控制器支持。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">PICO Neo3 Controller</code> (module <code class="usage-code">PICONeo3Controller</code>).</li><li>It provides OpenXR support for PICO Neo3 controllers: <code class="usage-code">/interaction_profiles/bytedance/pico_neo3_controller</code> (<code class="usage-code">XR_BD_controller_interaction</code>) plus controller meshes.</li><li>Use the matching interaction profile and visualization meshes in Neo3 OpenXR projects.</li><li>It is an OpenXR input extension; requires an OpenXR runtime.</li></ol><p class="usage-note">OpenXR PICO Neo3 controller support.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">PICONeo3Controller</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/PICONeo3Controller/PICONeo3Controller.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
