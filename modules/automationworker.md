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

ble for actually executing the commands sent by the controller and reporting back the results.

This module is essential for cross-platform testing, as it allows a central PC running the Session Frontend to “talk” to workers running on consoles, mobile devices, or separate PC instances to verify gameplay and performance.

Practical Usage Tips and Best Practices
1. Discovery and Registration

The AutomationWorker handles the “heartbeat” of an engine instance. When you open the Session Frontend, the workers on your local network automatically register themselves. If a device isn’t appearing, ensure the UDP Messaging plugin is enabled, as the worker relies on this transport layer to announce its presence to the controller.

2. Headless and NullRHI Execution

For automated build servers (CI/CD), you can run a worker in “Headless” mode using the -NullRHI command line flag. The AutomationWorker will still execute logic-based tests (Unit Tests and Functional Tests) without needing a GPU to render frames, which is much faster and more stable for non-visual validation.

3. Handling Crashes and “Elimination”

One of the worker’s primary roles is to report its status. If a worker instance crashes during a test, it stops sending its heartbeat. The controller will detect this “elimination” of the worker and mark the current test as “Crashed” in the results. Always check the Worker Log in the Session Frontend to see the last recorded string before the instance failed.

4. Parallel Test Distribution

You can run multiple workers on a single powerful machine by launching multiple instances of the editor or game with the -Unattended flag. The AutomationController can then distribute a large suite of tests across these workers, effectively parallelizing your testing process and cutting down total execution time.

5. Role-Based Testing

In multiplayer testing, you can assign different “Roles” to workers. For example, one worker can be the “Server” and another the “Client.” The AutomationWorker helps coordinate these roles, ensuring that the server worker completes its setup before the client worker attempts to join and begin its test logic.

6. Executing Console Commands

The worker is the gateway for remote execution. You can send console commands directly to a specific worker instance via the Session Frontend. This is useful for debugging remote hardware (e.g., toggling stat unit or show collision on a PlayStation or Xbox) without needing a direct debug cable.

7. Latent Command Processing

Many automation tests require multiple frames to complete (e.g., waiting for a level to load). The AutomationWorker manages the Latent Command Queue. It ensures that the engine continues to tick while the test is “waiting,” preventing the worker from becoming unresponsive and being “eliminated” by the controller for timing out.

C++ Interaction: Checking Worker Status

While you rarely modify the worker module itself, you may need to check if an instance is currently acting as a worker to disable certain “heavy” editor features during testing.

C++
	#include "IAutomationWorkerModule.h"

	 

	void UMyGameUtility::CheckWorkerStatus()

	{

	    // Check if the AutomationWorker module is loaded and active

	    if (FModuleManager::Get().IsModuleLoaded("AutomationWorker"))

	    {

	        // Logic to lower graphics settings or disable UI 

	        // to speed up automated test execution

	        UE_LOG(LogTemp, Log, TEXT("Running as an Automation Worker instance."));

	    }

	}
Copy code
Best Practices & Performance
Keep Workers Clean: Avoid using Tick in your functional tests whenever possible. Instead, use the Latent Commands provided by the worker to wait for specific events. This keeps the worker’s performance predictable.
Log Management: Workers can generate massive logs during long test runs. Use the -LogTimes command line argument so that when a worker reports an error, you can correlate it exactly with the controller’s timeline.
Network Isolation: If you are in a large studio, use the -MessagingSettings to set a specific Unicast Endpoint. This prevents your workers from being hijacked by a colleague’s Session Frontend on the same network.