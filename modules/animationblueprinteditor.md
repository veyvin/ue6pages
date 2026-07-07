---
layout: default
title: AnimationBlueprintEditor
---

<!-- ai-generation-failed -->

<h1>AnimationBlueprintEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationBlueprintEditor/AnimationBlueprintEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimGraph, AnimGraphRuntime, AppFramework, BlueprintGraph, Core, CoreUObject, EditorFramework, EditorStyle, EditorWidgets, Engine, GraphEditor, InputCore, Kismet, KismetCompiler, KismetWidgets, Persona, PropertyEditor, RHI, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ne that provides the specialized toolset for creating and managing Animation Blueprints. It extends the core Blueprint Editor to handle the unique requirements of skeletal animation logic.

Description and Purpose

This module is the backend for the Animation Blueprint Editor window. Its purpose is to manage the interaction between the Event Graph (where variables like speed or falling state are updated) and the AnimGraph (where pose blending and skeletal manipulation occur). It provides specialized UI components like the Anim Preview Editor, the Asset Browser, and the State Machine graph editor. It is the central hub where technical animators define how a character moves based on gameplay data.

Practical Usage Tips and Best Practices
Utilize “Warn About Blueprint Usage”
Inside the Class Settings provided by this module, enable Warn About Blueprint Usage. This highlights nodes in your AnimGraph that are calling into Blueprints, which can be a performance bottleneck. Aim to keep your AnimGraph “pure” by using the Animation Blueprint Property Access system to pull data directly from variables.
Enable Multi-Threaded Animation Update
In the module’s Class Settings, ensure Use Multi-Threaded Animation Update is enabled. This allows the engine to offload animation logic to worker threads, which is essential for maintaining a high frame rate when many characters are on screen.
Debug Transitions with the Pose Watch Manager
The module includes a Pose Watch Manager (found in the My Blueprint panel). Use this to “watch” specific pins in the AnimGraph. This allows you to visually inspect the pose at any point in the node chain, which is invaluable for debugging why a character’s posture looks incorrect during a complex blend.
Manage Root Motion Modes
Use the Class Defaults panel within the editor to set the correct Root Motion Mode. For most multiplayer games, you should use Root Motion from Montages Only to ensure movement remains predictable and to eliminate desync issues between the server and the client.
Handle Logic for Elimination Sequences
When a character undergoes an elimination, use the Event Graph to set a “Dead” boolean, then use a Linked Anim Graph or a specific State Machine transition to play the appropriate animation. This module allows you to preview these transitions instantly by modifying variable values in the Anim Preview Editor panel without launching the game.
Leverage the Asset Browser for Quick Iteration
Instead of dragging assets from the main Content Browser, use the Asset Browser tab docked within the Animation Blueprint Editor. It is filtered specifically for animations compatible with the current Skeleton, allowing you to drag-and-drop sequences directly into the AnimGraph for immediate testing.
Optimize with Linked Anim Blueprints
For complex characters, do not build everything in one graph. Use the Linked Anim Layer feature supported by this module. This allows you to split logic into manageable chunks (e.g., one Blueprint for locomotion, another for weapon handling), making the editor more responsive and the logic easier to maintain.
Use the Preview Mesh Switcher
If your character has multiple skins or variations (e.g., different armor sets), use the Preview Mesh button in the Toolbar. This allows you to verify that your animation logic and skeletal offsets work correctly across different skeletal mesh variations sharing the same skeleton.