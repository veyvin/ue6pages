---
layout: default
title: AutomationWindow
---

<!-- ai-generation-failed -->

<h1>AutomationWindow</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AutomationWindow/AutomationWindow.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AutomationController, AutomationTest, Core, CoreUObject, DesktopPlatform, EditorFramework, Engine, InputCore, Json, JsonUtilities, Kismet, Slate, SlateCore, SourceControl, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

interface and frontend logic for the Automation Tab within the Session Frontend. It serves as the primary visual hub for managing, filtering, and executing automated tests.

Description

This module is used to bridge the low-level AutomationController with a user-friendly Slate interface. It allows developers to see all available tests (Unit, Feature, and Stress tests) registered in the engine or project. Through this window, you can target specific local or remote sessions, run batches of tests, and visualize results in real-time. It is the essential tool for maintaining code quality and ensuring that new features do not introduce regressions or “break” existing gameplay systems.

Practical Usage Tips and Best Practices
1. Accessing via Tools Menu

The UI powered by this module is located at Tools > Session Frontend. Once open, navigate to the Automation tab. If you do not see any tests listed, ensure you have an active session selected in the “Session Browser” on the left—usually, this is your local editor instance.

2. Enable Required Plugins

In modern Unreal Engine versions (5.x+), many tests are moved to plugins. To see a full list of tests in the Automation Window, you must enable the Test Automation and Functional Testing Editor plugins. Without these, the window managed by this module may appear empty or missing core engine tests.

3. Use Search and Filters for Large Projects

As projects grow, the number of tests can reach into the thousands. Use the filter bar provided by the AutomationWindow to search by “Test Name” or “Source File.” You can also filter by “Smoke Tests” to run only the most critical, high-level checks, which helps eliminate long wait times during quick iterations.

4. Monitor Remote Sessions

One of the most powerful features of this module is the ability to run tests on a separate device (like an Android phone or a console) and view the results in the editor on your PC. As long as the remote device is on the same network and running a “Development” build, it will appear in the Session Browser, allowing you to trigger tests and see logs remotely.

5. Analyze Failures with the Results Panel

When a test fails, the AutomationWindow displays a detailed log in the bottom panel. Look for red text to identify the specific assertion that failed. This module also integrates with the Screenshot Comparison tool; if a visual test fails, you can use the window to compare the “Expected” image versus the “Actual” image side-by-side.

6. Leverage Grouping for Batch Execution

Tests are organized hierarchically (e.g., Project.Character.Movement). You can check the box for an entire group to run every sub-test. This is a best practice before submitting code to source control: run the relevant group for your module to ensure you haven’t caused a regression.

7. Automate Elimination Logic Testing

For gameplay-critical paths like player elimination, create Functional Tests. These are small levels that simulate an elimination event automatically. You can then use the Automation Window to run these tests across different characters or weapons to ensure that the “OnEliminated” events, VFX, and score logic always trigger correctly.

8. Performance and Memory Tracking

The window provides columns for “Duration” and “Participants.” Use these to identify “bottleneck” tests that take too long to run. By optimizing slow tests, you eliminate friction in your CI/CD pipeline, ensuring that the entire test suite remains fast enough for developers to run frequently throughout the day.