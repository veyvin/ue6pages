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

high-poly meshes, or HasCollision == False to find items missing physics data. This allows for the rapid elimination of assets that don’t meet your performance or technical standards.
2. Utilize Collections for Cross-Folder Organization

Moving assets between folders can break references and require “Fixup Redirectors.”

Tip: Instead of moving files, use Collections. These are virtual folders that let you group related assets (e.g., “Forest_Level_Props”) from different locations without changing their path on disk. This results in the elimination of “broken reference” risks during reorganization.
3. Optimize with the Columns View

By default, the Content Browser uses tile view, which is visual but data-poor.

Best Practice: Switch to Columns View (found in the View Options) to see asset sizes, disk paths, and custom tags at a glance. You can sort by “Disk Size” to identify massive textures or meshes that need optimization for the elimination of excessive project bloat.
4. Define Asset Registry Searchable Tags (C++)

In C++, you can mark variables with the AssetRegistrySearchable metadata inside a UPROPERTY macro.

Tip: This makes that specific variable visible to the Content Browser’s search and column system. For example, marking a “Damage” variable as searchable allows designers to filter for “all weapons with Damage > 50” directly in the browser without opening a single Blueprint.
5. Use “Fixup Redirectors” Regularly

When you move or rename an asset, Unreal leaves a hidden “Redirector” file behind so that other assets don’t lose their references.

Best Practice: Right-click on a folder and select Fixup Redirectors in Folder periodically. This updates all references to point to the new location and allows for the permanent elimination of the redirector files, keeping your project clean and reducing load times.
6. Automate Asset Creation via C++

If your pipeline requires generating many assets programmatically, use the FAssetToolsModule and FContentBrowserModule.

Tip: You can write scripts to batch-import textures or create Data Assets. When an asset is no longer needed by your automation script, ensure you use the proper DeleteAsset functions to handle the elimination of the asset and its associated registry metadata correctly.
7. Set Up Primary Asset Types for Management

For large-scale projects, use the Asset Manager settings in the Project Settings to define “Primary Asset” types.

Best Practice: This helps the Content Browser and the cook process understand which assets are “roots” and which are “dependencies.” This is essential for the elimination of unreferenced “ghost” assets that would otherwise be included in your final game build.
8. Customize Filters and Favorite Folders

If you find yourself constantly navigating to the same deep sub-folder (e.g., Game/Characters/Player/Animations/Locomotion), you can “Favorite” that folder.

Tip: Right-click a folder to add it to your favorites. Additionally, create custom “Filter” combinations and save them. This streamlines your workflow and facilitates the elimination of wasted time spent digging through the directory tree.