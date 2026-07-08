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

Browser. It acts as a unified abstraction layer that decouples the user interface from the underlying data sources.

What it is and What it’s used for

Before UE5, the Content Browser was strictly tied to the Asset Registry and .uasset files. The ContentBrowserData module introduced a “Data Source” system that allows the engine to treat many different types of information (files on disk, virtual assets, C++ classes, or cloud-based content) as a single, consistent object called an FContentBrowserItem.

Primary uses include:

Data Abstraction: Providing a common interface for the UI to interact with diverse backends without knowing their specific implementation.
Virtual Folder Support: Creating “logical” hierarchies that don’t exist on disk (e.g., a “Recently Modified” or “Favorites” view).
Custom Asset Browsers: Enabling developers to create their own data sources (like an external library of textures) that appear natively in the Content Browser.
Advanced Filtering: Powering the unified search and filter system that can query across different modules and plugins simultaneously.
Practical Usage Tips and Best Practices
1. Transition to FContentBrowserItem

If you are writing editor tools, move away from using FAssetData as your primary handle. Use FContentBrowserItem instead. This ensures your tools will work not just with standard assets, but also with folders, C++ classes, and virtualized items provided by other plugins.

2. Access via the UContentBrowserDataSubsystem

To query data programmatically, always use the UContentBrowserDataSubsystem. This is the central hub for the module. You can use it to fetch items by path or filter, and it will automatically aggregate results from all registered data sources (Asset Registry, Class Registry, etc.).

3. Implement UContentBrowserDataSource for Custom Data

If your team uses an external database for assets (like a web-based library), inherit from UContentBrowserDataSource. This allows you to “inject” those external items into the Content Browser, making them searchable and draggable just like local .uasset files.

4. Use Virtual Paths for Stability

The module uses Virtual Paths (e.g., beginning with /All/). Always use the subsystem’s utility functions to convert between “Internal Paths” (like /Game/Textures) and “Virtual Paths.” This ensures your code remains compatible even if the engine’s internal folder mounting logic changes.

5. Efficient Filtering with FContentBrowserDataFilter

When searching for items, use the FContentBrowserDataFilter struct. This allows you to combine multiple criteria—such as item categories (Assets vs. Folders), class names, and custom metadata—into a single high-performance query processed by the subsystem.

6. Handle Item States Appropriately

Items in the modern Content Browser can have different states (e.g., Virtual, Loading, or Pending Delete). Before performing an operation, check the item’s capabilities using Item.GetCapabilities(). This prevents your scripts from attempting to “Edit” or “Delete” items that are read-only or in the process of being downloaded.

7. Leverage Batch Operations

When dealing with hundreds of items, use the batch processing functions provided by the subsystem. This is significantly more efficient than iterating through items and performing individual actions, leading to the elimination of UI “hitch” or freezing during heavy asset management tasks.

8. Listen for Data Changes

If your editor tool displays a list of assets, register for the OnItemsChanged delegate on the UContentBrowserDataSubsystem. This ensures your UI stays in sync when files are added, moved, or deleted elsewhere in the engine, providing a more professional and reactive user experience.