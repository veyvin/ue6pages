---
layout: default
title: 模块化测试截图 / Modular Test Screenshot
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Modular Test Screenshot</div>
      <div class="hero-title-cn">模块化测试截图 · 用于模块化测试框架的可选屏幕截图捕获和比较实用程序。需要捕获或比</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/ModularTestScreenshot/ModularTestScreenshot.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于模块化测试框架的可选屏幕截图捕获和比较实用程序。需要捕获或比较客户端视口的测试伙伴应该依赖于此。</div><div class="lang-content">Optional screenshot capture and comparison utilities for the Modular Test Framework. Test companions that need to capture or compare a client viewport should depend on this.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于模块化测试框架的可选屏幕截图捕获和比较实用程序。需要捕获或比较客户端视口的测试伙伴应该依赖于此。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：ModularTestScreenshot, ModularTestScreenshotCompare。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Optional screenshot capture and comparison utilities for the Modular Test Framework. Test companions that need to capture or compare a client viewport should depend on this.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: ModularTestScreenshot, ModularTestScreenshotCompare. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Modular Test Screenshot</code>（模块 <code class="usage-code">ModularTestScreenshot</code>、<code class="usage-code">ModularTestScreenshotCompare</code>）。</li><li>它是模块化测试框架的可选截图捕获与比较实用程序。</li><li>需要捕获或比较客户端视口的测试应依赖它。</li><li>属测试可选插件；配合 <code class="usage-code">Modular Test Framework</code>。</li></ol><p class="usage-note">模块化测试框架的可选截图捕获/比较工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Modular Test Screenshot</code> (modules <code class="usage-code">ModularTestScreenshot</code>, <code class="usage-code">ModularTestScreenshotCompare</code>).</li><li>It is the optional screenshot capture and comparison utility for the Modular Test Framework.</li><li>Tests that need to capture or compare a client viewport should depend on it.</li><li>It is an optional test plugin; used with <code class="usage-code">Modular Test Framework</code>.</li></ol><p class="usage-note">Optional screenshot capture/compare utilities for the Modular Test Framework.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">ModularTestScreenshot</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModularTestScreenshotCompare</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/ModularTestScreenshot/ModularTestScreenshot.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
