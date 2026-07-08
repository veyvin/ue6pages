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

y used C++ testing framework (often referred to as GTest). It is part of Unreal Engine’s Low-Level Tests (LLT) framework, designed for high-performance, standalone unit testing that operates independently of the full engine environment.

Unlike the standard Automation System which runs inside the Editor or Game process, GoogleTest is used to create Explicit Tests. These are compiled into small, fast-executing console applications that can test core C++ logic, math libraries, or low-level containers. This approach helps eliminate the long startup times and overhead associated with launching the full Unreal Engine executable for simple logic verification.

Practical Usage Tips and Best Practices
Inherit from TestModuleRules
When setting up your test module in *.Build.cs, inherit your class from TestModuleRules. This specialized class automatically configures the include paths and dependencies for GoogleTest, helping to eliminate manual configuration errors for the testing environment.
Use for Non-UObject Logic
GoogleTest is most effective for testing “pure” C++ code that does not rely on the UObject system or the Engine’s reflection. Use it to verify math utilities, data parsing, or custom algorithms to eliminate the complexity of mocking the entire Unreal reflection system.
Implement “Death Tests” Safely
GoogleTest supports “Death Tests” (verifying that a program crashes or asserts when expected). In Unreal, use these to ensure your code correctly triggers a check() or ensure() under invalid conditions, which helps eliminate silent failures in your production code. (Note: use ASSERT_DEATH or EXPECT_DEATH macros).
Organize via Source/Programs
Place your GoogleTest projects in the Source/Programs directory of your engine or project. This keeps your testing code physically separated from your runtime code, ensuring that test artifacts are eliminated from your final game shipping builds.
Leverage GMock for Dependency Injection
The module typically includes GoogleMock (GMock). Use it to create mock objects for external services like file systems or network APIs. This allows you to eliminate side effects and test your logic in complete isolation from the OS or hardware.
Execute via Command Line for CI/CD
Run your GoogleTest executables via the command line with the --gtest_output=xml flag. This generates industry-standard reports that can be read by build servers (like Jenkins or TeamCity) to eliminate manual verification of test results in your automation pipeline.
Use Test Suites for Logical Grouping
Organize related tests into TEST_F (Test Fixture) classes. This allows you to define SetUp() and TearDown() logic once for multiple tests, helping to eliminate code duplication and ensuring a clean state for every individual test run.
Filter Tests with –gtest_filter
When running tests locally, use the --gtest_filter argument to run specific tests or suites (e.g., MyModule.*). This helps you eliminate time wasted running your entire test suite when you are only iterating on a single feature.