---
layout: default
title: GoogleTest
---

<!-- ai-generation-failed -->

<h1>GoogleTest</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/GoogleTest/GoogleTest.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ration of the popular Google C++ testing and mocking framework. While Unreal Engine 5 uses Catch2 as the primary backend for its modern Low-Level Tests (LLT) framework, the GoogleTest module is maintained to support developers who prefer GTest’s specific feature set, such as value-parameterized tests, typed tests, and advanced death tests.

It is primarily used for testing core C++ logic, mathematical utilities, and data structures that do not rely on the UObject system or the full Unreal Engine runtime environment.

Practical Usage Tips and Best Practices
1. Isolate as a Test-Only Dependency

The GoogleTest module should never be included in your runtime game modules.

Best Practice: Only add the "GoogleTest" dependency to modules specifically designed for testing, such as those with a LoadingPhase set to Developer or Editor. This ensures the testing framework is completely eliminated from your “Shipping” game binaries.
2. Target Non-UObject Logic

GoogleTest is most effective when testing “pure” C++ code that is difficult to isolate within the standard Unreal Automation System.

Tip: Use GTest for low-level libraries like custom JSON parsers, math extensions, or standalone pathfinding algorithms. This allows you to run tests in seconds by eliminating the need to boot the Unreal Editor or initialize the full Engine.
3. Use EXPECT vs ASSERT Correctly

GTest distinguishes between non-fatal and fatal failures.

Action: Use EXPECT_EQ() for standard checks to allow a test to continue and report multiple errors in a single run. Use ASSERT_EQ() only when a failure makes the rest of the test unsafe to execute (e.g., checking if a pointer is null). This helps you eliminate redundant debugging by providing more context per failure.
4. Leverage Test Fixtures

If multiple tests share the same setup or teardown logic, do not copy-paste code.

Best Practice: Inherit from testing::Test to create a fixture class. Use SetUp() to initialize resources and TearDown() to clean them up. This helps you eliminate code duplication and ensures that each test begins in a consistent, clean state.
5. Integrate into the Low-Level Tests (LLT) Runner

You can use the GTest module within Unreal’s LLT framework to create standalone console applications for testing.

Action: In your .Build.cs, inherit from TestModuleRules and set the second constructor parameter to false if you are using GTest instead of Catch2. This allows you to build a dedicated .exe for your tests, eliminating the overhead of the main engine executable during your iteration loop.
6. Run via Command Line with Filters

Running a full test suite can be time-consuming as your project grows.

Tip: Use the --gtest_filter command-line argument to run specific tests (e.g., MyProjectTests.exe --gtest_filter=MathTests.*). This allows you to focus only on the logic you are currently editing, effectively eliminating wasted time spent waiting for unrelated tests to pass.
7. Handle Unreal Types with Care

GTest does not natively know how to print Unreal-specific types like FString, FVector, or FName.

Action: When comparing these types, convert them to standard strings or floats (e.g., EXPECT_STREQ(*MyFString, "Expected")). Alternatively, provide a custom operator<< for those types in your test module to eliminate unreadable error messages in the test output.
8. Prefer Catch2 for “Unreal-First” Testing

Epic Games is increasingly optimizing the Unreal Engine ecosystem for Catch2.

Best Practice: Unless you have a specific requirement for GTest (like legacy code or a specific mocking feature), consider using the built-in Catch2 support in the LLT framework. This helps you eliminate friction by following the engine’s modern, preferred path for low-level C++ testing.