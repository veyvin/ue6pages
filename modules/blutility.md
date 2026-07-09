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

rs), and build custom UI panels that integrate directly into the Editor’s layout.

Core Components
Editor Utility Blueprints: Logic-only assets used for “Scripted Actions” (right-click menu items).
Editor Utility Widgets: UMG-based panels that can be docked anywhere in the Editor.
Editor Utility Objects: Background scripts that can run on startup or respond to specific Editor events.
Practical Usage Tips and Best Practices
1. Use the “Get Selected Assets” Node

The most common use for a Blutility script is acting upon a selection. Use the Get Selected Assets or Get Selected Actors nodes to create a loop. This allows you to perform batch operations—like “elimination” of unused components or bulk-editing properties—on hundreds of items instantly.

2. Leverage the Editor Utility Subsystem

In C++ or Blueprints, use the Editor Utility Subsystem to manage your tools programmatically. You can use it to spawn and register tabs for your Utility Widgets, ensuring that your custom tools are always accessible to the team via the “Tools” or “Windows” menu.

3. Run Logic on Editor Startup

You can configure an Editor Utility Object to run logic as soon as the project opens. By toggling “Run on Startup” in the Class Defaults and adding the asset path to your DefaultEditorPerProjectUserSettings.ini, you can automate environment checks or project-wide validation every time a developer starts work.

4. Access “Editor Only” Nodes

Blutility classes have access to a massive library of functions that are stripped out of shipping builds. This includes nodes for managing the Content Browser, modifying Level Sequences, and interacting with the Source Control API. If a node is missing in a standard Actor Blueprint, it is likely available here.

5. Implement “Scripted Actions” for Workflow

Create an Editor Utility Blueprint inherited from AssetActionUtility or ActorActionUtility. Any function marked as Call in Editor will appear in the right-click context menu under “Scripted Asset Actions.” This is ideal for team-specific workflows like “Auto-Generate Physics Asset” or “Fix Naming Conventions.”

6. Use Development-Only Notifications

Since Blutility tools are for developers, use the Export Text to Log or Show Message Dialog nodes instead of simple Print Strings. This ensures that the results of your automation (such as a summary of how many assets were processed) are visible and recorded in the Output Log.

7. Threading and Long-Running Tasks

If your Blutility script performs a heavy operation (like processing thousands of textures), it will freeze the Editor UI. To avoid this, use a Notification Item with a progress bar. For extremely long tasks, consider breaking the work into “chunks” to prevent the OS from thinking the Editor has crashed and “eliminating” the process.

8. Prevent Accidental Data Loss

Always use the Set Dirty node after modifying asset properties via a Blutility script. If you modify an asset’s data but don’t mark it as dirty, the changes may not be saved to disk, and the engine might “eliminate” your unsaved progress when the Editor closes.

Performance & Best Practices
Avoid Tick: Editor Utility Widgets can use Tick, but it is rarely necessary. Use event-driven logic (button clicks, selection changes) to keep the Editor responsive.
Transacting Actions: Wrap your logic in Begin Undo Transaction and End Undo Transaction nodes. This allows developers to “Undo” (Ctrl+Z) a batch operation if the script makes a mistake.
Validation: Always validate that your selection cast is successful. If your script expects a StaticMesh but the user selects a Material, the script should exit gracefully to prevent a crash.