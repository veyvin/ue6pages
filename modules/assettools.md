---
layout: default
title: AssetTools
---

<!-- ai-generation-failed -->

<h1>AssetTools</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AssetTools/AssetTools.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AssetDefinition, AssetRegistry, ClassViewer, Core, CoreUObject, DeveloperSettings, DeveloperToolSettings, EditorFramework, Engine, EngineSettings, Foliage, InputCore, InterchangeCore, InterchangeEngine, Kismet, Landscape, MaterialEditor, PhysicsCore, PhysicsUtilities, Projects, PropertyEditor, RHI, Slate, SlateCore, SourceControl, ToolMenus, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ogrammatic creation, management, and manipulation of assets within the Unreal Engine environment. It provides the IAssetTools interface, which is the primary gateway for automating tasks that a developer would normally perform manually in the Content Browser.

This module is essential for pipeline engineers and tools developers building custom importers, automated asset creators, or batch processing scripts. It handles the “heavy lifting” of the asset lifecycle, including package creation, naming validation, and asset registration.

Practical Usage Tips and Best Practices
1. Include Editor-Only Module Dependencies

Since AssetTools contains logic that is stripped from the final game build, it must be added to your [Project].Build.cs within an Editor-only block to avoid packaging errors.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AssetTools", "UnrealEd", "ContentBrowser" });

	}
Copy code
2. Access via the Module Manager

To use the asset tools functionality, you must load the module and access the interface via the FAssetToolsModule singleton.

C++
	FAssetToolsModule& AssetToolsModule = FModuleManager::LoadModuleChecked<FAssetToolsModule>("AssetTools");

	IAssetTools& AssetTools = AssetToolsModule.Get();
Copy code
3. Use CreateUniqueAssetName for Safety

When generating assets via code, avoid hardcoding file paths. Use CreateUniqueAssetName to automatically append a suffix (like _1, _2) if an asset with that name already exists. This ensures the total elimination of “file already exists” errors during automated runs.

4. Register Custom Asset Type Actions

If you create a custom C++ class that should appear as a unique asset type in the Content Browser, you must register an IAssetTypeActions class with this module. This allows you to define the asset’s color, category, and what happens when it is double-clicked (e.g., opening a custom editor window).

5. Automate Asset Creation via Factories

Use the CreateAsset function in conjunction with a UFactory. This is the standard way to programmatically spawn Blueprints, Materials, or Data Assets. It ensures the asset is correctly initialized, marked as “dirty” for saving, and registered with the Asset Registry immediately.

6. Leverage RenameAssets and DuplicateAssets

When organizing your project, use the module’s built-in functions for renaming or duplicating. These functions are superior to simple file-system moves because they correctly handle “Redirectors,” ensuring that other assets referencing the original objects do not break.

7. Implement Asset Validation

Before performing bulk operations, use AssetTools to check if a package is currently locked or checked out in source control (like Perforce). This prevents the engine from attempting to modify read-only files, which can cause the editor to hang or crash during automated asset elimination or updates.

8. Diffing Assets Programmatically

The module provides DiffAssets, which allows you to programmatically trigger the visual diffing tool between two versions of an asset (e.g., two different Blueprints). This is highly useful for building custom version control tools within the Unreal Editor to help artists see exactly what changed between iterations.