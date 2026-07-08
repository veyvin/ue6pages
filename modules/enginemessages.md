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

tures (USTRUCTs) used for inter-process communication (IPC) via the Message Bus. It defines a common “language” that different Unreal Engine instances, standalone tools, and external applications use to discover each other and exchange status information.

This module acts as the schema for the engine’s messaging system. By using these predefined message types, developers can eliminate the need to design custom network protocols for basic tasks like service discovery, heartbeats, and remote command execution.

Practical Usage Tips and Best Practices
Implement Service Discovery with FEngineServicePing
Use the FEngineServicePing message to broadcast a request for all active engine instances on the local network. Listening for the corresponding FEngineServicePong allows your tools to build a list of available targets (like a running editor or a mobile preview), helping to eliminate manual IP entry.
Add “EngineMessages” to Build.cs
Because this module defines the types for the Message Bus, you must include “EngineMessages” in your C++ module’s PublicDependencyModuleNames if you plan to send or receive these specific structs. This ensures the Unreal Header Tool (UHT) can find the reflected types and eliminate compilation errors.
Handle Auth with FEngineServiceAuthGrant
When building remote profiling or control tools, utilize the authentication messages to verify the connection. This practice helps eliminate unauthorized access to your running game instance, ensuring that only trusted developer tools can trigger commands or modify internal variables.
Monitor App Health via Heartbeats
Subscribe to FEngineServicePong messages to monitor the “LastSeen” time of a remote instance. If an instance stops responding to pings, you can eliminate it from your tool’s UI, providing a real-time status of which build machines or test devices are currently online.
Execute Remote Commands via FEngineServiceExecuteCommand
This message type allows you to send console commands to a remote instance. Use it to automate tasks like stat unit or dumpconsole on a device that doesn’t have a physical keyboard, helping to eliminate friction in mobile and console debugging.
Check InstanceId for Message Filtering
Each message in this module includes an InstanceId (an FGuid). Always check this ID in your message handler to eliminate processing messages from the wrong instance, which is especially important when multiple PIE (Play In Editor) windows are running simultaneously.
Ensure Proper Header Inclusion
Include headers like #include "EngineMessages/EngineServiceMessages.h" to access the core struct definitions. Being specific with your includes helps the compiler and helps eliminate unnecessary build time bloat by not pulling in unrelated messaging headers.
Distinguish between Editor and Game Messages
Some messages are more relevant to the Editor (like asset sync notifications), while others are for the Runtime. Use the FEngineServiceNotification message to send generic text updates to a developer console, which helps eliminate the need for complex UI updates when a simple status message will suffice.