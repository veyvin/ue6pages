---
layout: default
title: CelSpec
---

<!-- ai-generation-failed -->

<h1>CelSpec</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/cel-spec/CelSpec.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Protobuf</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ramework or specialized cel-shading implementations in certain engine branches) primarily refers to the Automation Spec system within Unreal Engine’s testing suite. It is a “Behavior Driven Development” (BDD) style testing module that allows developers to write human-readable, fluid specifications for code behavior.

It is used to define “Expectations” for how a unit of code should function, using a syntax similar to Jasmine or Mocha (e.g., Describe, It, BeforeEach). This module is the modern standard for writing unit tests in Unreal Engine 5, intended to eliminate the ambiguity of legacy functional tests.

Practical Usage Tips and Best Practices
Follow the BDD Hierarchy Structure your tests using Describe to group features and It to define specific behaviors. This hierarchy helps eliminate confusion when a test fails, as the error message will clearly state exactly which behavior (the “Spec”) was not met.
Use BeforeEach for Clean State Always initialize your variables and mock objects inside a BeforeEach block. This ensures that every individual test starts with a fresh environment, which is the best way to eliminate “leaky” tests where one failure causes subsequent tests to fail incorrectly.
Avoid the Game Thread for Input Simulation If your Spec involves simulating user input, use the EAsyncExecution::ThreadPool flag within the It block. This allows the test to run off the Game Thread, which is necessary to eliminate deadlocks when waiting for UI or input responses.
Leverage Latent Commands for Time-Based Logic If your code involves timers or delays, use LatentIt. This allows the Spec to wait for a certain condition to be met before proceeding, eliminating the need for fragile Sleep() calls that can make tests non-deterministic.
Use DefineSpec for Data Setup Utilize the BEGIN_DEFINE_SPEC and END_DEFINE_SPEC macros to define the members of your test class. This provides a structured way to hold references to Actors or Components during the test lifecycle, helping to eliminate manual memory management errors.
Implement “Elimination” Checks for Object Cleanup In your AfterEach block, ensure you destroy any Actors spawned during the test. Failing to do so will clutter the transient world and eventually eliminate available memory, potentially causing the Editor to crash during long test runs.
Utilize TEST_TRUE and TEST_EQUAL Always use the built-in macros for assertions. These macros are integrated into the Session Frontend, providing detailed logs of what the expected value was versus the actual value, which helps to eliminate time spent debugging failed tests.
Filter via Automation Flags Assign appropriate flags (like EAutomationTestFlags::ProductFilter) to your Spec. This allows you to eliminate slow-running tests from your daily developer iteration while ensuring they still run during your “Smoke Test” or CI/CD pass.