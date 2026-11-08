---
layout: default
title: DMX GDTF / DMX GDTF
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DMX GDTF</div>
      <div class="hero-title-cn">DMX GDTF · 使用虚幻引擎类型实现 GDTF 标准</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DMXGDTF/DMXGDTF.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用虚幻引擎类型实现 GDTF 标准</div><div class="lang-content">Implementation of the GDTF standard using Unreal Engine types</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用虚幻引擎类型实现 GDTF 标准</p><p>DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DMXGDTF, DMXGDTFTests, DMXZip。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implementation of the GDTF standard using Unreal Engine types</p><p>DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DMXGDTF, DMXGDTFTests, DMXZip. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">DMX Engine</code> 与 <code class="usage-code">DMX GDTF</code>（<code class="usage-code">DMXGDTF</code>、<code class="usage-code">DMXZip</code>；测试模块 <code class="usage-code">DMXGDTFTests</code> 不要进游戏）。</li><li>准备厂商 <code class="usage-code">.gdtf</code>（本质是 zip：模型、DMX 模式、几何），在 <code class="usage-code">DMX Library</code> 里用 GDTF 导入而不是手填几百个通道。</li><li><code class="usage-code">DMXZip</code> 负责解开 GDTF 容器；导入后检查 Fixture Type 的模式、几何和通道集是否齐全。</li><li>把导入的 Type 做成 Fixture Patch，挂到 <code class="usage-code">DMX Fixtures</code> Actor 或 Pixel Mapping 单元格。</li><li>需要回归时在 <code class="usage-code">Session Frontend &gt; Automation</code> 跑 <code class="usage-code">DMXGDTFTests</code>，不要把测试模块写进 <code class="usage-code">Build.cs</code>。</li><li>这是 GDTF 类型实现，不是灯台，也不是 Art-Net 端口配置。</li></ol><p class="usage-note">把 GDTF 标准解成 UE 的 Fixture Type；zip 解包走 `DMXZip`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">DMX Engine</code> and <code class="usage-code">DMX GDTF</code> (<code class="usage-code">DMXGDTF</code>, <code class="usage-code">DMXZip</code>; leave <code class="usage-code">DMXGDTFTests</code> out of the game).</li><li>Take a vendor <code class="usage-code">.gdtf</code> (a zip of models, DMX modes, geometry) and import it into a <code class="usage-code">DMX Library</code> instead of hand-authoring hundreds of channels.</li><li><code class="usage-code">DMXZip</code> unpacks the GDTF container; after import, check modes, geometry, and channel sets on the Fixture Type.</li><li>Create a Fixture Patch from that type and bind it to a <code class="usage-code">DMX Fixtures</code> actor or Pixel Mapping cells.</li><li>Run <code class="usage-code">DMXGDTFTests</code> from <code class="usage-code">Session Frontend &gt; Automation</code> when you need a regression; do not add the test module to <code class="usage-code">Build.cs</code>.</li><li>This is the GDTF type implementation, not a lighting desk or Art-Net port UI.</li></ol><p class="usage-note">Maps the GDTF standard onto UE Fixture Types; `DMXZip` unpacks the container.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">DMXGDTF</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXGDTFTests</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXZip</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DMXGDTF/DMXGDTF.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
