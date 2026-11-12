---
layout: default
title: 资产标签 / Asset Tags
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Asset Tags</div>
      <div class="hero-title-cn">资产标签 · 提供对运行时和编辑器脚本的资产标签和集合的高级管理和访问。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AssetTags/AssetTags.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">提供对运行时和编辑器脚本的资产标签和集合的高级管理和访问。</div><div class="lang-content">Provides high-level management and access to asset tags and collections for runtime and editor scripting.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：提供对运行时和编辑器脚本的资产标签和集合的高级管理和访问。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AssetTags。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Provides high-level management and access to asset tags and collections for runtime and editor scripting.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AssetTags. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用运行时插件 <code class="usage-code">Asset Tags</code>（模块 <code class="usage-code">AssetTags</code>）。</li><li>在内容浏览器用 Collections 把资产放进命名集合（共享集合才能进包被运行时读到）。</li><li>游戏模块 <code class="usage-code">Build.cs</code> 依赖 <code class="usage-code">AssetTags</code>，包含 <code class="usage-code">AssetTagsSubsystem.h</code>。</li><li>取 <code class="usage-code">GEngine-&gt;GetSubsystem&lt;UAssetTagsSubsystem&gt;()</code>（蓝图：<code class="usage-code">Asset Tags</code> 分类）。</li><li>运行时只用只读接口：<code class="usage-code">CollectionExists</code>、<code class="usage-code">GetCollections</code>、<code class="usage-code">GetAssetsInCollection</code>、<code class="usage-code">GetCollectionsContainingAsset</code>。</li><li>创建/增删集合成员改用编辑器的 Collection Manager Scripting；<code class="usage-code">UAssetTagsSubsystem</code> 上的写接口已弃用。</li><li>PIE/包装后用集合名拉资产列表，确认 Shared 集合已随内容煮入。</li></ol><p class="usage-note">运行时只读集合查询；本地/私有集合不会出现在 Shipping 包里。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the runtime plugin <code class="usage-code">Asset Tags</code> (module <code class="usage-code">AssetTags</code>).</li><li>In the Content Browser, add assets to named Collections (Shared collections are what cook for runtime).</li><li>Depend on <code class="usage-code">AssetTags</code> in the game module <code class="usage-code">Build.cs</code> and include <code class="usage-code">AssetTagsSubsystem.h</code>.</li><li>Get <code class="usage-code">GEngine-&gt;GetSubsystem&lt;UAssetTagsSubsystem&gt;()</code> (Blueprint: Asset Tags category).</li><li>At runtime use read-only APIs: <code class="usage-code">CollectionExists</code>, <code class="usage-code">GetCollections</code>, <code class="usage-code">GetAssetsInCollection</code>, <code class="usage-code">GetCollectionsContainingAsset</code>.</li><li>Create or mutate collections with Collection Manager Scripting in editor; write methods on <code class="usage-code">UAssetTagsSubsystem</code> are deprecated.</li><li>In PIE or a cooked build, resolve assets by collection name and confirm Shared collections were cooked.</li></ol><p class="usage-note">Runtime read-only collection queries; Local/Private collections do not ship.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AssetTags</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AssetTags/AssetTags.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
