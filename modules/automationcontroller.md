---
layout: default
title: AutomationController
---

<!-- ai-generation-failed -->

<h1>AutomationController</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AutomationController/AutomationController.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, AutomationMessages, AutomationTest, Core, CoreUObject, EditorFramework, Engine, HTTP, Json, JsonUtilities, MessageLog, ScreenShotComparisonTools, UnrealEdMessages</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or Unreal Engine’s automated testing framework. It acts as the “brain” that coordinates between the user interface (like the Session Frontend), the test worker instances, and the test reports.

What it is and What it’s used for

The module provides the logic for discovering, queuing, and executing tests across multiple local or remote instances. While the AutomationTest classes define what a test does, the AutomationController manages how and when those tests are run.

Primary uses include:

Test Discovery: Scanning the engine and plugins to build a comprehensive list of available Smoke, Unit, and Functional tests.
Worker Management: Tracking “Workers” (active game or editor instances) that are available to perform testing tasks.
Result Aggregation: Collecting pass/fail data, error logs, and screenshots from workers and consolidating them into a single report.
Execution Flow: Managing the lifecycle of a test suite, including handling timeouts and retries for flaky tests.
Practical Usage Tips and Best Practices
1. Accessing the Manager via C++

To interact with the automation system programmatically (e.g., to trigger a test suite from a custom editor button), use the IAutomationControllerManager interface. You can access it through the module:

C++
	IAutomationControllerModule& AutomationControllerModule = FModuleManager::LoadModuleChecked<IAutomationControllerModule>("AutomationController");

	IAutomationControllerManagerPtr Manager = AutomationControllerModule.GetAutomationController();
Copy code
2. Filtering Tests for CI/CD

In a Continuous Integration (CI) environment, you often want to run only a subset of tests. Use the SetFilter() and SetFilters() methods in the controller to isolate specific categories (like “SmokeTests”) before execution. This ensures quick feedback loops by eliminating the need to run heavy stress tests on every code commit.

3. Handling Remote Workers

The AutomationController can manage workers across a network via the Unreal Message Bus. Ensure that your remote devices (consoles or mobile) are on the same subnet and that the -Messaging command line argument is enabled. The controller will automatically discover these instances and allow you to distribute tests to them.

4. Monitor Test Timeouts

If a test hangs, the AutomationController will eventually time it out to prevent the entire pipeline from stalling. You can configure these thresholds in your BaseEngine.ini or via the manager. If your functional tests involve long loading screens, ensure your timeout values are high enough to prevent premature elimination of the test process.

5. Exporting Results to JSON

For automated reporting in tools like Jenkins or TeamCity, the controller can be configured to export results to a standardized format. Use the -ReportOutputPath="Path/To/Folder" command line argument when running the editor to tell the controller to generate a index.json containing all test results.

6. Use the “Run All” Strategy Carefully

When using the controller to “Run All” tests, be mindful of the Automation Test Guidelines. Tests should be isolated; if one test modifies a global setting or deletes an actor that a subsequent test requires, the AutomationController will report a failure that is difficult to debug. Always ensure tests “leave the state as they found it.”

7. Parallelization Benefits

The AutomationController supports running different tests on different workers simultaneously. If you have four connected devices, you can distribute a large suite across all of them. This is managed by the controller’s task distribution logic, significantly reducing the total time required for a full regression pass.

8. Verify Worker “Ping” State

In the Session Frontend, if a worker appears grayed out, the AutomationController has lost communication with it. This often happens if the worker process has crashed or is suspended. Before starting a long test run, verify that the controller shows all intended workers as “Available” to avoid missing data in your final report.