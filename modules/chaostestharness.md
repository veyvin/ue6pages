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

ctions as a testing fixture that integrates with the Catch2 framework (via Catch2Extras). It is designed to instantiate a “headless” version of the Chaos solver, allowing developers to programmatically spawn physics particles, apply forces, and simulate ticks. It is primarily used by engine and physics engineers to ensure the integrity of collision detection, joint constraints, and solver stability. By bypassing the UObject and Kismet systems, it provides a high-performance sandbox for unit-testing the raw C++ physics logic in isolation.

Practical Usage Tips and Best Practices
1. Use for Determinism Verification

The harness is the ideal environment to test for physics determinism. Because it allows you to specify a fixed time step and manually trigger solver updates, you can run the same simulation multiple times and use assertions to verify that the final transforms of physics bodies are identical, helping you identify and eliminate non-deterministic code paths.

2. Master the FChaosTestEnvironment

The core of most tests in this module is the FChaosTestEnvironment. Use this class to manage the lifecycle of your test. It handles the boilerplate of creating a FPBDRigidsSolver and a FPBDRigidsEvolution. Always ensure the environment is correctly initialized at the start of your TEST_CASE and properly torn down at the end to avoid memory leaks.

3. Minimal Particle Spawning

When testing specific solver logic, avoid complex meshes. Instead, use the harness to spawn simple geometric primitives (spheres or boxes) as TPBDRigidParticle. This simplifies the collision math and makes it easier to verify that the solver is responding correctly to your inputs without the “noise” of complex collision geometry.

4. Manually Step the Simulation

Unlike the main engine which ticks automatically, the ChaosTestHarness environment allows you to call AdvanceOneTimeStep(dt). This gives you total control; you can apply an impulse, step the solver exactly once, and immediately check the resulting velocity or position. This “step-by-step” approach is essential for debugging sub-step artifacts.

5. Verify Collision and Contact Points

Use the harness to programmatically place two bodies in an overlapping state and verify that the Broad Phase and Narrow Phase correctly generate contact constraints. You can iterate through the CurrentConstraints() in the solver to check that the normal and penetration depth match your expected mathematical values.

6. Test Physics Proxy Cleanup

Use the harness to verify the safe elimination of physics objects. Spawn a collection of particles, then trigger their removal from the evolution. Use the harness to assert that the solver’s internal particle arrays are empty and that all memory associated with the elimination of those proxies has been reclaimed by the system.

7. Performance Benchmarking

Because it runs without the overhead of the renderer or blueprint VM, the ChaosTestHarness is excellent for micro-benchmarking. You can wrap a solver update in a loop and use Catch2’s BENCHMARK macro to measure the time it takes to solve a specific number of constraints, helping you identify and eliminate performance regressions in the solver.

8. Validate Joint and Constraint Stability

If you are implementing custom physics constraints, use the harness to create “stress tests.” For example, create a long chain of joints and simulate them under high gravity. By using assertions on the joint error (positional drift), you can fine-tune your constraint projection settings to eliminate “stretching” or “jitter” before the code ever reaches the main engine.