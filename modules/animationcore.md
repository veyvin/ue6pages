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

l Engine that provides the mathematical and structural building blocks for the animation system. Unlike the Engine module—which handles high-level concepts like Animation Blueprints—AnimationCore focuses on the raw data structures and solvers that drive skeletal movement.

What it is and What it’s used for

AnimationCore contains the core C++ types and algorithms required to calculate bone transforms. It is designed to be lightweight and performant, often operating on “Compact Poses” rather than full Actor-space hierarchies.

Primary uses include:

Bone Infrastructure: Defining types like FBoneIndexType, FCompactPose, and FBoneContainer.
Mathematical Solvers: Housing low-level IK (Inverse Kinematics) algorithms such as CCDIK (Cyclic Coordinate Descent) and FABRIK.
Space Transformations: Providing utilities for converting between Component Space, Mesh Space, and Local Space.
Constraint Logic: Implementing the math behind basic transform constraints and bone offsets.
Practical Usage Tips and Best Practices
1. Use Compact Poses for Performance

When writing custom animation nodes in C++, always work with FCompactPose rather than FTransform arrays. Compact Poses use a contiguous memory layout and specific indexing (LOD-aware) that significantly reduces cache misses and speeds up bone calculations.

2. Implement Lightweight IK with CCDIK

If you need a simple, cost-effective IK solution for a chain of bones (like a finger reaching for a button or a tentacle), use the CCDIK solver found in this module. It is computationally cheaper than Full-Body IK and easier to constrain for small, specific movements.

3. Manage Bones with the FBoneContainer

Before sampling or modifying bones, ensure you use an FBoneContainer. This structure holds the mapping between the Skeleton and the Skeletal Mesh, ensuring that your logic respects the current LOD (Level of Detail) and doesn’t waste CPU cycles on bones that have been stripped out.

4. Prefer Local Space for Blending

To eliminate visual artifacts like “sliding” or “popping,” perform most of your bone blending and interpolation in Local Space. AnimationCore provides the FTransform math necessary to blend these rotations before they are converted to Component Space for the final pose.

5. Thread Safety and Parallelism

The types in AnimationCore are designed to be used within the engine’s parallel animation evaluation. When accessing bone data, ensure you are not modifying global state; stick to the data provided in the FAnimationUpdateContext or FPoseContext to ensure your code is thread-safe.

6. Minimize Component Space Conversions

Converting a whole bone chain from Local Space to Component Space is expensive. Only perform this conversion when absolutely necessary (e.g., at the very end of an IK solve or when checking for world collisions). AnimationCore’s FAnimationRuntime utilities can help you batch these conversions.

7. Leverage FABRIK for Long Chains

For long, flexible chains where natural-looking movement is more important than strict angular constraints, use the FABRIK (Forward And Backward Reaching Inverse Kinematics) solver. It converges quickly and is excellent for reaching targets with high precision across many joints.

8. Validate Bone Indices

Always check the validity of a bone index before using it. In C++, use BoneIndex.IsValid() or check against INDEX_NONE. Accessing an invalid bone index can lead to memory corruption or immediate crashes, especially when dealing with dynamically changed meshes or retargeted skeletons.