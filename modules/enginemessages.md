---
layout: default
title: EngineMessages
---

<!-- ai-generation-failed -->

<h1>EngineMessages</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/EngineMessages/EngineMessages.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

between different instances of Unreal Engine, such as the Editor, standalone game clients, or external developer tools.

It essentially acts as the “common language” for the engine’s internal messaging system, allowing disparate processes to identify each other and exchange heartbeat or authentication data.

Practical Usage Tips and Best Practices
1. Implement Heartbeats with FEngineServicePing

To detect if a remote engine instance (like a render node or a mobile device) is still active, you don’t need to build a custom networking protocol.

Best Practice: Broadcast an FEngineServicePing message over the message bus. Any active engine instance will respond with an FEngineServicePong, helping you eliminate “zombie” connections from your list of available remote targets.
2. Identify Remote Instances via Metadata

The FEngineServicePong message contains critical metadata about the responding instance.

Tip: Inspect the InstanceId, InstanceName, and WorldContext fields in the pong response. This allows your tool to differentiate between multiple PIE (Play In Editor) sessions or different builds running on the same network, eliminating the risk of sending commands to the wrong client.
3. Use FEngineServiceNotification for User Feedback

When building custom automation or multi-user tools, you may need to display a message to a user on a different machine.

Action: Send an FEngineServiceNotification. This message type is intended to trigger a toast or log entry on the recipient’s end, helping you eliminate the need for manual communication between team members during distributed tasks.
4. Handle Permission via FEngineServiceAuthGrant

If your tool performs sensitive operations (like triggering a remote build or shut down), you must manage permissions.

Best Practice: Use FEngineServiceAuthGrant and FEngineServiceAuthDeny messages to manage the “Authorized” state of a connection. This helps you eliminate unauthorized access to remote engine instances on a shared local area network.
5. Monitor Performance Remotely

The module provides FEngineServicePerformanceData to exchange high-level stat data.

Tip: Use this message to periodically fetch the FPS and memory usage of a remote client. This allows you to build a custom “Stage Monitor” dashboard that tracks the health of several devices at once, eliminating the need to check each screen physically.
6. Subscribe via IMessageBus

To utilize these messages in C++, you must interface with the IMessageBus.

Action: Use IMessageBus::Subscribe and specify the FEngineService... struct type you want to listen for. This provides a clean, event-driven way to react to engine events, eliminating the performance overhead of polling for status updates.
7. Filter Messages by InstanceID

In a busy development environment, the message bus can be flooded with pings from every machine on the subnet.

Best Practice: Always check the Sender address and the InstanceId within the message payload. Filter out messages that don’t match your target session to eliminate logic errors caused by cross-talk between different developer machines.
8. Ensure Module Dependencies

Since these messages are often used in cross-process tools, your project setup must be correct.

Action: Add "EngineMessages" to your PrivateDependencyModuleNames in your Build.cs file. Failure to include this will result in linker errors for the message UStructs, which eliminates your ability to serialize or deserialize these messages for network transport.