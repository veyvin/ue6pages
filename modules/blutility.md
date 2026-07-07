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

rints and Editor Utility Widgets. It enables developers to extend the Unreal Editor’s functionality using Blueprint visual scripting. While standard Blueprints are designed for runtime gameplay, Blutility allows for “Editor Scripting”—tasks such as bulk-renaming assets, automating level layout, or creating custom dockable UI tool properties.

Essentially, it bridges the gap between the high-level Blueprint system and the low-level Editor API, allowing technical artists and designers to create complex tools without writing Slate C++ code.

Practical Usage Tips & Best Practices
1. Module Scoping in Build.cs

Because Blutility contains editor-only classes (like UEditorUtilityWidget), it must be scoped correctly in your Build.cs. Including it in a runtime module will cause packaging errors because the module is stripped during the build process.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "Blutility", "UMGEditor" });

	}

	```

	 

	#### 2. Accessing the Global Subsystem

	In C++, the `UEditorUtilitySubsystem` is your primary entry point for managing utility widgets. You can use it to programmatically spawn tabs or check if a specific utility is currently running.

	```cpp

	// Required: #include "EditorUtilitySubsystem.h"

	UEditorUtilitySubsystem* EditorUtilitySubsystem = GEditor::GetEditorSubsystem<UEditorUtilitySubsystem>();

	if (EditorUtilitySubsystem)

	{

	    EditorUtilitySubsystem->SpawnAndRegisterTab(MyWidgetAsset);

	}

	```

	 

	#### 3. Widget vs. Blueprint Distinction

	Understand the two primary classes in the module:

	*   **`UEditorUtilityWidget`**: Best for tools requiring a UI (buttons, sliders, text) that stays docked in the editor.

	*   **`UEditorUtilityBlueprint`**: Best for "Global" logic or context-menu actions (e.g., "Right-click assets to rename") that don't need a persistent window.

	 

	#### 4. Avoid Runtime Logic Pollution

	Never reference `Blutility` classes or functions in your `AActor` or `UActorComponent` logic intended for gameplay. If an Actor needs an editor-only helper, place that logic in a separate `UEditorUtilityBlueprint` and have it act *upon* the actor to keep your game binary lean and packageable.

	 

	#### 5. Use "Run" for Persistent States

	When creating a tool that monitors the editor (e.g., an auto-saver or a scene validator), use the **Run Editor Utility Widget** command. This instantiates the object and keeps it alive in the editor's memory. If you simply call a function on an asset, the object may be garbage collected immediately after execution.

	 

	#### 6. Leverage the Editor Scripting Utilities Plugin

	The Blutility module works best when paired with the **Editor Scripting Utilities** plugin (the `EditorScriptingUtilities` module). This provides the actual nodes/functions for high-level operations like "Delete Unused Assets" or "Set Static Mesh LODs," which the Blutility module then executes.

	 

	#### 7. Threading Limitations

	All Blutility and Editor Scripting operations must occur on the **Game Thread**. Attempting to perform asset bulk-edits or UI updates from a background thread via this module will result in editor instability or crashes, as the underlying Slate and AssetRegistry systems are not thread-safe.

	 

	#### 8. Utilize Startup Objects

	In the `Editor Utility Subsystem` settings (found in Project Settings), you can register **Startup Objects**. These are Blutility classes that the engine will automatically instantiate as soon as the editor loads. Use this for project-wide hooks, such as custom editor notifications or enforcing team-wide asset naming conventions on load.
Copy code
2. Widget vs. Blueprint Choice
Editor Utility Widgets: Use these when you need a persistent, dockable UI (buttons, sliders) to interact with the world.
Editor Utility Blueprints: Use these for “Global” or “Asset” actions. For example, creating a right-click context menu option to “Check for Missing Collisions” on selected assets is best done via an Editor Utility Blueprint.
3. Use the Editor Utility Subsystem

In C++, use the UEditorUtilitySubsystem to manage your tools. This subsystem handles the registration of tabs and allows you to programmatically spawn or close utility widgets.

C++
	// #include "EditorUtilitySubsystem.h"

	UEditorUtilitySubsystem* Subsystem = GEditor->GetEditorSubsystem<UEditorUtilitySubsystem>();

	Subsystem->SpawnAndRegisterTab(MyWidgetAsset);
Copy code
4. Leverage the “Run” Workflow

To keep an Editor Utility Widget active in the editor’s memory (to listen for events or keep a state), you must right-click the asset and select Run Editor Utility Widget. Simply opening the asset in the Blueprint Editor only opens the logic designer; it does not instantiate the tool for use.

5. Avoid Runtime Object References

Never store references to Blutility objects inside your AActor or UActorComponent classes intended for the final game. If an actor needs editor-only logic, have the Blutility script act on the actor rather than the actor calling into the Blutility module. This ensures the clean elimination of editor dependencies during the cooking process.

6. Utilize Startup Objects

In Project Settings > Editor > Editor Utility Subsystem, you can add “Startup Objects.” These are Blutility classes that run automatically when the editor opens. This is ideal for project-wide initialization, such as setting up custom console variables or enforcing naming conventions for the team.

7. Clean Up Latent Actions

Blutility scripts can trigger latent actions like “Delay.” Be careful with these in the editor context; if you close the utility widget while a latent action is pending, it can sometimes lead to ghost executions or crashes. Always try to use event-driven logic rather than long delays.

8. Use with Editor Scripting Utilities Plugin

The Blutility module provides the framework, but the Editor Scripting Utilities plugin provides the functions. Always enable this plugin alongside Blutility to gain access to powerful nodes like “Set Folder Path,” “Get Selected Assets,” and “Consolidate Assets.”