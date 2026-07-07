---
layout: default
title: AssetTagsEditor
---

<!-- ai-generation-failed -->

<h1>AssetTagsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AssetTagsEditor/AssetTagsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

terface and high-level logic for managing Asset Collections and Asset Registry Tags. While the low-level data is handled by the AssetRegistry, this module is responsible for the “Manage Collections” context menu, the Collection view in the Content Browser, and the interaction between assets and their metadata tags.

Practical Usage Tips and Best Practices
1. Add to Editor-Only Build Dependencies

Because this module contains editor-specific UI and logic, it must be added to your Editor module’s Build.cs. Including it in a runtime module will cause packaging errors.

C#
	// In YourProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { 

	        "AssetTagsEditor", 

	        "CollectionManager",

	        "AssetRegistry"

	    });

	}

	```

	 

	#### 2. Transition to CollectionManagerScriptingSubsystem

	If you are writing C++ or Python scripts to automate asset organization, be aware that many older functions in the `AssetTagsSubsystem` are now deprecated.

	*   **Best Practice:** For UE 5.3 and later, use the `UCollectionManagerScriptingSubsystem`. It provides modern methods for creating, renaming, and adding assets to collections that are more robust and better integrated with source control.

	 

	#### 3. Leverage "Shared" Collections for Teams

	The module supports three types of collections: Local, Private, and Shared.

	*   **Best Practice:** Use **Shared Collections** for project-wide organization (e.g., "Ready for Lighting," "Alpha Prototypes"). Shared collections are saved in the `Content/Collections` folder as `.collection` files, allowing them to be checked into Source Control (Perforce/Git) so the whole team sees the same organization.

	 

	#### 4. Use AssetRegistrySearchable for Custom Metadata

	To make your custom C++ properties visible to the AssetTagsEditor and the Content Browser's filter system, use the `AssetRegistrySearchable` specifier.

	*   **Tip:** This allows you to filter and find assets based on their values without actually loading the asset into memory.

	```cpp

	UPROPERTY(EditAnywhere, AssetRegistrySearchable, Category = "ItemData")

	FString ItemRarity; // Now searchable/filterable in the Content Browser

	```

	 

	#### 5. Override GetAssetRegistryTags for Complex Data

	If you need to expose data that isn't a simple `UPROPERTY` (like the number of elements in an array or a bitmask), override `GetAssetRegistryTags` in your C++ class.

	*   **Best Practice:** This is the most efficient way to provide "tags" to the editor system. These tags are stored in the asset header and can be read by the `AssetTagsEditor` UI without the performance cost of a full asset load.

	 

	#### 6. Automate Asset Validation via Tags

	You can use the `AssetTagsEditor` logic to identify assets missing critical metadata.

	*   **Tip:** Write a utility that queries specific collections or tags. For example, you can create a "Dynamic Collection" that automatically gathers all Textures with a resolution higher than 2048 and mark them for review to optimize memory.

	 

	#### 7. Avoid "Dirtying" Assets for Organization

	One of the primary benefits of using Collections (managed by this module) over custom metadata variables is that adding an asset to a collection **does not** modify the asset file itself.

	*   **Best Practice:** Use Collections for temporary or workflow-based organization to avoid unnecessary check-outs or "dirtying" of source-controlled assets.

	 

	#### 8. Use Collections as Input for Build Tools

	If you have a custom build or export pipeline, you can use the `AssetTagsEditor` and `CollectionManager` to define your scope.

	*   **Tip:** Instead of hardcoding paths, have your tool process all assets in a collection named "ExportToMobile." This gives designers a simple, visual way to control what the build tool processes by simply dragging and dropping assets in the editor.
Copy code
2. Transition to CollectionManagerScriptingSubsystem

In recent versions (UE 5.3+), many functions previously associated with asset tags have migrated.

Best Practice: Use the UCollectionManagerScriptingSubsystem for modern C++ or Python scripts. It provides the current API for creating, renaming, or removing collections, replacing many deprecated functions in the older AssetTagsSubsystem.
3. Use Shared Collections for Team Workflows

The module supports Local, Private, and Shared collections.

Best Practice: Use Shared Collections for project-wide organization (e.g., “Assets for Elimination,” “Pending LOD Review”). These are saved in the Content/Collections folder and should be checked into Source Control so the entire team shares the same organization.
4. Leverage AssetRegistrySearchable for Custom Metadata

To make your custom C++ properties visible to the AssetTagsEditor and the Content Browser’s filter system, use the AssetRegistrySearchable specifier.

Tip: This allows you to find assets via tags without loading them into memory.
C++
	UPROPERTY(EditAnywhere, AssetRegistrySearchable, Category = "Gameplay")

	FString DamageType; // Searchable in the Content Browser via the AssetTags logic
Copy code
5. Override GetAssetRegistryTags for Complex Data

If you need to expose data that isn’t a simple UPROPERTY (like a calculated value), override GetAssetRegistryTags in your C++ class.

Best Practice: This is the most efficient way to provide tags to the editor. It allows the AssetTagsEditor to display information in the “View Options > Show Columns” menu without the performance hit of a full asset load.
6. Automate Organization with Dynamic Collections

The module supports “Dynamic Collections” which function like saved searches.

Tip: Create a dynamic collection for “High Poly Meshes” or “Missing Textures.” This automatically gathers assets based on their metadata tags, ensuring that problematic assets are never eliminated from your sight during the optimization phase.
7. Avoid Dirtying Assets for Organization

One of the primary advantages of the Collection system handled by this module is that it does not modify the asset file itself.

Best Practice: Use Collections for workflow organization (e.g., “To-Do List”) instead of adding temporary variables to your Blueprints. This avoids unnecessary file check-outs and prevents the “dirtying” of assets in Source Control.
8. Validate Tags via Asset Validation

You can combine this module’s logic with the UEditorValidator class to ensure assets are tagged correctly before they are allowed to be checked in.

Tip: Write a validator that checks if an asset belongs to at least one collection. This ensures that assets are properly categorized and reduces the risk of important content being accidentally eliminated or lost in a large project hierarchy.