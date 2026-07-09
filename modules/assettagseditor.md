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

vides the infrastructure for managing Asset Collections and Asset Tags. While the Asset Registry handles the low-level discovery of metadata, this module provides the high-level logic and UI components required to create, rename, and manage collections (static or dynamic) and manipulate asset metadata programmatically.

It is a vital component for pipeline engineers and technical artists who need to organize thousands of assets or create custom filtering systems for internal production tools.

Practical Usage Tips and Best Practices
Configure Editor Module Dependencies If you are developing custom editor tools or automation scripts in C++, you must add this module to your Editor.Build.cs. It is frequently used alongside CollectionManager and AssetRegistry.
C#
	    // In YourProjectEditor.Build.cs

	    if (Target.bBuildEditor)

	    {

	        PublicDependencyModuleNames.AddRange(new string[] { "AssetTagsEditor", "CollectionManager" });

	    }

	    ```

	 

	*   **Utilize the AssetTagsSubsystem for Scripting**

	    In UE5, most tagging tasks should be handled via the `UAssetTagsSubsystem`. This is accessible via C++, Blueprints, and Python, making it the standard way to "eliminate" manual tagging.

	    ```cpp

	    // C++ Example: Checking for a specific tag

	    UAssetTagsSubsystem* AssetTagsSubsystem = GEditor->GetEditorSubsystem<UAssetTagsSubsystem>();

	    TArray<FName> Collections = AssetTagsSubsystem->GetCollectionsContainingAssetData(MyAssetData);

	    ```

	 

	*   **Migrate to CollectionManager for Advanced Logic**

	    Note that in recent UE5 versions, many functions for creating and renaming collections have moved to the `CollectionManagerScriptingSubsystem`. If you find a function deprecated in `AssetTagsEditor`, check the Collection Manager for its replacement.

	 

	*   **Leverage `AssetRegistrySearchable` for Automatic Tagging**

	    You can create "tags" automatically by marking variables in your C++ classes with the `AssetRegistrySearchable` metadata. This allows the AssetTagsEditor and Content Browser to filter assets by these values without needing to load the actual asset file.

	    ```cpp

	    UPROPERTY(EditAnywhere, AssetRegistrySearchable, Category="Combat")

	    float EliminationDamage;

	    ```

	 

	*   **Use Dynamic Collections for Automatic Organization**

	    Instead of manually adding assets to tags, use **Dynamic Collections** (Smart Folders). These use the tags managed by this module to automatically group assets that meet specific criteria (e.g., "All Textures > 2048px" or "All Weapons with 'Fire' tag").

	 

	*   **Batch Process Tags via Python**

	    For large-scale project "clean-ups," use Python scripts to interface with this module. You can iterate through thousands of assets and apply organizational tags (like `Status.NeedsReview` or `Project.Phase2`) in seconds.

	 

	*   **Filter Builds using Asset Tags**

	    Use tags to "eliminate" development-only assets from your final cook. By tagging assets as `DevOnly`, you can write custom Cooker scripts that query the AssetTagsEditor to ensure those specific items are excluded from the shipping package.

	 

	*   **Verify Tag Integrity with Asset Registry Queries**

	    Since asset tags are stored in the asset header, they can sometimes become desynchronized if files are moved outside the editor. Regularly use the **Fix Up Redirectors** command and perform a "Rescan" in the Content Browser to ensure the tags managed by this module remain accurate.
Copy code
Utilize the AssetTagsSubsystem In modern UE5 versions, most tagging operations should be performed via the UAssetTagsSubsystem. This is accessible via C++, Blueprints, and Python. It provides a clean interface to “eliminate” manual asset organization by programmatically adding assets to collections based on specific criteria.
Migrate to CollectionManager for Advanced Logic Be aware that many collection-handling functions (like CreateCollection or AddAssetToCollection) have been transitioned from the AssetTags subsystem to the CollectionManagerScriptingSubsystem. If you find a function deprecated in the AssetTagsEditor context, look to the Collection Manager for its modern equivalent.
Leverage AssetRegistrySearchable Tags To make your custom data visible to the AssetTagsEditor without loading the asset, mark C++ variables with the AssetRegistrySearchable metadata. This allows the editor to filter assets (e.g., finding all weapons with an “Elimination” damage type) instantly.
C#
	    // In YourProjectEditor.Build.cs

	    if (Target.bBuildEditor)

	    {

	        PublicDependencyModuleNames.AddRange(new string[] { "AssetTagsEditor", "CollectionManager" });

	    }

	    ```

	 

	*   **Utilize the AssetTagsSubsystem for Scripting**

	    In UE5, most tagging tasks should be handled via the `UAssetTagsSubsystem`. This is accessible via C++, Blueprints, and Python, making it the standard way to "eliminate" manual tagging.

	    ```cpp

	    // C++ Example: Checking for a specific tag

	    UAssetTagsSubsystem* AssetTagsSubsystem = GEditor->GetEditorSubsystem<UAssetTagsSubsystem>();

	    TArray<FName> Collections = AssetTagsSubsystem->GetCollectionsContainingAssetData(MyAssetData);

	    ```

	 

	*   **Migrate to CollectionManager for Advanced Logic**

	    Note that in recent UE5 versions, many functions for creating and renaming collections have moved to the `CollectionManagerScriptingSubsystem`. If you find a function deprecated in `AssetTagsEditor`, check the Collection Manager for its replacement.

	 

	*   **Leverage `AssetRegistrySearchable` for Automatic Tagging**

	    You can create "tags" automatically by marking variables in your C++ classes with the `AssetRegistrySearchable` metadata. This allows the AssetTagsEditor and Content Browser to filter assets by these values without needing to load the actual asset file.

	    ```cpp

	    UPROPERTY(EditAnywhere, AssetRegistrySearchable, Category="Combat")

	    float EliminationDamage;

	    ```

	 

	*   **Use Dynamic Collections for Automatic Organization**

	    Instead of manually adding assets to tags, use **Dynamic Collections** (Smart Folders). These use the tags managed by this module to automatically group assets that meet specific criteria (e.g., "All Textures > 2048px" or "All Weapons with 'Fire' tag").

	 

	*   **Batch Process Tags via Python**

	    For large-scale project "clean-ups," use Python scripts to interface with this module. You can iterate through thousands of assets and apply organizational tags (like `Status.NeedsReview` or `Project.Phase2`) in seconds.

	 

	*   **Filter Builds using Asset Tags**

	    Use tags to "eliminate" development-only assets from your final cook. By tagging assets as `DevOnly`, you can write custom Cooker scripts that query the AssetTagsEditor to ensure those specific items are excluded from the shipping package.

	 

	*   **Verify Tag Integrity with Asset Registry Queries**

	    Since asset tags are stored in the asset header, they can sometimes become desynchronized if files are moved outside the editor. Regularly use the **Fix Up Redirectors** command and perform a "Rescan" in the Content Browser to ensure the tags managed by this module remain accurate.
Copy code
Automate Organization via Python The AssetTagsEditor module is highly compatible with the Unreal Python API. Use it to batch-process assets during import; for example, you can automatically tag all textures larger than 2048px with a “HighRes” tag or move them into a specific “NeedsOptimization” collection.
Use Dynamic Collections for Smart Filtering Instead of manually assigning tags, use this module’s logic to create Dynamic Collections. These act as “smart folders” that use queries to automatically include assets that meet certain tag criteria. This “eliminates” the risk of assets being left out of organizational structures as the project grows.
Exclude Development Assets from Builds You can use Asset Tags to “eliminate” debug or development-only assets from your final cook. By tagging assets as DevOnly, you can write a custom cook-rule or validation script that queries the AssetTagsEditor to ensure these files are never included in the shipping package.
Maintain Tag Integrity Asset tags are stored in the asset header. If you perform heavy tag manipulation, occasionally use the Fix Up Redirectors command and resave your assets. This ensures that the metadata tracked by the AssetTagsEditor remains synchronized with the physical files on disk.