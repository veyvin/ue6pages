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

ous physics sub-systems—including rigid bodies, cloth, destruction, and solvers—independently of a full game environment.

This module is essential for engine contributors and technical directors who need to verify that physics behavior remains consistent across different platforms or after making modifications to the physics source code.

Practical Usage Tips and Best Practices
1. Execute via the Session Frontend

The most common way to interact with this module is through the Session Frontend (Tools > Session Frontend). Under the Automation tab, you can find Chaos-specific tests by filtering for “Chaos.” Running these tests allows you to verify that the physics solver hasn’t been “eliminated” or broken by project-specific configuration changes.

2. Validate Solver Determinism

Use the tests within this module to check for Determinism. If your project relies on networked physics or replays, running the Chaos determinism tests ensures that the solver produces identical results across different runs. This is critical for preventing “Desyncs” in multiplayer matches.

3. Benchmark Physics Performance

The module includes performance benchmarks that measure the “Time to Solve” for complex scenes (e.g., hundreds of falling cubes). Run these benchmarks on your target hardware (consoles/mobile) to establish a performance baseline. This helps you identify if a specific engine update has “eliminated” your performance headroom.

4. Debug Narrow-Phase Collisions

If you suspect that specific shapes (like complex convex hulls) are not colliding correctly, look at the NarrowPhase tests in this module. These tests isolate the collision detection logic from the rest of the engine, allowing you to verify if a bug is in the physics representation or the actual collision math.

5. Verify Destruction Logic

For projects using Chaos Destruction, the module provides tests for geometry collection fracturing and strain calculation. Running these ensures that “Field System” interactions are correctly applying forces and that the “elimination” of broken chunks follows the expected sleep and crumbling thresholds.

6. Use as a Reference for Custom Tests

If you need to write your own C++ physics validation logic, the ChaosPhysicsTests source code is the best reference. It demonstrates how to use EXPECT_TRUE and EXPECT_NEAR macros to validate world-state values like velocity, position, and impulse after a specific number of steps.

7. Test Cross-Platform Consistency

Physics calculations can sometimes vary between ARM (Mobile) and x86 (PC) architectures due to floating-point differences. Run the tests in this module on all your target platforms to ensure that your gameplay-critical physics logic won’t “eliminate” the player’s progress due to platform-specific drift.

How to Run via Command Line (CI/CD)

For automated pipelines, you can trigger these tests without opening the editor: UnrealEditor-Cmd.exe "PathToProject.uproject" -ExecCmds="Automation RunTests Chaos.Physics;Quit" -log

Performance & Best Practices
Isolate Tests: When running physics tests, close other heavy applications to prevent CPU spikes from “eliminating” the accuracy of performance benchmarks.
Check Logs: If a test fails, the module outputs detailed logs to the Saved/Logs folder. These logs often contain the exact delta between the “Expected” and “Actual” physics transform.
Standard Solver Settings: Ensure your project’s Physics Settings match the engine defaults when running these tests; otherwise, custom gravity or sub-stepping values may cause standard unit tests to fail.