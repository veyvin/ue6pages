---
layout: default
title: 数据匠MVR / Datasmith MVR
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Datasmith MVR</div>
      <div class="hero-title-cn">数据匠MVR · 支持导入包含 MVR 内容的 .udatasmith 文件。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DatasmithMVR/DatasmithMVR.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持导入包含 MVR 内容的 .udatasmith 文件。</div><div class="lang-content">Enabled support to import .udatasmith files with MVR content.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持导入包含 MVR 内容的 .udatasmith 文件。</p><p>DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DatasmithMVRTranslator。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Enabled support to import .udatasmith files with MVR content.</p><p>DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DatasmithMVRTranslator. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>先在灯光设计软件（如 grandMA、Vectorworks）里导出 MVR 文件，再经 Datasmith 管线打包成带 MVR 内容的 <code class="usage-code">.udatasmith</code>。</li><li>启用 <code class="usage-code">Datasmith MVR</code>，连同 DMX 相关插件一起启用，然后重启编辑器。</li><li>导入 <code class="usage-code">.udatasmith</code> 后，<code class="usage-code">DatasmithMVRTranslator</code> 会把灯具、GDTF 参数和 DMX 地址解析成 DMX 库资产与灯具 Actor。</li><li>在 DMX 库面板（菜单 <code class="usage-code">Window → DMX → DMX Library</code>）里核对解析出的灯具型号、universe 与 patch 是否正确。</li><li>用 DMX 控制台或 DMX 预览驱动这些灯具，比对舞台布光与 MVR 设计是否一致。</li></ol><p class="usage-note">MVR 里灯具依赖 GDTF 描述；缺 GDTF 时灯具只能得到占位形状，需补齐 GDTF 再导入。</p></div><div class="lang-content"><ol class="usage-steps"><li>Export the MVR from your lighting design tool (grandMA, Vectorworks, etc.), then package it into a <code class="usage-code">.udatasmith</code> with MVR content through the Datasmith pipeline.</li><li>Enable <code class="usage-code">Datasmith MVR</code> together with the DMX-related plugins, then restart the editor.</li><li>On import, <code class="usage-code">DatasmithMVRTranslator</code> parses fixtures, GDTF parameters, and DMX addresses into DMX Library assets and fixture actors.</li><li>In the DMX Library panel (menu <code class="usage-code">Window → DMX → DMX Library</code>) verify the parsed fixture types, universes, and patch addresses.</li><li>Drive the fixtures from a DMX console or DMX preview and compare the stage lighting with the original MVR design.</li></ol><p class="usage-note">MVR fixtures rely on GDTF descriptions; missing GDTF yields placeholder shapes, so add the GDTF and reimport.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">DatasmithMVRTranslator</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DatasmithMVR/DatasmithMVR.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
