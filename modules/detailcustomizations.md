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

provides the standard implementation for customizing how properties and classes appear in the Details Panel.

Description

While Unreal Engine uses reflection (UPROPERTY) to automatically generate UI for variables, the DetailCustomizations module contains the specialized “Layout” logic that makes complex engine types (like Colors, Vectors, and Collision settings) look organized. It provides the base interfaces IDetailCustomization (for customizing an entire Actor/Object class) and IPropertyTypeCustomization (for customizing a specific Struct). This module is the primary tool for technical artists and tools engineers to create bespoke, user-friendly interfaces within the editor without writing raw Slate code for every individual field.

Practical Usage Tips and Best Practices
1. Register in the Editor Module

Detail customizations must be registered during the StartupModule phase of an Editor Module (not a Runtime module). Use FPropertyEditorModule::RegisterCustomClassLayout for classes or RegisterCustomPropertyTypeLayout for structs. Always ensure you unregister them during ShutdownModule to prevent memory leaks or crashes when the editor closes.

2. Use Property Handles, Not Raw Pointers

When manipulating data within a customization, always use IPropertyHandle. This interface provides a safe way to get and set values while automatically handling Undo/Redo and Multi-selection. Using raw pointers to your object’s data bypasses the engine’s transaction system and can lead to data corruption or crashes.

3. Leverage ForceRefreshDetails for Dynamic UI

If your UI needs to change based on a user’s selection (e.g., showing a “Texture” slot only if a “Use Texture” checkbox is ticked), call IDetailLayoutBuilder::ForceRefreshDetails(). You can bind this to a delegate using SetOnPropertyValueChanged on a property handle. This allows you to create reactive interfaces that eliminate unnecessary clutter.

4. Hide Default Properties to Reduce Noise

Use IDetailLayoutBuilder::HideProperty() to remove default engine properties that your users don’t need to see. This is a best practice for “Designer-Facing” tools where you want to simplify the interface and eliminate the risk of a user changing a critical internal variable by accident.

5. Group Properties into Custom Categories

Instead of letting every variable fall into the “Default” category, use DetailBuilder.EditCategory("My Category") to create logical groupings. You can also use SetSortOrder() on categories to ensure that the most important settings (like “Core Gameplay”) appear at the very top of the Details Panel.

6. Add Custom Slate Widgets

You can inject any Slate widget into the Details Panel using DetailCategoryBuilder.AddCustomRow(). This is ideal for adding “Utility Buttons” (e.g., a “Bake Lighting” or “Generate Points” button) directly into an Actor’s properties, providing a much faster workflow than searching through menus.

7. Handle Property Elimination Correctly

If you are customizing a struct that may be removed or “eliminated” from an array while the Details Panel is open, always check IPropertyHandle::IsValidHandle() before attempting to access its value. Accessing a handle for an eliminated property will return an error and can crash the editor if not handled gracefully.

8. Keep Customizations Lightweight

Since the Details Panel is rebuilt frequently (every time you click a different actor), avoid heavy computations or synchronous file loading inside CustomizeDetails. If you need to display complex data, cache it in a separate manager or use asynchronous loading to ensure the editor’s UI remains responsive and “snappy.”