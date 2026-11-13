---
layout: default
title: 媒体框架实用程序 / Media Framework Utilities
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Media Framework Utilities</div>
      <div class="hero-title-cn">媒体框架实用程序 · 该插件提供了旨在简化媒体框架设置的实用资产和参与者。它包括对媒体</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/MediaFrameworkUtilities/MediaFrameworkUtilities.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该插件提供了旨在简化媒体框架设置的实用资产和参与者。它包括对媒体配置文件编辑器的访问。</div><div class="lang-content">This plugin provides utility assets and actors designed to simplify the Media Framework setup. It includes access to the the Media Profile editor.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该插件提供了旨在简化媒体框架设置的实用资产和参与者。它包括对媒体配置文件编辑器的访问。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：MediaFrameworkUtilities, MediaFrameworkUtilitiesEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This plugin provides utility assets and actors designed to simplify the Media Framework setup. It includes access to the the Media Profile editor.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: MediaFrameworkUtilities, MediaFrameworkUtilitiesEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Media Framework Utilities</code>（运行时 <code class="usage-code">MediaFrameworkUtilities</code>，编辑器 <code class="usage-code">MediaFrameworkUtilitiesEditor</code>）。</li><li>用它提供的实用资产/ Actor 简化 Media Framework 设置，并访问 Media Profile 编辑器。</li><li>在关卡/蓝图里用这些工具快速搭建媒体源与输出。</li><li>Game 模块依赖 <code class="usage-code">MediaFrameworkUtilities</code>；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">简化 Media Framework 设置的实用资产/Actor + Media Profile 编辑器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Media Framework Utilities</code> (runtime <code class="usage-code">MediaFrameworkUtilities</code>, editor <code class="usage-code">MediaFrameworkUtilitiesEditor</code>).</li><li>Use its utility assets/actors to simplify Media Framework setup and access the Media Profile editor.</li><li>In levels/Blueprint, use these tools to quickly set up media sources and outputs.</li><li>Game modules depend on <code class="usage-code">MediaFrameworkUtilities</code>; editor modules go to Editor targets only.</li></ol><p class="usage-note">Utility assets/actors that simplify Media Framework setup plus the Media Profile editor.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">MediaFrameworkUtilities</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MediaFrameworkUtilitiesEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/MediaFrameworkUtilities/MediaFrameworkUtilities.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
