---
layout: default
title: AutomationDriver
---

<!-- ai-generation-failed -->

<h1>AutomationDriver</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AutomationDriver/AutomationDriver.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, InputCore, Json, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine designed to simulate user input at the platform layer. Unlike high-level gameplay scripts, it acts as a “shim” between the OS and the engine, allowing you to simulate cursor movement, mouse clicks, keyboard typing, and drag-and-drop actions in a way that is platform-agnostic.

It is primarily used for Functional Testing and UI Automation. Because it operates at the platform layer, it can interact with Slate widgets, UMG, and even scene actors, making it the ideal tool for writing “smoke tests” or verifying complex UI flows (like sign-up forms or inventory management) without manual testing.

1. Enable and Disable the Module Correctly

The Automation Driver is disabled by default to prevent it from interfering with standard user input. You must explicitly wrap your test logic with Enable/Disable calls. Failing to disable it will leave the engine’s input blocked for the remainder of the session.

C++
	IAutomationDriverModule::Get().Enable();

	// ... Run tests ...

	IAutomationDriverModule::Get().Disable();
Copy code
2. Leverage the Fluent API for Readability

The driver uses a “Fluent” syntax (method chaining) to make tests easy to read and maintain. This makes your automation scripts look like a sequence of human actions.

C++
	Driver->CreateSequence()->Actions()

	    .Focus(MyButton)

	    .Click(MyButton)

	    .Perform();
Copy code
3. Use Robust Element Locators

Avoid hardcoding pixel coordinates for clicks. Use the By::Id() or By::Path() locators to find UI elements. By::Id is particularly useful for finding specific widgets that have been tagged in the UMG designer, ensuring your tests don’t break if the UI layout changes.

4. Handle Latent Actions with Sequences

UI interactions often require time for animations or state changes to occur. Use FDriverSequenceRef to group actions together. The driver handles the timing between these actions, which is much more reliable than using standard Delay nodes or sleep commands.

5. Isolate Test State

A core best practice in automation is to ensure one test doesn’t affect the next. Before starting a sequence, always ensure the game or editor is in a “clean” state. If your test generates a file or changes a setting, your script should include logic to revert those changes or eliminate temporary assets once the test completes.

6. Use Tab and Shift+Tab for Form Testing

When testing complex UIs like login screens or character creators, use the .Type(TEXT("\t")) command. Simulating the Tab key is the most efficient way to verify that your UI’s “Focus Path” is correctly configured, ensuring that users can navigate your game using only a keyboard or controller.

7. Debug with Visual Feedback

If a test is failing, you can use the Wait action within a sequence to pause the simulation. This allows you to visually inspect the state of the UI at a specific moment.

Tip: Combined with the Screenshot Comparison Tool, you can have the driver navigate to a menu and automatically capture a screenshot to detect visual regressions.
8. Optimize Performance of Smoke Tests

While the Automation Driver is powerful, it is slower than a standard unit test because it must wait for the UI to respond.

Best Practice: Keep your “Smoke Tests” (tests that run on every build) limited to critical paths. Use the Automation Driver for “Feature Tests” that verify user experience, while keeping logic-heavy checks in the lower-level Automation Spec framework to minimize total build time.