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

rovides the standard implementations and framework for overriding how properties and classes are displayed in the Details Panel.

Description and Purpose

This module contains the logic for creating custom UI layouts for the Unreal Editor. It utilizes the IDetailCustomization and IPropertyTypeCustomization interfaces to allow developers to replace the default vertical list of properties with bespoke Slate widgets. Its primary purpose is to improve the designer experience by hiding complex technical variables and providing intuitive controls—such as buttons, custom sliders, or visual feedback—directly within an Actor’s or Struct’s property view.

Practical Usage Tips and Best Practices
Register in the Correct Module Lifecycle
Customizations must be registered in your Editor module’s StartupModule and unregistered in ShutdownModule. Use FPropertyEditorModule::RegisterCustomClassLayout for Actors and RegisterCustomPropertyTypeLayout for Structs. Failing to unregister can lead to crashes, so always eliminate these references when the module is unloaded.
Prefer Property Handles Over Direct Access
Always use IPropertyHandle to read or write data within your customization. Property handles automatically manage undo/redo history, multi-selection, and transaction buffering. Using raw pointers to your object’s variables bypasses these systems and can eliminate the stability of the Editor’s state.
Force Refresh for Dynamic Layouts
If your UI needs to change based on a variable’s value (e.g., showing a “Target” field only when a “Use Target” bool is true), use IDetailLayoutBuilder::ForceRefreshDetails(). This triggers a rebuild of the panel, allowing you to hide or show rows dynamically to eliminate unnecessary clutter for the user.
Use Category Sorting for Better UX
In large classes, use IDetailCategoryBuilder::SetSortOrder() to prioritize the most important settings. By moving critical gameplay variables to the top and pushing debug settings to the bottom, you eliminate the time designers spend scrolling through hundreds of properties.
Add Utility Buttons for Common Tasks
You can add SButton widgets to the Details Panel to trigger logic. For example, add a “Reset Character” button that resets a player’s health after an elimination test. This allows designers to test specific scenarios instantly without needing to start a full PIE (Play In Editor) session.
Implement Header Customizations for Structs
When customizing a Struct via IPropertyTypeCustomization, use CustomizeHeader to create a compact, single-line representation of the data. This helps eliminate the vertical “expansion” of the Details Panel, making it much easier to manage arrays of complex data structures.
Utilize “EditCondition” Metadata
Before writing a full C++ customization, check if the EditCondition or InlineEditConditionToggle metadata specifiers in your UPROPERTY macro satisfy your needs. These built-in features can eliminate the need for custom Slate code if you only need simple enable/disable logic.
Avoid Heavy Logic in the Customization
The CustomizeDetails function is called whenever the selection changes. Avoid performing heavy calculations or asset loading inside this function. Instead, keep the logic focused on UI construction to eliminate “hitching” when users click between different Actors in the level.