---
layout: default
title: AutomationWorker
---

<!-- ai-generation-failed -->

<h1>AutomationWorker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AutomationWorker/AutomationWorker.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, AnalyticsET, AutomationMessages, AutomationTest, Core, CoreUObject, Engine, Json, JsonUtilities, RHI</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine’s automation system. While the AutomationController acts as the manager/orchestrator, the AutomationWorker is the part that lives inside every running instance of the engine (Editor, Game, or Commandlet) to actually execute tests.

What it is and What it’s used for

This module is responsible for the low-level communication between a specific engine instance and the automation controller. It listens for commands over the Unreal Message Bus and handles the local “heavy lifting” of the testing process.

Primary uses include:

Test Execution: Receiving instructions to start a specific test and triggering the local code to run it.
Heartbeat & Status: Reporting back to the controller that the instance is still alive and whether it is currently “Available” or “Busy.”
Log & Error Capture: Intercepting local UE_LOG calls, warnings, and errors during a test and sending them back to the controller for the final report.
Environment Reporting: Informing the controller about the local hardware, OS, and project version so the manager can decide which tests are compatible with that worker.
Practical Usage Tips and Best Practices
1. Enable Messaging for Remote Workers

For an instance to act as an Automation Worker, it must be able to communicate. If you are running a packaged build on a mobile device or console, you must include the -Messaging flag in your launch command. Without this, the AutomationWorker module cannot “check in” with the controller.

2. Identify Workers via Instance Names

When running multiple workers on a single machine (or a farm), use the -InstanceName="Worker01" argument. The AutomationWorker will report this name to the controller, making it much easier to identify which specific device or process failed a test during a large-scale run.

3. Monitor the Heartbeat

If a worker crashes or hangs, the controller detects this because the AutomationWorker stops sending “heartbeat” messages. If you are writing a long-running functional test that performs heavy CPU tasks, ensure you aren’t blocking the main thread so long that the worker fails to send its heartbeat, which would cause the controller to eliminate the test prematurely.

4. Capturing Screenshots

The AutomationWorker handles the “Screen Shot” command during automated visual tests. It captures the render target data and sends it back to the controller (and the Screenshot Comparison tool). Ensure your worker has a valid window or “Offscreen Rendering” enabled, or the screenshot captured by the worker will be blank.

5. Use the “Worker” Filter in Session Frontend

In the Session Frontend, the “Session Browser” on the left shows all active workers. If a worker appears but has no tests listed, it usually means the AutomationWorker is active, but the specific test plugins (like FunctionalTesting) aren’t loaded in that instance.

6. Avoid Blocking the Message Bus

The AutomationWorker relies on the engine’s Message Bus (UDP by default). If your network has strict firewall rules or if your game logic is saturating the network thread, the worker may lose connection to the controller. Keep the testing network clear of heavy gameplay traffic when possible.

7. Handle Instance Shutdown Gracefully

When a test suite finishes, the controller might send a command to shut down the worker. The AutomationWorker module handles this request. If your game has custom cleanup logic (like saving a database), ensure it is called via FCoreDelegates::OnExit so the worker can close the process without leaving “ghost” tasks in the background.

8. Verify Automation Module Loading

By default, the worker logic is compiled into most builds, but it may not be initialized in “Shipping” configurations. If you need to run automation tests on a Shipping build for performance verification, you must ensure the AutomationWorker module is included in your *.Target.cs and that the -AutomationWorker flag is passed at runtime.