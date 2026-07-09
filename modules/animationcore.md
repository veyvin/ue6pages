---
layout: default
title: AnimationCore
---

<!-- ai-generation-failed -->

<h1>AnimationCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AnimationCore/AnimationCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ion system. While the high-level Engine module handles concepts like UAnimInstance and UAnimBlueprint, AnimationCore provides the raw mathematical structures and data types for bone transforms, skinning logic, and pose manipulation.

It is primarily used by developers building custom animation solvers, procedural rigging tools (like Control Rig), or performance-critical C++ animation nodes that need to operate directly on a skeleton’s bone data.

Practical Usage Tips and Best Practices
1. Prefer FCompactPose for Performance

When performing manual pose calculations, always use FCompactPose rather than a standard array of transforms. FCompactPose is a contiguous block of memory optimized for CPU cache locality and is the standard format for animation “Worker Threads.” This minimizes cache misses during heavy transform math.

2. Respect the FBoneContainer Lifecycle

The FBoneContainer acts as the mapping between a Skeleton and a specific Mesh’s bone indices. Never store a FBoneContainer long-term; it is typically generated per-frame during the Update or Evaluate pass. Always check BoneContainer.IsValid() before attempting to access indices to avoid crashes when skeletons are swapped.

3. Use Type-Safe Bone Indices

Unreal uses several index types (FMeshPoseBoneIndex, FSkeletonPoseBoneIndex, and FCompactPoseBoneIndex). Using the correct struct instead of raw int32 prevents common “Index Out of Bounds” errors that occur when you accidentally use a Skeleton index to look up a Mesh-specific bone.

4. Thread Safety and Parallel Updates

The types in AnimationCore are designed for thread-safe operations. If you are writing a custom solver, ensure your logic is compatible with the engine’s Parallel Animation Update. Avoid accessing UObjects or AActor data inside your solver; instead, “snapshot” required variables into a thread-safe struct before evaluation.

5. Efficient Virtual Bone Access

If your project uses Virtual Bones (bones added to the skeleton that don’t exist in the mesh), use AnimationCore methods to resolve them. Virtual bones are handled separately from the raw mesh hierarchy; accessing them via AnimationCore helpers ensures they are correctly updated after their parent bones move.

6. Minimize Memory Allocations

Avoid TArray::Add or NewObject inside an animation evaluation loop. The AnimationCore system relies on FMemStack or pre-allocated buffers. If you need temporary storage for a procedural pose, use the FAnimationPoseData structure which provides a managed view of the required memory.

7. Handle Bone “Elimination” (LODs)

Remember that AnimationCore only processes bones that are “Required” for the current Level of Detail (LOD). Always iterate using OutPose.ForEachBoneIndex() rather than the full Skeleton count. This automatically skips bones that have been “eliminated” by distance scaling, significantly saving CPU cycles.

C++ Usage Example: Low-Level Pose Access

If you are implementing a custom animation node, you will interact with AnimationCore types like this:

C#
	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "AnimationCore" });

	```

	 

	---

	 

	### C++ Usage Example: Low-Level Pose Access

	 

	If you are implementing a custom animation node, you will interact with `AnimationCore` types like this:

	 

	```cpp

	#include "Animation/AnimNodeBase.h"

	#include "BonePose.h"

	 

	void FAnimNode_MyCustomSolver::Evaluate_AnyThread(FPoseContext& Output)

	{

	    // FPoseContext contains an FCompactPose from AnimationCore

	    FCompactPose& OutPose = Output.Pose;

	    const FBoneContainer& BoneContainer = OutPose.GetBoneContainer();

	 

	    // Loop through bones using the type-safe FCompactPoseBoneIndex

	    for (FCompactPoseBoneIndex BoneIndex : OutPose.ForEachBoneIndex())

	    {

	        // Get raw transform data

	        FTransform& BoneTransform = OutPose[BoneIndex];

	        

	        // Example: Procedurally rotate a bone (e.g., a simple look-at)

	        // BoneTransform.SetRotation(...);

	    }

	}

	```

	 

	### Performance & Debugging

	*   **Insights:** Use **Unreal Insights** with the `Anim` trace enabled to see exactly how much time is being spent in the "Evaluate" phase vs the "Update" phase.

	*   **Validation:** Use `ensure(OutPose.IsValidIndex(BoneIndex))` during development. These checks are removed in Shipping builds but are invaluable for catching logic errors in custom solvers.

	*   **LODs:** Remember that `AnimationCore` only processes bones that are "Required" for the current LOD. Always iterate using `OutPose.ForEachBoneIndex()` rather than the full Skeleton count to save CPU cycles on distant characters.
Copy code
Performance & Best Practices
Build.cs: You must include "AnimationCore" in your PublicDependencyModuleNames to access these types.
Debugging: Use the console command showdebug animation to see real-time bone transforms and verify your AnimationCore math is behaving as expected.
Math Helpers: Use FAnimationRuntime for common tasks like blending or space conversions, as these are highly optimized and use AnimationCore types natively.