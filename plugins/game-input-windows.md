---
layout: default
title: 游戏输入（Windows） / Game Input (Windows)
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Game Input (Windows)</div>
      <div class="hero-title-cn">游戏输入（Windows） · GameInput 是下一代输入 API，它通过单一一致的接口公</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Input Devices</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/GameInputWindows/GameInputWindows.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">GameInput 是下一代输入 API，它通过单一一致的接口公开各种输入设备。</div><div class="lang-content">GameInput is a next-generation input API that exposes input devices of all kinds through a single consistent interface.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：GameInput 是下一代输入 API，它通过单一一致的接口公开各种输入设备。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：GameInputWindows。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: GameInput is a next-generation input API that exposes input devices of all kinds through a single consistent interface.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: GameInputWindows. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Game Input (Windows)</code> 插件（运行时模块 <code class="usage-code">GameInputWindows</code>），在 Windows 目标里可用。</li><li>在项目设置或初始化代码里调用 <code class="usage-code">GameInput</code> API 创建 device、注册回调，而不是走旧的 XInput / RawInput。</li><li>用统一的 device 接口读取手柄、键鼠等设备状态；同一套代码可映射到不同设备。</li><li>运行时游戏模块在 <code class="usage-code">Build.cs</code> 只依赖 <code class="usage-code">GameInputWindows</code>；非 Windows 平台不要直接依赖它。</li></ol><p class="usage-note">这是 Windows 上的新输入 API（GameInput）封装，不是 Enhanced Input 本身。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Game Input (Windows)</code> (runtime module <code class="usage-code">GameInputWindows</code>); it targets Windows.</li><li>Create devices and register callbacks through the <code class="usage-code">GameInput</code> API instead of legacy XInput / RawInput.</li><li>Read gamepad and mouse/keyboard state through the unified device interface so one code path maps to different devices.</li><li>At runtime depend on <code class="usage-code">GameInputWindows</code> via <code class="usage-code">Build.cs</code> only; do not depend on it on non-Windows platforms.</li></ol><p class="usage-note">A Windows wrapper over the GameInput API, not Enhanced Input itself.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GameInputWindows</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/GameInputWindows/GameInputWindows.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
