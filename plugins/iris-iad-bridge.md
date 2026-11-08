---
layout: default
title: IAD桥梁杂志 / Iris IAD Bridge
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">I</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Iris IAD Bridge</div>
      <div class="hero-title-cn">IAD桥梁杂志 · 实现 IrisCore 异步加载扩展点，以在 Iris 加载复制</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Networking</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/IrisIADBridge/IrisIADBridge.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">实现 IrisCore 异步加载扩展点，以在 Iris 加载复制包之前安装点播内容。将所有 IoStore/按需知识保留在 IrisCore 之外。</div><div class="lang-content">Implements the IrisCore async-load extension point to install on-demand content before Iris loads a replicated package. Keeps all IoStore/on-demand knowledge out of IrisCore.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Iris 是较新的复制后端，用来替代或补充旧的 Actor 复制路径，面向大规模 Actor 与更细的复制粒度。联网项目要在 DefaultEngine.ini 里显式打开。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：IrisIADBridge。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Iris is the newer replication backend meant to replace or sit beside classic Actor replication, aimed at large actor counts and finer filtering. Net projects turn it on in DefaultEngine.ini.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: IrisIADBridge. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Iris IAD Bridge</code>（模块 <code class="usage-code">IrisIADBridge</code>）。</li><li>它实现 IrisCore 的异步加载扩展点，在 Iris 加载复制包之前安装按需内容（on-demand）。</li><li>把 IoStore/按需知识保留在 IrisCore 之外，由本桥接处理。</li><li>属 Iris 网络的按需内容扩展，需 Iris 启用。</li></ol><p class="usage-note">Iris 按需内容加载桥接，把 on-demand 逻辑移出 IrisCore。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Iris IAD Bridge</code> (module <code class="usage-code">IrisIADBridge</code>).</li><li>It implements the IrisCore async-load extension point to install on-demand content before Iris loads a replicated package.</li><li>It keeps IoStore/on-demand knowledge out of IrisCore and handles it in the bridge.</li><li>It is an on-demand content extension for Iris networking; requires Iris enabled.</li></ol><p class="usage-note">An Iris on-demand content bridge that keeps on-demand logic out of IrisCore.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">IrisIADBridge</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/IrisIADBridge/IrisIADBridge.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
