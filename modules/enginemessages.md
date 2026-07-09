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

tatus pings.

This module is the protocol layer that allows different instances of the engine, standalone tools, or external applications (like Live Link providers or the Project Launcher) to understand each other. It “eliminates” the need for developers to define custom network protocols for basic administrative tasks between connected instances.

Practical Usage Tips and Best Practices
Understand the Discovery Handshake
The module provides FEngineServicePing and FEngineServicePong. When building custom remote tools, use these messages to “eliminate” manual IP entry; by broadcasting a ping, you can automatically discover all active engine instances on the local network that respond with a pong.
Decouple Systems via Message Bus
Use the messages in this module to facilitate communication between the Game and UI systems. This “elimination” of hard dependencies allows a dedicated server (which has no UI) to send an FEngineServiceNotification that a client-side UI can listen for and display.
Include in Build.cs for Networking Tools
If you are creating an editor plugin or a standalone C# tool that interacts with a running game, you must add "EngineMessages" to your PrivateDependencyModuleNames. This ensures your project has access to the reflected USTRUCT definitions required for message serialization.
Use for Remote Console Commands
The module includes FEngineServiceExecuteCommand. You can use this to send console commands to a remote instance (like a mobile device or a console). This “eliminates” the need to use a physical keyboard on the device during remote debugging sessions.
Check for Authentication Denials
When connecting to a protected instance, listen for FEngineServiceAuthDeny. Handling this message allows your tool to “eliminate” user frustration by providing a clear “Access Denied” UI rather than simply failing to connect with no explanation.
Monitor Instance Health
Use the FEngineServiceStatus message to monitor the “heartbeat” of remote instances. This is a best practice for “eliminating” the risk of sending commands to a “zombie” instance that has crashed or hung but still appears to be connected to the network.
Leverage Message Bus for Multi-User Workflows
In multi-user editing scenarios, these messages form the backbone of session management. By utilizing the existing structures, you “eliminate” the complexity of synchronizing basic engine states (like the current level name) across multiple workstations.
Avoid High-Frequency Message Spam
While the Message Bus is robust, “eliminating” high-frequency traffic (like sending a message every tick) is critical. Use these messages for “event-based” logic—such as a status change—rather than continuous data streaming, which should be handled by specialized modules like Live Link.