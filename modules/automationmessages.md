---
layout: default
title: AutomationMessages
---

<!-- ai-generation-failed -->

<h1>AutomationMessages</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AutomationMessages/AutomationMessages.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutomationTest, Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t defines the data structures and network protocols used for communication within the Unreal Automation Framework. It acts as the “language” spoken between the Session Frontend, the Automation Controller, and various connected Automation Workers (such as instances of the game running on a console, mobile device, or remote PC).

This module contains the USTRUCT definitions for messages that handle worker discovery, test execution commands, and the reporting of test results (logs, warnings, and errors) back to the editor.

Practical Usage Tips and Best Practices
1. Include the Module for Custom Automation Tools

If you are building a custom external tool or a specialized CI/CD dashboard that needs to interpret Unreal’s automation traffic, you must include this module in your Build.cs.

C#
	// In YourProject.Build.cs

	if (Target.Type == TargetType.Editor || Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PrivateDependencyModuleNames.Add("AutomationMessages");

	}
Copy code
2. Understand the Message Bus Architecture

The AutomationMessages module relies on the engine’s MessageBus.

Best Practice: When debugging connection issues between a remote device and the editor, use the Messaging Debugger (found in Tools > Debug). This allows you to see the actual FAutomationWorkerDiscover and FAutomationWorkerPing packets being sent, helping you eliminate network configuration errors.
3. Handle Remote Worker Discovery

This module defines how the editor “finds” a game instance running on another machine.

Tip: Ensure that the AutomationWorker is enabled on your target device. If the device isn’t appearing in the Session Frontend, it usually means the discovery messages defined in this module are being blocked by a firewall or a mismatch in the -Messaging command-line parameter.
4. Analyze Test Results Programmatically

The FAutomationWorkerRunTestsReply struct is used to send results back to the controller.

Best Practice: If you are implementing a custom IAutomationLatentCommand, use the logging macros (UE_LOG or AddError) within the test. These are serialized into the message structures of this module. Clearer logging in the test code will eliminate ambiguity when reviewing failed builds in your build farm.
5. Coordinate Parallel Test Execution

The messages in this module allow for “test distributed” workflows.

Tip: When running tests on multiple instances (e.g., 4 instances of the game on one PC), the AutomationMessages module handles the routing of specific test commands to specific workers. This is essential for eliminating long wait times by running your unit tests in parallel.
6. Use for ScreenShot Comparison Workflows

This module handles the metadata transfer for screenshot comparison tests.

Best Practice: When a screenshot test fails, the module sends a message containing the path to the “New” versus “Expected” image. Use the ScreenShot Comparison Tool to visualize these differences; the underlying data transfer is managed by the structs in this module.
7. Filter Logs to Reduce Message Bloat

In large-scale stress tests, a worker can generate thousands of log messages, which can saturate the message bus.

Tip: Use the -NoLog command-line argument on your workers or configure your test to only report errors and warnings. This helps eliminate network congestion and prevents the editor from becoming unresponsive while processing high volumes of automation data.
8. Monitor for “Lost” Workers

The FAutomationWorkerPing message is sent periodically to verify a worker is still alive.

Best Practice: If a worker becomes unresponsive (e.g., due to a crash), the controller will wait for a timeout before marking the test as “Aborted.” Monitor your logs for “Worker Timeout” to identify crashes that eliminate the process before it can send a proper completion message.