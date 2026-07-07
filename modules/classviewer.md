---
layout: default
title: ClassViewer
---

<!-- ai-generation-failed -->

<h1>ClassViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ClassViewer/ClassViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, ContentBrowserData, Core, CoreUObject, EditorFramework, Engine, InputCore, PropertyEditor, Settings, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e editor—such as when choosing a parent class for a new Blueprint or selecting a class type in a Details panel property.

This module is essential for managing the engine’s vast class hierarchy, allowing developers to filter between C++ and Blueprint classes, find placeable actors, and examine class relationships.

1. Master the Global Search and Filters

The Class Viewer is the most efficient way to find classes when you aren’t sure of their exact name.

Best Practice: Use the Filters dropdown to restrict results to “Placeable” actors if you intend to drag them into the level, or “Blueprint Bases” if you are looking for a parent class. This eliminates clutter from internal engine classes and abstract base types.
2. Drag-and-Drop to Viewport or Details

You can drag any Actor class directly from the Class Viewer into the Level Editor viewport to spawn it.

Tip: You can also drag classes from the viewer into Class-type properties in the Details panel (such as a “Projectile Class” variable). If the class is compatible with the property’s restricted type, it will be assigned automatically.
3. Implement Custom Class Pickers in C++

If you are building a custom editor tool or a specialized Details panel, you can use the SClassViewer Slate widget to create a filtered class selection UI.

Tip: Use the FClassViewerInitializationOptions struct to define which classes are visible. For example, you can set bShowUnloadedBlueprints = true to ensure users can pick Blueprints that aren’t currently in memory.
4. Use IClassViewerFilter for Complex Logic

Standard class pickers often show too many options. To create a professional tool, implement the IClassViewerFilter interface.

Best Practice: Use a custom filter to only show classes that have specific metadata tags or those that implement a particular Blueprint Interface. This ensures that designers can only pick classes that are functionally valid for the specific tool you are building.
5. Quickly Access C++ Source Code

The Class Viewer provides a direct link between the editor and your IDE.

Tip: Right-clicking any C++ class in the viewer allows you to “Open C++ Header.” This is often faster than navigating through the Solution Explorer in Visual Studio or Rider, especially in large projects with many modules.
6. Examine the “Internal” Class Hierarchy

By default, the viewer hides many internal engine classes to keep the UI clean.

Tip: In the Class Viewer settings (the gear icon), toggle Show Internal Classes to see the full inheritance tree. This is incredibly helpful when you are trying to find the underlying C++ parent of a complex engine component or system.
7. Create Blueprints Directly from the Viewer

Instead of right-clicking in the Content Browser, you can right-click any class in the Class Viewer and select Create Blueprint Class based on….

Best Practice: This is the preferred way to create Blueprints from obscure C++ classes that don’t appear in the “Basic Classes” list of the New Blueprint dialog. It ensures you are inheriting from the exact class you’ve identified in the hierarchy.
8. Optimize Editor Performance with Class Filtering

In very large projects with thousands of Blueprints, the Class Viewer can occasionally hitch while scanning.

Tip: If you are using SClassViewer in a custom tool, use the NameFilterToValidateAgainst option. This allows the viewer to skip the initial scan of the entire class tree and only populate results that match your specific criteria, significantly improving the responsiveness of your custom UI.