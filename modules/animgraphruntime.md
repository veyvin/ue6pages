---
layout: default
title: AnimGraphRuntime
---

<!-- ai-generation-failed -->

<h1>AnimGraphRuntime</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AnimGraphRuntime/AnimGraphRuntime.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationCore, Core, CoreUObject, Engine, GeometryCollectionEngine, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

within Animation Blueprints. While the core Engine module provides basic animation playback, AnimGraphRuntime contains the math and logic for advanced pose manipulation, including Inverse Kinematics (IK), blend logic, and skeletal controllers.

It is the primary toolkit for creating “procedural” animation, allowing characters to dynamically react to the environment (e.g., feet snapping to uneven ground or a head looking at a target).

1. Module Configuration

To use any of these nodes (like FABRIK, CCDIK, or LookAt) in C++ or to extend them, you must include the module in your Build.cs.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "AnimGraphRuntime" });
Copy code
2. Practical Usage Tips & Best Practices
Use LOD Thresholds for Performance

Every Skeletal Control node in this module (e.g., Modify Bone, Leg IK) has a LOD Threshold property in the Details panel. Set this to a specific LOD level (e.g., 2) to “eliminate” the performance cost of procedural math when the character is far away. If the mesh LOD is higher than the threshold, the node is skipped entirely.

Maximize “Fast Path” Compatibility

The AnimGraph is most efficient when it can use the Fast Path, which avoids the overhead of the Blueprint Virtual Machine. To keep your nodes in the Fast Path, avoid accessing variables through complex logic or function calls inside the graph. Instead, use “Property Access” (direct variable binding) or Anim Node Functions to update data.

Minimize Space Conversions

Nodes in AnimGraphRuntime often operate in Component Space (blue pins) rather than Local Space (white pins). Converting between these spaces has a CPU cost. Group your Skeletal Control nodes together so you only perform one “Local to Component” and one “Component to Local” conversion for the entire stack.

Leverage FABRIK for Simple IK

For multi-bone chains like arms or tails, prefer the FABRIK (Forward And Backward Reaching Inverse Kinematics) node over CCDIK. FABRIK is generally faster to converge and produces more natural-looking results for simple kinematic chains, “eliminating” the jitter often seen with other solvers.

Use “Blend Mask” for Precise Layering

When using Layered blend per bone, utilize Blend Masks (defined in the Skeleton asset) instead of manually entering bone names and depths in the node. This makes your logic reusable across different Animation Blueprints and ensures that “elimination” of specific bones in a LOD doesn’t break your layering logic.

Utilize Thread-Safe Update Functions

Unreal Engine 5 handles animation updates on worker threads. If you are writing custom logic to drive nodes in this module, ensure your functions are marked as Thread Safe. If you call non-thread-safe functions from the AnimGraph, the engine will be forced to sync with the Game Thread, causing significant performance bottlenecks.

Cache Poses to Avoid Redundant Work

If you need to use the same pose (e.g., the output of a complex state machine) in multiple branches of your graph, use a New Saved Cached Pose node. This allows the AnimGraphRuntime to evaluate the pose once and reuse it, “eliminating” the need to re-calculate the same blend logic multiple times in a single frame.

Debug with “ShowDebug Animation”

When procedural nodes are not behaving as expected, use the console command showdebug animation. This provides a real-time breakdown of which nodes are active, their current weights, and their performance cost, allowing you to identify nodes that should be disabled via LODs or distance checks.