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

Editor’s UI and viewport interactions.

It is primarily used to manage how the debugger behaves within Play In Editor (PIE) and Simulate modes, allowing developers to configure categories, toggle visibility, and “eliminate” the friction of switching between gameplay and debugging views.

Practical Usage Tips and Best Practices
Customize Debugger Categories
You can use this module to register custom debugger categories that are only relevant in the editor. This “eliminates” clutter in the shipping build while providing deep introspection of complex systems like procedural generation or custom physics during development.
Bind Activation Keys in Project Settings
If the default apostrophe (‘) key conflicts with your regional keyboard layout, navigate to Project Settings > Gameplay Debugger. Using this module’s settings page “eliminates” the need to manually edit .ini files to rebind the activation or category toggle keys.
Utilize the Debug AI Show Flag
In “Simulate” mode, the debugger behaves differently than in PIE. To “eliminate” confusion when it doesn’t appear, ensure the Debug AI show flag is enabled in the viewport’s “Show” menu. This module facilitates the link between that flag and the debugger’s rendering state.
Inspect the GameplayDebuggerReplicator
When the debugger is active, an actor named GameplayDebuggerReplicator is spawned. You can select this actor in the World Outliner during a PIE session to “eliminate” manual keypresses; you can toggle categories and adjust settings directly within its Details panel.
Add to Module Dependencies for Tooling
If you are writing an editor plugin that needs to manipulate the debugger’s state—such as a button that automatically selects a specific AI for debugging—you must add "GameplayDebuggerEditor" to your Build.cs. This “eliminates” linker errors when accessing editor-specific debugger delegates.
Debug Multi-User/Networking Locally
The debugger is fully replicated. Use the editor settings provided by this module to “eliminate” the difficulty of debugging clients. You can set the debugger to follow the “Local Player” or a “Selected Actor,” allowing you to see what the server perceives versus what the client sees in real-time.
Leverage Spectator Mode for Navigation
When the debugger is active, you can press Tab to enter a spectator view. This “eliminates” the restriction of the player camera, allowing you to fly around the level to inspect AI paths or EQS grids while the game logic remains active.
Optimize HUD Overlays
If the debug information is obscuring the screen, use the editor-bound shortcuts (Ctrl + Tilde by default) to toggle the HUD. This “eliminates” visual noise when you only need to see the in-world visualizations (like NavMesh links) without the accompanying text data.