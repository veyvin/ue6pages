---
layout: default
title: Cadence场景图 / Cadence SceneGraph
---



<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence SceneGraph</div>
      <div class="hero-title-cn">Cadence场景图 · 跟踪玩家在 Cadence 状态缓存中拥有的 SceneGrap</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Physics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/CadenceSceneGraph/CadenceSceneGraph.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">跟踪玩家在 Cadence 状态缓存中拥有的 SceneGraph 实体，因此将其复制的变换与客户端对同一帧的预测进行比较，并通过重新模拟进行纠正；将 Cadence 复制的输入提供给服务器上的 Verse 输入以及各处的 own_input_component。</div><div class="lang-content">Tracks SceneGraph entities a player possesses in the Cadence state cache, so their replicated transforms are compared against the client's prediction for the same frame and corrected by a resimulation; feeds Cadence-replicated input to Verse input on the server and to possessed_input_component everywhere.</div></div></div>
    </div>
    
  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CadenceSceneGraph</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/CadenceSceneGraph/CadenceSceneGraph.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
