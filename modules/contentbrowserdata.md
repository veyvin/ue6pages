---
layout: default
title: ContentBrowserData
---

<!-- ai-generation-failed -->

<h1>ContentBrowserData</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ContentBrowserData/ContentBrowserData.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorSubsystem, Engine, Projects, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e files from a DAM system or virtual folders) into a single, cohesive interface.

Practical Usage Tips and Best Practices
1. Distinguish between AssetData and ContentBrowserItem

When writing editor tools, distinguish between FAssetData (Asset Registry) and FContentBrowserItem. A FContentBrowserItem is a polymorphic object that can represent an asset, a folder, or a custom external file. Use the Content Browser Data Subsystem to convert between these types when you need to interact with the UI selection.

2. Implement a Custom Data Source for Remote Assets

If your studio uses an external Digital Asset Management (DAM) tool or a cloud-based library (like Quixel Bridge), you can create a class inheriting from UContentBrowserDataSource. This allows you to display remote files in the Content Browser as if they were local assets, without needing to “eliminate” the user’s familiar workflow by forcing them into a separate plugin window.

3. Leverage Virtual Folders

The ContentBrowserData module supports Virtual Folders. You can use this to create “Logical Collections” that do not exist on the physical disk. This is a best practice for project organization, allowing you to group assets by “Biome,” “Character,” or “Strike Team” across multiple different plugin and game folders.

4. Use the Subsystem for Batch Operations

Instead of iterating through the Asset Registry, use the UContentBrowserDataSubsystem. It provides a unified API to perform actions like RenameItem, CopyItem, or DeleteItem across different data sources. This ensures that if you rename a “Virtual” asset, the specific logic for that data source is triggered correctly.

5. Utilize Item Data Interfaces for UI Customization

You can extend how items appear in the Content Browser by using Data Interfaces. By implementing interfaces on your custom items, you can define custom tooltips, thumbnail overlays, and “Discovery” logic. This is highly effective for “elimination” of confusion when dealing with custom file types that aren’t standard Unreal assets.

6. Optimize Path Querying

Querying thousands of items can be slow. The ContentBrowserData module uses a caching and tick-based discovery system. When searching for items programmatically, use FContentBrowserDataFilter to restrict your search to specific sources or paths. This prevents the engine from “eliminating” performance by scanning irrelevant data sources (like the entire C++ class hierarchy).

7. Handle Folder Events via Delegates

The module provides delegates for folder-level operations. If your tool needs to react when a user creates a new folder (e.g., to automatically generate a README or a specific sub-folder structure), bind to the OnItemDataUpdated delegates in the UContentBrowserDataSubsystem.

8. Validation and Path Safety

Because this module handles data from multiple sources (Disk, Memory, Remote), always validate paths using the module’s internal logic. Use PathUtils within the module to ensure that a “Virtual Path” is correctly mapped to a “Physical Path” before attempting any file-system operations, preventing the accidental “elimination” of data due to path mismatch.

C++ Module Dependency

To use this module in your Editor plugin, add it to your Build.cs:

C#
PublicDependencyModuleNames.AddRange(new string[] { "ContentBrowserData" });
Copy code
Common Header Includes
C++
	#include "ContentBrowserDataSubsystem.h"

	#include "ContentBrowserItem.h"

	#include "ContentBrowserDataSource.h"
Copy code
Performance Tip

When dealing with large selections in the Content Browser, always prefer using the FContentBrowserItem handles over resolving the full UObject. Resolving a UObject forces the asset to load into memory, which can “eliminate” your editor’s available RAM if you accidentally select thousands of high-resolution textures.