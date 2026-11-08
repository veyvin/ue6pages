---
layout: default
title: 涂鸦 / Doodle
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Doodle</div>
      <div class="hero-title-cn">涂鸦 · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">6</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Doodle/Doodle.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">（无描述）</div><div class="lang-content">(no description)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：Doodle, DoodleMovieScene, DoodleSequencer, DoodleEditor, DoodleSlate, DoodleTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: Doodle, DoodleMovieScene, DoodleSequencer, DoodleEditor, DoodleSlate, DoodleTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental <code class="usage-code">Doodle</code>（<code class="usage-code">Doodle</code>、<code class="usage-code">DoodleSlate</code>、<code class="usage-code">DoodleEditor</code>、<code class="usage-code">DoodleMovieScene</code>、<code class="usage-code">DoodleSequencer</code>）并重启。</li><li>打开关卡 <code class="usage-code">Sequencer</code>，用 <code class="usage-code">DoodleSequencer</code> 提供的 Doodle 轨/工具在视口用 <code class="usage-code">DoodleSlate</code> 画笔做镜头批注（箭头、圈字），不是材质涂鸦，也不是 Control Rig。</li><li>笔画由 <code class="usage-code">DoodleMovieScene</code> 写成 Movie Scene section，随序列 scrub 显示/隐藏，可给导演或现场做画面指示。</li><li>播放序列确认批注跟镜头对齐；需要导出发片时把它当叠加层，不要指望它进游戏 HUD。</li><li><code class="usage-code">DoodleEditor</code> / <code class="usage-code">DoodleTests</code> 不要进 Game Target；现场工具链可保留 Runtime + MovieScene 模块。</li><li>接口无官方描述且 Experimental，不要当镜头完成稿的永久资产格式。</li></ol><p class="usage-note">Sequencer 视口批注/涂鸦轨，服务虚拟制片看片，不是运行时绘画玩法。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Doodle</code> (<code class="usage-code">Doodle</code>, <code class="usage-code">DoodleSlate</code>, <code class="usage-code">DoodleEditor</code>, <code class="usage-code">DoodleMovieScene</code>, <code class="usage-code">DoodleSequencer</code>) and restart.</li><li>Open level <code class="usage-code">Sequencer</code> and use the Doodle track/tools from <code class="usage-code">DoodleSequencer</code> to draw shot notes (arrows, circles) in the viewport via <code class="usage-code">DoodleSlate</code> — not a paintable material and not Control Rig.</li><li><code class="usage-code">DoodleMovieScene</code> stores strokes as Movie Scene sections that appear/hide while you scrub, for director or set callouts.</li><li>Play the sequence to confirm notes stay locked to the shot. Treat them as overlays for review, not as in-game HUD.</li><li>Keep <code class="usage-code">DoodleEditor</code> / <code class="usage-code">DoodleTests</code> off Game targets; the stage toolchain can keep Runtime + MovieScene.</li><li>Undocumented and Experimental; do not freeze it as the archival format for finished shots.</li></ol><p class="usage-note">Sequencer viewport annotation tracks for VP reviews, not a gameplay painting system.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (6)</div><div class="module-item"><span class="dot"></span><span class="name mono">Doodle</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DoodleMovieScene</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DoodleSequencer</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DoodleEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DoodleSlate</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DoodleTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Doodle/Doodle.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
