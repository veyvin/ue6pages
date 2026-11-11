---
layout: default
title: 演员序列（实验） / Actor Sequence (Experimental)
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Actor Sequence (Experimental)</div>
      <div class="hero-title-cn">演员序列（实验） · 嵌入式演员序列的运行时</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MovieScene/ActorSequence/ActorSequence.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">嵌入式演员序列的运行时</div><div class="lang-content">Runtime for embedded actor sequences</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：嵌入式演员序列的运行时</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：ActorSequence, ActorSequenceEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Runtime for embedded actor sequences</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: ActorSequence, ActorSequenceEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Actor Sequence (Experimental)</code>（<code class="usage-code">ActorSequence</code> + <code class="usage-code">ActorSequenceEditor</code>）。</li><li>给目标 Actor 添加 <code class="usage-code">Actor Sequence Component</code>（<code class="usage-code">UActorSequenceComponent</code>）。</li><li>在该组件 Details 里打开内嵌 Sequence，用 Sequencer 对该 Actor 自身做关键帧（不是关卡上的 Level Sequence 资产）。</li><li>运行时或蓝图调用组件的 Play 播放这段嵌入序列。</li><li>插件名已标明 Experimental；新项目优先用 Level Sequence + Sequencer。</li><li><code class="usage-code">ActorSequenceEditor</code> 不要写入 Game Target。</li></ol><p class="usage-note">嵌入式 Actor Sequence 仍是实验路径，长期维护请改用 Level Sequence。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Actor Sequence (Experimental)</code> (<code class="usage-code">ActorSequence</code> + <code class="usage-code">ActorSequenceEditor</code>).</li><li>Add an <code class="usage-code">Actor Sequence Component</code> (<code class="usage-code">UActorSequenceComponent</code>) to the actor.</li><li>Open the embedded Sequence from the component Details and keyframe that actor in Sequencer (this is not a Level Sequence asset).</li><li>At runtime or from Blueprint, call Play on the component to run the embedded sequence.</li><li>The plugin is Experimental; prefer Level Sequence + Sequencer for new work.</li><li>Do not add <code class="usage-code">ActorSequenceEditor</code> to a Game target.</li></ol><p class="usage-note">Embedded actor sequences remain experimental; use Level Sequence for anything you must maintain.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">ActorSequence</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ActorSequenceEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MovieScene/ActorSequence/ActorSequence.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
