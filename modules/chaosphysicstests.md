---
layout: default
title: ChaosPhysicsTests
---

<!-- ai-generation-failed -->

<h1>ChaosPhysicsTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/ChaosPhysicsTests/ChaosPhysicsTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ChaosTestHarness, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ite used to verify the mathematical accuracy, stability, and performance of the Chaos Physics engine. It is located within the Programs/LowLevelTests directory of the Unreal Engine source.

What it is and What it’s used for

Unlike “Functional Tests” which run inside a game map, this module consists of Unit Tests and Integration Tests that run in a standalone, headless environment using the Catch2 framework. It bypasses the Unreal Editor and the UObject system to test the raw physics solvers directly.

Primary uses include:

Solver Verification: Ensuring the PBD (Position-Based Dynamics) solvers for rigid bodies and cloth produce mathematically correct results.
Collision Math: Validating intersection algorithms and contact manifold generation for shapes like Spheres, Boxes, and Convex hulls.
Regression Testing: Identifying if changes to the physics source code have introduced instabilities or performance regressions.
Joint Stability: Testing if constraints (hinges, ball-and-socket) maintain integrity under extreme forces.
Practical Usage Tips and Best Practices
1. Reference for Custom Physics Logic

If you are writing custom C++ physics extensions, study this module’s source at Engine/Source/Programs/LowLevelTests/ChaosPhysicsTests/. It provides the best examples of how to manually initialize a FChaosWorld, create particles, and step a simulation without the overhead of the full engine.

2. Run via BuildGraph for CI/CD

To ensure physics stability in a build pipeline, execute these tests using the Unreal Automation Tool (UAT). This command builds and runs the tests in a console environment:

bash
	.\RunUAT.bat BuildGraph -Script="Engine/Build/LowLevelTests.xml" -Target="Chaos Physics Tests Win64"

	```

	 

	#### 3. Use for "Pure Math" Testing

	If you are implementing custom physical equations (e.g., a specialized buoyancy or aerodynamic model), add a test case here. Because it doesn't require a `.uproject` or the Editor, the iteration loop (Compile -> Run -> Result) is seconds rather than minutes.

	 

	#### 4. Debugging with "Catch2" Tags

	Chaos tests are heavily tagged. You can run only specific subsets (like only collision tests) by passing tags to the executable. If running the compiled `.exe` directly from `Binaries/Win64/ChaosPhysicsTests.exe`, use:

	```bash

	ChaosPhysicsTests.exe [Collision]

	```

	This eliminates the noise of unrelated tests when focusing on a specific physics bug.

	 

	#### 5. Analyze "Mock" Physics Worlds

	The module demonstrates how to create a "Mock" physics environment. This is a best practice for high-performance C++ development: by simulating physics in a headless environment, you can profile the raw CPU cost of the solver without interference from the GPU or Main Thread gameplay logic.

	 

	#### 6. Verify Solver Iterations

	Use the tests to understand the impact of solver iterations. Many tests in this module compare the result of a simulation at 4 iterations vs. 10 iterations to establish a baseline for "acceptable error" in the physics engine's stability.

	 

	#### 7. Test Narrow-Phase Manifolds

	If you are adding a custom collision shape, mimic the patterns in `CollisionTests.cpp`. It shows how to manually create two `FImplicitObject` shapes, generate a `FPBDCollisionConstraint`, and verify the resulting contact manifold points and normals.

	 

	#### 8. Prefer LLT for Physics over Blueprints

	While Blueprint functional tests are great for "Game Logic," they are poor for "Physics Logic" because frame-rate fluctuations in the Editor can introduce non-determinism. **ChaosPhysicsTests** use a fixed-step, deterministic clock, making them the superior choice for verifying that a physical interaction is truly fixed.
Copy code
3. Use Tags to Isolate Tests

The module is heavily tagged (e.g., [Collision], [Joints], [Geometry]). When debugging a specific physics issue, run the compiled executable directly from Binaries/Win64 with a tag to save time and eliminate irrelevant output:

bash
ChaosPhysicsTests.exe [Collision]
Copy code
4. Validate Determinism

Use these tests to verify “Fixed Tick” behavior. Because the module runs in a controlled environment, it is the primary place to check if a specific physical interaction produces the exact same result across multiple runs, which is critical for networked physics.

5. Leverage “Mock” Environments

The module demonstrates how to set up a “Mock” solver. When profiling physics performance, do it here to isolate the CPU cost of the Chaos solver from the overhead of the Main Thread, Slate, and the Renderer.

6. Test Edge-Case Collisions

When creating custom collision shapes, use the patterns in CollisionTests.cpp. You can programmatically place shapes at specific overlapping coordinates and verify that the FPBDCollisionConstraint generates the expected contact normals and penetration depths.

7. Monitor Solver Iterations

Many tests in this module compare results across different iteration counts (e.g., 1 vs 4 vs 10). Use this pattern in your own testing to find the “sweet spot” where physical stability is achieved without excessive CPU cost, aiding in the elimination of performance bottlenecks.

8. Check for Memory Leaks in Physics

Since these tests run outside the standard Garbage Collection (GC) path, they are excellent for identifying raw memory leaks in custom physics code. Running these tests with a memory profiler (like Valgrind or Dr. Memory) helps ensure that every FPhysicsParticle and FConstraint is correctly deleted.