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

anagement and automation within the Unreal Editor. It provides the IAssetTools interface, which allows developers to create, duplicate, rename, and organize assets via C++ or Python without manual interaction with the Content Browser.

It is essential for building pipeline tools, such as automated asset importers, bulk processors, or custom asset types that require specific creation logic.

1. Module Configuration

To use AssetTools in your C++ code, you must include the module in your editor-specific Build.cs file and load it via the FModuleManager.

C#
	// MyProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AssetTools", "UnrealEd", "AssetRegistry" });

	}
Copy code
C++
	// Accessing the interface in C++

	FAssetToolsModule& AssetToolsModule = FModuleManager::LoadModuleChecked<FAssetToolsModule>("AssetTools");

	IAssetTools& AssetTools = AssetToolsModule.Get();
Copy code
2. Practical Usage Tips & Best Practices
Use CreateUniqueAssetName for Safety

When automating asset creation, never hardcode the destination path. Use CreateUniqueAssetName() to check for existing files. This prevents accidental “elimination” or overwriting of existing data by automatically appending a numeric suffix (e.g., MyAsset_1) if a name collision occurs.

Modernize with UAssetDefinition (UE 5.2+)

In older versions of Unreal, custom assets were registered using IAssetTypeActions. In modern UE5 versions, you should use UAssetDefinition. This is a data-driven approach that defines the asset’s color, icon, and associated actions (like double-click behavior) in a more modular way, making it easier to maintain than the legacy interface.

Automate with Factories

When using CreateAsset(), you must provide a UFactory. If you are importing external files (like textures or CSVs), ensure you configure the factory’s properties (such as bEditorImport) before calling the creation function. This ensures the asset is initialized with the correct settings immediately upon creation.

Bulk Export and Migration

IAssetTools provides methods for exporting assets to disk. If you need to “eliminate” a dependency on the engine for a specific set of data, you can use ExportAssets() to batch-process objects into formats like .fbx, .obj, or .tga programmatically.

Manage Redirectors Correctly

Renaming or moving assets via RenameAssets() or RenameReferencingSoftTargets() will create Redirectors. Always follow up bulk move operations by calling the FixupRedirectors functions (found in the AssetRegistry or specialized commandlets) to keep your project structure clean and prevent broken references.

Filter Asset Pickers

When creating custom UI that allows a user to select an asset, use AssetTools in conjunction with FAssetPickerConfig. You can filter by class, tags, or even custom metadata, ensuring that the user can only select valid assets for your tool, “eliminating” potential runtime crashes from invalid input.

Efficient Asset Duplication

Use DuplicateAsset() to create variations of a template. This is significantly faster and safer than manually copying files on the OS level, as AssetTools ensures the internal Header and GUID of the new .uasset are correctly regenerated to avoid “Duplicate Package” errors.

Integration with the Asset Registry

AssetTools works best when paired with the Asset Registry. Before performing operations, use the registry to ensure the target package is fully loaded. If you attempt to manipulate an asset that the registry hasn’t indexed yet, the AssetTools functions may fail or return null pointers.