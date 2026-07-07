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

Unreal Engine Automation Framework. While individual tests are defined in various modules (like Core or Engine), this module provides the logic to discover, manage, and execute those tests across one or more connected “workers” (local or remote instances of the engine).

It acts as the backend for the Session Frontend and Automation tabs, tracking test states, aggregating results, and handling the communication between the UI and the underlying test runners.

Practical Usage Tips & Best Practices
1. Include for Custom Test Runners

If you are building a custom editor utility or a dedicated test-reporting tool in C++, you must add AutomationController to your Build.cs. It is the primary interface for programmatically triggering tests without manually clicking the UI.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AutomationController");

	}
Copy code
2. Access the Manager Singleton

To interact with the test suite in C++, access the IAutomationControllerManager through its module interface. This allows you to query the list of available tests, start a specific test, or filter tests by name or category:

C++
	IAutomationControllerModule& AutomationModule = FModuleManager::LoadModuleChecked<IAutomationControllerModule>("AutomationController");

	IAutomationControllerManagerPtr Manager = AutomationModule.GetAutomationController();
Copy code
3. Use for Multi-Machine Orchestration

The AutomationController is designed to handle multiple “workers.” This means you can have a single Session Frontend on your PC controlling an Xbox, a PlayStation, and a mobile device simultaneously. The module handles the distribution of tests and ensures that the elimination of a single device (e.g., a crash) is reported correctly without stopping the entire suite.

4. Filter by Machine for Consistency

When running a large suite, use the SetFilter() functions to isolate tests to specific hardware. Some tests may only be valid on platforms with specific graphics capabilities (like Ray Tracing). Using the controller to apply metadata filters ensures you don’t receive “False Fail” results from incompatible workers.

5. Monitor Test Completion Delegates

Instead of polling for test results, bind to the delegates provided by the manager, such as OnTestsComplete or OnTestStateChanged. This is the most efficient way to trigger follow-up actions, such as automatically closing the engine or sending a notification to a Discord/Slack webhook once the run finishes.

6. Leverage for CI/CD Integration

In a Continuous Integration (CI) environment, the AutomationController logic is what processes the command-line arguments like -ExecCmds="Automation RunTests ...". Understanding how the controller parses these commands allows you to construct complex, automated test runs that output standardized JSON reports for your build server.

7. Handle Latent Commands Correctly

The controller manages the lifecycle of “Latent Commands” (tests that take multiple frames). If your test involves loading a map or waiting for an actor to be eliminated, ensure your commands return true only when the action is finished. The controller uses this return value to know when to move to the next test in the queue.

8. Verify Worker Connectivity

If tests are not appearing in the list, use the AutomationController to verify the “Worker Count.” If the controller doesn’t see any workers, it usually indicates a network/firewall issue or that the target instances do not have the Automation Utilities plugin enabled. Ensure your worker and controller are on the same subnet for reliable discovery.