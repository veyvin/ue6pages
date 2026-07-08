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

the visual scripting of character poses within Animation Blueprints. It acts as the editor-side counterpart to the runtime animation system. While the Engine module handles the actual skeletal math at runtime, the AnimGraph module defines how nodes appear, how pins are connected, and how the graph is compiled into executable runtime instructions.

Its primary role is to manage UAnimGraphNode classes, which wrap runtime FAnimNode structs to provide a user interface for designers to blend animations, apply IK, and manage state machines.

Practical Usage Tips and Best Practices
Architectural Separation (Editor vs. Runtime) Always separate your animation logic into two parts: a Runtime struct (derived from FAnimNode_Base) in a runtime module, and an Editor class (derived from UAnimGraphNode_Base) in an editor module. This ensures that heavy editor-only metadata is “eliminated” from your final game build.
Strict Build Dependency Scoping Ensure AnimGraph is only referenced in your ProjectEditor.Build.cs. Including it in a non-editor target will cause a compilation failure during packaging.
C++
	if (Target.Type == TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "AnimGraph", "BlueprintGraph" });

	}
Copy code
Use Property Access for Performance In modern Unreal Engine versions (5.x+), the AnimGraph uses Property Access to “eliminate” the overhead of the Blueprint Virtual Machine. When creating custom nodes, ensure your variables are exposed so the compiler can thread-optimize the data copying from the Event Graph to the Anim Graph.
Customize Node Visuals for Clarity Override GetNodeTitle and GetNodeTitleColor in your UAnimGraphNode class. Giving different colors to “Logic” nodes vs. “Skeletal Control” nodes helps designers navigate complex graphs and reduces the time spent on “elimination” of logic errors.
Implement Thread-Safe Logic The AnimGraph often runs on worker threads. When writing logic for your nodes, avoid accessing non-thread-safe data. Use the meta = (BlueprintThreadSafe) tag in your function libraries to allow them to be used inside AnimGraph node functions without forcing a sync back to the Game Thread.
Leverage Node Validation Override the ValidateAnimNodePostCompile function in your editor node. This allows you to “eliminate” potential crashes by checking if the user has provided valid data (like a valid Skeleton or a non-null Animation Sequence) before the graph is even allowed to run.
Expose Pins Dynamically Use the PinShownByDefault or AlwaysAsPin metadata on your runtime struct properties. This allows you to control which variables are hidden in the details panel and which are exposed as connectable pins in the graph, keeping the node UI clean.
Optimize with Pose Watching Utilize the Pose Watch feature during debugging. By right-clicking a node, you can visualize the skeletal pose at that specific point in the flow. This is the fastest way to “eliminate” issues with additive blending or incorrect IK offsets.