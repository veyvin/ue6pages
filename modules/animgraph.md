---
layout: default
title: AnimGraph
---

<!-- ai-generation-failed -->

<h1>AnimGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimGraph/AnimGraph.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimGraphRuntime, AnimationEditMode, BlueprintGraph, Core, CoreUObject, DeveloperSettings, EditorFramework, EditorStyle, EditorWidgets, Engine, GraphEditor, InputCore, Kismet, KismetCompiler, KismetWidgets, PropertyEditor, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

es the framework for the visual node-based scripting environment within Animation Blueprints. While the AnimGraphRuntime module handles the actual execution of animation logic at runtime, the AnimGraph module is responsible for the editor-side representation, including node visualization, graph schema, and the compilation of visual nodes into runtime instructions.

It is the primary tool used by technical animators to define pose blending, skeletal transformations, state machine transitions, and IK (Inverse Kinematics) logic.

Practical Usage Tips and Best Practices
Understand the Two-Part Node Architecture When creating custom nodes in C++, you must split them into two parts: the Runtime Struct (inheriting from FAnimNode_Base in a runtime module) and the Editor Node (inheriting from UAnimGraphNode_Base in an editor module). The AnimGraph module manages the latter, handling the node’s title, color, and pin visibility.
Optimize via the “Fast Path” To ensure high performance, aim for nodes to follow the “Fast Path.” This occurs when the AnimGraph can access variables directly without executing complex Blueprint logic. In the editor, look for the lightning bolt icon on nodes; if it’s missing, your graph is running slower than it could. “Eliminate” logic that requires casting or function calls inside the AnimGraph to maintain this optimization.
Use Thread-Safe Functions In modern Unreal Engine versions, use Thread-Safe functions for variable updates. The AnimGraph is evaluated on a worker thread. By ensuring your data-gathering functions are marked as thread-safe, you allow the engine to process animation logic in parallel with the game thread, significantly improving frame rates.
Leverage Property Access Instead of using the “Event Graph” to copy variables every frame, use Property Access directly on AnimGraph nodes. In the node’s details panel, you can bind pins to variables or nested properties. This is more efficient and helps “eliminate” unnecessary execution flow in the Event Graph.
Implement Pose Watching for Debugging When a character’s pose looks incorrect (e.g., during an “elimination” animation where bones are snapping), right-click any node in the AnimGraph and select Toggle Pose Watch. This draws a debug skeleton in the viewport at that specific point in the graph, helping you pinpoint exactly which node is corrupting the pose.
Organize with Linked Animation Blueprints For complex characters, avoid one massive AnimGraph. Use the Linked Anim Graph node to split logic into modular pieces (e.g., one AnimBP for locomotion, another for “elimination” sequences or combat). This improves maintainability and allows different animators to work on separate sections of the logic simultaneously.
Utilize Anim Node Functions AnimGraph nodes now support “On Initialize,” “On Update,” and “On Become Relevant” functions. Use these specialized hooks to trigger logic (like resetting a state) only when a specific node becomes active, rather than running that logic every single frame in the main Update loop.
Module Dependencies in Build.cs If you are extending the animation editor or creating custom UAnimGraphNode classes, ensure your Editor module includes AnimGraph and BlueprintGraph in its dependencies.
C#
	// In YourProjectEditor.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "AnimGraph", "AnimGraphRuntime", "BlueprintGraph" });
Copy code