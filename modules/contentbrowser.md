---
layout: default
title: ContentBrowser
---

<!-- ai-generation-failed -->

<h1>ContentBrowser</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ContentBrowser/ContentBrowser.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AddContentDialog, AppFramework, ApplicationCore, AssetDefinition, AssetRegistry, AssetTagsEditor, AssetTools, ContentBrowserData, Core, CoreUObject, DesktopPlatform, DeveloperSettings, Documentation, EditorConfig, EditorFramework, EditorStyle, EditorWidgets, Engine, InputCore, Projects, Slate, SlateCore, SourceControl, SourceControlWindows, StatusBar, TelemetryUtils, ToolMenus, ToolWidgets, TypedElementFramework, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

framework for managing, searching, and interacting with assets within the Unreal Editor.

Description and Purpose

This module defines the Content Browser UI and its underlying asset discovery systems. It provides the IContentBrowserModule interface, which allows developers to programmatically interact with the editor’s asset management tools. Its primary purpose is to provide a unified workspace where developers can import, organize, filter, and perform bulk operations on assets (such as Blueprints, Meshes, and Materials). It also manages the Content Drawer, asset collections, and the integration of C++ classes into the asset view.

Practical Usage Tips and Best Practices
Access via Singleton in C++
To interact with the Content Browser in editor-only code, use FModuleManager::LoadModuleChecked<IContentBrowserModule>("ContentBrowser"). This gives you access to the Get() method, allowing you to trigger asset syncs, open specific folders, or create custom asset pickers in your own editor windows.
Utilize Advanced Search Syntax
The search bar supports powerful metadata filtering. You can type Triangles > 1000 or Vertices < 500 to find unoptimized meshes. Using these filters helps you quickly identify and eliminate high-poly assets that may be causing performance bottlenecks in your levels.
Create Local and Shared Collections
Use Collections to group assets without moving them on the disk. This is ideal for managing a set of related assets, like all “Impact VFX” used for a player elimination. Shared collections are particularly useful in team environments to ensure everyone is using the correct, approved version of an asset.
Leverage the Content Drawer (Ctrl+Space)
In UE5, the Content Drawer provides a non-intrusive way to access assets. Use the “Dock in Layout” option only when performing heavy organization tasks. Otherwise, keeping it as a pop-up helps eliminate screen clutter, providing more room for the Viewport and Blueprint Editor.
Set Folder Colors for Organization
Right-click any folder and select Set Color. This visual shorthand is excellent for quickly identifying critical folders (e.g., Red for “Core Logic,” Green for “Environment”). This practice helps eliminate the time spent reading folder names in large, complex directory structures.
Use “Bulk Edit via Property Matrix”
If you need to change settings across dozens of assets—such as adjusting the “Compression Settings” on a hundred textures—select them all, right-click, and choose Asset Actions > Bulk Edit via Property Matrix. This allows you to eliminate the tedious task of opening and saving assets individually.
Filter by “Referenced By”
To find unused assets that should be eliminated before packaging, use the “Filters” menu or the Reference Viewer. By identifying assets that have zero “In-Referencers,” you can significantly reduce your final build size and clean up your project structure.
Integration with Fab
When bringing in new assets from Fab, use the Content Browser’s import settings to ensure textures and meshes are assigned to the correct project sub-folders. Proper initial organization in the Content Browser is the best way to eliminate “technical debt” caused by disorganized asset paths later in development.