---
layout: default
title: 音频联觉 / Audio Synesthesia
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Audio Synesthesia</div>
      <div class="hero-title-cn">音频联觉 · 各种离线分析器，用于将提取的音频元数据集成到蓝图中。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AudioSynesthesia/AudioSynesthesia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">各种离线分析器，用于将提取的音频元数据集成到蓝图中。</div><div class="lang-content">A variety of offline analyzers for integrating exposing extracted audio metadata to blueprints.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：各种离线分析器，用于将提取的音频元数据集成到蓝图中。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AudioSynesthesiaCore, AudioSynesthesia, AudioSynesthesiaEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A variety of offline analyzers for integrating exposing extracted audio metadata to blueprints.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AudioSynesthesiaCore, AudioSynesthesia, AudioSynesthesiaEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Audio Synesthesia</code>（<code class="usage-code">AudioSynesthesiaCore</code>、<code class="usage-code">AudioSynesthesia</code>、<code class="usage-code">AudioSynesthesiaEditor</code>）。</li><li>先创建 NRT Settings 资产，例如 <code class="usage-code">Loudness NRT Settings</code>、<code class="usage-code">ConstantQNRT Settings</code>、<code class="usage-code">Onset NRT Settings</code>，再创建对应分析器 <code class="usage-code">ULoudnessNRT</code>、<code class="usage-code">UConstantQNRT</code>、<code class="usage-code">UOnsetNRT</code>。</li><li>把分析器的 Sound 指到目标 <code class="usage-code">Sound Wave</code>，在资产编辑器里 Analyze，生成离线响度 / Constant-Q / onset 曲线（不是实时子混合）。</li><li>蓝图用 <code class="usage-code">Get Normalized Loudness At Time</code>、<code class="usage-code">Get Constant Q At Time</code>、<code class="usage-code">Get Channel Onsets Between Times</code> 按时间取样，驱动材质、灯光或游戏逻辑。</li><li>需要实时频谱时改用同插件的 Analyzer 组件（Loudness / ConstantQ / Meter），与 NRT 资产分开。</li><li>游戏模块依赖 <code class="usage-code">AudioSynesthesia</code> / <code class="usage-code">AudioSynesthesiaCore</code>；<code class="usage-code">AudioSynesthesiaEditor</code> 仅 Editor。</li></ol><p class="usage-note">NRT 分析器离线提取元数据给蓝图，不是播放插件也不是 Modulation。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Audio Synesthesia</code> (<code class="usage-code">AudioSynesthesiaCore</code>, <code class="usage-code">AudioSynesthesia</code>, <code class="usage-code">AudioSynesthesiaEditor</code>).</li><li>Create NRT Settings assets (<code class="usage-code">Loudness NRT Settings</code>, <code class="usage-code">ConstantQNRT Settings</code>, <code class="usage-code">Onset NRT Settings</code>) and matching analyzers <code class="usage-code">ULoudnessNRT</code>, <code class="usage-code">UConstantQNRT</code>, <code class="usage-code">UOnsetNRT</code>.</li><li>Point the analyzer at a <code class="usage-code">Sound Wave</code> and Analyze in the asset editor to bake loudness / Constant-Q / onset curves (not a live submix).</li><li>From Blueprint sample with <code class="usage-code">Get Normalized Loudness At Time</code>, <code class="usage-code">Get Constant Q At Time</code>, <code class="usage-code">Get Channel Onsets Between Times</code> to drive materials, lights, or gameplay.</li><li>For live analysis use the plugin’s Analyzer components (Loudness / ConstantQ / Meter), separate from NRT assets.</li><li>Game modules depend on <code class="usage-code">AudioSynesthesia</code> / <code class="usage-code">AudioSynesthesiaCore</code>; <code class="usage-code">AudioSynesthesiaEditor</code> is Editor-only.</li></ol><p class="usage-note">NRT analyzers bake audio metadata for Blueprint; they do not play sound and are not Modulation.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AudioSynesthesiaCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioSynesthesia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioSynesthesiaEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AudioSynesthesia/AudioSynesthesia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
