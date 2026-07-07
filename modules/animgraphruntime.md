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

ional implementation (the C++ structs) for many of the standard nodes used in Animation Blueprints. While the Engine module defines the basic animation interfaces, AnimGraphRuntime provides the actual math and logic for complex features like Inverse Kinematics (IK), blends, and skeletal controllers.

This module is used to calculate bone transforms on worker threads during the animation update phase, enabling procedural and dynamic character movement such as foot alignment, look-at targets, and layered blending.

Practical Usage Tips and Best Practices
1. Add Required Build Dependencies

To extend animation nodes or use specific runtime structs (like FAnimNode_ModifyBone) in C++, you must include this module in your project’s Build.cs.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "Engine", 

	    "AnimGraphRuntime", // Required for FAnimNode_Base and standard nodes

	    "AnimationCore" 

	});

	```

	 

	#### 2. Distinguish Runtime vs. Editor Modules

	When creating custom Animation Nodes, remember that the logic (the `FAnimNode_...` struct) belongs in a Runtime module (like `AnimGraphRuntime`), while the visual representation (the `UAnimGraphNode_...` class) belongs in an **UnrealEd** or **AnimGraph** Editor module. This separation is vital for successful game packaging.

	 

	#### 3. Leverage LOD Thresholds

	Almost every skeletal control node in this module (like `FAnimNode_ModifyBone` or `FAnimNode_LookAt`) includes a `LODThreshold` property. **Best Practice:** Always set this to a reasonable value (e.g., 2). This ensures that expensive procedural calculations are automatically skipped for distant characters, providing a significant performance boost.

	 

	#### 4. Minimize Space Conversions

	Nodes in this module operate in either **Local Space** (white pins) or **Component Space** (blue pins). Converting between them (e.g., `LocalToComponent`) has a performance cost. Group your Component Space nodes (like IK and Skeletal Controls) together in the graph to perform the conversion only once.

	 

	#### 5. Use Native Getters for Blackboard/Variables

	When using nodes like `FAnimNode_BlendListByBool`, avoid performing complex logic inside the AnimGraph's visual nodes. Instead, calculate the boolean or integer in the **Blueprint Thread Safe Update** or via a C++ native getter to keep the animation evaluation off the Game Thread and fully parallelized.

	 

	#### 6. Initialize and Cache in `OnInitializeAnimInstance`

	If your custom runtime node requires references to other actors or components, do not find them inside the `Update_AnyThread` function. Use the initialization phase to cache references. This prevents the "elimination" of performance gains by avoiding expensive searches during the high-frequency animation tick.

	 

	#### 7. Handle Bone Indices Safely

	When writing C++ nodes that manipulate bones, always use `FBoneReference` and verify it with `IsValidToEvaluate()`. Bone indices can change if the LOD or Mesh changes; using the `AnimGraphRuntime` safety checks prevents crashes during the **elimination** of meshes or during skeletal swaps at runtime.

	 

	#### 8. Utilize Native Pose Caching

	For complex graphs that reuse the same pose in multiple branches, use the **Pose Caching** nodes implemented in this module. This allows the engine to evaluate a branch once and reuse the result, rather than recalculating the entire pose tree for every blend input.
Copy code
2. Distinguish Runtime vs. Editor Nodes

Animation nodes are split into two parts: the Runtime Node (a struct in this module, e.g., FAnimNode_Base) and the Editor Node (a class in the AnimGraph module, e.g., UAnimGraphNode_Base). When creating custom nodes, ensure your logic stays in the runtime struct to allow it to function in packaged builds.

3. Use LOD Thresholds for Performance

Most nodes in this module, especially skeletal controls like FAnimNode_Fabrik or FAnimNode_LookAt, include an LODThreshold property. Best Practice: Set this to a value like 2 or 3. This ensures the expensive procedural math is skipped for distant characters, providing a significant performance boost.

4. Minimize Space Conversions

Nodes in this module operate in either Local Space (white pins) or Component Space (blue pins). Converting between them (e.g., LocalToComponent) carries a performance cost. Group your Component Space nodes together to perform the conversion only once per graph update.

5. Leverage Native Getters for Variables

For nodes like FAnimNode_BlendListByBool, avoid complex logic inside the AnimGraph’s visual “Compute” pins. Instead, calculate your booleans or integers in the Blueprint Thread Safe Update or via a C++ native getter to keep the animation evaluation fully parallelized and off the Game Thread.

6. Implement Safe Bone References

When writing C++ nodes that manipulate specific bones, use FBoneReference rather than raw strings or indices. Always call BoneReference.Initialize(RequiredBones) during the node’s initialization to ensure the bone index is valid, preventing crashes during the elimination of meshes or LOD changes.

7. Utilize Pose Caching

For complex graphs that reuse the same pose in multiple branches, use the Pose Caching nodes implemented in this module. This prevents the engine from recalculating the entire pose tree for every blend input, effectively performing an elimination of redundant computation.

8. Verify Thread Safety

The functions in this module (like Update_AnyThread and Evaluate_AnyThread) are designed to run on worker threads. When overriding or extending these, ensure you do not access non-thread-safe data (like AActor variables) directly. Use the FAnimationUpdateContext to safely access the data you need.