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

grated into Unreal Engine specifically for Low-Level Testing (LLT). It is a header-only library that allows developers to create “mocks” of C++ interfaces and classes.

In the context of Unreal Engine, it is used to “eliminate” dependencies on complex engine systems during unit testing. For example, if you are testing a piece of logic that requires a database or a network interface, you can use FakeIt to create a fake version of that interface that returns predefined values, allowing you to test your code in total isolation.

Practical Usage Tips and Best Practices
Integrate via Build.cs
To use FakeIt in your test module, you must include it in your Build.cs. Since it is typically used with the Low-Level Testing framework, ensure your module inherits from TestModuleRules and adds "FakeIt" to your dependencies. This “eliminates” compilation errors when including the mocking headers.
Mock Interfaces for Isolation
The primary best practice is to mock Abstract Interfaces (IInterface) rather than concrete classes. This “eliminates” the need to instantiate heavy engine objects (like UWorld or GEngine) just to run a simple unit test for a gameplay calculator or data processor.
Use When for Behavior Definition
Use the When(...) syntax to define what a function should return. For example: When(Method(mock, GetHealth)).Return(100.0f);. This “eliminates” non-deterministic behavior in your tests by ensuring the mock always provides the exact data your test case requires.
Verify Method Invocations
Use the Verify(...) macro to ensure that your code actually called a specific function. This is a best practice for “eliminating” logical bugs where a function appears to work but fails to trigger critical side effects, such as sending a notification or saving data.
Strictly for Low-Level Tests (LLT)
FakeIt is designed for pure C++ testing and does not natively support the UObject reflection system or UFUNCTION macros. Use it for “eliminating” dependencies in non-reflected C++ classes. For testing UObject logic, you should generally stick to the native Automation Framework or CQTest.
Reset Mocks Between Tests
Always reset your mocks in the Setup or Teardown phase of your test suite. This “eliminates” state leakage where a configuration from a previous test case accidentally causes a subsequent test to pass or fail incorrectly.
Avoid Mocking the Engine Core
Do not try to mock massive engine classes like AActor. Instead, refactor your code to depend on a small interface that performs the specific task you need. This “eliminates” the complexity of trying to “fake” the entire engine hierarchy, which is often impossible with simple mocking frameworks.
Use “Spying” for Existing Objects
FakeIt allows you to “spy” on a real object to verify calls while still executing the original code. This is useful for “eliminating” uncertainty in integration tests where you want the real logic to run but need to confirm that a specific delegate or log was triggered.