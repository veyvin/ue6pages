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

the visual scripting of character poses. While the Engine and AnimGraphRuntime modules handle the actual movement of bones during gameplay, the AnimGraph module is responsible for the nodes, pins, and compilation logic used within the Animation Blueprint Editor.

It defines the editor-side behavior for all animation nodes (such as Blends, IK, and State Machines) and handles the conversion of the visual node graph into an optimized runtime executable form.

Practical Usage Tips and Best Practices
1. Understand the Editor/Runtime Split

Every animation node consists of two parts: a runtime struct (e.g., FAnimNode_Base) and an editor class (e.g., UAnimGraphNode_Base).

Best Practice: When creating custom nodes, ensure all visual properties, titles, and pin configurations are kept in the UAnimGraphNode class within an Editor module. This keeps your runtime builds lean by eliminating editor-only metadata.
2. Leverage “Fast Path” Optimization

The AnimGraph compiler tries to optimize data flow to avoid expensive Blueprint virtual machine calls.

Tip: Look for the lightning bolt icon on your nodes in the AnimGraph. This indicates the node is using the “Fast Path.” To maintain this, avoid complex logic or function calls directly on the node pins; instead, pre-calculate values in the Thread Safe Update function.
3. Use Thread Safe Functions

Modern Unreal Engine animation updates run on worker threads rather than the Game Thread.

Best Practice: Use the Blueprint Thread Safe Update animation event. Accessing variables directly from the Character or Movement Component in the AnimGraph can cause race conditions. By using thread-safe logic, you eliminate potential crashes and improve performance.
4. Configure Module Dependencies

If you are developing custom animation nodes (like a specialized Look-At or a custom Pose Driver), you must include the module in your Editor.Build.cs file.

C#
	// In YourProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { 

	        "AnimGraph", 

	        "BlueprintGraph", 

	        "AnimGraphRuntime" 

	    });

	}
Copy code
5. Implement Node Validation

The AnimGraph module allows you to write custom validation logic for your nodes.

Tip: Override the ValidateAnimNodeDuringCompilation function in your UAnimGraphNode class. Use this to catch errors—such as a missing skeleton reference or invalid variable ranges—before the game even runs, eliminating bugs during the development phase.
6. Organize with Linked Anim Graphs

For complex characters, a single AnimGraph can become unmanageable.

Best Practice: Use Linked Anim Blueprints or Linked Anim Layers. This allows you to break your logic into modular pieces (e.g., one graph for Locomotion, one for Upper Body). This module manages how these graphs are compiled together, making the system easier to debug and maintain.
7. Customize Node Appearance for Clarity

You can override visual aspects of your nodes to help technical artists.

Tip: Use GetNodeTitleColor and GetContextMenuCategory in C++. By color-coding your custom nodes (e.g., orange for procedural physics, blue for basic blends), you make large graphs much easier to read and eliminate time spent searching for specific logic.
8. Monitor Attribute Flow

The AnimGraph supports passing more than just poses; it can pass attributes like “Curve Data” or “Custom Payload.”

Best Practice: Use the Pose Watch feature in the editor to see how these attributes change frame-by-frame. This is essential for debugging why a specific curve (like a “Footstep” trigger) is being eliminated or scaled incorrectly during a blend.