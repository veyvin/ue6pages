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

l Editor’s asset management system. It provides the framework for searching, filtering, and interacting with all assets within a project’s directory.

Description

This module defines the logic for the Content Browser and the Content Drawer UI panels. It handles the integration between the underlying AssetRegistry (which tracks asset metadata) and the Slate-based UI that developers use to browse folders. It allows developers to create custom filters, context menu extensions, and “Asset Definitions” that determine how different file types appear and behave. In Unreal Engine 5.x, this module also manages the PathView (folder tree) and the Collections system, which are essential for organizing large-scale projects.

Practical Usage Tips and Best Practices
1. Use the Content Browser Singleton

To interact with the Content Browser via C++, always access it through the IContentBrowserSingleton. You can retrieve this by loading the module: FModuleManager::LoadModuleChecked<FContentBrowserModule>("ContentBrowser").Get(). This singleton allows you to programmatically focus on specific folders, sync the browser to a list of assets, or open a “Save Asset” dialog.

2. Implement Custom Asset Filters

If your project has many specialized assets, you can create custom filters to help your team find what they need. Use FFrontendFilter to define logic that filters assets based on metadata, such as “Show only Textures with a resolution higher than 2048” or “Show only Blueprints that implement a specific Interface.” This is a best practice for eliminating visual clutter in complex projects.

3. Leverage Collections for Organization

Instead of moving files and risking broken references, use Collections. Collections are virtual folders that don’t change the file’s path on disk. You can manage these via the IContentBrowserSingleton::CreateCollection API. This allows developers to group related assets (e.g., “Forest Level Props”) across multiple folders without affecting the project structure.

4. Optimize with the Path Picker

If you are building an Editor Utility or a custom tool that needs a folder input, use the SContentBrowserPathPicker Slate widget. This provides a native-looking folder tree that is consistent with the rest of the editor. It includes built-in search functionality and handles the logic for showing/hiding engine or plugin content automatically.

5. Extend the Asset Context Menu

You can add custom actions to the right-click menu of assets by registering a FContentBrowserMenuExtensions delegate. For example, you could add a “Compress Texture” option that appears only when right-clicking a Texture asset. This allows you to integrate custom pipeline tools directly into the artist’s existing workflow.

6. Sync to Assets Programmatically

When a tool generates a new asset or performs a fix-up, it is a best practice to “ping” that asset for the user. Use the SyncBrowserToAssets function. This automatically scrolls the Content Browser to the specified assets and highlights them, eliminating the need for the developer to manually search for the output of a tool.

7. Safety During Asset Elimination

When writing tools that delete assets, you must ensure the Content Browser is updated correctly. Always use the ObjectTools::DeleteAssets or AssetViewUtils::DeleteAssets functions rather than manually deleting files from the disk. These functions handle the elimination of the asset from memory, check for references to prevent crashes, and update the Content Browser UI to reflect the elimination immediately.

8. Configure “Show Engine Content” Settings

In the Content Browser “Settings” menu (cog icon), you can toggle the visibility of Engine Content, Plugin Content, and C++ Classes. When developing tools, it is often helpful to keep these off to simplify the view, but you should toggle them on when you need to study how Epic implements their own core assets and systems.