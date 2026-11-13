---
layout: default
title: 录音机 / Take Recorder
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">T</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Take Recorder</div>
      <div class="hero-title-cn">录音机 · 一套工具和界面，专为在虚拟制作环境中录制、审查和回放而设计。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">9</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/Takes/Takes.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">一套工具和界面，专为在虚拟制作环境中录制、审查和回放而设计。</div><div class="lang-content">A suite of tools and interfaces designed for recording, reviewing and playing back takes in a virtual production environment.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：一套工具和界面，专为在虚拟制作环境中录制、审查和回放而设计。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：TakesCore, TakeTrackRecorders, TakeRecorderSources, TakeRecorder, TakeRecorderEditor, TakeMovieScene, TakeSequencer, CacheTrackRecorder 等。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A suite of tools and interfaces designed for recording, reviewing and playing back takes in a virtual production environment.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: TakesCore, TakeTrackRecorders, TakeRecorderSources, TakeRecorder, TakeRecorderEditor, TakeMovieScene, TakeSequencer, CacheTrackRecorder 等. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Take Recorder</code>（模块 <code class="usage-code">TakesCore</code>、<code class="usage-code">TakeRecorder</code>、<code class="usage-code">TakeRecorderSources</code>、<code class="usage-code">TakeTrackRecorders</code>、<code class="usage-code">TakeMovieScene</code>、<code class="usage-code">CacheTrackRecorder</code>，编辑器 <code class="usage-code">TakeRecorderEditor</code> 等）。</li><li>它是为虚拟制片设计的录制、审查与回放工具集与界面。</li><li>用 Take Recorder 录制镜头/表演（多源），再回放审查。</li><li>Game 模块依赖运行时模块；<code class="usage-code">TakeRecorderEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">虚拟制片用的录制/审查/回放工具集（Take Recorder）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Take Recorder</code> (modules <code class="usage-code">TakesCore</code>, <code class="usage-code">TakeRecorder</code>, <code class="usage-code">TakeRecorderSources</code>, <code class="usage-code">TakeTrackRecorders</code>, <code class="usage-code">TakeMovieScene</code>, <code class="usage-code">CacheTrackRecorder</code>, editor <code class="usage-code">TakeRecorderEditor</code>, etc.).</li><li>It is a tools/UI set designed for recording, reviewing, and playing back takes in virtual production.</li><li>Use Take Recorder to record shots/performances (multi-source) and play back for review.</li><li>Game modules depend on runtime modules; <code class="usage-code">TakeRecorderEditor</code> is Editor-target only.</li></ol><p class="usage-note">A recording/reviewing/playback toolset for virtual production (Take Recorder).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (9)</div><div class="module-item"><span class="dot"></span><span class="name mono">TakesCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeTrackRecorders</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeRecorderSources</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeRecorder</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeRecorderEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeMovieScene</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeSequencer</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CacheTrackRecorder</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeRecorderNamingTokens</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/Takes/Takes.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
