---
layout: default
title: AudioWidget工具包 / AudioWidgetToolkit
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AudioWidgetToolkit</div>
      <div class="hero-title-cn">AudioWidget工具包 · 用于构建与音频相关数据和系统交互的小部件的工具包。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/AudioWidgetToolkit/AudioWidgetToolkit.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于构建与音频相关数据和系统交互的小部件的工具包。</div><div class="lang-content">Toolkit for building widgets that interact with audio-related data and systems.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于构建与音频相关数据和系统交互的小部件的工具包。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：AudioWidgetToolkitCore, AudioWidgetToolkit, AudioWidgetToolkitTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Toolkit for building widgets that interact with audio-related data and systems.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: AudioWidgetToolkitCore, AudioWidgetToolkit, AudioWidgetToolkitTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 插件 <code class="usage-code">AudioWidgetToolkit</code>（<code class="usage-code">AudioWidgetToolkitCore</code>、<code class="usage-code">AudioWidgetToolkit</code>）；测试模块 <code class="usage-code">AudioWidgetToolkitTests</code> 可选。</li><li>在自定义音频 UI 模块的 <code class="usage-code">Build.cs</code> 中依赖 <code class="usage-code">AudioWidgetToolkitCore</code> / <code class="usage-code">AudioWidgetToolkit</code>，用工具包组装可与音频系统绑定的复合控件（在 <code class="usage-code">AudioWidgets</code> 单控件之上）。</li><li>把工具包控件嵌进编辑器工具或 UMG，绑定到同一套音频参数/总线，而不是再拖一套普通 Slider。</li><li>用 <code class="usage-code">Tools &gt; Session Frontend &gt; Automation</code> 跑 <code class="usage-code">AudioWidgetToolkitTests</code> 验证控件行为。</li><li>Experimental，不要当 Shipping HUD 的稳定 API；游戏内简单电平条优先用 <code class="usage-code">AudioWidgets</code>。</li></ol><p class="usage-note">Experimental 工具包，用来搭建与音频系统交互的复合控件，不是现成的混音台窗口。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">AudioWidgetToolkit</code> (<code class="usage-code">AudioWidgetToolkitCore</code>, <code class="usage-code">AudioWidgetToolkit</code>); <code class="usage-code">AudioWidgetToolkitTests</code> is optional.</li><li>Depend on <code class="usage-code">AudioWidgetToolkitCore</code> / <code class="usage-code">AudioWidgetToolkit</code> in your audio-UI <code class="usage-code">Build.cs</code> and compose compound controls that bind to audio systems (a layer above <code class="usage-code">AudioWidgets</code>).</li><li>Embed those toolkit widgets in an editor tool or UMG and bind the same audio parameters/buses; do not fall back to a plain Slider.</li><li>Run <code class="usage-code">AudioWidgetToolkitTests</code> from <code class="usage-code">Tools &gt; Session Frontend &gt; Automation</code>.</li><li>Experimental — not a stable shipping HUD API; prefer <code class="usage-code">AudioWidgets</code> for simple in-game meters.</li></ol><p class="usage-note">Experimental toolkit for building composite audio-bound widgets, not a ready-made mixer window.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AudioWidgetToolkitCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioWidgetToolkit</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioWidgetToolkitTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/AudioWidgetToolkit/AudioWidgetToolkit.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
