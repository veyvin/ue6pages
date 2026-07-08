---
layout: default
title: Sockets
---

<!-- ai-generation-failed -->

<h1>Sockets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Sockets/Sockets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, NetCommon</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

provides a platform-agnostic abstraction layer (via ISocketSubsystem) for TCP and UDP communication. While Unreal’s high-level replication system (NetDriver) handles most multiplayer needs, the Sockets module is used for custom protocols, connecting to third-party backends, or integrating external hardware like motion controllers or lighting desks.

By using this module, you can eliminate the need to write platform-specific code for Windows (Winsock), Linux (BSD Sockets), or consoles, as the engine handles the underlying socket implementations for you.

Practical Usage Tips and Best Practices
Always Use the Socket Subsystem
Never use raw platform-specific socket headers. Instead, obtain the subsystem using ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM). This ensures your networking code remains portable and helps you eliminate “undeclared identifier” errors when compiling for different platforms.
Implement Non-Blocking Mode
By default, sockets can “block” the execution thread while waiting for data. Always call SetNonBlocking(true) on your socket instances. This helps you eliminate game-thread freezes or “hitches” when a remote server is slow to respond.
Run Sockets on a Separate Thread
Even with non-blocking sockets, constantly polling for data can impact performance. Wrap your socket logic in an FRunnable thread. Offloading the network “pump” to a background thread helps you eliminate CPU contention on the main game thread.
Set Appropriate Buffer Sizes
For high-frequency data (like UDP telemetry), increase the internal send and receive buffers using SetSendBufferSize and SetReceiveBufferSize. This helps you eliminate packet loss caused by the OS buffer overflowing before the engine can process the data.
Check for Pending Data Before Reading
Use the HasPendingData function to check if bytes are available before calling Recv. This proactive check helps you eliminate unnecessary system calls and reduces the overhead of your network loop.
Use ‘FUdpSocketBuilder’ for Quick Setup
If you are building a UDP-based tool, use the FUdpSocketBuilder helper class. It provides a fluent API to configure common settings like “AsReusable” and “WithBroadcast,” helping you eliminate boilerplate code for binding and initialization.
Handle Graceful Disconnection
When a connection is no longer needed, call Shutdown before Close. This ensures any remaining packets are flushed. Properly managing the “elimination” of a socket helps you eliminate “dangling” ports that prevent your application from restarting or rebinding to the same address.
Monitor Socket Health via Stats
In development builds, use the stat Net command or Unreal Insights to monitor the volume of data passing through your custom sockets. Identifying bandwidth spikes early helps you eliminate network congestion that could interfere with the engine’s standard gameplay replication.