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

rface for the Session Frontend Automation tab. While the AutomationController module handles the underlying logic and execution of tests, AutomationWindow is responsible for the visual representation of test suites, the results panel, filtering tools, and the controls used to trigger unit, feature, and stress tests within the Unreal Editor or standalone Unreal Frontend (UFE).

Practical Usage Tips & Best Practices
1. Use Standalone Unreal Frontend for Heavy Testing

Running complex automation tests within the main Editor can lead to performance degradation or crashes.

Best Practice: Navigate to Engine/Binaries/Win64/UnrealFrontend.exe. This standalone application uses the AutomationWindow module to run tests on external devices or separate instances of the game, keeping your main development environment stable.
2. Leverage Filters to Isolate Failures

The Automation Window can display thousands of tests. Use the Filter search bar and the Checkbox tree to isolate specific areas (e.g., “Project.Maps” or “System.Core”). This allows you to focus on relevant tests and ignore unrelated failures that might be present in a large-scale project.

3. Enable “Error” and “Warning” Toggles

In the results panel, use the high-level toggle icons for Errors and Warnings. If a test suite fails, disabling the “Display Success” toggle allows for the immediate elimination of visual clutter, leaving only the specific log entries that caused the failure.

4. Batch Tests for Efficient Execution

Instead of running tests one by one, you can select entire categories in the tree view and click Start Tests. The window will queue these tests and execute them in sequence. This is the best practice for a “Pre-Checkin” routine to ensure that local changes haven’t broken core systems.

5. Integrate Screenshot Comparison

The Automation Window works in tandem with the Screen Comparison tab. When running functional tests that capture images, use the window’s results to jump directly to the comparison tool. This is essential for verifying that UI elements or rendering features haven’t regressed after an engine update.

6. Export Results for Documentation

After a large test run (such as a full night-build sweep), use the Export button in the toolbar to save the results as a CSV file. This data can be archived or used to track the elimination of persistent bugs over the course of a development sprint.

7. Monitor “In Progress” Status

The window provides real-time feedback on which test is currently running. If a test hangs, the window will show it as “In Progress” indefinitely. This is a clear indicator that the specific test has hit an infinite loop or a deadlock, requiring a manual elimination of the test process to resume the suite.

8. Utilize Device Groups for Multiplayer Testing

If you have multiple instances of the game connected via the Session Browser, the Automation Window allows you to group these devices. You can trigger a single test that runs across all selected instances simultaneously, which is a best practice for verifying network replication and server-side logic.