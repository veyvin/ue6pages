---
layout: default
title: 可定制的音序器轨道（实验性） / Customizable Sequencer Tracks (Experimental)
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Customizable Sequencer Tracks (Experimental)</div>
      <div class="hero-title-cn">可定制的音序器轨道（实验性） · 提供可添加到音序器的可蓝图轨道类型的库</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Runtime</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MovieScene/CustomizableSequencerTracks/CustomizableSequencerTracks.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">提供可添加到音序器的可蓝图轨道类型的库</div><div class="lang-content">Library that provides a blueprintable track type that can be added to sequencer</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：提供可添加到音序器的可蓝图轨道类型的库</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CustomizableSequencerTracks, CustomizableSequencerTracksEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Library that provides a blueprintable track type that can be added to sequencer</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CustomizableSequencerTracks, CustomizableSequencerTracksEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 插件 <code class="usage-code">Customizable Sequencer Tracks (Experimental)</code>（运行时 <code class="usage-code">CustomizableSequencerTracks</code>，编辑器 <code class="usage-code">CustomizableSequencerTracksEditor</code>）。</li><li>内容浏览器右键 <code class="usage-code">Blueprint Class</code>，父类选 <code class="usage-code">MovieSceneCustomizableTrack</code> / <code class="usage-code">UMovieSceneCustomizableTrack</code>（以及配套的 Customizable Section）。</li><li>在该蓝图里实现求值逻辑：按时间读取 Section 参数，写到绑定对象的属性或调用自定义函数；编译蓝图。</li><li>打开关卡 <code class="usage-code">Sequencer</code>，<code class="usage-code">+ Track</code> 添加你的自定义轨道类型，创建 Section，在曲线/关键帧上刷参数。</li><li>把轨道绑定到场景 Actor；播放/PIE 时确认自定义求值在 Tick 里改了目标，而不是普通 Transform/Animation 轨。</li><li>游戏模块只依赖 <code class="usage-code">CustomizableSequencerTracks</code>；<code class="usage-code">CustomizableSequencerTracksEditor</code> 仅进 Editor Target。</li><li>接口仍是 Experimental，不要把该轨类型写进必须跨引擎版本升级的过场资产。</li></ol><p class="usage-note">蓝图可扩展的 Sequencer 轨，不是内置 Animation/Audio 轨的替代分类。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Customizable Sequencer Tracks (Experimental)</code> (runtime <code class="usage-code">CustomizableSequencerTracks</code>, editor <code class="usage-code">CustomizableSequencerTracksEditor</code>).</li><li>Create a Blueprint class parented to <code class="usage-code">MovieSceneCustomizableTrack</code> / <code class="usage-code">UMovieSceneCustomizableTrack</code> (and the matching Customizable Section).</li><li>Implement evaluation in that Blueprint: read section parameters by time and write bound-object properties or custom functions, then compile.</li><li>In level <code class="usage-code">Sequencer</code>, <code class="usage-code">+ Track</code> your customizable track type, add a section, and key its parameters.</li><li>Bind the track to a scene actor; play/PIE and confirm custom evaluation mutates the target — it is not a Transform/Animation track.</li><li>Game modules depend on <code class="usage-code">CustomizableSequencerTracks</code> only; <code class="usage-code">CustomizableSequencerTracksEditor</code> stays on Editor targets.</li><li>The API is Experimental; do not bake this track type into cinematics that must survive engine upgrades.</li></ol><p class="usage-note">Blueprintable Sequencer tracks, not a stand-in for built-in Animation/Audio tracks.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">CustomizableSequencerTracks</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CustomizableSequencerTracksEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MovieScene/CustomizableSequencerTracks/CustomizableSequencerTracks.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
