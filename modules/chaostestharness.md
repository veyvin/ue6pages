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

+ without the overhead of the full Unreal Editor or a game world. It is primarily used by engine and physics programmers to verify solver math, ensure collision stability, and catch regressions in the physics pipeline.

Practical Usage Tips & Best Practices
1. Isolated Solver Validation

Use the harness to test new physics features (such as custom Joint Constraints or specialized collision shapes) before integrating them into the main engine. By using the raw Chaos::FPBDRigidsSolver within the harness, you can verify math in a controlled environment. This facilitates the elimination of external variables like networking, actor lifecycle, or rendering issues that could mask physics bugs.

2. Manual Simulation Stepping

The harness provides a Step(dt) function that gives you total control over the passage of time.

Tip: Instead of waiting for real-time frames, you can execute 1,000 steps of a complex physics simulation in a few milliseconds. This is essential for testing the “settling” behavior of a stack of rigid bodies or verifying long-term stability.
3. Deterministic Regression Testing

The primary use case for this module is ensuring that physics changes do not break existing behaviors.

Best Practice: When you identify a physics bug, such as a jittering constraint, write a test case in the harness that reproduces it. Once fixed, that test remains in the suite to ensure the elimination of that bug is permanent and cannot regress in future engine versions.
4. Programmatic Geometric Definition

In the harness, you do not need to import .uasset files from the Content Browser. You can programmatically define physics objects using FImplicitObject (Spheres, Boxes, Convex Hulls).

Tip: This is ideal for testing “tunnelling” (high-speed collisions) by precisely placing two thin boxes and stepping the simulation to verify that Continuous Collision Detection (CCD) prevents a pass-through.
5. Use Physics-Aware Assertions

Physics simulations are rarely “pixel-perfect” due to floating-point drift and iterative solvers.

Best Practice: Do not use exact boolean checks for positions or velocities. Instead, use macros like EXPECT_NEAR or EXPECT_VECTOR_NEAR with a small epsilon (e.g., 1e-4f). This prevents tests from failing due to minor, acceptable precision changes.
6. Profile Pure Physics Performance

The harness is an excellent tool for benchmarking. Since it runs without rendering or game logic, you can use Unreal Insights to profile the raw CPU cost of a specific solver configuration. This leads to the elimination of “noise” in your performance data, providing a clear view of how a code change affects the physics thread.

7. Memory Management of Physics Particles

When adding particles (rigid bodies) to the harness solver, you are responsible for their lifecycle.

Best Practice: Use TUniquePtr or TSharedPtr patterns within your test fixture to manage FGeometryParticles. This ensures the clean elimination of memory leaks when a test suite finishes and the solver is destroyed.
8. Headless Execution for CI/CD

Chaos tests are typically compiled into a standalone executable (e.g., ChaosTests.exe).

Tip: Integrate these into your build farm by running the executable with the --gtest_filter argument. This provides a “fail-fast” mechanism that catches physics regressions before they ever reach the main project branch, ensuring the elimination of broken builds.