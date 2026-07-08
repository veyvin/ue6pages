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

nd Core frameworks) provides the essential C++ macros and classes for Unreal Engine’s built-in testing suite. It allows developers to write scripted tests that verify everything from low-level math functions to complex gameplay flows that span multiple frames.

This module is the backbone of Unreal’s quality assurance pipeline, enabling the elimination of regressions by running automated checks in the Editor, through the command line (for CI/CD), or on target hardware.

Practical Usage Tips and Best Practices
1. Distinguish Between Simple and Complex Tests

Use IMPLEMENT_SIMPLE_AUTOMATION_TEST for a single, focused test (e.g., verifying a specific function). Use IMPLEMENT_COMPLEX_AUTOMATION_TEST when you need to run the same test logic across multiple data points or assets, such as attempting to load every map in your project.

2. Categorize with EAutomationTestFlags

Always apply appropriate filters to your tests. Use ATF_SmokeTest for critical, fast-running tests (under 1 second) that should run on every build. Use ATF_Editor or ATF_Game to specify if the test requires the full Editor environment or should run in a standalone “game” context.

3. Queue Async Logic with Latent Commands

Many engine operations (like spawning actors or loading levels) take more than one frame. Use ADD_LATENT_AUTOMATION_COMMAND to queue operations that wait for a specific state before proceeding. This is critical for the elimination of race conditions in your tests.

C++
	// Example: Wait for 5 seconds before checking a result

	ADD_LATENT_AUTOMATION_COMMAND(FWaitLatentCommand(5.0f));

	```

	 

	#### 4. Use "Automation Spec" for Modern BDD

	For more readable and organized tests, use the **Automation Spec** (Behavior-Driven Development) style. Using `BEGIN_DEFINE_SPEC` and `Describe/It` blocks makes it easier to set up complex "Given/When/Then" scenarios and handle shared state via `BeforeEach` and `AfterEach` lambdas.

	 

	#### 5. Clean Up After Yourself (Idempotency)

	A test should leave the engine exactly as it found it. If your test spawns actors or creates temporary files on disk, use a latent command or the `AfterEach` block to delete them. This prevents "test pollution" where a failing test causes subsequent unrelated tests to fail.

	 

	#### 6. Utilize the Session Frontend

	During development, use the **Session Frontend** (Window > Tools > Session Frontend) to run and debug tests. You can filter by your custom category (e.g., `"MyGame.Combat.Spells"`) and see real-time log output for `TestTrue`, `TestEqual`, or `AddError` calls.

	 

	#### 7. Keep Tests Content-Agnostic

	Avoid hardcoding paths to specific assets (e.g., `/Game/Characters/Bob`) unless that asset is part of a dedicated "Test Content" plugin. Hardcoded paths break easily when artists move files. Instead, use `FAssetRegistryModule` to find assets by tag or class within your test's `GetTests` setup.

	 

	#### 8. Implement "Smoke" Tests for CI

	Mark your most critical code (saving/loading, character movement, UI initialization) as **Smoke Tests**. Set your build pipeline to run these tests automatically on every pull request. This provides an immediate **elimination** of "day one" bugs that would otherwise block the entire team from working.
Copy code
4. Adopt the Automation Spec (BDD) Style

For more complex scenarios, use the Automation Spec (Behavior-Driven Development) syntax. By using Describe and It blocks with BeforeEach/AfterEach lambdas, you can create highly readable and organized tests that mirror natural language requirements.

5. Ensure Test Idempotency

A test must leave the environment exactly as it found it. Use the AfterEach block or a final latent command to destroy spawned actors or delete temporary files. This prevents a failure in one test from causing a cascading elimination of stability in subsequent tests.

6. Utilize the Session Frontend for Debugging

Access the Session Frontend (Window > Tools > Session Frontend) to run your tests during development. This tool provides a visual interface to trigger tests, view real-time logs, and inspect the exact point of failure for TestTrue, TestEqual, or AddError calls.

7. Avoid Hardcoded Asset Paths

When testing assets, do not hardcode paths like /Game/Characters/MyHero. Instead, use the Asset Registry to find assets by tag or class. This ensures that if an artist moves a file, your test suite doesn’t suffer a total elimination of functionality.

8. Run Tests via Command Line for CI

Integrate your tests into your build pipeline by running the editor with the -ExecCmds="Automation RunTests [Filter]" command-line argument. This allows for the automatic elimination of broken builds by catching errors before they reach the rest of the development team.