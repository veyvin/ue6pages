---
layout: default
title: 媒体合成 / Media Compositing
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Media Compositing</div>
      <div class="hero-title-cn">媒体合成 · 用于合成媒体的 Actor、组件和 Sequencer 扩展</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/MediaCompositing/MediaCompositing.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于合成媒体的 Actor、组件和 Sequencer 扩展</div><div class="lang-content">Actors, components and Sequencer extensions for compositing media</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于合成媒体的 Actor、组件和 Sequencer 扩展</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：MediaCompositing, MediaCompositingEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Actors, components and Sequencer extensions for compositing media</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: MediaCompositing, MediaCompositingEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Media Compositing</code>（运行时 <code class="usage-code">MediaCompositing</code>，编辑器 <code class="usage-code">MediaCompositingEditor</code>）。</li><li>用它提供的 Actor/组件把媒体合成进场景，并在 Sequencer 里用其扩展编排出片。</li><li>把 Media Texture 合成到画面/几何上，用于虚拟制片与合成。</li><li>Game 模块依赖 <code class="usage-code">MediaCompositing</code>；<code class="usage-code">MediaCompositingEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">把媒体合成进场景的 Actor/组件 + Sequencer 扩展。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Media Compositing</code> (runtime <code class="usage-code">MediaCompositing</code>, editor <code class="usage-code">MediaCompositingEditor</code>).</li><li>Use its actors/components to composite media into the scene and its Sequencer extensions to author output.</li><li>Composite Media Textures onto the frame/geometry for virtual production and compositing.</li><li>Game modules depend on <code class="usage-code">MediaCompositing</code>; <code class="usage-code">MediaCompositingEditor</code> is Editor-target only.</li></ol><p class="usage-note">Actors/components plus Sequencer extensions to composite media into scenes.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">MediaCompositing</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MediaCompositingEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/MediaCompositing/MediaCompositing.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
