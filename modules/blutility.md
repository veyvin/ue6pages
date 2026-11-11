---
layout: default
title: Blutility
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>B</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">Blutility</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">35 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">35</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Editor/Blutility/Blutility.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 35 个其他模块：AssetDefinition、AssetRegistry、AssetTools、AutomationController、BlueprintGraph、ClassViewer、CollectionManager、ContentBrowser、ContentBrowserData、Core、CoreUObject、DeveloperSettings、EditorFramework、EditorSubsystem、EditorToolEvents、EditorViewport、Engine、ImageWrapper、ImageWriteQueue、InputCore、Json、JsonUtilities、Kismet、MainFrame、PropertyEditor、RHI、 RenderCore、Slate、SlateCore、ToolMenus、ToolWidgets、UMG、UMGEditor、UnrealEd、WorkspaceMenuStructure。</div><div class="lang-content">This module depends on 35 other module(s): AssetDefinition, AssetRegistry, AssetTools, AutomationController, BlueprintGraph, ClassViewer, CollectionManager, ContentBrowser, ContentBrowserData, Core, CoreUObject, DeveloperSettings, EditorFramework, EditorSubsystem, EditorToolEvents, EditorViewport, Engine, ImageWrapper, ImageWriteQueue, InputCore, Json, JsonUtilities, Kismet, MainFrame, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolMenus, ToolWidgets, UMG, UMGEditor, UnrealEd, WorkspaceMenuStructure.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该模块依赖于 35 个其他模块：AssetDefinition、AssetRegistry、AssetTools、AutomationController、BlueprintGraph、ClassViewer、CollectionManager、ContentBrowser、ContentBrowserData、Core、CoreUObject、DeveloperSettings、EditorFramework、EditorSubsystem、EditorToolEvents、EditorViewport、Engine、ImageWrapper、ImageWriteQueue、InputCore、Json、JsonUtilities、Kismet、MainFrame、PropertyEditor、RHI、 RenderCore、Slate、SlateCore、ToolMenus、ToolWidgets、UMG、UMGEditor、UnrealEd、WorkspaceMenuStructure。</p><p>这是 Editor 模块，只在编辑器进程加载，不能链进 Game Target。</p><p>UBT 声明它还依赖：AssetDefinition, AssetRegistry, AssetTools, AutomationController, BlueprintGraph, ClassViewer, CollectionManager, ContentBrowser。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This module depends on 35 other module(s): AssetDefinition, AssetRegistry, AssetTools, AutomationController, BlueprintGraph, ClassViewer, CollectionManager, ContentBrowser, ContentBrowserData, Core, CoreUObject, DeveloperSettings, EditorFramework, EditorSubsystem, EditorToolEvents, EditorViewport, Engine, ImageWrapper, ImageWriteQueue, InputCore, Json, JsonUtilities, Kismet, MainFrame, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolMenus, ToolWidgets, UMG, UMGEditor, UnrealEd, WorkspaceMenuStructure.</p><p>This is an Editor module, loaded only in the editor process — do not link it into a Game target.</p><p>UBT also lists dependencies on: AssetDefinition, AssetRegistry, AssetTools, AutomationController, BlueprintGraph, ClassViewer, CollectionManager, ContentBrowser. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Blutility</code>：它是编辑器侧工具模块（编辑器 UI、面板、细节定制、资产编辑器）。位于 <code class="usage-code">Editor</code>，构建规则 <code class="usage-code">Editor/Blutility/Blutility.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">AssetDefinition</code>、<code class="usage-code">AssetRegistry</code>、<code class="usage-code">AssetTools</code>、<code class="usage-code">AutomationController</code>、<code class="usage-code">BlueprintGraph</code> 等。</li><li>部署：<code class="usage-code">Blutility</code> 编辑器模块，只能写进 *Editor.Build.cs 或编辑器插件，加进 Game Target 会链接失败。</li><li>怎么用：仅编辑器使用，写进 *Editor.Build.cs；重启后在 Window/Tools 菜单或资产编辑器里找对应面板。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;Blutility&quot; });</code>；对外暴露 <code class="usage-code">Blutility</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`Blutility`：它是编辑器侧工具模块（编辑器 UI、面板、细节定制、资产编辑器）；构建规则 `Editor/Blutility/Blutility.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Blutility</code>: it is an editor-side tool module (editor UI, panels, detail customization, asset editors). Located under <code class="usage-code">Editor</code>; build rule <code class="usage-code">Editor/Blutility/Blutility.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">AssetDefinition</code>, <code class="usage-code">AssetRegistry</code>, <code class="usage-code">AssetTools</code>, <code class="usage-code">AutomationController</code>, <code class="usage-code">BlueprintGraph</code> etc.</li><li>Placement: <code class="usage-code">Blutility</code> is a editor-only; put it in *Editor.Build.cs or an editor plugin — never a Game target.</li><li>How to use: editor-only; put it in *Editor.Build.cs. After restart, find the panel under Window/Tools or in the relevant asset editor.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;Blutility&quot; });</code>. Use Public when exposing <code class="usage-code">Blutility</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`Blutility`: it is an editor-side tool module (editor UI, panels, detail customization, asset editors); build rule `Editor/Blutility/Blutility.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (35)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">AssetDefinition</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AssetRegistry</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AssetTools</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AutomationController</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlueprintGraph</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ClassViewer</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CollectionManager</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ContentBrowser</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ContentBrowserData</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DeveloperSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorFramework</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorSubsystem</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorToolEvents</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorViewport</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ImageWrapper</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ImageWriteQueue</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InputCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">JsonUtilities</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Kismet</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MainFrame</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RHI</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RenderCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Slate</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SlateCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ToolMenus</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ToolWidgets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UMG</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UMGEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealEd</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WorkspaceMenuStructure</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Editor/Blutility/Blutility.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
