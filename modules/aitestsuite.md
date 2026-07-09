---
layout: default
title: AITestSuite
---


<h1>AITestSuite</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AITestSuite/AITestSuite.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, Core, CoreUObject, Engine, GameplayTasks</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

to provide a robust framework for automated testing of AI systems. It serves as the foundation for testing Behavior Trees, Navigation, and AI Controller logic by providing specialized test fixtures and base classes that simplify the simulation of AI behaviors without needing a full game environment.

Practical Usage Tips & Best Practices
1. Module Configuration in Build.cs

Since AITestSuite is a developer module, it should only be included in non-shipping builds. Ensure you wrap it in a target check within your Build.cs to prevent build failures during packaging for release.

C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PrivateDependencyModuleNames.Add("AITestSuite");

	}
Copy code
2. Inherit from FAITestBase for Custom Tests

When writing C++ automation tests for AI, inherit your test class from FAITestBase. This class provides helper methods to spawn AI-specific actors (Pawns and Controllers) and automatically handles the cleanup of the world to prevent memory leaks between test runs.

3. Use UTestBTTask for Behavior Tree Validation

The module includes UTestBTTask, a specialized Behavior Tree task designed specifically for verification. You can use it to force success, failure, or “latent” (in-progress) states to ensure your decorators and services react correctly to different task outcomes.

4. Mocking AI Controllers

Avoid using your actual game AAIController for simple logic tests. Instead, create a minimal mock controller within your test suite. This prevents dependencies on complex game systems (like perception or high-level blackboard keys) that might interfere with the specific unit being tested.

5. Verification of the “Elimination” Event

When testing combat AI, use the suite to simulate damage that results in the elimination of a pawn. You can verify that the AI Controller correctly unpossesses the pawn or transitions to a “Dead” state in the Behavior Tree immediately following the elimination event.

6. Latent Testing for Navigation

AI testing often requires time (e.g., waiting for a MoveTo to complete). Use the FAITestBase::WaitFor or LatentIt patterns to allow the simulation to run for several frames. This is essential for verifying that pathfinding correctly handles dynamic obstacles or reachability.

7. Keep Tests in the Developer Folder

Place your AI Test Suite code in a Developer or Private/Tests folder. Because the module is intended for internal quality assurance, this keeps your runtime game module clean and ensures that test-only assets (like specific test Behavior Trees) do not bloat the final game data.

8. Use Behavior Tree Mocking

Instead of running a massive, 50-node Behavior Tree, use the suite to run “Micro-Trees”—small tree assets that contain only the specific branch or decorator you are testing. This isolates the logic and makes it much easier to identify why a specific transition failed.

9. Leverage the Command Line for CI/CD

You can trigger these tests through the Automation Controller via command line. This allows you to automatically run your AI suite on a Build Server, ensuring that changes to the Navigation Mesh or AI Controller code don’t cause regressions in agent behavior.