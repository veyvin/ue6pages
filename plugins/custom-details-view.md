---
layout: default
title: 定制详情查看 / Custom Details View
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Custom Details View</div>
      <div class="hero-title-cn">定制详情查看 · （无描述）</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/CustomDetailsView/CustomDetailsView.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">（无描述）</div><div class="lang-content">(no description)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：（无描述）</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：CustomDetailsView。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: (no description)</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: CustomDetailsView. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 的 Virtual Production 分组启用 <code class="usage-code">Custom Details View</code>（模块 <code class="usage-code">CustomDetailsView</code>）并重启；它是可嵌入的属性树工厂，不是关卡组件。</li><li>在你的编辑器/VP 模块 <code class="usage-code">Build.cs</code> 加入 <code class="usage-code">CustomDetailsView</code>，<code class="usage-code">#include &quot;CustomDetailsViewModule.h&quot;</code> 与 <code class="usage-code">ICustomDetailsView.h</code>。</li><li>调用 <code class="usage-code">ICustomDetailsViewModule::Get().CreateCustomDetailsView(FCustomDetailsViewArgs)</code> 拿到 <code class="usage-code">TSharedRef&lt;ICustomDetailsView&gt;</code>；在 <code class="usage-code">FCustomDetailsViewArgs</code> 里设 <code class="usage-code">bAllowSearch</code>、<code class="usage-code">bShowKeyable</code>、要排除的类别。</li><li>对选中的 <code class="usage-code">UObject</code>/<code class="usage-code">AActor</code> 调用 <code class="usage-code">SetObjects</code>，把返回的 Slate（<code class="usage-code">SCustomDetailsView</code>）塞进 Remote Control、nDisplay 或自研 VP 面板，而不是打开默认 <code class="usage-code">Details</code> 面板。</li><li>用 <code class="usage-code">FCustomDetailsViewItemId</code> / <code class="usage-code">GetRootItem</code> 只展开需要的属性路径；属性改完后走对象自己的事务，确认关卡里对应 Actor 已脏且可撤销。</li><li>不要把 <code class="usage-code">CustomDetailsView</code> 写进 Game Target；Shipping 包没有这套编辑器细节视图。</li></ol><p class="usage-note">VP 用的嵌入式 Details 控件，不是 Window 菜单里的独立工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Custom Details View</code> under <code class="usage-code">Edit &gt; Plugins</code> (Virtual Production, module <code class="usage-code">CustomDetailsView</code>) and restart. It is an embeddable property-tree factory, not a level component.</li><li>Add <code class="usage-code">CustomDetailsView</code> to your editor/VP module <code class="usage-code">Build.cs</code> and include <code class="usage-code">CustomDetailsViewModule.h</code> plus <code class="usage-code">ICustomDetailsView.h</code>.</li><li>Call <code class="usage-code">ICustomDetailsViewModule::Get().CreateCustomDetailsView(FCustomDetailsViewArgs)</code> to get a <code class="usage-code">TSharedRef&lt;ICustomDetailsView&gt;</code>; set <code class="usage-code">bAllowSearch</code>, <code class="usage-code">bShowKeyable</code>, and category filters on <code class="usage-code">FCustomDetailsViewArgs</code>.</li><li>Pass selected <code class="usage-code">UObject</code>/<code class="usage-code">AActor</code> instances to <code class="usage-code">SetObjects</code> and host the <code class="usage-code">SCustomDetailsView</code> widget inside Remote Control, nDisplay, or a custom VP panel instead of the default Details tab.</li><li>Use <code class="usage-code">FCustomDetailsViewItemId</code> / <code class="usage-code">GetRootItem</code> to expand only the property paths you need; edits go through the object&#x27;s transaction so the actor dirties and undo works.</li><li>Keep <code class="usage-code">CustomDetailsView</code> off Game targets; shipping builds do not host this editor details view.</li></ol><p class="usage-note">Embedded VP details widget, not a standalone Window-menu tool.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CustomDetailsView</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/CustomDetailsView/CustomDetailsView.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
