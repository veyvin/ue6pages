---
layout: default
title: 所有 MetaHuman 工具集 / All MetaHuman Toolsets
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">All MetaHuman Toolsets</div>
      <div class="hero-title-cn">所有 MetaHuman 工具集 · 依赖于所有 MetaHuman 工具集插件的聚合器插件。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">0</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/AllMetaHumanToolsets/AllMetaHumanToolsets.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">依赖于所有 MetaHuman 工具集插件的聚合器插件。</div><div class="lang-content">Aggregator plugin that depends on all MetaHuman Toolsets plugins.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：依赖于所有 MetaHuman 工具集插件的聚合器插件。</p><p>MetaHuman 家族：数字人生成、面捕、校准或运行时绑定，建立在 Control Rig / Live Link 之上。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Aggregator plugin that depends on all MetaHuman Toolsets plugins.</p><p>MetaHuman family: digital-human generation, face capture, calibration, or runtime, on Control Rig / Live Link.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 聚合插件 <code class="usage-code">All MetaHuman Toolsets</code>（<code class="usage-code">AllMetaHumanToolsets.uplugin</code>，无独立运行时模块）。</li><li>它会依赖并拉起各 MetaHuman Toolset 插件；同时启用 <code class="usage-code">AI Assistant</code>，让助手拿到面捕/装配相关工具。</li><li>在 AI Assistant 里对 MetaHuman / Control Rig 资产提问或改绑定，确认工具来自被聚合的 Toolset，而不是 Quixel Bridge 窗口。</li><li>数字人生成、导出仍走 MetaHuman Creator / Bridge / <code class="usage-code">MetaHuman</code> 运行时插件；本项不会在内容浏览器创建 Character。</li><li>不要把它写进 Game <code class="usage-code">Build.cs</code>；Shipping 只保留真正的 MetaHuman 运行时插件。</li></ol><p class="usage-note">无模块的 Toolset 聚合器，只服务编辑器助手，不能替代 MetaHuman 内容管线。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental aggregator <code class="usage-code">All MetaHuman Toolsets</code> (<code class="usage-code">AllMetaHumanToolsets.uplugin</code>; no runtime modules of its own).</li><li>It pulls in every MetaHuman Toolset plugin; also enable <code class="usage-code">AI Assistant</code> so those face-capture/rig tools register.</li><li>Ask the assistant about a MetaHuman / Control Rig asset and confirm tools come from the aggregated toolsets, not the Quixel Bridge UI.</li><li>Authoring and export still go through MetaHuman Creator / Bridge / the <code class="usage-code">MetaHuman</code> runtime plugin; this does not create a Character in the Content Browser.</li><li>Do not add it to a game <code class="usage-code">Build.cs</code>; Shipping should keep only the real MetaHuman runtime plugins.</li></ol><p class="usage-note">Module-less toolset aggregator for the editor assistant; it does not replace the MetaHuman content pipeline.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/AllMetaHumanToolsets/AllMetaHumanToolsets.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
