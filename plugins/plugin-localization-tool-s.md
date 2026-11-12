---
layout: default
title: 插件本地化工具 / Plugin Localization Tool's
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Plugin Localization Tool's</div>
      <div class="hero-title-cn">插件本地化工具 · 当资产具有可本地化文本但其所属插件没有本地化目标时，在保存/预提</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Localization</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Editor/Localization/PluginLocalizationTools/PluginLocalizationTools.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">当资产具有可本地化文本但其所属插件没有本地化目标时，在保存/预提交期间发出警告，并提供一个窗口来编辑每个插件的本地化目标。</div><div class="lang-content">Warns during Save/Pre-Submit when an asset has localizable text but its owning plugin has no localization targets, and provides a window to edit each plugin's localization targets.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：当资产具有可本地化文本但其所属插件没有本地化目标时，在保存/预提交期间发出警告，并提供一个窗口来编辑每个插件的本地化目标。</p><p>编辑器或开发者插件，服务制作流程，默认不进 Shipping。</p><p>它打包的模块包括：PluginLocalizationTools。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Warns during Save/Pre-Submit when an asset has localizable text but its owning plugin has no localization targets, and provides a window to edit each plugin's localization targets.</p><p>An editor/developer plugin for the authoring pipeline; it does not ship by default.</p><p>It ships these modules: PluginLocalizationTools. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Plugin Localization Tool&#x27;s</code>（模块 <code class="usage-code">PluginLocalizationTools</code>）。</li><li>当资产含可本地化文本但所属插件没有本地化目标时，它在保存/预提交期间发出警告。</li><li>并用窗口编辑每个插件的本地化目标。</li><li>属编辑器本地化工具；服务制作流程。</li></ol><p class="usage-note">检查并编辑插件本地化目标（保存/预提交警告）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Plugin Localization Tool&#x27;s</code> (module <code class="usage-code">PluginLocalizationTools</code>).</li><li>It warns during Save/Pre-Submit when an asset has localizable text but its owning plugin has no localization targets.</li><li>It also provides a window to edit each plugin&#x27;s localization targets.</li><li>It is an editor localization tool for the authoring pipeline.</li></ol><p class="usage-note">Warns and edits plugin localization targets (Save/Pre-Submit).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">PluginLocalizationTools</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Editor/Localization/PluginLocalizationTools/PluginLocalizationTools.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
