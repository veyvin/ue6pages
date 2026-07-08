---
layout: default
title: LowLevelTestsRunner
---

<!-- ai-generation-failed -->

<h1>LowLevelTestsRunner</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/LowLevelTestsRunner/LowLevelTestsRunner.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Catch2, Core, CoreUObject, DerivedDataCache, Engine, Slate, SlateCore, SlateNullRenderer, UnrealEd, src</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Tests (LLT) framework. Built upon an extended version of the Catch2 C++ testing library, this module allows developers to write and run compiled C++ tests that operate outside the full Unreal Engine environment.

Its primary purpose is to provide a “lean” testing path. Unlike the Automation System (which requires the Editor or Game to be running), the LowLevelTestsRunner executes standalone binaries that link only against the specific modules being tested. This helps eliminate the massive overhead of engine startup, allowing unit and integration tests to run in seconds rather than minutes.

Practical Usage Tips and Best Practices
Define Explicit Test Targets
To use the runner, you must create a TestTargetRules class in a .target.cs file. Set IsTestTarget = true; and inherit from TestTargetRules. This tells the Unreal Build Tool (UBT) to use the LowLevelTestsRunner instead of the standard game entry point, helping you eliminate unnecessary engine dependencies during compilation.
Leverage Platform File Stubs
In your test target configuration, use bUsePlatformFileStub = true;. This replaces actual disk I/O with a mock system. This is critical to eliminate side effects on your local file system and to ensure that tests remain fast and deterministic.
Use Catch2 Macros for Assertions
Since the runner is based on Catch2, use macros like REQUIRE(), CHECK(), and SECTION(). These provide much more descriptive failure messages than standard C assert(), helping you eliminate time spent debugging why a test failed.
C++
	TEST_CASE("Math::Addition", "[unit][math]")

	{

	    SECTION("Adding two integers") {

	        REQUIRE(1 + 1 == 2);

	    }

	}
Copy code
Group Tests with Lifecycle Events
The runner supports GROUP_BEFORE_ALL and GROUP_AFTER_ALL macros. Use these to perform one-time setup for a suite of tests (like initializing a library). This helps you eliminate redundant setup code inside every individual TEST_CASE.
Run via Command Line for CI/CD
The runner creates a standalone .exe. You can run this directly from a terminal or build server using arguments like -labels or -tags. This allows you to eliminate manual testing by integrating these low-level checks into your automated “Continuous Integration” pipeline.
Mock UObjects with ‘bMockEngineDefaults’
If your test requires CoreUObject but you don’t want to load actual assets, set bMockEngineDefaults = true; in your target rules. This provides a “fake” environment for UObjects, helping you eliminate the need for cooked content or a valid Content folder during testing.
Use ‘Tests’ Solution Configuration
In Visual Studio or Rider, switch your solution configuration to Tests. This filters the project tree to show only the test-related projects managed by the LowLevelTestsRunner, helping you eliminate visual clutter and focus on your test suite.
Isolate Modules in Build.cs
When writing tests, only include the specific modules you are testing in your TestModuleRules. Minimal dependencies eliminate long link times and ensure that you are truly performing a “unit test” rather than a bloated integration test.