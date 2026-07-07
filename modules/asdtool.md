---
layout: default
title: ASDTool
---

<!-- ai-generation-failed -->

<h1>ASDTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Windows/ASDTool/ASDTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ASDCore, ApplicationCore, Core, CoreUObject, D3D12RHI, DerivedDataCache, DistributedBuildInterface, PakFile, PakFileUtilities, Projects, RHI, RHICore, RenderCore, SQLiteCore, ShaderCompilerCommon, UbaController</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

al Engine C++ API (up to version 5.6). It is highly likely that this refers to a custom internal module, a third-party plugin, or is a typographical error for one of the following official modules:

AssetTools: The standard module for managing assets (creating, importing, and renaming).
TextAssetTool: A commandlet-based tool used for managing text-based asset formats.
AssetManager: The primary system for handling asset auditing and loading.

If you intended to inquire about AssetTools (the most likely candidate for general development), here is a brief overview and best practices for that system.

AssetTools Overview (Likely Intended)

The AssetTools module is an Editor-only framework used to automate asset-related tasks. It provides a C++ interface (IAssetTools) to create new assets from factories, perform bulk renaming, and handle advanced logic like asset “diffing” or merging.

Practical Usage Tips and Best Practices
1. Accessing the Interface

To use the tools provided by this module, you must first load the module and then access the singleton interface.

C++
IAssetTools& AssetTools = FModuleManager::LoadModuleChecked<FAssetToolsModule>("AssetTools").Get();
Copy code
2. Automate Asset Creation

Use CreateAsset to bypass manual Editor clicks. This is ideal for pipeline tools where you want to generate hundreds of data assets or materials based on external JSON or CSV data.

3. Implement Advanced Naming Logic

When renaming assets, use RenameAssetsWithDialog. This handles the elimination of old redirectors and ensures that the “Fix Up Redirectors” process is suggested to the user, maintaining project integrity.

4. Differentiate Between Assets

DiffAssets is a powerful function within this module that allows you to programmatically trigger the visual diff tool between two different versions of an asset, which is essential for custom version control integrations.

5. Register Custom Asset Categories

If you are creating a new type of asset (e.g., a “DialogTree”), use RegisterAdvancedAssetCategory via this module to give your asset its own dedicated sub-menu in the “Right Click > Create” context menu of the Content Browser.

6. Safe Elimination of Assets

When programmatically deleting assets, don’t just delete the file. Use the AssetTools combined with the ObjectTools module to check for references. This ensures the proper elimination of the asset without leaving “Broken Reference” errors in other levels or blueprints.

7. Bulk Exporting

Use ExportAssets to automate the process of moving assets out of Unreal and into common formats (like FBX or TGA). This is highly useful for automated build pipelines that need to send assets to external processing tools.

8. Verify Module Dependencies

Ensure AssetTools is added to your Build.cs only for Editor targets.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AssetTools");

	}
Copy code

If “asdtool” refers to a specific private plugin or a tool unique to your organization, please provide further context so I can assist you more accurately.