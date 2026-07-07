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

components of Chaos (evolution, collision detection, joint constraints, and cloth/destruction logic) in isolation. It is used by engine developers and technical animators to ensure that changes to the physics engine do not introduce regressions or non-deterministic behavior.

Practical Usage Tips & Best Practices
1. Use as a Template for Custom Physics Logic

If you are developing a custom physics solver or a specialized constraint in C++, use the source code of ChaosPhysicsTests (found in Engine/Source/Programs/LowLevelTests) as a reference. It demonstrates how to instantiate a FPBDRigidsEvolution and step the simulation manually without the overhead of the UWorld.

2. Filtering Tests with Catch2 Tags

Since this module contains thousands of tests, use Catch2 tags to isolate specific areas. For example, if you are debugging a ragdoll or vehicle issue, you can run tests specifically tagged with [Joints] or [Collision].

Command Line Example: ChaosPhysicsTests.exe [Joints]
3. Validate Bit-Wise Determinism

Chaos is designed to be deterministic. This module includes tests that run the same simulation multiple times and compare the results bit-for-bit. If you are implementing a networked physics solution and seeing “desyncs,” run these tests to verify that the core solver is behaving consistently on your target platform.

4. Debugging via Visual Studio Test Explorer

For the best workflow, install the UnrealVS extension. This allows the Visual Studio Test Explorer to discover tests within the ChaosPhysicsTests module. You can then right-click specific test cases (like a sphere-vs-capsule collision test) and click “Debug” to step through the solver’s narrow-phase math.

5. Benchmarking Solver Performance

The module utilizes Catch2’s benchmarking capabilities. You can run these tests to measure the “micro-performance” of different collision algorithms. This is useful for determining if a specific optimization truly reduces the time taken to process contact pairs.

6. Identify “Elimination” of Collision Precision

Use the collision-specific tests to investigate “tunneling” (where objects pass through each other). The tests often simulate high-velocity impacts to ensure that the Continuous Collision Detection (CCD) logic correctly prevents the elimination of collision responses at high speeds.

7. Module Dependency in .Target.cs

Since ChaosPhysicsTests is a standalone program, it requires its own .Target.cs file inheriting from TestTargetRules. If you are creating your own physics test suite, ensure your target type is set to TargetType.Program and that you link against Chaos and LowLevelTestsRunner.

8. Running in CI/CD via RunUAT

To automate physics validation in a build pipeline, use the AutomationTool (RunUAT). This ensures that every engine update is checked for physics regressions before it reaches the rest of the team:

bash
RunUAT.bat BuildGraph -Script="Engine/Build/LowLevelTests.xml" -Target="Chaos Physics Tests Win64"
Copy code