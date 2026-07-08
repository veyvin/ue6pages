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

prehensive collection of pre-built animation nodes and skeletal controllers. While the core “Engine” module handles basic animation playback, AnimGraphRuntime contains the more advanced mathematical and procedural logic needed for modern character movement.

It is primarily used to implement procedural animation features such as IK (Inverse Kinematics), Bone Look-At, Spline IK, CCD IK, and the Pose Driver node. If you are creating custom Animation Blueprint nodes in C++, you will almost always inherit from the base classes provided by this module.

Practical Usage Tips and Best Practices
1. Add Module Dependencies for Custom Nodes

If you are developing a custom FAnimNode_Base or skeletal controller in C++, you must include this module in your [Project].Build.cs. Many common structs like FAnimNode_SkeletalControlBase reside here.

C#
PublicDependencyModuleNames.AddRange(new string[] { "AnimGraphRuntime", "AnimationCore" });
Copy code
2. Leverage the “Fast Path” Optimization

The nodes in AnimGraphRuntime are highly optimized to use the engine’s Fast Path. To maintain this performance, avoid using Blueprint logic (like “plus” or “multiply” nodes) to drive the pins of these nodes. Instead, calculate values in the Thread Safe Update Animation function and pass the raw variables directly to the node pins.

3. Use FABRIK for Lightweight IK

For limb adjustments (like hands on a steering wheel or feet on uneven ground), use the FABRIK (Forward And Backward Reaching Inverse Kinematics) node. It is significantly more performant than CCD IK for simple chains and is the preferred choice in AnimGraphRuntime for real-time procedural adjustments.

4. Implement Thread Safety

Nodes within this module are designed to run on worker threads (Multi-Threaded Animation Update). When writing custom logic that interacts with these nodes, ensure your functions are marked as Thread Safe. Avoid accessing non-thread-safe game data (like the PlayerController) directly inside the node’s update loop.

5. Optimize via LOD Thresholds

Almost every skeletal control node in AnimGraphRuntime (like Modify Bone or Look At) has an LOD Threshold property. Use this to disable procedural animation on characters that are far away. This leads to a massive elimination of CPU overhead in scenes with many NPCs.

6. Utilize Pose Drivers for Corrective Blending

To prevent “candy wrapper” mesh collapsing at joints (like shoulders or hips), use the Pose Driver node. It uses RBF (Radial Basis Functions) to drive morph targets or bone transforms based on the rotation of a joint, providing high-quality deformations with minimal performance cost.

7. Handle Bone elimination and Virtual Bones

If your character logic involves the elimination of certain bones at runtime (e.g., dismemberment systems), ensure your AnimGraphRuntime nodes are targeting the correct bone indices. Use Virtual Bones to create stable targets for IK nodes that won’t be affected if the physical bone hierarchy changes.

8. Debug via the “Anim Outliner”

When troubleshooting why a procedural node (like a Look-At) isn’t working, use the Animation Insights tool (part of Unreal Insights). This allows you to see the exact pose data flowing through the AnimGraphRuntime nodes frame-by-frame, helping you identify if a node is being bypassed or receiving incorrect data.