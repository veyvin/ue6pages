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

support large-scale automated testing in complex projects (such as Sea of Thieves), the CQTest module introduces “test fixtures” and improved macros that reduce the boilerplate code typically associated with Unreal’s automation system. It excels at handling asynchronous execution and provides built-in mechanisms for “Before” and “After” test actions, ensuring a clean state between test runs. It is the preferred choice for developers who need to write tests that are easy to read, maintain, and execute within the Session Frontend or via the command line.

Practical Usage Tips and Best Practices
1. Add the Dependency to Build.cs

To use CQTest in your project, you must first add the module to your *.Build.cs file. Include "CQTest" in your PrivateDependencyModuleNames. Because this is a developer tool, it is common practice to wrap this dependency in a check for the Editor or Development build configurations to ensure it is not included in your final shipping build.

2. Use the BEGIN_CQTEST Macros

Standard Unreal tests require manual class definitions. CQTest provides the BEGIN_CQTEST and END_CQTEST macros. These macros automatically handle the registration of the test with the engine’s automation controller and set up a dedicated namespace, helping to eliminate naming collisions in large test suites.

3. Leverage FTestFixture for State Management

One of the core features of the module is the FTestFixture. Create a custom fixture class to store common variables, such as a pointer to a specific Actor or a temporary Data Table. This allows you to share setup logic across multiple tests. A best practice is to use the fixture to manage the lifetime of objects, ensuring they are correctly cleaned up after every test.

4. Implement BeforeEach and AfterEach

CQTest supports the “Setup/Teardown” pattern through BeforeEach() and AfterEach() methods within your fixture. Use BeforeEach to spawn a test level or initialize a component, and use AfterEach to eliminate any spawned actors. This ensures that a failure in one test does not leave “ghost” objects that cause subsequent tests to fail.

5. Simplify Asynchronous Testing

Testing logic that spans multiple frames (like a character movement or a timer) is notoriously difficult in standard unit tests. CQTest provides helper functions to handle “Latent” commands more cleanly. You can write tests that wait for a specific condition to be met before proceeding, which is essential for verifying gameplay systems like AI or networking.

6. Utilize the CQTest Command Line

For CI/CD pipelines, you can run these tests using the Unreal Automation Controller via the command line. Use the -ExecCmds="Automation RunTests Project.Tests.MyModule" argument. CQTest’s hierarchical naming makes it easy to filter for specific categories, allowing you to run only the most relevant tests for a specific code change.

7. Safety During Actor Elimination Tests

When testing the elimination of gameplay elements, use CQTest to verify the destruction flow. Spawn a target actor, perform the elimination logic (e.g., calling Destroy()), and then use the fixture’s assertions to verify that IsValid(TargetActor) returns false and that the physics proxy has been removed from the world. This ensures your elimination logic is leak-free and network-stable.

8. Refer to the Code Quality Test Plugin

If you are new to the module, enable the Code Quality Unreal Test Plugin in the Editor (Edit > Plugins). This plugin contains a suite of example tests that demonstrate best practices for using the CQTest API. Studying these examples is the fastest way to understand how to structure your own fixtures and assertions effectively.