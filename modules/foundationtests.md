---
layout: default
title: FoundationTests
---

<!-- ai-generation-failed -->

<h1>FoundationTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/LowLevelTests/FoundationTests/FoundationTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, Cbor, Core, CoreUObject, DerivedDataCache, DesktopPlatform, NetworkCacheStores, Serialization, ShaderCompilerCommon, ShaderPreprocessor, TelemetryUtils, ZenOplogUtils</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

el Tests (LLT) framework. It is designed to validate the core, non-UObject C++ systems that form the “foundation” of the engine, such as containers, memory allocators, and math libraries.

What it is and What it’s used for

Located in Engine/Source/Programs/LowLevelTests/FoundationTests, this is an Explicit Test project. Unlike standard Automation Tests that run inside the Editor, FoundationTests are compiled as a standalone executable. This allows them to test the most basic engine modules without the overhead of the Renderer, Slate, or the Blueprints virtual machine.

Primary uses include:

Unit Testing Core Types: Verifying the reliability of base types like FString, TArray, and TMap.
Memory Management Validation: Testing custom allocators and garbage collection primitives in a controlled environment.
Platform Porting: Ensuring that fundamental C++ logic behaves identically across Windows, Linux, and Consoles.
Performance Benchmarking: Running high-iteration loops on low-level functions to detect performance regressions in core code.
Practical Usage Tips and Best Practices
1. Build via the “Tests” Configuration

To work with FoundationTests in Visual Studio, you must change your Solution Configuration to Tests. Then, set FoundationTests as your Startup Project. This compiles a lean version of the engine stripped of gameplay systems, leading to the elimination of long compile times during core logic iteration.

2. Leverage Catch2 Macros

The module is built on the Catch2 framework. Use REQUIRE() for hard requirements that should stop the test immediately upon failure, and CHECK() for non-fatal assertions. This is a best practice for “Unit” style tests where you want to validate multiple states in a single run.

C++
	SECTION("String Concatenation")

	{

	    FString TestStr = TEXT("Epic");

	    TestStr += TEXT(" Games");

	    REQUIRE(TestStr == TEXT("Epic Games"));

	}
Copy code
3. Use Tags for Filtering

FoundationTests uses a tagging system (e.g., [Core][Containers]). When running the executable from the command line, you can specify these tags to run only a subset of tests. This allows for the elimination of unnecessary test runs when you are only modifying a specific system like TArray.

4. Manage Lifecycle in TestGroupEvents.cpp

If your tests require global setup (like initializing a mock file system), use the Tests/TestGroupEvents.cpp file. Be precise with the execution order of BeforeEachGroup and AfterEachGroup to ensure that one test’s data does not leak into the next, which can cause “flaky” or non-deterministic results.

5. Build via RunUAT for CI/CD

To run these tests in a continuous integration pipeline, use the RunUAT (Run Unreal Automation Tool) command: .\RunUAT BuildGraph -Script="Engine/Build/LowLevelTests.xml" -Target="Foundation Tests Win64" This is the standard way to ensure that core engine foundations are stable before a new build is distributed to the wider team.

6. Utilize the “Foundation” as a Template

When creating your own low-level C++ module, use the structure of FoundationTests as a template. Create a .Build.cs that inherits from TestModuleRules and a .Target.cs that inherits from TestTargetRules. This allows your custom code to benefit from the same high-speed, standalone testing environment.

7. Keep Tests Atomic and Deterministic

A best practice within this module is the elimination of external dependencies. Foundation tests should not rely on local databases, network connections, or specific file paths on a hard drive. Use mocking and keep each TEST_CASE focused on a single responsibility to ensure they remain fast and reliable.

8. Verify Platform-Agnostic Code

Always use FPlatform types (like FPlatformMemory) within these tests rather than raw C++ headers. FoundationTests are often the first thing run on new hardware; ensuring your tests use Unreal’s abstraction layers guarantees that the tests themselves aren’t the cause of a platform-specific crash.