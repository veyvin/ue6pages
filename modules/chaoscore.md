---
layout: default
title: ChaosCore
---

<!-- ai-generation-failed -->

<h1>ChaosCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosCore/ChaosCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, IntelISPC</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Chaos Physics engine in Unreal Engine.

Description and Purpose

This module serves as the low-level architecture for all Chaos-based physics systems. It contains the core data structures, geometric types (like spheres, boxes, and convex hulls), and fundamental mathematical definitions used by the physics solver. Unlike high-level modules that handle destruction or vehicle logic, ChaosCore is focused on the underlying “primitive” logic, providing the vector math, bounding volumes, and intersection routines required for collision detection and rigid body dynamics. Its primary purpose is to provide a performance-optimized, engine-agnostic math library that powers the rest of the Chaos ecosystem.

Practical Usage Tips and Best Practices
Utilize Native Chaos Math Types
When working in the physics source or extending Chaos, use the specialized types found in this module, such as Chaos::FVec3 and Chaos::FRotation3. These are often aliases for FVector and FQuat but are specifically typed to ensure compatibility with the solver’s templates and to facilitate future optimizations within the physics pipeline.
Optimize Collision Geometry Early
The performance of the ChaosCore intersection routines depends on the complexity of your shapes. Prefer simple primitives (Box, Sphere, Capsule) over complex Convex Hulls whenever possible. This allows the core solver to use highly optimized analytic intersection tests, which helps eliminate CPU overhead during dense physics simulations.
Manage Physics Thread Safety
Because Chaos runs on its own dedicated thread (the Physics Thread), data from ChaosCore must be accessed carefully. Always use the “GT to PT” (Game Thread to Physics Thread) data marshalling patterns. Directly modifying core physics data from the Game Thread can lead to race conditions and must be eliminated to maintain engine stability.
Leverage Bounding Volume Hierarchies (BVH)
The core module utilizes spatial acceleration structures to speed up queries. If you are procedurally generating geometry for physics, ensure you are correctly updating the bounding boxes. A poorly fit bounding box forces the solver to perform unnecessary Narrow Phase checks, which you should eliminate to keep your simulation fast.
Tune Position and Velocity Iterations
In your project’s Physics Settings, you can adjust the iteration counts for the solver. These iterations directly affect how ChaosCore resolves constraints. Increasing these improves stability for complex joint chains but increases cost; find the lowest possible values that maintain stability to eliminate wasted performance.
Debug with Chaos Visual Debugger (CVD)
When a physics object behaves unexpectedly—such as during a high-speed player elimination where a character becomes a ragdoll—use the Chaos Visual Debugger. This tool pulls data directly from the ChaosCore structures to show you exactly where collision contacts and constraints are being generated in real-time.
Use Chaos-Specific Raycasts for Accuracy
For low-level physics queries, you can interface directly with the Chaos structures via FPhysicsInterface_Chaos. This provides more granular control than standard Scene Queries and allows you to perform “Sweep” and “Raycast” tests against the raw ChaosCore geometry without the overhead of the higher-level engine wrappers.
Monitor Chaos Stats and Counters
Use the console command stat Chaos to see the workload being handled by the core module. Pay close attention to the number of active particles and constraints. If the “Active Particles” count remains high for objects that should be still, adjust your sleep thresholds to eliminate unnecessary updates for stationary actors.