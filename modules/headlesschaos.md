---
layout: default
title: HeadlessChaos
---

<!-- ai-generation-failed -->

<h1>HeadlessChaos</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/HeadlessChaos/HeadlessChaos.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, ChaosVehiclesCore, Core, CoreUObject, GeometryCore, GoogleTest, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rk within the Unreal Engine Low-Level Tests (LLT) ecosystem. It is designed to execute and validate the core logic of the Chaos Physics Engine in a “headless” environment—meaning it runs without the Unreal Editor, the Renderer, or the UObject system overhead.

What it is and What it’s used for

Located in Engine/Source/Programs/LowLevelTests/ChaosTests, this module provides a lean C++ environment to unit-test the mathematical and physical foundations of Chaos. It allows developers to instantiate physics solvers and simulate collisions, joints, and rigid body dynamics using purely native C++ code.

Primary uses include:

Physics Core Validation: Verifying the correctness of the Chaos evolution solver, collision detection, and constraint resolution.
CI/CD Integration: Running thousands of physics tests in seconds on build machines to detect regressions before they reach the main engine branch.
Deterministic Testing: Manually “ticking” the physics solver with fixed time steps to ensure that physics behavior is reproducible across different platforms.
Low-Level Debugging: Isolating complex physics bugs (like “jittering” or solver instability) in a minimal environment free from gameplay-layer interference.
Practical Usage Tips and Best Practices
1. Use Catch2 for Test Definition

HeadlessChaos is built on the Catch2 framework. Organize your tests using TEST_CASE and SECTION macros. This is a best practice for grouping related physics scenarios (e.g., “Sphere-Box Collision”) while maintaining the elimination of shared state between tests.

2. Manually Step the Solver

In a headless environment, you are responsible for the simulation “Tick.” Use a fixed delta time (e.g., 1/60.0f) when calling Evolution->AdvanceOneTimeStep(Dt). This ensures your tests are deterministic and reproducible, which is critical for identifying floating-point drift.

3. Initialize a Minimal Chaos Scene

To run a test, you typically need to create an FPBDRigidsEvolution or FPBDRigidsSolver. Ensure you provide a minimal configuration and avoid loading unnecessary plugins; keeping the dependency list small in your .Build.cs leads to the elimination of long compilation times.

4. Leverage the Chaos Test API

The module provides helper classes like FChaosTestEnvironment. Use these to quickly spawn rigid bodies or geometries (Spheres, Boxes, Convex hulls) without having to manually manage the memory and registration of every individual particle and constraint.

5. Profile with Standalone Executables

Since HeadlessChaos compiles into a standalone .exe (found in Binaries/Win64/ChaosTests/), you can profile your physics logic directly using Unreal Insights or external tools. This provides a “clean” profile of the solver’s CPU usage without the noise of the rest of the engine.

6. Use Tags for Test Filtering

When running ChaosTests.exe from the command line, use tags (e.g., [RigidBodies][Collision]) to run only the relevant subset of tests. This allows for the elimination of wait times when you are only iterating on a specific feature like “Joint Constraints.”

7. Validate with Assertions, Not Logs

Avoid using UE_LOG for validation. Instead, use REQUIRE or CHECK macros to validate physics states (e.g., REQUIRE(BodyLocation.Z > 0.0f)). This allows the LLT runner to automatically catch failures and report them to your build system’s dashboard.

8. Strategic Elimination of UObject Overhead

Never use NewObject<T> or AActor within a HeadlessChaos test. The system is designed to test the Native C++ API of Chaos. Sticking to raw Chaos:: types ensures your tests run at maximum speed and remain compatible with the core physics library even if the high-level Engine API changes.