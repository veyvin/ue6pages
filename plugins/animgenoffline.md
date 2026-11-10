---
layout: default
title: 动画生成离线 / AnimGenOffline
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AnimGenOffline</div>
      <div class="hero-title-cn">动画生成离线 · 添加对音序器内离线生成动画的支持。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Animation</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Animation/AnimGenOffline/AnimGenOffline.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">添加对音序器内离线生成动画的支持。</div><div class="lang-content">Add support for offline generated animations inside sequencer.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：添加对音序器内离线生成动画的支持。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：AnimGenOfflineRuntime, AnimGenOffline。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Add support for offline generated animations inside sequencer.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: AnimGenOfflineRuntime, AnimGenOffline. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental <code class="usage-code">AnimGenOffline</code>（运行时 <code class="usage-code">AnimGenOfflineRuntime</code>，编辑器 <code class="usage-code">AnimGenOffline</code>）；离线烘焙通常还需 <code class="usage-code">AnimGen</code> / <code class="usage-code">AnimDatabase</code>。</li><li>用 AnimGen 管线在编辑器里生成运动，导出/保存为标准 <code class="usage-code">AnimSequence</code>，而不是在 PIE 里每帧跑神经网络。</li><li>新建 <code class="usage-code">Level Sequence</code>，绑定带 <code class="usage-code">SkeletalMeshComponent</code> 的 Actor，添加 <code class="usage-code">MovieSceneSkeletalAnimationTrack</code>。</li><li>把离线生成的 <code class="usage-code">AnimSequence</code> 赋给 <code class="usage-code">MovieSceneSkeletalAnimationSection</code>，对齐序列帧范围后播放/渲染。</li><li>游戏若只需播已烘焙片段，依赖 <code class="usage-code">AnimGenOfflineRuntime</code> 即可；不要把编辑器模块写进 Game Target。</li></ol><p class="usage-note">职责是让 Sequencer 使用离线生成的动画；不要把它当成运行时 AnimGenController。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">AnimGenOffline</code> (runtime <code class="usage-code">AnimGenOfflineRuntime</code>, editor <code class="usage-code">AnimGenOffline</code>); offline bake usually also needs <code class="usage-code">AnimGen</code> / <code class="usage-code">AnimDatabase</code>.</li><li>Generate motion with the AnimGen pipeline in the editor and save a normal <code class="usage-code">AnimSequence</code> instead of evaluating the network every PIE frame.</li><li>Create a <code class="usage-code">Level Sequence</code>, bind an actor with a <code class="usage-code">SkeletalMeshComponent</code>, and add a <code class="usage-code">MovieSceneSkeletalAnimationTrack</code>.</li><li>Assign the offline <code class="usage-code">AnimSequence</code> to a <code class="usage-code">MovieSceneSkeletalAnimationSection</code>, match the sequence range, then play or render.</li><li>If the game only plays baked clips, depend on <code class="usage-code">AnimGenOfflineRuntime</code>; keep the editor module off Game targets.</li></ol><p class="usage-note">Adds Sequencer support for offline-generated clips; it is not the runtime AnimGenController.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AnimGenOfflineRuntime</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AnimGenOffline</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Animation/AnimGenOffline/AnimGenOffline.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
