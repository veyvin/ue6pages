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

Engine that provides the user interface for the Automation Tab within the Session Frontend.

Description and Purpose

This module defines the UI components and logic for the Automation Window, which is the primary hub for running automated tests (Unit, Feature, and Stress tests) within the editor or on remote sessions. It interfaces with the AutomationController to display available tests, trigger execution, and visualize real-time results. Its purpose is to give developers a centralized location to verify code stability, content integrity, and performance across multiple local or networked devices simultaneously.

Practical Usage Tips and Best Practices
Access via Session Frontend
The window is most commonly accessed by navigating to Tools > Session Frontend and selecting the Automation tab. If no tests appear, ensure you have selected your local machine or a connected device in the Session Browser on the left.
Enable Test Plugins First
In modern versions of Unreal Engine (5.x), many automation tests are moved to specific plugins (e.g., EditorTests, RuntimeTests). You must enable these plugins and restart the editor before the AutomationWindow can populate its list with those specific test suites.
Utilize Filters to Reduce Noise
As your project grows, the list of tests can become overwhelming. Use the Filter bar in the Automation window to isolate tests by category (e.g., “Project,” “System,” or “Smoke”) or use the search bar to find specific functional tests quickly.
Run Tests in Parallel
By selecting multiple instances in the Session Browser (e.g., a PC and a connected mobile device), the Automation window allows you to run tests in parallel. This is the most efficient way to verify cross-platform features and eliminate bugs that only appear on specific hardware architectures.
Review Screenshot Comparisons
The Automation window is closely tied to the Screenshot Comparison tool. When running rendering tests, use the window to identify visual regressions. It allows you to “blink” between the “Ground Truth” image and the “Current” test result to spot subtle pixel differences.
Automated Elimination Logic Testing
When building combat systems, create a Functional Test that simulates an elimination event (e.g., spawning an actor, applying damage, and checking for the destroyed state). You can then use the Automation window to run this test repeatedly across different characters to ensure the elimination logic remains consistent as your codebase changes.
Monitor the Output Log for Errors
While the Automation window shows a Green/Red status, the detailed reasons for failure are pushed to the Results panel at the bottom. Check this area for specific “Error” or “Warning” strings; fixing these will help you eliminate the root cause of a failing test suite.
Keep “Smoke Tests” Fast
A best practice is to tag your most vital tests as “Smoke Tests.” Use the Automation window to run these every time you sync code. Because these tests are designed to be nearly instantaneous, they provide immediate feedback, helping you eliminate catastrophic breaks before they affect the rest of the team.