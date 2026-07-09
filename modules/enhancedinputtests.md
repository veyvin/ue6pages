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

gned to validate the functionality of the Enhanced Input system. It contains a collection of C++ automation tests that verify complex input scenarios, including Input Action triggering, Mapping Context prioritization, chorded inputs, and modifier logic. This module is essential for developers extending the input system or for studios that need to ensure their custom input configurations remain functional across engine updates.

Practical Usage Tips & Best Practices
1. Enable via the “Enhanced Input Code Quality” Plugin

The tests within this module are not visible by default. To access them, you must enable the Enhanced Input Code Quality Unreal Test Plugin in the Editor’s plugin menu.

Best Practice: Once enabled, restart the Editor and open the Session Frontend (Tools > Sessions Frontend). Look for the Project.Plugins.EnhancedInput category to run the suite, facilitating the elimination of guesswork regarding whether your input stack is properly initialized.
2. Use for Verifying Input Action Chords

Chorded actions (where Action B only triggers if Action A is held) can be prone to logic errors as the project grows.

Tip: Refer to the tests in this module to see how the engine validates UInputTriggerChordedAction. Running these tests ensures the elimination of “input ghosting” or cases where complex combinations fail to trigger under specific framerate conditions.
3. Test Mapping Context Prioritization

When multiple UInputMappingContext assets are pushed to the UEnhancedInputLocalPlayerSubsystem, their priority values determine which mappings override others.

Best Practice: Use the automation tests to verify that “Vehicle” mappings correctly override “OnFoot” mappings when both are active. This leads to the elimination of control conflicts where a player accidentally performs a foot-based action while driving.
4. Reference for Mocking Input in C++

Writing unit tests for player input can be difficult because it usually requires hardware interaction.

Tip: Study the FAutomationTestBase implementations within this module to see how they use FEnhancedInputEditorSystem::InjectInputForAction. This pattern allows for the elimination of manual “play-in-editor” testing by simulating key presses directly in code.
5. Validate Custom Modifiers and Triggers

If you create custom UInputModifier or UInputTrigger classes in C++, you should create a test class in a sibling module modeled after the ones here.

Best Practice: Model your tests after the existing InputModifierTests. Verifying that your custom “Deadzone” or “Sensitivity Curve” logic handles edge cases (like zero or negative input) ensures the elimination of erratic camera behavior.
6. Debugging Input Consumption

The “Consume Input” setting on Input Actions can prevent lower-priority actions from firing.

Tip: Use the tests to observe how the engine handles “consumed” vs “non-consumed” states. Understanding this logic through the provided tests results in the elimination of bugs where UI inputs “leak” through to the character movement logic.
7. Isolate Input State in Tests

Input state can persist between test runs if not handled carefully, leading to “false positives.”

Best Practice: Follow the module’s pattern of using Setup() and Teardown() to clear the IEnhancedInputSubsystemInterface after each test. This cleanup ensures the elimination of state contamination, where a “Held” key from a previous test affects the next one.
8. Verify Enhanced Input vs. Legacy Input

If your project is transitioning from the legacy “Action/Axis Mappings,” these tests provide a baseline for expected behavior.

Tip: Run the module’s full suite to ensure the elimination of inconsistencies between the old system and the new Enhanced Input architecture, ensuring that “Digital” and “Analog” inputs behave as expected across all platforms.