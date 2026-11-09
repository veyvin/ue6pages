---
layout: default
title: 数据图表 / Data Charts
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Data Charts</div>
      <div class="hero-title-cn">数据图表 · 根据数据表生成图表</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Misc</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DataCharts/DataCharts.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">根据数据表生成图表</div><div class="lang-content">Generate charts based on data tables</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：根据数据表生成图表</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DataCharts, DataChartsEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Generate charts based on data tables</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DataCharts, DataChartsEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Data Charts</code>（运行时 <code class="usage-code">DataCharts</code>，编辑器 <code class="usage-code">DataChartsEditor</code>）。</li><li>先建一张 <code class="usage-code">Data Table</code>：行结构含数值列（float/int）和用作类别轴的名字/枚举列，填入拍摄日志、镜头时长或设备读数。</li><li>内容浏览器新建 Data Chart 资产（<code class="usage-code">DataCharts</code>），指定源 <code class="usage-code">UDataTable</code>、系列列、图表类型（折线/柱状/散点）和坐标轴。</li><li>双击资产在编辑器图表视口核对系列；改 Data Table 行后刷新图表，确认虚拟制片仪表用的是表数据而不是手绘曲线。</li><li>需要进关卡/UMG 时用运行时 <code class="usage-code">DataCharts</code> 模块把同一数据源绑到图表控件；<code class="usage-code">DataChartsEditor</code> 只留在 Editor Target。</li><li>这是表驱动可视化，不要把它当成 Sequencer 曲线编辑器或 Control Rig 绘图工具。</li></ol><p class="usage-note">从 Data Table 出图，服务 VP 仪表；编辑器模块勿进游戏包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Data Charts</code> (runtime <code class="usage-code">DataCharts</code>, editor <code class="usage-code">DataChartsEditor</code>).</li><li>Create a <code class="usage-code">Data Table</code> whose row struct has numeric columns (float/int) plus a name/enum column for the category axis; fill shoot logs, shot durations, or device readings.</li><li>Create a Data Chart asset (<code class="usage-code">DataCharts</code>), point it at that <code class="usage-code">UDataTable</code>, pick series columns, chart type (line/bar/scatter), and axes.</li><li>Open the asset’s chart viewport; after editing table rows, refresh and confirm the VP dashboard reads table data, not hand-drawn curves.</li><li>For in-level/UMG use, bind the same source through the runtime <code class="usage-code">DataCharts</code> module; keep <code class="usage-code">DataChartsEditor</code> on Editor targets only.</li><li>This is table-driven visualization, not a Sequencer curve editor or Control Rig drawing tool.</li></ol><p class="usage-note">Charts from Data Tables for VP dashboards; keep the editor module out of the game package.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">DataCharts</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataChartsEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DataCharts/DataCharts.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
