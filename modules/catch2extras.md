---
layout: default
title: Catch2Extras
---

<!-- ai-generation-failed -->

<h1>Catch2Extras</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Catch2/Catch2Extras.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

h2 C++ testing framework, integrated specifically for the Unreal Engine Low-Level Tests (LLT) ecosystem.

Description and Purpose

While Catch2 is a popular open-source testing framework, it is not natively aware of Unreal Engine’s modular architecture or its specific runtime requirements. The Catch2Extras module provides a suite of macros and utilities that “wrap” Catch2 to make it compatible with the UE build system. Its primary purpose is to provide Test Groups and Lifecycle Events (such as global setup/teardown) that allow developers to write tests that can initialize Unreal modules, handle UObjects, or set up mock engine environments without the overhead of a full Editor instance.

Practical Usage Tips and Best Practices
Utilize GROUP_ Macros for Organization
Instead of standard Catch2 macros, use GROUP_TEST_CASE. This allows you to categorize tests into logical groups (e.g., “Physics”, “AI”, “UI”). Grouping makes it easier to run specific subsets of tests from the command line, helping to eliminate wasted time running unrelated tests.
Leverage Lifecycle Events for Setup
Use GROUP_BEFORE_ALL and GROUP_AFTER_ALL to handle heavy initialization tasks, such as starting up a core engine module or loading a Data Table. This ensures that the setup happens only once for a suite of tests, rather than before every single test case, significantly improving execution speed.
Manage Global State with GROUP_BEFORE_GLOBAL
If your tests require a fundamental engine change (like mocking a specific Console Variable), use GROUP_BEFORE_GLOBAL. This runs before any test groups are executed, ensuring a consistent environment and helping to eliminate intermittent failures caused by “dirty” global states.
Use the TestHarness for UObject Support
The Catch2Extras module is designed to work alongside the TestHarness.h. When writing Low-Level Tests, always include TestHarness.h after CoreMinimal.h. This enables the specialized UE-Catch2 runners to manage the lifetime of UObjects created during your unit tests.
Implement Teardown to Prevent Leaks
Always use GROUP_AFTER_EACH or GROUP_AFTER_ALL to clean up any actors or components spawned during testing. If you fail to eliminate these objects from memory, subsequent tests may experience “state leakage,” where data from a previous test causes a later test to fail incorrectly.
Testing Combat and Elimination Logic
When writing a low-level test for a damage system, use a GROUP_TEST_CASE to verify the elimination sequence. You can check that the “OnEliminated” delegate fires and that the actor’s state changes correctly, all within a lightweight C++ environment that executes in milliseconds.
Run via the LowLevelTestsRunner
Tests using Catch2Extras are best executed using the LowLevelTestsRunner executable found in your project’s Binaries folder. Use command-line arguments like --list-test-names-only to see your groups and verify that your Catch2Extras macros are correctly registered.
Prefer REQUIRE over CHECK for Critical Path
In your test logic, use the REQUIRE macro for conditions that must be true for the test to continue. If a REQUIRE fails, the test stops immediately. This is better than CHECK for complex logic because it helps eliminate a “cascade” of confusing error messages caused by a single initial failure.