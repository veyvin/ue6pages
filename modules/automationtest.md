---
layout: default
title: AutomationTest
---

<!-- ai-generation-failed -->

<h1>AutomationTest</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AutomationTest/AutomationTest.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ller and Core testing utilities) is the foundational framework for creating automated C++ tests within Unreal Engine. It allows developers to write unit tests, feature tests, and integration tests that verify code stability without requiring manual playtests.

These tests run outside the standard UObject ecosystem in a dedicated environment, making them ideal for testing core math, data structures, and low-level engine logic.

1. Module Configuration

To write automation tests in C++, you must include the relevant modules in your Build.cs file. Note that tests are typically placed within a Private/Tests directory.

C#
	// MyProject.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "Core", "UnrealEd", "AutomationController" });

	}
Copy code
2. Practical Usage Tips & Best Practices
Choose the Right Test Type (Simple vs. Complex)
Simple Tests: Use the IMPLEMENT_SIMPLE_AUTOMATION_TEST macro for atomic unit tests (e.g., “Does this math function return 5?”).
Complex Tests: Use IMPLEMENT_COMPLEX_AUTOMATION_TEST when you need to run the same logic against multiple inputs, such as “Does every map in this folder load without errors?”. This “eliminates” the need for writing dozens of nearly identical tests.
Use Latent Commands for Time-Based Logic

Since tests run on the main thread, you cannot use standard Sleep() or Delay() calls. Use ADD_LATENT_AUTOMATION_COMMAND. This allows the test to wait for several frames or for an asynchronous process (like a level load) to finish before proceeding, “eliminating” race conditions in your test results.

Leverage Automation Specs for BDD

For more readable, modern tests, use the Automation Spec (BEGIN_DEFINE_SPEC). This follows the Behavior-Driven Development (BDD) style using Describe and It blocks. It is much easier to organize than legacy macros and supports BeforeEach and AfterEach for consistent setup and cleanup of test data.

Categorize with Proper Flags

Always use the EAutomationTestFlags correctly.

SmokeFilter: For critical tests that must run quickly (under 1 second).
EngineFilter/ProductFilter: For more extensive feature tests.
EditorContext/ClientContext: Ensures the test only runs in the appropriate environment, “eliminating” crashes caused by running Editor-only code in a cooked client.
Standardize Assertions

Use the built-in TestEqual, TestTrue, and TestNotNull functions provided by FAutomationTestBase. These functions automatically log detailed failure messages to the Session Frontend, including the file name and line number, which is essential for rapid debugging.

Always Clean Up Assets and State

Automation tests do not automatically reset the world. If your test spawns an actor or creates a temporary file, use a latent command or an AfterEach block to “eliminate” those objects. Failing to do so can cause “polluted” states that make subsequent tests fail.

Run Tests via Command Line (CI/CD)

To truly benefit from automation, run your tests in a Continuous Integration (CI) pipeline using the AutomationTool. Use the command line argument -ExecCmds="Automation RunTests [TestName]" to run tests automatically whenever code is pushed, “eliminating” the risk of regressions reaching the main branch.

Monitor Performance with Smoke Tests

Mark your most frequent unit tests as Smoke Tests. These should be designed to complete almost instantaneously. If a Smoke Test begins to take longer than a few milliseconds, it serves as an early warning that the underlying C++ logic has become inefficient or bloated.