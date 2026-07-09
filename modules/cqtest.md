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

testing framework for Unreal Engine. Originally developed by Ubisoft and integrated into the engine as a first-party module, it acts as an abstraction layer over the standard FAutomationTestBase. It is designed to provide a “GTest-like” (Google Test) experience, offering a more intuitive C++ syntax for writing unit and integration tests, better state management via fixtures, and improved handling of asynchronous engine operations.

Practical Usage Tips & Best Practices
1. Use Fixtures for Automatic State Reset

One of the strongest features of CQTest is the FCQTestFixture. You can define a Setup() and Teardown() once in a base class and reuse it across multiple tests.

Best Practice: Use fixtures to spawn test worlds or temporary actors. The Teardown() function is guaranteed to run even if a test fails, ensuring the total elimination of leaked objects and preventing one test’s failure from polluting the results of the next.
2. Leverage Fluent Assertions

Instead of the standard TestTrue or TestEqual macros, CQTest provides a more expressive assertion library.

Tip: Use ASSERT_THAT(Value, Eq(Expected)) or EXPECT_THAT. These provide much clearer error messages in the Automation Front-end, showing exactly what the actual value was versus what was expected, which speeds up the elimination of logic errors.
3. Define Tests with CQ_TEST Macros

The CQ_TEST and CQ_TEST_CASE macros simplify the boilerplate required for automation tests.

Best Practice: Organize your tests into clear hierarchies using category strings (e.g., "Project.Combat.Damage"). This allows developers to run specific sub-sections of the test suite from the Session Frontend, leading to a more focused and efficient debugging workflow.
4. Handle Asynchronous Logic with Latent Commands

Testing features that take time, such as character movement or network replication, is traditionally difficult in UE.

Tip: Use the latent command wrappers provided by CQTest. They allow you to write tests that “Wait until” a specific condition is met—such as the elimination event of a target dummy—without blocking the main thread or requiring complex state machine logic.
5. Include CQTest in Build.cs

To use the module, you must explicitly add it to your module’s dependency list.

Best Practice: Add "CQTest" to your PrivateDependencyModuleNames in your .Build.cs file. Ensure this is only done in a dedicated Test module or wrapped in #if WITH_DEV_AUTOMATION_TESTS to avoid including testing overhead in your final production shipping builds.
6. Smart UObject and World Management

CQTest includes specialized fixtures for UObject and Actor testing.

Tip: Use TTestObjectPtr and similar helper classes provided by the module. These are designed to work with the engine’s Garbage Collector to ensure that any objects created during a test session are properly tracked and marked for elimination once the test completes.
7. Fail Fast with ASSERT vs. EXPECT

The module distinguishes between fatal and non-fatal failures.

Best Practice: Use ASSERT for critical requirements (like “Is the player pointer valid?”) and EXPECT for secondary checks. An ASSERT failure will stop the test immediately, which is essential to prevent null-pointer crashes and allow for the immediate elimination of the root cause.
8. Follow the “Code Quality” Plugin Examples

Unreal Engine includes a “Code Quality Unreal Test Plugin” (under Plugins/Tests).

Tip: If you are unsure about the syntax, enable this plugin in the Editor and browse its source code. It contains a comprehensive suite of example tests that demonstrate best practices for using the CQTest module in a production environment.