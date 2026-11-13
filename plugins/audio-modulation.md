---
layout: default
title: 音频调制 / Audio Modulation
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Audio Modulation</div>
      <div class="hero-title-cn">音频调制 · 虚幻音频引擎中音频调制的默认实现。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">2.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AudioModulation/AudioModulation.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">虚幻音频引擎中音频调制的默认实现。</div><div class="lang-content">Default implementation of Audio Modulation in the Unreal Audio Engine.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：虚幻音频引擎中音频调制的默认实现。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AudioModulation, AudioModulationEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Default implementation of Audio Modulation in the Unreal Audio Engine.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AudioModulation, AudioModulationEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Audio Modulation</code>（运行时 <code class="usage-code">AudioModulation</code>，编辑器 <code class="usage-code">AudioModulationEditor</code>）并重启。</li><li>在内容浏览器 <code class="usage-code">Sounds &gt; Modulation</code> 下创建 <code class="usage-code">Sound Control Bus</code>、<code class="usage-code">Sound Control Bus Mix</code>，以及 <code class="usage-code">Modulation Parameter</code>（Volume / Pitch / Lowpass 等）。</li><li>需要周期或包络驱动时，再创建 <code class="usage-code">Modulation Generator</code> 资产（<code class="usage-code">LFO</code>、<code class="usage-code">Envelope Follower</code>），并接到对应 Control Bus。</li><li>打开 Sound Wave / Sound Cue / MetaSound / <code class="usage-code">Audio Component</code>，在 Modulation Destinations 里把上述 Bus 绑到音量、音调或滤波。</li><li>运行时用 <code class="usage-code">UAudioModulationStatics</code> 的 <code class="usage-code">Activate Bus Mix</code> / <code class="usage-code">Deactivate Bus Mix</code> / <code class="usage-code">Update Mix</code> 启用混音；全局值用 <code class="usage-code">Set Global Bus Mix Value</code>。</li><li>C++ 游戏模块只依赖 <code class="usage-code">AudioModulation</code>；<code class="usage-code">AudioModulationEditor</code> 仅进 Editor Target。</li><li>PIE 中改 Mix 权重，听目标声音是否跟随 Bus，而不是去 Audio 项目设置里找一个叫 Audio Modulation 的子混合。</li></ol><p class="usage-note">默认调制实现靠 Control Bus / Mix 资产驱动声音目的地，不是新的 Sound Class。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Audio Modulation</code> (runtime <code class="usage-code">AudioModulation</code>, editor <code class="usage-code">AudioModulationEditor</code>) and restart.</li><li>In Content Browser under <code class="usage-code">Sounds &gt; Modulation</code>, create a <code class="usage-code">Sound Control Bus</code>, a <code class="usage-code">Sound Control Bus Mix</code>, and a <code class="usage-code">Modulation Parameter</code> (Volume / Pitch / Lowpass, etc.).</li><li>For periodic or envelope drive, add a <code class="usage-code">Modulation Generator</code> asset (<code class="usage-code">LFO</code>, <code class="usage-code">Envelope Follower</code>) and wire it to the bus.</li><li>On a Sound Wave / Sound Cue / MetaSound / <code class="usage-code">Audio Component</code>, bind that bus in Modulation Destinations (volume, pitch, or filter).</li><li>At runtime call <code class="usage-code">UAudioModulationStatics</code> <code class="usage-code">Activate Bus Mix</code> / <code class="usage-code">Deactivate Bus Mix</code> / <code class="usage-code">Update Mix</code>; use <code class="usage-code">Set Global Bus Mix Value</code> for a global bus.</li><li>Game modules depend on <code class="usage-code">AudioModulation</code> only; keep <code class="usage-code">AudioModulationEditor</code> on an Editor target.</li><li>In PIE, change mix weights and confirm the destination sound follows the bus — this is not a Project Settings submix named Audio Modulation.</li></ol><p class="usage-note">The default modulator drives sound destinations through Control Bus / Mix assets, not a new Sound Class.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AudioModulation</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioModulationEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AudioModulation/AudioModulation.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
