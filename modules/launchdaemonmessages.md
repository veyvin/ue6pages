---
layout: default
title: LaunchDaemonMessages
---

<!-- ai-generation-failed -->

<h1>LaunchDaemonMessages</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/IOS/LaunchDaemonMessages/LaunchDaemonMessages.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Launch Daemon, a background service typically used during mobile development (specifically for iOS). It defines the structured data and message protocols used to communicate between a developer’s PC/Mac and a remote device over a network or USB connection.

This module is the technical glue that allows the Unreal Editor and Unreal Automation Tool (UAT) to “talk” to a physical device to handle remote application launching, log retrieval, and process management. It facilitates the elimination of manual application management on the device by automating the deployment and execution cycle.

Practical Usage Tips and Best Practices
1. Essential for Remote iOS Deployment

When you use the “Project Launcher” to deploy a build to an iOS device without using a direct Xcode connection, this module handles the “Launch Request” messages. Ensuring your firewall allows the specific ports used by the Launch Daemon is the first step toward the elimination of “Device Not Found” errors during remote deployment.

2. Utilize for Remote Log Streaming

The module defines message types for log output. When you see your iPhone’s output logs appearing in the Unreal Editor’s Output Log window, the FUnrealLaunchDaemonOutputMessage is being used to pipe that data. This practice leads to the elimination of “black box” debugging on mobile, as you can see crashes in real-time without an IDE.

3. Monitor Device Heartbeats (Ping/Pong)

The Launch Daemon uses “Ping” and “Pong” message structures to maintain a connection state. If your device frequently disappears from the device list, it may be failing these heartbeat checks. Checking for network stability between your PC and the device facilitates the elimination of dropped connections during long “cook-on-the-fly” sessions.

4. Automate Mobile Testing via UAT

If you are building a CI/CD pipeline, the Unreal Automation Tool uses this module to send command-line arguments to the device. Using the Launch Daemon to trigger an “elimination” (shutdown) of an old app version and the launch of a new one is a best practice for the elimination of stale data on your test hardware.

5. Verify Module in Build.cs for Custom Tools

If you are developing a custom editor utility or a standalone C# tool to monitor a fleet of mobile devices, you must include "LaunchDaemonMessages" in your dependencies. Proper referencing of the message structs (like FUnrealLaunchDaemonLaunchRequest) is required for the elimination of malformed packet errors when sending custom commands.

6. Coordinate with the Message Bus

The LaunchDaemonMessages module relies on the engine’s internal Message Bus. If you are experiencing communication failures, ensure that the Message Bus is not being blocked by other high-traffic plugins. Optimizing your message bus settings leads to the elimination of latency when sending “Stop” or “Restart” commands to the remote daemon.

7. Handle Application “Elimination” Requests

The module includes messages to terminate a running process on the target device. This is used when you click “Stop” in the Project Launcher. Implementing clean shutdown logic in your game ensures that the daemon can execute the elimination of the app process without leaving “hanging” memory handles on the mobile OS.

8. Debugging with “LogLaunchDaemon”

To see the raw messages being passed between your PC and the device, you can enable verbose logging for the daemon. This assists in the elimination of confusion when a launch request is sent but the device fails to respond, allowing you to see if the message was lost or if the daemon on the device encountered an internal error.