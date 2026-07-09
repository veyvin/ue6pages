---
layout: default
title: DetailCustomizations
---

<!-- ai-generation-failed -->

<h1>DetailCustomizations</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DetailCustomizations/DetailCustomizations.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, AdvancedPreviewScene, AdvancedWidgets, AnimGraph, AppFramework, ApplicationCore, AudioEditor, AudioSettingsEditor, BlueprintGraph, CinematicCamera, ClassViewer, ComponentVisualizers, ContentBrowser, Core, CoreUObject, DataTableEditor, DesktopPlatform, DesktopWidgets, DeveloperToolSettings, EditorFramework, EditorViewport, EditorWidgets, Engine, ExternalImagePicker, GraphEditor, HardwareTargeting, HeadMountedDisplay, InputCore, InternationalizationSettings, Json, JsonUtilities, Kismet, KismetWidgets, Landscape, LevelEditor, LevelSequence, MaterialEditor, MoviePlayer, MovieScene, MovieSceneCapture, MovieSceneTools, MovieSceneTracks, NavigationSystem, PhysicsCore, PropertyEditor, RHI, RenderCore, Sequencer, SettingsEditor, ShaderPlatformConfigEditor, SharedSettingsWidgets, SkeletonEditor, Slate, SlateCore, SourceCodeAccess, SourceControl, TargetPlatform, TimeManagement, ToolMenus, ToolWidgets, UnrealEd, VirtualTexturingEditor</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

to modify how properties appear in the Details Panel. While the engine uses reflection to display properties automatically, this module allows developers to override that behavior to create custom layouts, add interactive buttons, or group properties more logically. It is the primary tool for improving the “Quality of Life” for designers by providing bespoke, intuitive interfaces for complex C++ classes and structs.

Practical Usage Tips & Best Practices
1. Choose Between Class and Property Customization

The module provides two primary interfaces: IDetailCustomization for entire classes (Actors/Objects) and IPropertyTypeCustomization for specific structs.

Best Practice: If you have a custom struct (like FWeaponStats) used in many different Actors, use a Property Type Customization. This ensures a consistent UI across the entire project and leads to the elimination of redundant code in multiple class customizations.
2. Use “ForceRefreshDetails” Sparingly

You can trigger the Details Panel to rebuild itself using IDetailLayoutBuilder::ForceRefreshDetails(), which is useful for showing or hiding fields based on a checkbox.

Tip: Only call this when a value actually changes via a delegate. Excessive refreshing can cause the editor to flicker or lag, so proper logic here is essential for the elimination of UI performance bottlenecks.
3. Leverage “EditCategory” to Reorganize

Standard UPROPERTY macros use categories, but they appear in the order they are encountered.

Best Practice: Use DetailBuilder.EditCategory in C++ to explicitly set the order of categories. You can move important settings to the top and relegate advanced debugging tools to the bottom, facilitating the elimination of “clutter” for the end-user.
4. Add Custom Slate Widgets for Functionality

Details panels are not limited to text and numbers; you can embed any Slate widget, such as a “Bake Lighting” button or a “Preview” toggle.

Tip: Use AddCustomRow to insert a row that contains an SButton or SColorPicker. This allows designers to trigger complex logic directly from the panel, leading to the elimination of “hidden” setup steps or separate utility windows.
5. Safe Property Access via IPropertyHandle

Never try to access variables directly via pointers in a customization; use IPropertyHandle.

Best Practice: Handles manage the “Undo/Redo” buffer and multi-selection automatically. Using handles ensures that if a user changes a value, it is correctly recorded by the transaction system, which results in the elimination of “desync” bugs where the UI doesn’t match the actual object state.
6. Register and Unregister in the Editor Module

Customizations must be registered with the FPropertyEditorModule during the module’s startup.

Tip: Always unregister your layouts in ShutdownModule. Forgetting to do so can cause the editor to crash when it tries to call a customization from a module that has been unloaded, ensuring the elimination of “zombie” references during hot-reloads.
7. Filter Visibility with Metadata

You can use HideProperty or IDetailPropertyRow::Visibility to hide properties that aren’t relevant in certain states.

Best Practice: If a “Melee” weapon is selected, hide the “Ammo Count” property. Dynamic visibility leads to the elimination of confusion and prevents users from editing values that have no effect on the current object configuration.
8. Implement “CustomizeChildren” for Structs

When customizing a struct, you must decide how its internal variables are displayed.

Tip: If you don’t need a collapsible header, override CustomizeChildren but leave CustomizeHeader empty. This allows the struct’s properties to appear “flat” in the parent Actor’s details, which facilitates the elimination of unnecessary clicks and nested menus.