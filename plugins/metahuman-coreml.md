---
layout: default
title: 元人类 CoreML / MetaHuman CoreML
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">MetaHuman CoreML</div>
      <div class="hero-title-cn">元人类 CoreML · Apple 平台上 MetaHuman 推理的 CoreML 模</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>MetaHuman</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">0</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MetaHuman/MetaHumanCoreML/MetaHumanCoreML.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Apple 平台上 MetaHuman 推理的 CoreML 模型和依赖项。</div><div class="lang-content">CoreML models and dependencies for MetaHuman inference on Apple platforms.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MetaHuman CoreML</code> 插件（无独立模块列表），面向 Apple 平台。</li><li>它提供 MetaHuman 推理所需的 CoreML 模型与依赖，在 macOS/iOS 上走 CoreML 推理。</li><li>随 MetaHuman 面捕/推理相关插件在 Apple 平台上一起使用。</li><li>这是平台推理资源包，非 Apple 平台不需要。</li></ol><p class="usage-note">Apple 平台 MetaHuman 推理的 CoreML 模型/依赖包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the <code class="usage-code">MetaHuman CoreML</code> plugin (no standalone module list) for Apple platforms.</li><li>It provides the CoreML models and dependencies for MetaHuman inference, using CoreML on macOS/iOS.</li><li>Use it alongside MetaHuman face-capture/inference plugins on Apple platforms.</li><li>It is a platform inference asset pack; not needed on non-Apple platforms.</li></ol><p class="usage-note">A CoreML model/dependency pack for MetaHuman inference on Apple platforms.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MetaHuman/MetaHumanCoreML/MetaHumanCoreML.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
