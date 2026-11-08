---
layout: default
title: 电影预流 / Cinematic Prestreaming
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cinematic Prestreaming</div>
      <div class="hero-title-cn">电影预流 · 添加了一种在电影过场动画中记录某些类型的流数据请求的方法。然后可</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MovieScene/CinematicPrestreaming/CinematicPrestreaming.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">添加了一种在电影过场动画中记录某些类型的流数据请求的方法。然后可以在 Sequencer 时间轴上提前回放这些请求，以在正常游戏/渲染期间预传输数据。</div><div class="lang-content">Adds a way to record certain types of streaming data requests in cinematic cutscenes. The requests can then be played back in advance on the Sequencer timeline to pre-stream data during normal gameplay/rendering.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：添加了一种在电影过场动画中记录某些类型的流数据请求的方法。然后可以在 Sequencer 时间轴上提前回放这些请求，以在正常游戏/渲染期间预传输数据。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CinematicPrestreaming, CinematicPrestreamingEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adds a way to record certain types of streaming data requests in cinematic cutscenes. The requests can then be played back in advance on the Sequencer timeline to pre-stream data during normal gameplay/rendering.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CinematicPrestreaming, CinematicPrestreamingEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Cinematic Prestreaming</code>（运行时 <code class="usage-code">CinematicPrestreaming</code>，编辑器 <code class="usage-code">CinematicPrestreamingEditor</code>）。</li><li>打开过场 <code class="usage-code">Level Sequence</code>，确保镜头会触发虚拟纹理、Nanite 或纹理流送（远切近、大场景）。</li><li>用插件的录制流程（Sequencer / Movie Render 相关入口）在过场中记录流送请求，生成 <code class="usage-code">Cinematic Prestreaming</code> 数据资产。</li><li>回到时间轴，为该 Sequence 加上 Prestreaming 轨道，把资产挂上，并让请求比摄像机到达提前若干帧/秒。</li><li>PIE 或 MRQ 回放同一镜头，对比未挂轨道时的贴图/几何弹出；预流是提前排队 IO，不是后期处理开关。</li><li>游戏模块只链 <code class="usage-code">CinematicPrestreaming</code>；录制 UI 留在 Editor。</li></ol><p class="usage-note">给过场预热流送请求，不是 Show Flag 也不是后期体积选项。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cinematic Prestreaming</code> (runtime <code class="usage-code">CinematicPrestreaming</code>, editor <code class="usage-code">CinematicPrestreamingEditor</code>).</li><li>Open the cinematic <code class="usage-code">Level Sequence</code> and make sure the camera move will hitch virtual textures, Nanite, or texture streaming (hard cuts, large worlds).</li><li>Run the plugin’s record path (Sequencer / Movie Render related) during the cutscene to capture streaming requests into a Cinematic Prestreaming asset.</li><li>Add a Prestreaming track on the sequence, assign that asset, and offset so requests fire seconds/frames before the camera arrives.</li><li>PIE or MRQ the same shot and compare pop-in with the track disabled. This queues IO early; it is not a post-process toggle.</li><li>Link only <code class="usage-code">CinematicPrestreaming</code> in game modules; keep recording UI on Editor.</li></ol><p class="usage-note">Warms streaming requests for cinematics; not a show flag or post-process volume setting.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">CinematicPrestreaming</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CinematicPrestreamingEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MovieScene/CinematicPrestreaming/CinematicPrestreaming.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
