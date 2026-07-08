---
layout: default
title: CollectionManager
---

<!-- ai-generation-failed -->

<h1>CollectionManager</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CollectionManager/CollectionManager.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, DeveloperSettings, DirectoryWatcher, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ganize project data.

As of UE 5.6, this system is primarily interfaced through the ICollectionManager singleton in C++ or the Collection Manager Scripting Subsystem in Blueprints, providing a robust way to automate asset organization.

Practical Usage Tips and Best Practices
Strict Editor-Only Dependency Since this module is removed during the packaging process, you must wrap its usage in WITH_EDITOR macros and place the dependency in an editor-only block in your Build.cs. Failing to do so will “eliminate” your ability to package the game for shipping.
C#
	    if (Target.Type == TargetType.Editor)

	    {

	        PublicDependencyModuleNames.AddRange(new string[] { "CollectionManager" });

	    }

	    ```

	 

	*   **Access via the Module Manager**  

	    The recommended way to access the API in C++ is by loading the module and retrieving the singleton interface. Always check if the module is available before use:

	    ```cpp

	    #include "CollectionManagerModule.h"

	    #include "ICollectionManager.h"

	 

	    FCollectionManagerModule& CMModule = FModuleManager::LoadModuleChecked<FCollectionManagerModule>("CollectionManager");

	    ICollectionManager& CollectionManager = CMModule.Get();

	    ```

	 

	*   **Understand Share Types (Local vs. Private vs. Shared)**  

	    Explicitly define the `ECollectionShareType` when creating collections. Use **Local** for personal organization, **Private** for source-controlled personal lists, and **Shared** for team-wide organization. This "eliminates" the risk of cluttering the shared project environment with temporary debug collections.

	 

	*   **Utilize for Automated Asset Validation**  

	    Incorporate the CollectionManager into your build pipeline to "eliminate" invalid assets. For example, write a script that finds all assets in a "To-Be-Fixed" collection and prevents the project from being cooked if that collection is not empty.

	 

	*   **Prefer Smart Collections for Large Projects**  

	    Instead of manually adding assets to static collections, use **Dynamic (Smart) Collections**. These use search queries to automatically include assets that meet specific criteria (e.g., "All textures larger than 2K"). This "eliminates" the manual maintenance of asset lists as the project grows.

	 

	*   **Handle Collection Name Collisions**  

	    Collections are identified by name and share type. Since multiple share types can have collections with the same name, always verify the existence of a collection using both the name and the `ECollectionShareType` to "eliminate" the logic targeting the wrong asset list.

	 

	*   **Integrate with UE 5.6 Content Containers**  

	    If your project uses modular features or "Metaverse" workflows, leverage the new **Collection Containers**. This allows you to associate collections with specific plugins or sub-projects rather than the base game, helping to "eliminate" dependency issues in modular architectures.

	 

	*   **Batch Operations for Performance**  

	    When adding or removing hundreds of assets from a collection, use the bulk API functions (like `AddToCollection` with a list of names) rather than iterating in a loop. This reduces the number of notifications sent to the Content Browser, "eliminating" editor UI hitches during large operations.
Copy code
Understand Share Types (Local vs. Private vs. Shared) Explicitly define the ECollectionShareType when creating collections. Use Local for personal organization, Private for source-controlled personal lists, and Shared for team-wide organization. This “eliminates” the risk of cluttering the shared project environment with temporary debug collections.
Access via the Module Manager The recommended way to access the API in C++ is by loading the module and retrieving the singleton interface. Always check if the module is available before use:
C#
	    if (Target.Type == TargetType.Editor)

	    {

	        PublicDependencyModuleNames.AddRange(new string[] { "CollectionManager" });

	    }

	    ```

	 

	*   **Access via the Module Manager**  

	    The recommended way to access the API in C++ is by loading the module and retrieving the singleton interface. Always check if the module is available before use:

	    ```cpp

	    #include "CollectionManagerModule.h"

	    #include "ICollectionManager.h"

	 

	    FCollectionManagerModule& CMModule = FModuleManager::LoadModuleChecked<FCollectionManagerModule>("CollectionManager");

	    ICollectionManager& CollectionManager = CMModule.Get();

	    ```

	 

	*   **Understand Share Types (Local vs. Private vs. Shared)**  

	    Explicitly define the `ECollectionShareType` when creating collections. Use **Local** for personal organization, **Private** for source-controlled personal lists, and **Shared** for team-wide organization. This "eliminates" the risk of cluttering the shared project environment with temporary debug collections.

	 

	*   **Utilize for Automated Asset Validation**  

	    Incorporate the CollectionManager into your build pipeline to "eliminate" invalid assets. For example, write a script that finds all assets in a "To-Be-Fixed" collection and prevents the project from being cooked if that collection is not empty.

	 

	*   **Prefer Smart Collections for Large Projects**  

	    Instead of manually adding assets to static collections, use **Dynamic (Smart) Collections**. These use search queries to automatically include assets that meet specific criteria (e.g., "All textures larger than 2K"). This "eliminates" the manual maintenance of asset lists as the project grows.

	 

	*   **Handle Collection Name Collisions**  

	    Collections are identified by name and share type. Since multiple share types can have collections with the same name, always verify the existence of a collection using both the name and the `ECollectionShareType` to "eliminate" the logic targeting the wrong asset list.

	 

	*   **Integrate with UE 5.6 Content Containers**  

	    If your project uses modular features or "Metaverse" workflows, leverage the new **Collection Containers**. This allows you to associate collections with specific plugins or sub-projects rather than the base game, helping to "eliminate" dependency issues in modular architectures.

	 

	*   **Batch Operations for Performance**  

	    When adding or removing hundreds of assets from a collection, use the bulk API functions (like `AddToCollection` with a list of names) rather than iterating in a loop. This reduces the number of notifications sent to the Content Browser, "eliminating" editor UI hitches during large operations.
Copy code
Utilize for Automated Asset Validation Incorporate the CollectionManager into your build pipeline to “eliminate” invalid assets. For example, write a script that finds all assets in a “To-Be-Fixed” collection and prevents the project from being cooked if that collection is not empty.
Handle Collection Name Collisions Collections are identified by name and share type. Since multiple share types can have collections with the same name, always verify the existence of a collection using both the name and the ECollectionShareType to “eliminate” the logic targeting the wrong asset list.
Batch Operations for Performance When adding or removing hundreds of assets from a collection, use the bulk API functions (passing a TArray<FSoftObjectPath>) rather than iterating in a loop. This reduces the number of notifications sent to the Content Browser, “eliminating” editor UI hitches during large operations.
Integrate with UE 5.6 Content Containers If your project uses modular features or “Metaverse” workflows, leverage the new Collection Containers. This allows you to associate collections with specific plugins or sub-projects rather than the base game, helping to “eliminate” dependency issues in modular architectures.
Prefer Smart Collections for Large Projects Instead of manually adding assets to static collections, use Dynamic (Smart) Collections. These use search queries to automatically include assets that meet specific criteria (e.g., “All textures larger than 2K”). This “eliminates” the manual maintenance of asset lists as the project grows.