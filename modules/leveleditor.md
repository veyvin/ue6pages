---
layout: default
title: LevelEditor
---

<!-- ai-generation-failed -->

<h1>LevelEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/LevelEditor/LevelEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ActionableMessage, ActorPickerMode, Analytics, AppFramework, ApplicationCore, CommonMenuExtensions, ContentBrowser, Core, CoreUObject, DataLayerEditor, DerivedDataEditor, DerivedDataWidgets, DesktopPlatform, DeveloperSettings, DeveloperToolSettings, DeviceProfileServices, EditorFramework, EditorInteractiveToolsFramework, EditorSubsystem, EditorViewport, EditorWidgets, Engine, EngineSettings, EnvironmentLightingViewer, Foliage, HierarchicalLODUtilities, InputCore, InteractiveToolsFramework, Json, JsonUtilities, KismetWidgets, LauncherPlatform, LevelSequence, MaterialShaderQualitySettings, MessageLog, Projects, PropertyEditor, PropertyEditorToolkit, RHI, RenderCore, SceneOutliner, Slate, SlateCore, SourceControl, SourceControlWindows, StatusBar, SubobjectDataInterface, SubobjectEditor, ToolMenus, ToolWidgets, TypedElementFramework, TypedElementRuntime, UncontrolledChangelists, UnrealEd, UnsavedAssetsTracker, ZenEditor</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e for the Unreal Editor’s primary workspace where levels are constructed and actors are manipulated.

Description and Purpose

This module defines the UI and functionality for the main viewport, the toolbar, and the surrounding menus used during world building. It acts as the “glue” that connects various editor sub-systems—such as the Outliner, Details panel, and World Partition—into a cohesive interface. Its primary purpose is to manage the SLevelEditor Slate widget and provide extension points (via FLevelEditorModule) that allow developers to inject custom buttons, menus, and viewport overlays. By extending this module, you can eliminate repetitive manual tasks by creating bespoke tools tailored to your project’s specific level-design needs.

Practical Usage Tips and Best Practices
Extend Menus via ToolMenus
Instead of using legacy extenders, use the ToolMenus system to add buttons to the Level Editor’s main toolbar or right-click context menus. This is the modern way to eliminate hard-coded UI modifications, making your tools easier to maintain across engine updates.
Add Viewport Overlays for Debugging
Use the ILevelViewport::AddOverlayWidget interface to place custom Slate widgets directly over the 3D viewport. This is an excellent way to eliminate the need for print-to-log debugging by displaying real-time technical data (like memory usage or actor counts) directly in the designer’s field of view.
Register Custom Level Editor Commands
You can map C++ functions to specific hotkeys within the Level Editor by registering them with FLevelEditorCommands. Creating keyboard shortcuts for common tasks (like “Align Selected Actors to Floor”) helps you eliminate excessive mouse travel and speeds up the world-building process.
Listen for Actor Selection Changes
Bind to the OnActorSelectionChanged delegate provided by the module to trigger custom logic when a designer clicks an object. This allows you to automatically open specific tool windows or update custom HUDs, helping you eliminate the friction of searching for specific tools in the UI.
Utilize Viewport Client for Input Handling
If you are building a custom tool that requires clicking in the 3D scene (like a placement brush), interact with the FLevelEditorViewportClient. This allows you to capture mouse events and perform line traces against the world to eliminate imprecise object placement.
Minimize “Heavy” Slate Operations in Tick
The Level Editor UI is built on Slate. Avoid running expensive logic or deep searches in a widget’s Tick function. Instead, use event-driven updates to eliminate UI lag and ensure the viewport remains responsive at high frame rates.
Check Module Dependencies in Build.cs
When creating editor extensions, you must add "LevelEditor" to your PrivateDependencyModuleNames in your MyProjectEditor.Build.cs. Failing to do so will eliminate your ability to access the FLevelEditorModule header and result in linker errors.
Respect World Partition Streaming
When writing scripts that modify the level, be aware that not all actors may be loaded if World Partition is active. Use the module’s streaming queries to check actor availability. This helps you eliminate “Actor Not Found” errors when running batch operations on massive open-world maps.

Would you like a summary of the next reasonably large segment, such as the LevelInstanceEditor module?