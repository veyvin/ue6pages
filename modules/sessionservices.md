---
layout: default
title: SessionServices
---

<!-- ai-generation-failed -->

<h1>SessionServices</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/SessionServices/SessionServices.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EngineMessages, SessionMessages</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e underlying infrastructure for discovering and managing Unreal Engine instances across a network. It acts as the backbone for the Session Frontend, enabling the editor to “find” other running instances—such as packaged builds on consoles, mobile devices, or other PCs—for the purpose of remote debugging, automation, and log monitoring.

It primarily utilizes the Message Bus (via the Messaging module) to broadcast and listen for heartbeats from engine sessions. This allows developers to eliminate the need for manual IP entry when connecting tools to remote targets, facilitating a seamless “plug-and-play” experience for cross-platform development.

Practical Usage Tips and Best Practices
Include Module Dependencies
To interact with session discovery in C++, you must add "SessionServices" and "Messaging" to your Build.cs file. Use the ISessionManager interface to track active instances. This setup helps you eliminate manual socket programming when building custom remote-control tools.
Filter via the Session Manager
The ISessionManager provides delegates for when sessions are discovered or lost. Use these to maintain a clean list of available targets in your UI. Filtering by “Session Name” or “Platform” allows you to eliminate irrelevant instances (like background shaders or other users’ builds) from your view.
Monitor Remote Logs in Real-Time
The SessionServices module routes UE_LOG output from remote instances back to the local editor. Use this during console or mobile testing to eliminate the need to physically tether a device to a PC just to see why a crash or “elimination” event occurred during gameplay.
Send Remote Automation Commands
You can use this module to broadcast commands to all discovered sessions. For example, sending a “Quit” command to all instances on the network helps you eliminate the tedious task of manually closing multiple test clients across different development kits.
Leverage for Multi-User Collaboration
SessionServices is a core component of the Multi-User Editing workflow. It allows the server to identify which users are currently “Active” or “Idle.” Monitoring these session states helps you eliminate data conflicts by ensuring you only sync with reachable and valid peers.
Use Heartbeats for Connection Health
The module automatically handles “Heartbeat” messages to detect if a remote instance has crashed or disconnected. If a heartbeat is missed for a set duration, the session is marked as “Timed Out,” helping you eliminate “ghost” entries in your device lists that are no longer responsive.
Configure Session Visibility via Console
If your instance isn’t showing up on the network, check the SessionName and InstanceId console variables. Ensuring these are unique across your local area network (LAN) helps you eliminate discovery collisions where multiple builds are mistaken for a single session.
Properly Shutdown Session Discovery
When your tool or module is closed (the “elimination” of the developer tool), ensure you stop the session service discovery thread. This helps you eliminate unnecessary network traffic and background CPU usage from the Message Bus when discovery is no longer required.