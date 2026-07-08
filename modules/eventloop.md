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

d in Developer/EventLoop) that provides a generic framework for asynchronous event processing and I/O multiplexing.

Description

The EventLoop module implements the TEventLoop class, which serves as a specialized, single-threaded execution context designed to handle high-frequency events such as timers, socket notifications, and custom tasks. Unlike the main Game Thread, which is bound to frame-rate and heavy engine systems, an EventLoop is typically used in background threads or standalone commandlets (like the Zen storage service) to handle non-blocking I/O or background synchronization tasks. It allows a thread to “sleep” efficiently until an event is triggered, reducing CPU consumption for idle processes.

Practical Usage Tips and Best Practices
1. Use for Low-Level Tooling

The EventLoop module is a developer-only tool. It is not intended for gameplay logic or AActor ticking. Its best use case is for background network proxies, custom asset-cooking helpers, or file-monitoring tools that need to react to external triggers without the overhead of the full engine framework.

2. Declare the Build Dependency

To use the module, you must add it to your module’s Build.cs file. Since it is a developer module, ensure you handle configuration checks if your code might be included in a multi-platform environment:

C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("EventLoop");

	}

	```

	 

	#### 3. Integrate with FRunnable

	The most common way to use an `FEventLoop` is inside an `FRunnable` thread. Initialize the loop in the `Init()` function, call `Run()` in the runnable's `Run()` method, and use `RequestStop()` to cleanly exit the loop. This allows you to have a dedicated thread that efficiently sleeps until an event (like a timer or network packet) occurs.

	 

	#### 4. Thread-Safe Event Submission via Post

	If you need to trigger logic on the event loop from a different thread (e.g., the Game Thread), use the `Post()` method. This ensures that the provided lambda or function is executed safely within the event loop's own thread, preventing race conditions when modifying data owned by the loop.

	 

	#### 5. Don't Block the Loop

	The efficiency of an event loop depends on how quickly it can process the "ready" events and return to its polling state. Never perform long-running calculations or blocking I/O inside an event loop callback. If a task is heavy, use the `Post()` method to hand that work off to the **Task Graph** or a **ThreadPool** instead.

	 

	#### 6. Leverage Built-in Timers

	The module includes a robust timer system. Instead of manual "delta time" accumulation, use `RegisterTimer`. This is far more efficient than ticking every frame to check if a duration has passed, as the loop can sleep until the exact moment the timer is scheduled to fire.

	 

	#### 7. Use IEventLoopSource for I/O

	If you are building a custom socket-based tool, implement the `IEventLoopSource` interface. This allows you to register your socket with the loop so it only wakes up when there is actual data to read (`OnReadReady`), significantly reducing the CPU usage of idle background processes.

	 

	#### 8. Graceful Shutdown and Elimination

	Always ensure you cleanly **eliminate** the loop during shutdown. If you are using timers or event sources, unregister them before the loop is destroyed. Failing to stop the loop or clear its sources can lead to "hanging" processes in the Task Manager even after the Unreal Editor has been closed.
Copy code
3. Integrate with FRunnable for Threading

The standard way to use an EventLoop is within an FRunnable object. Initialize the loop in Init(), call Run() in the runnable’s Run() method, and use RequestStop() to exit. This allows a dedicated background thread to manage a queue of events independently of the game’s framerate.

4. Post Tasks for Thread Safety

If you need to trigger a function on the event loop from a different thread (such as the Game Thread), use the Post() method. This ensures that the provided lambda or function is executed within the event loop’s own thread context, effectively performing the elimination of race conditions when modifying data owned by the loop.

5. Prioritize Timers over Ticking

If you need a background task to occur at a specific interval, use RegisterTimer instead of manual time accumulation. The event loop is optimized to calculate the exact sleep duration until the next timer is due, which is much more energy-efficient than a thread that constantly wakes up to check the time.

6. Implement IEventLoopSource for I/O

For custom network tools, implement the IEventLoopSource interface. This allows you to register a socket or file descriptor with the loop. The loop will then wake up only when there is actual data to process (OnReadReady), ensuring that idle network connections do not waste CPU cycles.

7. Avoid Blocking Calls in Callbacks

The event loop is single-threaded. If a callback (timer or I/O event) performs a long-running calculation or a blocking disk read, it will stall every other event in that loop. For heavy tasks, use the loop to detect the event, but then offload the actual work to the Task Graph or a ThreadPool.

8. Ensure Clean Shutdown and Elimination

Always ensure the loop is properly stopped and all sources are unregistered during shutdown. If an event loop is left running, it can cause the process to hang in the background. Properly handling the elimination of the loop and its associated FExternalHandle references is critical for preventing memory leaks and orphaned threads.