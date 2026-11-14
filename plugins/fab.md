---
layout: default
title: 极品 / Fab
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Fab</div>
      <div class="hero-title-cn">极品 · 制作插件</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.0.21</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Fab/Fab.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">制作插件</div><div class="lang-content">Fab Plugin</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：制作插件</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：Fab。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Fab Plugin</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: Fab. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Fab</code> 插件并重启，在编辑器主工具栏或 <code class="usage-code">Window</code> 菜单打开 Fab 面板。</li><li>在 Fab 面板登录 Epic 账号，搜索或浏览要用的资产、插件与工具。</li><li>获取/购买后，在面板里对该资产点 <code class="usage-code">Add to Project</code>，把它直接导入当前项目的内容浏览器。</li><li>导入后在内容浏览器定位新生成的资产目录，按需迁移到你项目自己的 <code class="usage-code">Content</code> 结构里整理。</li><li>若安装的是插件类产品，再到 <code class="usage-code">编辑 &gt; 插件</code> 确认已启用并重启，使其模块生效。</li><li>团队协作时把导入资产纳入版本管理，留意 Fab 资产的授权条款与体积，避免把大文件塞进仓库。</li></ol><p class="usage-note">Fab 面板内登录、获取资产后 `Add to Project` 直接导入；插件类产品还要去插件面板启用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the <code class="usage-code">Fab</code> plugin and restart, then open the Fab panel from the editor main toolbar or the <code class="usage-code">Window</code> menu.</li><li>Log in with your Epic account in the Fab panel and search or browse for the assets, plugins, and tools you need.</li><li>After acquiring/purchasing, click <code class="usage-code">Add to Project</code> on the asset in the panel to import it directly into the current project&#x27;s Content Browser.</li><li>Locate the newly created asset folder in the Content Browser and move things into your project&#x27;s own <code class="usage-code">Content</code> structure as needed.</li><li>If the product is a plugin, confirm it under <code class="usage-code">Edit &gt; Plugins</code> and restart so its modules take effect.</li><li>For team work, put imported assets under version control, watch Fab licensing terms, and check size so you do not commit huge files.</li></ol><p class="usage-note">Log in and acquire assets in the Fab panel, then `Add to Project` to import; plugin products still need enabling in the Plugins panel.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">Fab</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Fab/Fab.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
