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

Engine that provides the essential mathematical structures and data types for the animation system. Unlike the Engine module, which handles high-level concepts like UAnimInstance, AnimationCore focuses on the raw data: bone indices, pose containers, and the mathematical operations required to manipulate skeletons.

It acts as the “math layer” that sits between the core engine and specific animation systems like Control Rig or the AnimGraph.

Practical Usage Tips & Best Practices
1. Add as a Low-Level Dependency

When building custom animation nodes, IK solvers, or skeletal controllers in C++, you must include AnimationCore in your Build.cs file. It is a runtime module, so it is required for both editor and packaged builds:

C#
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "AnimationCore" });
Copy code
2. Use FBoneContainer for Bone Mapping

If you are writing C++ logic to manipulate bones, never use raw integer indices. Always use FBoneContainer. It maps “Skeleton-space” indices to “SkeletalMesh-space” indices. This is critical for ensuring your code works correctly when a character uses a different mesh than the one the animation was authored on.

3. Prefer FCompactPose for Performance

When performing per-frame pose calculations, use FCompactPose (and the associated FCSPose). These structures are optimized for memory alignment and cache efficiency. They allow you to iterate through a skeleton’s transforms significantly faster than using standard arrays of FTransform, which is essential for maintaining high frame rates in scenes with many characters.

4. Utilize Bone Index Types

The module defines specific types like FMeshPoseBoneIndex and FSkeletonPoseBoneIndex. Always use these specific types in your function signatures rather than generic int32. This creates “type-safety” for your skeleton logic, preventing bugs where you accidentally pass a skeleton index into a function expecting a mesh index.

5. Thread-Safe Math Operations

The math utilities within AnimationCore are designed to be thread-safe. When implementing NativeUpdateAnimation or custom worker threads, use the transform and blending functions provided here. This ensures that your animation calculations can be offloaded to worker threads by the engine’s Task Graph, helping to eliminate Game Thread bottlenecks.

6. Leverage FBoneIndexType for Memory

If you are storing large arrays of bone indices (e.g., for a custom skinning system or hit detection), use FBoneIndexType. This is typically a uint16, which reduces the memory footprint of your structures by half compared to int32, which is vital when handling complex skeletons with hundreds of bones.

7. Mirroring and Retargeting Logic

AnimationCore contains the underlying logic for data-driven mirroring. If you are building a custom mirroring system (e.g., for a combat system where an elimination move must work for both left and right hands), look at the mirroring structures in this module to ensure you are following the engine’s standard for bone pair mapping.

8. Avoid Raw Transform Manipulation

When possible, use the module’s built-in blending and interpolation functions (like FAnimationRuntime utilities) rather than manually interpolating FQuat or FVector. These built-in methods are optimized to handle edge cases like “shortest-path” rotation blending, which prevents bones from spinning 360 degrees during transitions.