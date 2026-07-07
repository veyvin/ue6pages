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

xecuting automated tests in Unreal Engine. It exists outside the UObject reflection system to allow for low-level testing of core engine systems, though it is commonly used for higher-level gameplay and editor validation.

It is primarily used to build Simple Tests (single atomic units), Complex Tests (iterative tests for multiple assets), and Automation Specs (behavior-driven development style), all of which are managed via the Session Frontend in the editor.

Practical Usage Tips and Best Practices
1. Follow the Module Directory Convention

To keep your project organized and ensure the engine discovers your tests, place all test files in a Private\Tests directory within your module. If a test is specific to a class, name the file [ClassFilename]Test.cpp (e.g., InventoryComponentTest.cpp).

2. Choose the Right Test Type

Use IMPLEMENT_SIMPLE_AUTOMATION_TEST for atomic unit tests that don’t change state (e.g., math or string parsing). Use IMPLEMENT_COMPLEX_AUTOMATION_TEST when you need to run the same logic across multiple assets, such as checking every Static Mesh in a folder for missing collision.

3. Use Latent Commands for Time-Based Logic

Because tests often need to wait for frames to render or assets to load, use ADD_LATENT_AUTOMATION_COMMAND. This allows the test to pause and resume across multiple frames, which is essential for verifying that an actor’s elimination actually occurred after a delay or animation.

4. Categorize with Flags

Always use appropriate EAutomationTestFlags to control when and where tests run.

SmokeFilter: For critical tests that must run in less than one second.
EditorContext: For tests that require the Unreal Editor to be open.
ProductFilter: For high-level functional tests of game features.
5. Clean Up the Test Environment

Automation tests should be “stateless.” If your test creates a temporary file or spawns an actor, you must ensure the elimination of those objects happens before the test concludes. Use the TearDown functionality or latent commands to reset the world to its original state.

6. Leverage Automation Specs for BDD

For more readable, “human-language” tests, use BEGIN_DEFINE_SPEC. This allows you to write tests using Describe and It blocks (Behavior-Driven Development). This is the modern standard for writing complex gameplay logic tests in C++.

7. Verify via Session Frontend

Run your tests by opening Tools > Session Frontend and navigating to the Automation tab. Here you can filter by your custom categories, view detailed error logs, and see visual indicators of which steps in your test failed.

8. Prevent Code Bloat in Build.cs

Since many automation tests are only relevant during development, you can wrap your test code in #if WITH_DEV_AUTOMATION_TESTS blocks. Ensure the module is added to your Build.cs only when needed to keep shipping builds optimized.

C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("AutomationTest");

	}
Copy code