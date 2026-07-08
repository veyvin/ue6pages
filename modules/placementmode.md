---
layout: default
title: PlacementMode
---

<!-- ai-generation-failed -->

<h1>PlacementMode</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PlacementMode/PlacementMode.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetTools, CollectionManager, ContentBrowser, ContentBrowserData, Core, CoreUObject, EditorFramework, EditorWidgets, Engine, InputCore, LevelEditor, Slate, SlateCore, ToolMenus, TypedElementFramework, TypedElementRuntime, UnrealEd, WidgetRegistration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

and UI for the Place Actors panel (typically found on the left side of the Unreal Editor). It provides the framework for categorizing, searching, and dragging-and-dropping actors into the 3D viewport.

This module is responsible for the registry of “Placeable” items. By using its API, developers can add custom categories and assets to the Place Actors panel, ensuring that frequently used project-specific actors (like custom triggers, gameplay volumes, or base classes) are immediately accessible. This facilitates the elimination of the need to repeatedly search through the deep folder structure of the Content Browser.

Practical Usage Tips and Best Practices
1. Register Custom Categories

Use the IPlacementModeModule interface to register your own categories. If your project has a specific set of “Gameplay Tools,” creating a dedicated tab leads to the elimination of visual clutter in the “All Classes” list, allowing level designers to find relevant tools much faster.

2. Set Category Priority

When registering a new category using FPlacementCategoryInfo, you can specify a SortOrder. A lower value puts your category closer to the top of the list. Strategic sorting assists in the elimination of excessive scrolling, placing the most vital project-specific assets at the designer’s fingertips.

3. Use Asset Tags for Automatic Filtering

The PlacementMode module can filter assets based on metadata tags. By tagging specific Blueprints or C++ classes, you can ensure they appear in the “Place Actors” panel only when appropriate. This practice leads to the elimination of non-placeable or “internal-only” assets from the UI, preventing designers from accidentally dragging broken actors into a level.

4. Register via StartupModule

If you are adding custom actors to the placement panel, perform the registration within the StartupModule() function of your editor module. This ensures that the assets are available as soon as the editor finishes loading, facilitating the elimination of “missing item” bugs that occur if registration is triggered too late.

5. Utilize Search Keywords

You can associate keywords with your placeable entries. Adding keywords like “light,” “vfx,” or “trigger” to a custom actor leads to the elimination of search failures, as the PlacementMode module will surface your actor even if the user doesn’t type its exact technical name.

6. Implement Custom Factory Logic

For complex assets that require specific initialization when dragged into the world, the PlacementMode module allows you to define a custom factory or “Actor Creator.” This leads to the elimination of manual post-placement setup, as you can automatically configure components or variables the moment the actor is dropped into the viewport.

7. Avoid Duplicate Registrations

Always check if a category or item is already registered before adding it to avoid duplicates in the UI. Implementing a check like IPlacementModeModule::Get().IsCategoryRegistered() leads to the elimination of redundant tabs and entries that can confuse the user and clutter the interface.

8. Leverage for Plugin Distribution

If you are developing a plugin for Fab, use the PlacementMode module to expose your plugin’s main actors. Providing a dedicated tab for your plugin leads to the elimination of friction for your users, making your plugin feel like a native, integrated part of the Unreal Engine toolset.