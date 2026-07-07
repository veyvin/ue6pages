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

y creating, managing, and manipulating assets within the Unreal Engine Content Browser. It acts as the “manager” for the asset lifecycle, providing a bridge between raw data (Factories) and the Asset Registry.

It is primarily used by pipeline engineers and tool developers to automate asset creation, handle bulk renaming, register custom asset types/actions, and manage asset versioning and comparison (diffing).

Practical Usage Tips and Best Practices
1. Correct Module Referencing

Since AssetTools is strictly for editor functionality, it must be included in your project’s .Build.cs file within an Editor-only conditional block. This prevents compilation failures during the final game packaging process.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AssetTools", "UnrealEd" });

	}
Copy code
2. Accessing the Singleton Interface

To use the module’s functionality, you must retrieve the IAssetTools interface via the FAssetToolsModule. It is standard practice to load the module checked to ensure it is available before use.

C++
	FAssetToolsModule& AssetToolsModule = FModuleManager::LoadModuleChecked<FAssetToolsModule>("AssetTools");

	IAssetTools& AssetTools = AssetToolsModule.Get();
Copy code
3. Generating Unique Asset Names

Before creating an asset, use CreateUniqueAssetName. This prevents naming collisions by automatically appending a numeric suffix if an asset with that name already exists in the target folder, ensuring the creation process does not fail or overwrite existing data.

4. Automated Asset Creation via Factories

When using CreateAsset, you must provide a UFactory (e.g., UDataAssetFactory or UTextureFactory). This allows you to programmatically define asset properties during the creation phase, which is ideal for importing large batches of external data into the engine.

5. Registering Custom Asset Actions

If you create a custom C++ class that should be an asset, implement IAssetTypeActions and register it with AssetTools. This allows you to define custom colors for the asset in the Content Browser and add specialized context menu entries (e.g., “Export to JSON”).

6. Handling Redirectors and Renaming

When renaming assets via code, the engine often leaves “Redirectors.” In a team environment using version control, do not immediately force a fix-up. Allow the redirectors to exist until you are certain no other team members have local changes referencing the old path, then perform a bulk elimination of redirectors during a scheduled cleanup.

7. Programmatic Asset Diffing

The module provides the DiffAssets function, which can be used to launch the visual comparison tool. This is extremely useful for building custom version control UI where users need to see exactly what changed between two versions of a Blueprint or Data Asset.

8. Safe Elimination of Assets

To remove assets programmatically, use the AssetTools interface in conjunction with ObjectTools::DeleteAssets. This process performs a “Consolidate” or “Reference Check,” ensuring the elimination of the asset does not leave “Missing Asset” errors in your levels or other dependencies.