---
layout: default
title: ChaosTestHarness
---

<!-- ai-generation-failed -->

<h1>ChaosTestHarness</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ChaosTestHarness/ChaosTestHarness.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Catch2, Core, CoreUObject, Engine, LowLevelTestsRunner</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

real Engine designed for the validation and performance benchmarking of the Chaos Physics engine.

Description and Purpose

This module provides a suite of fixtures, mocks, and automated test runners specifically tailored for physics simulations. It sits between the low-level physics math and the high-level engine integration, allowing developers to run isolated “harness” tests that verify the stability of solvers, collision detection, and joint constraints without needing to load a full game level. Its primary purpose is to ensure that changes to the physics source code do not introduce regressions in simulation accuracy, performance, or determinism.

Practical Usage Tips and Best Practices
Utilize for Isolated Physics Debugging
If you encounter a bug in complex physics behavior—such as jittering ragdolls or unstable constraints—use the ChaosTestHarness to create a “minimal reproducible case.” Testing in the harness allows you to eliminate outside variables like character movement logic or networking, isolating the issue purely to the physics solver.
Verify Determinism across Platforms
Physics determinism is critical for replay systems and networked games. Use the harness to run identical simulation scenarios across different platforms (e.g., PC vs. Console). Comparing the results helps you identify and eliminate floating-point discrepancies that could lead to desynchronization in a live environment.
Benchmark Solver Performance
The harness includes tools to measure the CPU time spent on various physics tasks. When optimizing your project, run the harness tests to see how different “Position” and “Velocity” iteration counts affect the frame budget. This data allows you to eliminate settings that provide diminishing returns for simulation quality.
Test Elimination State Ragdolls
A common use case for the harness is validating the transition from a kinematic state to a simulated ragdoll state during a player elimination. You can automate tests to ensure that the ragdoll does not “explode” or fall through the floor when physics simulation is enabled, even under high-velocity impacts.
Integrate with Low-Level Tests (LLT)
The ChaosTestHarness is compatible with the UE Low-Level Test framework and Catch2. Use the GROUP_TEST_CASE macros to organize your physics tests. This allows you to run a quick suite of physics “Smoke Tests” during every build to eliminate code regressions before they reach the rest of the team.
Mock Collision Environments
Instead of building a level with Static Meshes, use the harness to programmatically spawn primitive collision shapes (spheres, boxes, capsules). This makes tests faster to run and easier to maintain, as you don’t have to worry about asset paths or missing level data.
Analyze Constraint Stability
Use the harness to stress-test complex constraint chains (like ropes or bridges). By applying extreme forces within the harness, you can find the “breaking point” of the solver and adjust linear/angular limits to eliminate “stretching” artifacts that occur during intense gameplay moments.
Monitor Memory Allocations
Running physics in the harness allows you to use memory profiling tools to track exactly how much memory the physics scene is consuming. This is an effective way to eliminate memory leaks in custom physics components or specialized simulation logic before deploying to memory-constrained platforms.