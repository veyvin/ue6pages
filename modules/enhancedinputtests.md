---
layout: default
title: EnhancedInputTests
---

<!-- ai-generation-failed -->

<h1>EnhancedInputTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/EnhancedInputTests/EnhancedInputTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, EnhancedInput, EnhancedInputTestSuite, InputCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

suite designed to validate the functionality of the Enhanced Input system through automated tests.

Description and Purpose

This module utilizes the CQTest (Code Quality Test) framework to provide a collection of functional and unit tests specifically for the Enhanced Input plugin. Its primary purpose is to verify that input actions, mapping contexts, modifiers, and triggers behave as expected across various scenarios. It serves as both a validation layer for the engine’s input architecture and a reference point for developers who wish to implement their own automated input testing. By using this module, teams can ensure that critical gameplay mechanics—such as character movement or ability activation—are not broken by engine updates or configuration changes.

Practical Usage Tips and Best Practices
Study the CQTest Implementation
This module is one of the best examples of how to use the CQTest fixture system. Analyze its source to see how it sets up a temporary UEnhancedInputLocalPlayerSubsystem and a dummy Player Controller. This will help you eliminate boilerplate when writing your own custom input tests.
Test Input Injection for Reliability
Use the InjectInputForAction patterns found in this module to simulate player behavior without needing a physical controller or keyboard. This allows you to eliminate human error and nondeterministic results when testing complex sequences, such as a multi-key combo required for an elimination move.
Validate Custom Triggers and Modifiers
If you create a custom UInputTrigger (e.g., a “Triple Tap”), create a test modeled after this module to verify it. Testing edge cases, like the user releasing the key exactly one frame before the threshold, helps you eliminate “feel” issues before they reach the players.
Verify Mapping Context Priorities
Use automated tests to ensure that higher-priority Input Mapping Contexts (IMCs) correctly override lower ones. For instance, you can write a test to confirm that a “Menu” context successfully eliminates the character’s “Jump” action when a UI overlay is active.
Monitor Input State Transitions
The tests in this module frequently check for ETriggerState::Triggered, Started, and Completed. When debugging why an action won’t fire, model your debug logic after these tests to eliminate confusion regarding which part of the trigger lifecycle is failing.
Enable the Plugin for Reference
The “Enhanced Input Code Quality Unreal Test Plugin” can be enabled in the editor. Once active, you can view and run these tests via the Session Frontend. This is an excellent way to eliminate guesswork when trying to understand the engine’s internal input processing order.
Automate Platform Redirect Tests
If you use “Mapping Context Redirects” for different platforms (like swapping Face Buttons for different consoles), use the logic found in this module to verify that the correct assets are loaded on each simulated platform. This helps you eliminate “wrong button” bugs in cross-platform titles.
Combine with Automation Driver
For high-level functional tests, combine the Enhanced Input injection found here with the Automation Driver to simulate a full gameplay loop. For example, simulate a player walking into a zone and pressing a button to trigger an elimination sequence, then use the test to verify that the actor was successfully removed from the world.