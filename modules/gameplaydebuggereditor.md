---
layout: default
title: GameplayDebuggerEditor
---

<!-- ai-generation-failed -->

<h1>GameplayDebuggerEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/GameplayDebugger/GameplayDebuggerEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, DrawPrimitiveDebugger, EditorFramework, Engine, GameplayDebugger, InputCore, LevelEditor, PropertyEditor, RenderCore, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e Gameplay Debugger Tool (GDT). While the core GameplayDebugger module handles the runtime logic, replication, and data collection of debug information, the Editor module is responsible for the integration within the Unreal Editor environment.

Its primary roles include managing the GDT settings in the Project Preferences, registering the debugger’s functionality with the Editor’s viewport, and handling the “Simulation” mode logic. It provides the UI and configuration hooks that allow developers to eliminate guesswork when troubleshooting AI, Navigation, and Gameplay Ability System (GAS) data directly within the editor’s workspace.

Practical Usage Tips and Best Practices
Configure Categories in Project Settings
Use the Project Settings > Gameplay Debugger menu (managed by this module) to define your custom categories and input bindings. Setting these up early helps you eliminate confusion during playtests by ensuring that every team member uses the same hotkeys to toggle specific debug overlays.
Debug AI in “Simulate” Mode
Unlike standard PIE, “Simulate” mode requires specific viewport flags. The Editor module allows you to enable the Debug AI show flag. This is essential to eliminate the need for a possessed pawn to see AI paths, allowing you to fly the camera around the world and inspect behavior trees in real-time.
Extend the Editor UI with Custom Categories
You can use the IGameplayDebuggerEditor interface to register new editor-only categories. This is useful for tools that don’t need to replicate data to a client but do need to draw complex editor-specific visualizations, helping you eliminate cluttered debug text in your production code.
Utilize the ‘EnableGDT’ Console Command
If the default apostrophe (‘) key binding is blocked by other editor plugins, use the EnableGDT command in the console. The Editor module listens for this to initialize the debugger’s viewport overlay, which helps eliminate roadblocks when the standard input routing fails.
Adjust Extension Menu Visibility
Within the Editor module settings, you can toggle which extensions are visible by default. If your project does not use EQS (Environment Query System), you should disable that category in the editor settings to eliminate visual noise and save screen real estate for more relevant data.
Wrap Editor Logic in Module Guards
Because this module is strictly for the editor, any C++ code that references its classes or settings must be wrapped in #if WITH_EDITOR. Additionally, ensure it is only listed in the Editor dependency section of your .uplugin or .uproject to eliminate linker errors during the final packaging process.
Monitor GameplayDebuggerReplicator in the Outliner
When the debugger is active, the Editor module helps manage the AGameplayDebuggerReplicator actor. You can select this actor in the World Outliner during a PIE session to see its properties in the Details panel. This is a powerful way to eliminate bugs related to how debug data is being synchronized between the server and the local editor instance.
Use Spectator View for Better Perspective
While the debugger is active in the editor, press the Tab key to enter spectator mode. The Editor module’s integration ensures the debug data remains anchored to the selected actor even as you fly away, helping you eliminate perspective issues when checking long-distance AI navigation or perception ranges.