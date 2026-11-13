---
layout: default
title: 游戏输入库 / Game Input Base
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Game Input Base</div>
      <div class="hero-title-cn">游戏输入库 · GameInput 是下一代输入 API，它通过单一一致的接口公</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Input Devices</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/GameInput/GameInput.uplugin</div></div></div>
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
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：GameInput 是下一代输入 API，它通过单一一致的接口公开各种输入设备。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：GameInputBase, GameInputBaseEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: GameInput is a next-generation input API that exposes input devices of all kinds through a single consistent interface.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: GameInputBase, GameInputBaseEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Game Input Base</code>（运行时 <code class="usage-code">GameInputBase</code>，编辑器 <code class="usage-code">GameInputBaseEditor</code>）。它封装 Microsoft GameInput 的设备枚举与读输入，需搭配平台插件（如 <code class="usage-code">Game Input (Windows)</code>）才有真实设备。</li><li>Windows/GDK 目标同时启用对应平台 GameInput 插件。Enhanced Input 的 <code class="usage-code">Input Device</code> 后端可走 GameInput，而不是 RawInput/XInput 各写一套。</li><li>插上手柄/方向盘，PIE 看设备出现在 GameInput 设备列表（编辑器 <code class="usage-code">GameInputBaseEditor</code> 辅助）。<code class="usage-code">FKey</code> 事件应进 PlayerController / Enhanced Input Mapping Context。</li><li>振动、触摸板、方向盘轴从 GameInput 设备对象读，不要假设 XInput 的 4 手柄上限。设备被系统占用时（Game Bar、其它全屏游戏）枚举会空。</li><li>游戏 <code class="usage-code">Build.cs</code> 依赖 <code class="usage-code">GameInputBase</code>；<code class="usage-code">GameInputBaseEditor</code> 只进编辑器。非微软平台不会凭空冒出 GameInput 设备。</li></ol><p class="usage-note">GameInput 设备层，不是 Enhanced Input 的 Mapping Context 编辑器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Game Input Base</code> (runtime <code class="usage-code">GameInputBase</code>, editor <code class="usage-code">GameInputBaseEditor</code>). It wraps Microsoft GameInput device enumeration and reads; pair it with a platform plugin such as <code class="usage-code">Game Input (Windows)</code> for real devices.</li><li>On Windows/GDK also enable the matching GameInput platform plugin. Enhanced Input can use GameInput as the device backend instead of separate RawInput/XInput paths.</li><li>Plug in a pad/wheel and PIE: the device should list via GameInput (<code class="usage-code">GameInputBaseEditor</code> helps in-editor). <code class="usage-code">FKey</code> events should reach the PlayerController / Enhanced Input mapping context.</li><li>Read rumble, touchpad, and wheel axes from the GameInput device object; do not assume XInput’s four-pad cap. Enumeration is empty if Game Bar or another fullscreen app owns the device.</li><li>Game <code class="usage-code">Build.cs</code> depends on <code class="usage-code">GameInputBase</code>; <code class="usage-code">GameInputBaseEditor</code> is editor-only. Non-Microsoft platforms will not magically grow GameInput devices.</li></ol><p class="usage-note">GameInput device layer, not the Enhanced Input mapping-context editor.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">GameInputBase</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GameInputBaseEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/GameInput/GameInput.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
