---
layout: default
title: 元音 / MetaSound
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">MetaSound</div>
      <div class="hero-title-cn">元音 · 高性能音频系统，使声音设计人员能够使用来自游戏数据和蓝图的音频参</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">7</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Metasound/Metasound.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">高性能音频系统，使声音设计人员能够使用来自游戏数据和蓝图的音频参数和音频事件对声音进行采样精确控制和调制，从而完全控制声源的音频 DSP 图形生成</div><div class="lang-content">A high-performance audio system that enables sound designers to have complete control over audio DSP graph generation of sound sources, via sample-accurate control and modulation of sound using audio parameters and audio events from game data and Blueprints</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>MetaSound 是音频的节点图合成系统，类似 Niagara 之于粒子：在图里做振荡、滤波、调制，运行时生成声音，而不是只播 Wave 文件。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：MetasoundGraphCore, MetasoundGenerator, MetasoundFrontend, MetasoundStandardNodes, MetasoundEngine, MetasoundEngineTest, MetasoundEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine</a></p></div><div class="lang-content"><p>MetaSound is a node-graph audio synthesis system (Niagara for audio): oscillators, filters, and modulation generate sound at runtime instead of only playing waves.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: MetasoundGraphCore, MetasoundGenerator, MetasoundFrontend, MetasoundStandardNodes, MetasoundEngine, MetasoundEngineTest, MetasoundEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MetaSound</code>（模块 <code class="usage-code">MetasoundGraphCore</code>、<code class="usage-code">MetasoundFrontend</code>、<code class="usage-code">MetasoundGenerator</code>、<code class="usage-code">MetasoundStandardNodes</code>、<code class="usage-code">MetasoundEngine</code>，编辑器 <code class="usage-code">MetasoundEditor</code>）。</li><li>用节点图做音频合成：振荡、滤波、调制，运行时按游戏数据/蓝图参数精确生成声音。</li><li>创建 MetaSound Source/Preset 资产，挂到 Sound 组件播放，用参数实时调制。</li><li>Game 模块依赖运行时模块；<code class="usage-code">MetasoundEditor</code>/Test 模块只进 Editor Target。</li></ol><p class="usage-note">MetaSound 节点图音频合成系统（“音频界的 Niagara”）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MetaSound</code> (modules <code class="usage-code">MetasoundGraphCore</code>, <code class="usage-code">MetasoundFrontend</code>, <code class="usage-code">MetasoundGenerator</code>, <code class="usage-code">MetasoundStandardNodes</code>, <code class="usage-code">MetasoundEngine</code>, editor <code class="usage-code">MetasoundEditor</code>).</li><li>Synthesize audio in a node graph: oscillators, filters, modulation, generating sound at runtime driven by game data/Blueprint params.</li><li>Create MetaSound Source/Preset assets, play them via a Sound component, and modulate with parameters in real time.</li><li>Game modules depend on runtime modules; <code class="usage-code">MetasoundEditor</code>/test modules go to Editor targets only.</li></ol><p class="usage-note">The MetaSound node-graph audio synthesis system (&quot;Niagara for audio&quot;).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (7)</div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundGraphCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundGenerator</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundFrontend</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundStandardNodes</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundEngine</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundEngineTest</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetasoundEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Metasound/Metasound.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
