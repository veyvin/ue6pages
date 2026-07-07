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

al Engine Automation Framework. While the AutomationController acts as the “manager” that dictates which tests to run, the AutomationWorker resides within each running instance of the engine (the “worker”) to execute those instructions.

It is responsible for reporting the local machine’s capabilities to the controller, executing individual test commands, and sending back the results (pass/fail, logs, and screenshots). Every instance appearing in your Session Frontend is running an AutomationWorker.

Practical Usage Tips & Best Practices
1. Enable via Plugin for Discovery

The AutomationWorker logic is primarily contained within the Automation Utilities plugin. Ensure this plugin is enabled in your project settings; otherwise, the instance will not appear as a valid worker in the Session Frontend, making it impossible to run remote tests on that device.

2. Identify Workers via Instance Name

When running multiple workers on a local network (e.g., a PC and a mobile dev-kit), give your instances unique names using the -InstanceName="MyDevice" command-line argument. This allows the AutomationWorker to report a distinct identity, helping you distinguish between logs from different hardware.

3. Use for Performance Profiling on Device

The AutomationWorker is the bridge for remote performance testing. You can use it to trigger “Functional Tests” on a target console or mobile device. The worker will execute the gameplay logic and send the performance data (like frame times) back to your PC, which is critical for identifying bottlenecks on specific hardware.

4. Manage Worker Network Connectivity

AutomationWorkers communicate with the controller via the Unreal Message Bus. If a worker is not showing up in your list, verify that your firewall allows traffic on the UDP ports used by the engine (typically 6666 and 11111). On mobile devices, ensure the worker is on the same Wi-Fi subnet as the PC running the controller.

5. Handle “Elimination” of Stalled Workers

In CI/CD pipelines, a worker might hang due to an infinite loop or a hard crash. Use the Timeout settings in your test commands. The worker is designed to be monitored by the controller; if the worker stops heartbeat reporting, the controller can “eliminate” that session and move on to the next test to prevent the entire build pipeline from stalling.

6. Screen Capture and Comparison

The AutomationWorker handles the AddScreenshotComparison command. When a test requests a screenshot, the worker captures the frame buffer and transmits the image back to the controller. Ensure your worker has a valid window focus (or use -RenderOffscreen) to ensure the captured images are valid and not obscured by OS dialogs.

7. Latent Command Execution

The worker manages the execution of Latent Commands. These are tasks that require multiple frames to complete, such as FWaitUntil. The worker’s tick loop checks these commands every frame; to maintain performance, avoid putting heavy computational logic inside the Update() function of a latent command on the worker side.

8. Deployment for Non-Editor Workers

When testing “Cooked” or “Shipping” builds, the AutomationWorker must be compiled into the executable. Use the Development build configuration for your testing targets, as the Shipping configuration typically strips out the automation modules to save space and security, preventing the worker from initializing.