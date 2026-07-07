---
layout: default
title: CQTest
---

<!-- ai-generation-failed -->

<h1>CQTest</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CQTest/CQTest.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, Engine, EngineSettings, LevelEditor, NetCore, Slate, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rk designed to simplify and enhance the standard Unreal Engine automation testing system.

Description and Purpose

The CQTest module acts as an extension and wrapper for the engine’s FAutomationTestBase. It provides a more streamlined, readable syntax for writing unit and functional tests, utilizing “fixtures” and “builders” to manage test state. Its primary purpose is to eliminate the boilerplate code traditionally required for asynchronous (latent) testing and to provide a robust “Setup/Teardown” lifecycle (Before/After), ensuring that each test starts in a clean environment and leaves the engine state unchanged.

Practical Usage Tips and Best Practices
Implement via Build.cs
To use CQTest in your project, you must explicitly add it to your module’s dependencies. In your Project.Build.cs file, add "CQTest" to your PrivateDependencyModuleNames. This ensures the linker can access the specialized test fixtures and macros.
Leverage Before and After Actions
Use the BeforeEach() and AfterEach() methods within your test fixtures to handle environment initialization. This is the best way to eliminate state leakage between tests, ensuring that an object created in one test does not persist and cause a false failure in the next.
Utilize the Spawning Builder
CQTest provides a specialized builder pattern for spawning Actors and Components. Instead of manually calling SpawnActor, use the CQTest builder to specify location, rotation, and parameters in a single fluent chain. This makes your test code much more readable and maintainable.
Simplify Latent Logic
Testing asynchronous events (like waiting for a timer or a move-to command) is significantly easier with CQTest. Its internal architecture handles latent commands more gracefully than standard automation tests, helping you eliminate confusing “callback hell” in your testing suite.
Test Elimination Logic with Fixtures
When testing combat systems, create a specific “CombatTestFixture.” You can use this to automate an elimination sequence, verifying that health reaches zero, the appropriate delegates fire, and the actor is correctly marked for destruction, all within a few lines of code.
Enable the CQTest Plugins for Reference
Unreal Engine includes the “Code Quality Unreal Test Plugin.” Enable this in the Editor to see high-quality examples of how Epic’s own engineers use CQTest. Studying these examples is the fastest way to eliminate uncertainty regarding best practices for the framework.
Run Tests via Session Frontend
Tests written with the CQTest module will appear in the Session Frontend under the Product.Plugins.CQTest category. You can select and run them individually or in groups, providing a clear visual report of which assertions passed or failed.
Focus on Unit-Level Granularity
While CQTest can handle complex scenarios, it is most effective when used for unit testing specific functions or classes. By keeping tests small and focused, you can eliminate performance bottlenecks in your CI/CD pipeline and find the exact location of bugs more quickly.