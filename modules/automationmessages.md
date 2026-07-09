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

the data structures (USTRUCTs) used for communication within the Unreal Engine Automation System. It acts as the common language between the Automation Controller (the Session Frontend in the Editor) and the Automation Workers (instances of the game or editor running locally or on remote devices).

These messages are transmitted via the Unreal Message Bus, enabling discovery, test execution commands, and real-time result reporting across a network.

Practical Usage Tips and Best Practices
Include in Build Dependencies
If you are creating custom low-level test workers or extending how the engine communicates with remote devices, you must add the module to your Build.cs.
C#
	    // In YourProject.Build.cs

	    PublicDependencyModuleNames.AddRange(new string[] { "AutomationMessages", "Messaging" });

	    ```

	 

	*   **Understand the Ping/Pong Flow**  

	    The system uses `FAutomationWorkerPing` and `FAutomationWorkerPong` for discovery. When you open the Session Frontend, the controller broadcasts a Ping. Any active worker running with the `-AutomationWorker` command line flag will respond with a Pong containing its machine name and hardware details. Ensure your firewall doesn't block these UDP messages if testing across a network.

	 

	*   **Leverage Message Serialization**  

	    Because these messages are `USTRUCT`s, they are automatically compatible with the engine’s JSON and Binary serializers. This makes it possible to "eliminate" manual parsing when building external dashboards or web-based test monitors that need to read test results from a running instance.

	 

	*   **Filter via Message Attributes**  

	    The messages (like `FAutomationWorkerRunTests`) contain metadata about the environment. When running tests on a "farm," use these attributes to ensure you aren't accidentally sending "Editor-only" test commands to a "Game-mode" worker, which would "eliminate" the validity of your results.

	 

	*   **Monitor Test Heartbeats**  

	    Automation messages include timestamps. If a worker stops sending updates during a heavy stress test (e.g., a 100-player "elimination" simulation), the controller uses the lack of messages to determine if the worker has crashed or hung, allowing the automation suite to move on to the next test automatically.

	 

	*   **Use for Remote Commands**  

	    You can programmatically send an `FAutomationWorkerNextTest` message to skip a hanging test. This is useful when building custom CI/CD "watchdog" scripts that monitor the health of a long-running automation session and need to "eliminate" stuck processes.

	 

	*   **Observe Result Aggregation**  

	    The `FAutomationWorkerRunTestsReply` message returns an array of results. When implementing custom `VisualLogger` data in your tests, ensure your data is small enough to fit within the message bus's packet limits; otherwise, the automation controller might drop the detailed log data for a failed test.

	 

	*   **Command Line Initialization**  

	    To ensure a standalone build initializes the `AutomationMessages` module and starts listening for controller commands immediately, launch your executable with the following arguments: `-Messaging -AutomationWorker -SessionName="YourTestSession"`. This "eliminates" the need for manual setup within the game's UI.
Copy code
Understand the Discovery Handshake
The system uses FAutomationWorkerPing and FAutomationWorkerPong for worker discovery. If a remote device isn’t appearing in your Session Frontend, ensure that UDP messaging is enabled in your project settings and that no firewall is “eliminating” these packets.
Leverage Message Serialization
Because these messages are reflected USTRUCTs, they can be easily serialized to JSON or CBOR. This is useful for building external web-dashboards that monitor test progress or “elimination” counts in automated stress-test scenarios without needing a full engine instance to read the data.
Monitor Heartbeats for Reliability
Automation messages include timestamps and machine IDs. If a worker stops sending updates during a heavy physics simulation, the controller uses the absence of messages to determine if the worker has crashed. Use this “heartbeat” logic to “eliminate” stalled tests automatically in your CI/CD pipeline.
Filter via Message Attributes
Messages like FAutomationWorkerRunTests contain metadata about the worker’s environment (e.g., Platform, Build Type). Use these attributes in your controller logic to ensure you don’t accidentally send “Editor-only” tests to a “Shipping” build worker, which would “eliminate” the accuracy of your test suite.
Command Line Initialization
To ensure a standalone build starts listening for automation messages immediately upon launch, use the following arguments: -Messaging -AutomationWorker -SessionName="AutomatedTest". This “eliminates” the need for manual setup in the game’s UI.
Batch Result Reporting
The FAutomationWorkerRunTestsReply message returns an array of results. When reporting many small test outcomes, batch them into a single reply message. This reduces network overhead and prevents the message bus from becoming a bottleneck during high-volume “elimination” logic verification.
Programmatic Test Skipping
You can send an FAutomationWorkerNextTest message to a worker to force it to move to the next item in the queue. This is a best practice for managing “hanging” tests that haven’t crashed the process but are failing to progress, helping you “eliminate” manual intervention in overnight test runs.