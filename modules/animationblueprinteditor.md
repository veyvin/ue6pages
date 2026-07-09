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

alized toolset, user interface, and graph-management logic for Animation Blueprints (AnimBPs). While standard Blueprints focus on general gameplay logic, this module implements the unique features required for character movement, such as the AnimGraph, State Machines, Pose Watching, and the Animation Preview system.

Practical Usage Tips & Best Practices
1. Enable Multi-Threaded Animation Update

Inside the Animation Blueprint Editor, go to Class Settings and ensure Use Multi-Threaded Animation Update is enabled. This allows the AnimGraph to be evaluated on worker threads instead of the Game Thread, which is critical for maintaining high frame rates when managing many characters.

2. Monitor “Fast Path” Optimization

Look for the Lightning Bolt icon on your AnimGraph nodes. This indicates that the node is using the “Fast Path,” which skips the expensive Blueprint Virtual Machine.

Best Practice: To stay on the Fast Path, avoid performing math logic (like + or *) directly on the pins of the AnimGraph nodes. Instead, calculate those values in the Thread Safe Update Animation function.
3. Use Thread-Safe Update Functions

Instead of putting all your logic in the BlueprintUpdateAnimation event (which runs on the Game Thread), use the BlueprintThreadSafeUpdateAnimation override. This function is specifically designed by the editor module to run safely on worker threads, significantly reducing the performance cost of your animation logic.

4. Leverage the “Property Access” System

When you need to pull a variable from your Character or Pawn into your AnimBP, use the Property Access node (the “Bind” button next to pins). This system is designed to be thread-safe and highly optimized, allowing the Animation Blueprint Editor to bypass standard Blueprint getter calls that would otherwise break the Fast Path.

5. Debugging with Pose Watchers

If a character’s pose looks incorrect, right-click any pose wire in the AnimGraph and select Watch Pose. This module provides a visual representation (a ghosted mesh) of the pose at that specific node in the graph, making it much easier to isolate which blend or IK node is causing an issue.

6. Transition Events for Elimination Logic

When a character undergoes elimination, use State Machine Transition Events (like On Entered State or On Left State) rather than checking variables every frame in the Update tick. For example, triggering a “Ragdoll” state immediately upon the elimination event is more efficient than constantly polling a bIsDead boolean.

7. Enable “Warn About Blueprint Usage”

In the Class Settings of the Animation Blueprint Editor, enable the Warn About Blueprint Usage flag. This will cause the editor to throw a compiler warning whenever the AnimGraph falls off the Fast Path into the Blueprint VM, helping you identify and fix performance bottlenecks during development.

8. Use Asset Browsers and Sync Groups

Within the editor’s interface, use Sync Groups to synchronize the foot-planting phase between different animations (like walking and running). This ensures that when you blend between movements, the character’s feet don’t slide, providing a much higher quality of visual fidelity without extra code.