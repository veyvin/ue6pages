---
layout: default
title: FunctionalTesting
---

<!-- ai-generation-failed -->

<h1>FunctionalTesting</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/FunctionalTesting/FunctionalTesting.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, AssetRegistry, AutomationController, Core, CoreUObject, EditorFramework, Engine, ImageWrapper, LevelEditor, MessageLog, NavigationSystem, RHI, RenderCore, SessionFrontend, Slate, SlateCore, SourceControl, UMG, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ine designed for gameplay-level validation and automated testing of interactive logic.

Description and Purpose

This module revolves around the AFunctionalTest Actor, which serves as a container for scripted testing logic. Unlike unit tests that check isolated code functions, functional tests are designed to run in a live game world. They are used to verify complex gameplay scenarios—such as a character successfully traversing a platforming section or a specific projectile causing an elimination event. By placing these actors in “Test Maps,” developers can create a suite of automated scenarios that simulate player behavior and validate that the game’s high-level systems are functioning correctly in a real-world environment.

Practical Usage Tips and Best Practices
Utilize the Child Class Method for Reusability
Instead of putting all logic into the Level Blueprint, create a C++ or Blueprint class inheriting from AFunctionalTest. This allows you to define reusable test logic, such as a “Damage Test” that can be dropped into any level. This approach helps you eliminate code duplication across different testing environments.
Leverage PrepareTest for Async Setup
Use the PrepareTest and IsReady functions for tests that require setup time, such as waiting for a level to stream in or an AI to spawn. The test will not begin until IsReady returns true, which helps you eliminate “false negative” failures caused by race conditions during initialization.
Inject Input for Realistic Simulation
In UE 5.6, you can use the EnhancedInput system to inject raw input actions directly into the player controller from a Functional Test. This allows you to simulate a player pressing buttons to trigger an elimination sequence, helping you eliminate the need for manual playtesting of specific mechanics.
Register Auto-Destroy Actors for Cleanup
Use the RegisterAutoDestroyActor function during your test setup. The framework will automatically handle the elimination of these actors once the test completes, regardless of whether it succeeded or failed. This ensures you eliminate memory leaks or world clutter between consecutive tests.
Discover Tests via the Session Frontend
Functional tests are automatically discovered by the Session Frontend (under the Automation tab). You can group tests by folder or name, allowing you to run a specific suite—like “CombatTests”—to eliminate the time spent manually searching for and loading individual test maps.
Implement OnTestFinished for State Reset
Always use the OnTestFinished event to restore the game state, such as resetting the player’s health or teleporting them back to a starting location. Proper cleanup is essential to eliminate side effects that could cause subsequent tests in the same session to fail.
Use Functional Test Actors for Performance Profiling
You can script a functional test to move the camera through a specific path in a level while capturing performance data. This allows you to eliminate performance regressions by running the same automated “fly-through” test on every build to check for frame rate drops.
Integrate with World Partition
When testing in large open worlds, place your Functional Test Actors in specific cells. You can use the test logic to force-load the surrounding cells before the test begins, which helps you eliminate issues where the test actor falls through the floor because the landscape hadn’t loaded yet.