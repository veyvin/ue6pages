---
layout: default
title: 数据流笔划字段 / Dataflow Stroke Field
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Dataflow Stroke Field</div>
      <div class="hero-title-cn">数据流笔划字段 · 数据流图的手绘方向、权重和弧长字段，通过在构造视口上绘图来创作。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/DataflowStrokeField/DataflowStrokeField.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">数据流图的手绘方向、权重和弧长字段，通过在构造视口上绘图来创作。</div><div class="lang-content">Hand drawn direction, weight and arc length fields for Dataflow graphs, authored by drawing over the construction viewport.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：数据流图的手绘方向、权重和弧长字段，通过在构造视口上绘图来创作。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：DataflowStrokeField, DataflowStrokeFieldEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Hand drawn direction, weight and arc length fields for Dataflow graphs, authored by drawing over the construction viewport.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: DataflowStrokeField, DataflowStrokeFieldEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 插件 <code class="usage-code">Dataflow Stroke Field</code>（<code class="usage-code">DataflowStrokeField</code> + <code class="usage-code">DataflowStrokeFieldEditor</code>），并确保 Dataflow 编辑器已开。</li><li>打开 <code class="usage-code">UDataflow</code> / Geometry Collection Dataflow 资产，切到 Construction 视口（不是关卡视口）。</li><li>在图中加入 Stroke Field 相关节点（方向场、权重场、弧长场），把输出接到形变、生长或沿切线分布的后续节点。</li><li>在 Construction 视口对着参考网格用鼠标/数位板涂抹笔划；笔划写入场采样，而不是画材质贴花。</li><li>求值 Dataflow，检查下游网格是否沿笔划方向拉伸/变密；擦除或重画笔划后再次求值。</li><li><code class="usage-code">DataflowStrokeFieldEditor</code> 只进编辑器；运行时若求值场数据，游戏模块最多依赖 <code class="usage-code">DataflowStrokeField</code>。</li><li>Experimental 场格式可能变，不要把笔划资产当作长期互换格式。</li></ol><p class="usage-note">在 Dataflow 构造视口手绘方向/权重/弧长场，不是关卡喷绘工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Dataflow Stroke Field</code> (<code class="usage-code">DataflowStrokeField</code> + <code class="usage-code">DataflowStrokeFieldEditor</code>) and make sure the Dataflow editor is on.</li><li>Open a <code class="usage-code">UDataflow</code> / Geometry Collection Dataflow asset and switch to the Construction viewport (not the level viewport).</li><li>Add Stroke Field nodes (direction, weight, arc length) and wire them into deform, grow, or tangent-scatter nodes.</li><li>Draw over the reference mesh in the Construction viewport with mouse or stylus; strokes write field samples, they are not material decals.</li><li>Evaluate the graph and check that downstream meshes stretch or densify along the stroke. Erase or redraw, then evaluate again.</li><li><code class="usage-code">DataflowStrokeFieldEditor</code> is editor-only; a game module may depend on <code class="usage-code">DataflowStrokeField</code> only if it evaluates stored fields at runtime.</li><li>The Experimental field format can change; do not treat stroke assets as a long-term interchange format.</li></ol><p class="usage-note">Hand-drawn direction/weight/arc-length fields in the Dataflow construction viewport, not a level spray tool.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowStrokeField</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowStrokeFieldEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/DataflowStrokeField/DataflowStrokeField.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
