---
layout: default
title: FakeIt
---

<!-- ai-generation-failed -->

<h1>FakeIt</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/FakeIt/FakeIt.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ome a popular choice for developers writing Low-Level Tests (LLT) in Unreal Engine. It is a header-only library that allows you to create “mocks”—simulated versions of interfaces or classes—without the need for the boilerplate code usually associated with manual stubbing.

In Unreal development, it is primarily used to isolate a specific unit of code by “faking” its dependencies (such as a Game Instance, a Data Provider, or a Network Service). This allows you to test logic in a vacuum, eliminating the need to initialize the full Engine, World, or complex Actor hierarchies.

Practical Usage Tips and Best Practices
1. Wrap as a Third-Party Module

Since FakeIt is a header-only library, it should be integrated into your project as a ThirdParty module.

Best Practice: Place the fakeit.hpp file in a Source/ThirdParty/FakeIt directory and create a FakeIt.Build.cs. Only add this as a dependency to your Test modules. This ensures the library is excluded from your final game binaries, eliminating any unnecessary footprint in your “Shipping” build.
2. Focus on Mocking C++ Interfaces

FakeIt is highly effective at mocking pure C++ interfaces or UInterfaces.

Tip: If you have a system that relies on an interface like IMyDataService, use Mock<IMyDataService> MockService;. You can then use MockService.get() to pass a “fake” implementation into your class constructor. This helps you eliminate the complex setup required to spawn a real UObject during a unit test.
3. Verify Method Calls for Side Effects

One of the most powerful features of FakeIt is its ability to ensure that a specific function was called during a test.

Action: Use Verify(Method(MockObj, MyFunction)).Once(); to confirm that your code triggered a critical event, such as an “EliminatePlayer” notification or a “SaveGame” call. This allows you to test side effects without actually modifying a database or file, eliminating potential side-effect bugs.
4. Use ‘When’ to Stub Return Values

If your logic branches based on the result of a function call (e.g., checking if a player has enough gold):

Tip: Use When(Method(MockObj, GetCurrentGold)).Return(500);. This allows you to force a specific logic path instantly. By controlling the environment this way, you eliminate the need to set up complex inventory or economy states just to test a single “Purchase” function.
5. Reset Mocks Between Test Sections

FakeIt mocks maintain their internal state (like call counts) throughout their lifetime.

Best Practice: If you are using Catch2 (the framework behind Unreal’s LLT), always call MockObj.Reset(); inside your SECTION blocks or TearDown functions. This ensures each test starts with a clean slate, eliminating “flaky tests” where one test fails because of the actions of a previous one.
6. Avoid Mocking Complex UObjects Directly

FakeIt relies on standard C++ virtual tables, which can conflict with Unreal’s UObject reflection and memory management system.

Action: Do not try to mock an ACharacter or ULevel. Instead, extract the specific logic you want to test into a separate C++ interface and mock that. This approach helps you eliminate the “Object Initializer” and “World” crashes that often occur when trying to use mocks with the garbage collector.
7. Combine with ‘CQTest’ for Cleaner Code

If you are using the Code Quality Test (CQTest) plugin:

Tip: Define your FakeIt mocks as members of your FTestFixture. This allows you to access them across multiple test cases within the same suite, eliminating repetitive setup code and keeping your test files concise and readable.
8. Stub Multiple Calls with Sequences

Sometimes a function needs to return different values on subsequent calls (e.g., a random number generator or a paginated data fetch).

Action: Use FakeIt’s sequence support: When(Method(MockObj, GetData)).Return(1, 2, 3);. This ensures the first call returns 1, the second returns 2, and so on. This allows for more realistic testing of loops and iterators, eliminating the need to manually track state inside your mocks.