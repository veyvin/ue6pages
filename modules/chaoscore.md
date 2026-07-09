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

eal Engine. It provides the essential, low-level data structures, math primitives, and memory management utilities required for high-performance physics simulation. While other modules like Chaos handle complex solver logic and ChaosSolverEngine integrates physics into the gameplay world, ChaosCore defines the fundamental building blocks—such as vectors, matrices, and geometric primitives—that are optimized for SIMD (Single Instruction, Multiple Data) and parallel execution.

Practical Usage Tips & Best Practices
1. Use Chaos-Specific Math Types

When working within low-level physics code, prefer using the types defined in ChaosCore (e.g., Chaos::FReal, Chaos::FVec3) rather than the standard FVector.

Best Practice: These types are alias-compatible with standard Unreal math but are specifically designed to respect the precision settings (Float vs. Double) configured for the physics engine, ensuring consistency across the simulation.
2. Leverage SIMD and ISPC

ChaosCore is built to work with the Intel Implicit SPMD Program Compiler (ISPC). If you are writing custom physics extensions, organize your data into contiguous arrays. This allows the core module to process physics calculations in “batches” via SIMD instructions, which can lead to the elimination of CPU bottlenecks in scenes with thousands of active bodies.

3. Optimize for Async Physics

Unreal Engine 5 supports Async Physics, where simulation runs on its own thread.

Tip: Because ChaosCore utilities are often accessed on a background thread, ensure any custom physics logic is thread-safe. Avoid accessing UObjects directly from core physics functions; instead, pass raw data types defined in this module.
4. Manage Geometric Primitives Efficiently

This module defines primitives like Spheres, Capsules, and Convex hulls.

Best Practice: When performing manual intersection tests or custom collision logic, use the primitives in ChaosCore. They are optimized for the GJK (Gilbert-Johnson-Keerthi) and EPA (Expansion Polytope Algorithm) solvers used by the engine for collision detection.
5. Understand the FReal Precision

Chaos can be compiled to use either float or double for its calculations.

Tip: Always use Chaos::FReal for scalar values in your physics code. This ensures that if your project switches to Large World Coordinates (LWC) or high-precision physics, your code will remain compatible without manual refactoring.
6. Minimize Memory Allocations during Simulation

ChaosCore utilizes specialized allocators to handle the high-frequency creation and elimination of temporary physics data (like contact points).

Best Practice: When writing custom solvers or force fields, avoid using new or malloc. Utilize the engine’s TArray with slack or the specific memory pools provided by the core physics module to maintain high cache coherency.
7. Debug with “p.Chaos.Solver.DebugDraw”

The core module handles the math for debug visualizations. If you need to verify that your custom core-level math is working, use console commands like p.Chaos.Solver.DebugDraw 1. This allows you to see the raw geometric data being processed by the solver before it is smoothed out for the visual representation.

8. Implement Efficient Collision Elimination

When a physics object is no longer needed, it must be removed from the solver’s spatial acceleration structures (like AABB trees). Use the core module’s optimized removal functions to ensure the elimination of the object does not cause a structural rebuild of the tree, which can cause significant performance spikes in complex scenes.