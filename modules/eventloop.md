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

cture for managing asynchronous events and I/O operations within Unreal Engine. It centers around the IEventLoop interface and is designed to handle “event-driven” logic, such as network socket readiness, timers, and inter-thread signaling. Unlike the primary game loop (which is tied to frame rendering), the EventLoop is built to facilitate non-blocking, multi-threaded communication, ensuring the engine can respond to system-level events without stalling the main execution thread.

Practical Usage Tips & Best Practices
1. Utilize for Non-Blocking Network I/O

The EventLoop is ideally suited for managing sockets where waiting for data would otherwise block a thread.

Best Practice: Register your file descriptors or sockets with the EventLoop to receive notifications when they are “ready to read” or “ready to write.” This ensures the elimination of “busy-wait” loops that waste CPU cycles while waiting for network packets.
2. Prefer EventLoop Timers for Precise Intervals

While FTimerManager is convenient for gameplay, it is tied to the Actor Tick and variable frame rates.

Tip: Use IEventLoop::RequestTimer for low-level system tasks that require consistent timing regardless of the current FPS. This allows for the elimination of timing drift in background tasks like heartbeat signals or telemetry data collection.
3. Implement Thread-Safe Signaling

The EventLoop provides mechanisms to wake up a sleeping thread when new work is available.

Best Practice: Use the EventLoop’s signaling API to notify a worker thread that a task is ready. This results in the elimination of thread contention and minimizes the latency between a task being queued and its execution beginning.
4. Avoid Heavy Processing in Callbacks

Callbacks triggered by the EventLoop are executed on the loop’s own thread, which must remain responsive.

Tip: If an event requires a complex calculation, offload that work to the Tasks System or a separate thread pool. Keeping EventLoop callbacks “lean” leads to the elimination of bottlenecks that could delay subsequent system events.
5. Integrate with the Tasks System

Modern Unreal development (UE 5.6+) encourages combining the EventLoop with UE::Tasks.

Best Practice: Use the EventLoop to detect an event (like a file being loaded) and then launch a Task to process the data. This hybrid approach facilitates the elimination of complex manual thread management while maintaining high responsiveness.
6. Monitor Loop Latency for Performance

A “congested” event loop can cause delayed responses to critical system inputs.

Tip: Use Unreal Insights to track the time spent within the EventLoop’s processing phase. Identifying long-running callbacks is the first step toward the elimination of “hitchiness” in asynchronous systems like audio streaming or asset loading.
7. Ensure Clean Shutdown

Failing to unregister events or timers from the loop can lead to crashes or memory leaks during module unloading.

Best Practice: Always clear your registered handles in the ShutdownModule or destructor of your class. Proper cleanup ensures the permanent elimination of “zombie” callbacks that attempt to access memory that has already been freed.
8. Use for Cross-Platform Abstraction

The EventLoop module abstracts away platform-specific details (like epoll on Linux or IOCP on Windows).

Tip: Write your asynchronous logic against the IEventLoop interface rather than native platform APIs. This ensures the elimination of platform-specific bugs and makes your C++ code significantly more portable across PC, console, and mobile.