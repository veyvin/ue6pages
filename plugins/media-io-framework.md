---
layout: default
title: 媒体IO框架 / Media IO Framework
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Media IO Framework</div>
      <div class="hero-title-cn">媒体IO框架 · 支持虚拟制作行业使用的专业媒体 IO 的媒体框架类。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/MediaIOFramework/MediaIOFramework.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持虚拟制作行业使用的专业媒体 IO 的媒体框架类。</div><div class="lang-content">Media Framework classes to support Professional Media IO used by the Virtual Production industry.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持虚拟制作行业使用的专业媒体 IO 的媒体框架类。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：MediaIOCore, MediaIOEditor, GPUTextureTransfer。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Media Framework classes to support Professional Media IO used by the Virtual Production industry.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: MediaIOCore, MediaIOEditor, GPUTextureTransfer. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Media IO Framework</code>（模块 <code class="usage-code">MediaIOCore</code>、<code class="usage-code">GPUTextureTransfer</code>，编辑器 <code class="usage-code">MediaIOEditor</code>），属 Virtual Production。</li><li>用其类支持专业媒体 IO（如 SDI/采集卡），做虚拟制片的实时输入输出。</li><li>配置 Media IO 设备源/输出，把信号接进或送出引擎。</li><li>Game 模块依赖 <code class="usage-code">MediaIOCore</code>；<code class="usage-code">MediaIOEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">专业媒体 IO（SDI/采集）框架，虚拟制片用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Media IO Framework</code> (modules <code class="usage-code">MediaIOCore</code>, <code class="usage-code">GPUTextureTransfer</code>, editor <code class="usage-code">MediaIOEditor</code>), part of Virtual Production.</li><li>Use its classes to support professional media IO (e.g. SDI/capture cards) for real-time virtual production I/O.</li><li>Configure Media IO device sources/outputs to bring signals into or out of the engine.</li><li>Game modules depend on <code class="usage-code">MediaIOCore</code>; <code class="usage-code">MediaIOEditor</code> is Editor-target only.</li></ol><p class="usage-note">Professional media IO (SDI/capture) framework for virtual production.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">MediaIOCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MediaIOEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GPUTextureTransfer</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/MediaIOFramework/MediaIOFramework.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
