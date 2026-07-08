---
layout: default
title: Blutility
---

<!-- ai-generation-failed -->

<h1>Blutility</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Blutility/Blutility.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetDefinition, AssetRegistry, AssetTools, AutomationController, BlueprintGraph, ClassViewer, CollectionManager, ContentBrowser, ContentBrowserData, Core, CoreUObject, DeveloperSettings, EditorFramework, EditorSubsystem, EditorToolEvents, EditorViewport, Engine, ImageWrapper, ImageWriteQueue, InputCore, Json, JsonUtilities, Kismet, KismetCompiler, MainFrame, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolMenus, ToolWidgets, UMG, UMGEditor, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

s Editor Utility Blueprints. It allows developers to create Blueprint-based tools that execute logic within the Unreal Editor environment rather than during gameplay.

What it is and What it’s used for

The term “Blutility” (Blueprint Utility) refers to the C++ module that enables the creation of UEditorUtilityObject and related classes. It is the bridge that allows Blueprints to access editor-only functions, such as asset manipulation, actor placement, and batch processing.

Primary uses include:

Editor Scripting: Creating custom buttons and logic to automate repetitive tasks in the Level Editor.
Asset Management: Renaming, moving, or modifying properties of thousands of assets in the Content Browser via a single click.
Custom Tooling: Building specialized UI panels (Editor Utility Widgets) to help level designers or technical artists manage complex scenes.
Validation: Running scripts to check for naming convention errors or missing collision before a project is packaged.
Practical Usage Tips and Best Practices
1. Transition to Editor Utility Blueprints

While the module is named Blutility, you should primarily create Editor Utility Blueprints (EUB) or Editor Utility Widgets (EUW) via the “Editor Utilities” menu in the Content Browser. This modern workflow replaces the older “Blutility” shelf and provides a more robust interface for tool creation.

2. Use “Call in Editor” Functions

To create a simple tool quickly, add a Function to an Actor or an Editor Utility Blueprint and check the Call in Editor checkbox in the function’s details. This exposes a button in the Actor’s details panel, allowing you to trigger logic (like “Snap to Floor” or “Randomize Rotation”) without entering Play Mode.

3. Leverage the Editor Utility Subsystem

In C++ or Blueprints, use the UEditorUtilitySubsystem to manage your tools. This subsystem allows you to programmatically spawn and register tabs for your Editor Utility Widgets, ensuring they are correctly saved and restored when the editor restarts.

4. Safely Access Selected Assets/Actors

Use the Get Selected Assets or Get Selected Level Actors nodes to make your tools context-sensitive. This allows you to build a tool once and apply it to whatever the artist currently has highlighted, significantly increasing efficiency and eliminating manual searching.

5. Handle “Run on Startup” Objects

You can configure specific Editor Utility Objects to run automatically when the project opens. By adding your utility class to the StartupObjects array in the Editor Utility Subsystem settings, you can ensure that custom validation or environment setup scripts are always active.

6. Minimize Side Effects with Undo

When modifying the world or assets via Blutility, always use the Modify node (or Modify() in C++) before making changes. This ensures the change is registered in the Editor’s Undo/Redo buffer. Without this, your script might make permanent changes that cannot be reversed without restarting the editor.

7. Avoid Hard Casting to Gameplay Classes

Editor Utility Blueprints should remain decoupled from your specific gameplay classes whenever possible. Use Blueprint Interfaces to communicate between your editor tools and your game actors. This prevents your utility tools from creating “Circular Dependencies” that can slow down compilation.

8. Use Asset Tags for Metadata

Use Blutility scripts to read and write Asset Registry Tags. This is incredibly useful for technical artists to “tag” assets as “Optimized” or “Needs Review,” allowing you to build custom filters in the Content Browser that go beyond standard folder structures.