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

ne that provides the C++ framework and UI logic for the Animation Blueprint (AnimBP) interface. It extends the core Blueprint editor functionality to handle animation-specific features like State Machines, the AnimGraph, and the Persona viewport integration.

Description

This module is responsible for the specialized “Persona” experience within the AnimBP window. It manages the communication between the visual node graph and the live preview of the skeletal mesh. Developers use this module primarily to extend the editor, create custom graph schemas for animation, or build specialized tools that interact with the AnimGraph’s compilation and visualization processes.

Practical Usage Tips and Best Practices
1. Separate Editor and Runtime Logic

Because the AnimationBlueprintEditor is an Editor-only module, any custom nodes or logic you create must be split. Put your node’s execution logic in a Runtime module (e.g., AnimGraphRuntime) and the visual/UI logic in an Editor module that depends on AnimationBlueprintEditor. This ensures your game can package successfully without editor dependencies.

2. Leverage Multi-Threaded Update

In the editor’s Class Settings for an AnimBP, ensure “Use Multi-Threaded Animation Update” is enabled. This allows the engine to offload the animation evaluation to worker threads. While working in the editor, this module helps visualize potential “thread-safe” violations, which you should resolve immediately to prevent performance bottlenecks.

3. Enable Optimization Warnings

Within the Animation Blueprint Editor settings, toggle “Warn About Blueprint Usage”. This is a best practice that causes the editor to highlight nodes in the AnimGraph that are calling back into the Event Graph. Eliminating these calls in favor of Native Variables or Fast Path variables will significantly improve your character’s performance.

4. Utilize the Pose Watch Manager

When debugging complex blends, use the Pose Watch feature managed by this module. Right-click any pose pin in the AnimGraph and select “Watch Pose.” This allows you to see a wireframe representation of the bone transformations at that specific point in the graph, helping you identify exactly where a pose becomes corrupted.

5. Organize Logic with State Machines

Avoid creating a “spaghetti” AnimGraph. Use the module’s State Machine functionality to compartmentalize logic. For example, keep locomotion, combat, and “elimination” states separate. This makes the graph easier to read and allows the editor to more efficiently cache and transition between animation states.

6. Debugging with the Anim Inspector

Use the Anim Preview Editor panel (provided by this module) to test variables in real-time. Instead of playing the game, you can manually adjust “Speed” or “IsDead” sliders to see how the character transitions into an elimination pose. This is the fastest way to verify that your transition logic and blend times are correct.

7. Build.cs Dependency Filtering

When adding this module to your project’s *.Build.cs, always wrap it in a target check. This prevents your build system from attempting to link editor-only UI code into your standalone game client:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AnimationBlueprintEditor");

	}
Copy code
8. Use Asset Browser Filters

The Animation Blueprint Editor includes a built-in Asset Browser docked with the AnimGraph. Use the Filter options to show only animations compatible with the current Skeleton. This helps eliminate the risk of dragging an incompatible animation into the graph, which would otherwise result in a skeletal mismatch error during compilation.