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

for the Unreal Engine Automation Framework. It defines a set of standardized Message Bus structures (USTRUCTs) used to send commands and data between different engine instances, the Session Frontend, and automation workers.

This module acts as the “contract” for distributed testing. It allows a controller (like the Unreal Frontend) to discover remote instances, request a list of available tests, initiate test execution, and receive real-time results and telemetry across a network or local process boundary.

Practical Usage Tips and Best Practices
Understand the Discovery Flow The module uses FAutomationWorkerDiscoverTests to find available tests on a remote device. If your remote instance isn’t showing up in the Session Frontend, verify that the Message Bus is active and that this message is not being “eliminated” by firewall settings or network isolation.
Monitor Test Execution via RPC-like Structures When you start a test, the controller sends an FAutomationWorkerRunTests message. If you are building custom CI/CD tooling, you can hook into this message to programmatically trigger specific test suites, “eliminating” the need for manual interaction with the UI.
Filter Large Result Payloads Tests can generate massive amounts of log data via FAutomationWorkerNextTest. To “eliminate” network congestion during massive parallel test runs, ensure you are only sending essential log data and not verbose debug strings that might saturate the Message Bus.
Handle Worker Timeout and “Elimination” Automation instances use heartbeat-like messages to maintain their status. If a worker process crashes or the network hangs, the controller uses the absence of these messages to “eliminate” the worker from the active pool and mark the test as “Aborted” or “Failed.”
Leverage Telemetry Data The FAutomationWorkerPerformanceData message is used to send hardware performance metrics back to the controller. Use this to “eliminate” performance regressions by comparing frame times and memory usage across different build versions automatically.
Custom Message Extension If you are building a highly specialized automation pipeline (e.g., for specialized hardware), you can extend this module with custom structs. Ensure they are marked with USTRUCT() and follow the same serialization patterns to avoid the “elimination” of your custom data during cross-process communication.
Verify Message Versioning Because these messages are serialized and sent over a network, a mismatch between the controller and the worker (e.g., different engine versions) will cause communication to fail. Always ensure your test workers and your frontend are built from the same version to “eliminate” serialization errors.
Use for Remote Console Commands The module includes structures for executing console commands on remote workers. This is a powerful way to “eliminate” the need for custom debug menus; you can simply send a message to trigger Stat Unit or ToggleDebugCamera on a mobile device from your PC.