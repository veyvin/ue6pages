---
layout: default
title: AssetRegistry
---

<!-- ai-generation-failed -->

<h1>AssetRegistry</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AssetRegistry/AssetRegistry.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, PakFile, Projects, TelemetryUtils, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

earchable database of metadata for all assets in an Unreal Engine project. It gathers information asynchronously from the headers of .uasset files without needing to load the full asset into memory.

It is primarily used for querying asset properties, such as finding all Blueprints that implement a specific interface, listing all textures above a certain resolution, or managing asset discovery in packaged games where a traditional file-system crawl is inefficient.

1. Query Assets Without Loading

The most powerful use of the Asset Registry is retrieving FAssetData instead of UObject*. This allows you to check asset names, paths, and custom tags across thousands of files instantly. Loading an asset consumes RAM; querying the registry does not. Always use IAssetRegistry::GetAssets() or GetAssetsByPath() before deciding to call LoadObject or StaticLoadObject.

2. Use FARFilter for Performance

When searching for assets, utilize the FARFilter struct. This allows you to combine multiple criteria (Package Paths, Class Names, Tags, and Recursion) into a single query.

Tip: Set bRecursivePaths = true if you want to search a folder and all its subfolders.
Tip: Use Filter.ClassPaths to find specific types (e.g., UStaticMesh::StaticClass()->GetClassPathName()).
3. Asynchronous Discovery Callbacks

The Asset Registry builds its database asynchronously when the Editor starts. If you write code that runs on startup, it may return empty results because the registry is still “discovering” files.

Best Practice: Bind to the OnFilesLoaded() delegate to ensure your logic only runs once the database is complete.
Code Example:
C++
	IAssetRegistry& AssetRegistry = FModuleManager::LoadModuleChecked<FAssetRegistryModule>("AssetRegistry").Get();

	AssetRegistry.OnFilesLoaded().AddRaw(this, &FMyClass::OnRegistryLoaded);
Copy code
4. Create Custom Searchable Tags

You can expose variables to the Asset Registry so they can be searched without loading the asset. Use the AssetRegistrySearchable UPROPERTY specifier.

Example: A UPROPERTY(AssetRegistrySearchable) variable called ItemRarity on a Data Asset allows you to find all “Legendary” items in your project in milliseconds using AssetData.GetTagValue<FString>("ItemRarity", OutValue).
5. Overriding GetAssetRegistryTags

For complex metadata that isn’t a simple variable (like a struct or calculated data), override GetAssetRegistryTags in your C++ class. This allows you to manually inject key-value pairs into the registry database when the asset is saved.

Note: Assets must be re-saved for new tags or changes in GetAssetRegistryTags to appear in the registry.
6. Runtime Asset Discovery

While primarily used in the Editor, the Asset Registry is available at runtime. In packaged builds, the registry is serialized into a development/binary file. This is essential for DLC systems or “Mod” support where the game needs to find new content added to specific folders after the game has been shipped.

7. Managing Memory and FAssetData

An FAssetData object contains a TagsAndValues map. In recent Unreal versions (5.x+), this is often stored as an FAssetDataTagMapSharedView.

Best Practice: Avoid copying FAssetData objects frequently in loops. Use references or pointers where possible to minimize memory overhead when processing large search results.
8. Handling Asset Elimination (Deletions)

If your system maintains a cache of assets (like a custom UI browser), you must listen for the OnAssetRemoved and OnAssetRenamed delegates. If an asset is eliminated or moved in the Content Browser, your internal list will contain “Stale” references. Syncing with these delegates ensures your tool remains accurate and prevents crashes when trying to load non-existent assets.