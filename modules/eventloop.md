---
layout: default
title: EventLoop
---

<!-- ai-generation-failed -->

<h1>EventLoop</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/EventLoop/EventLoop.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, NetCommon</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e engine’s main loop and asynchronous task processing in a modular fashion.

Description and Purpose

Introduced to support the engine’s move toward a more modular “Modular Program” architecture, the EventLoop module abstracts the core “tick” logic into a reusable interface (IEventLoop). This allows standalone C++ tools, utility programs, and specific engine subsystems to run a persistent loop that processes events, timers, and tasks without the massive overhead of the full FEngineLoop. It serves as the infrastructure for the Tasks System and LowLevelTasks, ensuring that even headless applications can handle asynchronous operations and “heartbeat” logic effectively.

Practical Usage Tips and Best Practices
Utilize for Headless Utility Tools
When creating a standalone C++ program using Unreal’s modules (e.g., a custom build agent or data harvester), use FEventLoop to manage its lifecycle. This allows you to use FTimerManager and TaskGraph in a “headless” environment, helping you eliminate the need to initialize the full renderer or game world.
Integrate with the Tasks System
The EventLoop is designed to work seamlessly with UE::Tasks. If you are running a custom loop, ensure you are calling the appropriate processing functions to eliminate deadlocks where background tasks are waiting for the main thread to acknowledge completion.
Throttle Custom Loops to Save CPU
Unlike a game loop that often targets maximum frame rates, a custom event loop should be throttled using FPlatformProcess::Sleep() when idle. This will eliminate 100% CPU usage on a single core for tools that are merely waiting for network I/O or file system events.
Avoid Heavy Blocking on the Loop Thread
The thread running the EventLoop should remain responsive. If you perform a heavy, synchronous file I/O operation directly inside a loop iteration, you eliminate the engine’s ability to process urgent background tasks or timers, leading to “hanging” behavior.
Register Custom Event Sources
Advanced developers can register custom IEventSource objects. This is useful for integrating external network sockets (like ZeroMQ) directly into the engine’s polling mechanism. This approach helps you eliminate the overhead and complexity of managing separate threads just for polling.
Handle Clean Shutdown Sequences
Always call the exit functions on your EventLoop instance during program termination. Abruptly ending a process can lead to “zombie” tasks or unflushed logs; a proper shutdown ensures you eliminate these persistent background processes.
Monitor Timing with High Precision
The EventLoop module provides access to high-precision timing delegates. Use these when benchmarking performance-critical code—such as an automated character elimination stress test—to ensure your measurements are accurate to the microsecond.
Reference the “Programs” Source Code
To see the EventLoop in a production environment, study the source code for engine programs like LiveCodingConsole or UnrealInsights. These examples show how to correctly initialize and run the loop, which will eliminate any boilerplate confusion during your own implementation.