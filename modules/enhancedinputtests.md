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

contains the automated testing suite and unit tests for the Enhanced Input plugin.

Description

This module is used to validate the core logic of the Enhanced Input system, including Input Actions, Mapping Contexts, Triggers, and Modifiers. It leverages the CQTest (Code Quality Test) framework and the Automation Driver to simulate complex player inputs without requiring a human operator. Its primary role is to ensure that the input system remains stable across engine updates and to provide a reference for how developers can write their own automated tests to verify gameplay input logic.

Practical Usage Tips and Best Practices
1. Use InjectInputForAction for Logic Validation

The module demonstrates how to use InjectInputForAction to simulate player behavior. Instead of manually moving a joystick, your tests can call this function to feed specific values (like FVector2D for movement) directly into the Enhanced Input Local Player Subsystem. This is the best practice for the elimination of manual “smoke testing” for basic character controls.

2. Verify Custom Triggers and Modifiers

If you create custom UInputTrigger or UInputModifier classes, use the patterns found in this module to write unit tests for them. You can test edge cases—such as extreme dead zones or rapid-fire triggers—by feeding precise values into the modifier and asserting that the output matches your mathematical expectations.

3. Test Priority with Multiple Mapping Contexts

Use the module’s approach to verify “Mapping Context” prioritization. You can programmatically add a “Vehicle Context” on top of a “Character Context” and use an automated test to ensure the vehicle inputs successfully consume the raw input, preventing the character from moving while driving.

4. Leverage the Automation Driver for Fluent Input

The EnhancedInputTests module utilizes the Automation Driver to create “fluent” test sequences. This allows you to write readable code that says “Press A, wait 0.5 seconds, then Release A.” This is highly effective for testing “Hold” or “Charge” triggers that rely on specific timing intervals.

5. Organize Tests in the Private/Tests Directory

Following the convention used in this module, always place your input tests in a Private/Tests folder within your plugin or project module. This keeps your production code clean and ensures that the Unreal Automation Tool (UAT) can easily locate and execute your input validation scripts.

6. Use ShowDebug EnhancedInput for Visual Verification

While the tests run programmatically, you can use the console command showdebug enhancedinput to visually verify what the tests are doing in real-time. This display shows active mapping contexts and the “Trigger State” of every action, which is invaluable for debugging why a specific test might be failing.

7. Implement Timeout Guards

When testing complex input sequences (like a combo system), always implement a timeout. As seen in the module’s functional tests, if a character fails to reach a specific state because an input wasn’t registered, the test should eliminate the session and report a failure rather than hanging the entire automation pipeline.

8. Validate Input Device Elimination

Use automated tests to simulate the “Elimination” of an input device (e.g., a controller being unplugged). You can verify that the Enhanced Input system correctly clears the “Ongoing” state of any actions that were being held, ensuring your character doesn’t get stuck running in a circle when a battery dies.