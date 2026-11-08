---
layout: default
title: 和谐 / Harmonix
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">H</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Harmonix</div>
      <div class="hero-title-cn">和谐 · Harmonix 音乐相关音频功能包。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc. - Harmonix GenTech</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc. - Harmonix GenTech</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">11</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Harmonix/Harmonix.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Harmonix 音乐相关音频功能包。</div><div class="lang-content">A package of Harmonix music related audio functionality.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Harmonix 音乐相关音频功能包。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：Harmonix, HarmonixEditor, HarmonixDsp, HarmonixDspTests, HarmonixDspEditor, HarmonixMidi, HarmonixMidiEditor, HarmonixMidiTests 等。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A package of Harmonix music related audio functionality.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: Harmonix, HarmonixEditor, HarmonixDsp, HarmonixDspTests, HarmonixDspEditor, HarmonixMidi, HarmonixMidiEditor, HarmonixMidiTests 等. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Harmonix</code>（运行时 <code class="usage-code">Harmonix</code>、<code class="usage-code">HarmonixDsp</code>、<code class="usage-code">HarmonixMidi</code>，编辑器 <code class="usage-code">HarmonixEditor</code> 等）。</li><li>用于音乐相关的音频功能（律动、MIDI、DSP 处理等），把 Harmonix 组件/资产接入音频或玩法。</li><li>配置 MIDI/DSP 参数，在 PIE 里试听并调音。</li><li>Game 模块依赖运行时模块；<code class="usage-code">HarmonixEditor</code>、测试模块不要进游戏包。</li></ol><p class="usage-note">Harmonix 音乐音频功能包，偏节奏/MIDI/DSP。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Harmonix</code> (runtime <code class="usage-code">Harmonix</code>, <code class="usage-code">HarmonixDsp</code>, <code class="usage-code">HarmonixMidi</code>; editor <code class="usage-code">HarmonixEditor</code>, etc.).</li><li>For music-related audio features (rhythm, MIDI, DSP), hook Harmonix components/assets into audio or gameplay.</li><li>Configure MIDI/DSP parameters and audition/tune in PIE.</li><li>Game modules depend on runtime modules; keep <code class="usage-code">HarmonixEditor</code> and test modules out of the cooked game.</li></ol><p class="usage-note">The Harmonix music-audio package, rhythm/MIDI/DSP oriented.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (11)</div><div class="module-item"><span class="dot"></span><span class="name mono">Harmonix</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixDsp</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixDspTests</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixDspEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixMidi</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixMidiEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixMidiTests</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixMetasound</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixMetasoundEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HarmonixMetasoundTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Harmonix/Harmonix.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
