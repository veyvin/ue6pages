---
layout: default
title: 人工智能意识洞察 / AI Awareness Insights
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AI Awareness Insights</div>
      <div class="hero-title-cn">人工智能意识洞察 · 记录 AI 意识（噪声、感知、警报级别）并在 Spatial a</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Insights</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/AI/AIAwarenessInsights/AIAwarenessInsights.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">记录 AI 意识（噪声、感知、警报级别）并在 Spatial and Timing Insights 中将其可视化。</div><div class="lang-content">Records AI awareness (noise, perception, alert levels) and visualizes it in Spatial and Timing Insights.</div></div></div>
    </div>
    
    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">AI Awareness Insights</code>（运行时 <code class="usage-code">AIAwarenessTrace</code>，编辑器 <code class="usage-code">AIAwarenessInsights</code>），属 Insights。</li><li>它记录 AI 意识状态（噪声、感知、警报级别），并在 Spatial and Timing Insights 中可视化。</li><li>调试 AI 时先采集 trace，再到 Unreal Insights 的 Spatial/Timing 视图查看感知范围与警报变化。</li><li>Game 模块依赖 <code class="usage-code">AIAwarenessTrace</code>；<code class="usage-code">AIAwarenessInsights</code> 只进 Editor Target。</li></ol><p class="usage-note">记录 AI 意识并在 Spatial/Timing Insights 中可视化。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AI Awareness Insights</code> (runtime <code class="usage-code">AIAwarenessTrace</code>, editor <code class="usage-code">AIAwarenessInsights</code>), part of Insights.</li><li>It records AI awareness (noise, perception, alert levels) and visualizes it in Spatial and Timing Insights.</li><li>When debugging AI, capture a trace, then inspect perception ranges and alert changes in Unreal Insights&#x27; Spatial/Timing views.</li><li>Game modules depend on <code class="usage-code">AIAwarenessTrace</code>; <code class="usage-code">AIAwarenessInsights</code> is Editor-target only.</li></ol><p class="usage-note">Records AI awareness and visualizes it in Spatial/Timing Insights.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AIAwarenessTrace</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AIAwarenessInsights</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/AI/AIAwarenessInsights/AIAwarenessInsights.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
