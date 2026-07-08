---
layout: default
title: Instrumentation
---

<!-- ai-generation-failed -->

<h1>Instrumentation</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Instrumentation/Instrumentation.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Unreal Insights ecosystem, allowing developers to see exactly what the CPU and GPU are doing at any given microsecond.

Primary uses include:

CPU Profiling: Using scoped timers to measure how long specific functions or blocks of code take to execute across different threads.
Memory Tracking: Emitting events for allocations and deallocations to visualize memory growth and fragmentation in Memory Insights.
Custom Event Logging: Allowing developers to define “Bookmarks” or custom “Channels” to track game-specific logic (e.g., “Player Spawn” or “AI Pathfinding”).
Data Serialization: Packaging these events into a compressed .utrace stream that can be sent over a network or saved to a file for later analysis.
Practical Usage Tips and Best Practices
1. Use TRACE_CPUPROFILER_EVENT_SCOPE for Logic

The most common usage of this module is wrapping heavy logic in the TRACE_CPUPROFILER_EVENT_SCOPE(Name) macro. This creates a visible “bar” in the Timing Insights window. It is a best practice to name these scopes clearly (e.g., TRACE_CPUPROFILER_EVENT_SCOPE(CalculateAIPath)) to ensure the elimination of confusion during a profile review.

2. Leverage Dynamic Strings Sparingly

While TRACE_CPUPROFILER_EVENT_SCOPE_STR allows you to pass dynamic strings (like an Actor’s name), it is much more expensive than the standard macro. Use static strings whenever possible to ensure the elimination of unnecessary CPU overhead during the tracing process itself.

3. Enable Channels via Command Line

The instrumentation system is divided into Channels (e.g., CPU, GPU, LoadTime, Memory). To minimize the impact on performance, only enable what you need. Launch your game with -trace=cpu,frame,memory to capture specific data. This selective activation ensures the elimination of “data noise” in your trace files.

4. Monitor “Overhead” in Insights

Tracing is not free; it takes a small amount of CPU time to emit events. If you see a high frequency of very small events (less than 1 microsecond), it can actually distort your timings. A best practice is to remove or combine instrumentation in high-frequency loops to ensure the elimination of “observer effect” bias in your data.

5. Implement Custom Trace Channels

For complex systems, define your own channel in C++ using UE_TRACE_CHANNEL_EXTERN. This allows you to toggle your specific system’s profiling on or off independently of the rest of the engine, which is a best practice for teams working on specific sub-systems like Networking or Physics.

6. Use Bookmarks for High-Level Events

Use the TRACE_BOOKMARK macro to mark significant game events, such as a player’s elimination or the start of a boss fight. These appear as vertical lines across all threads in Unreal Insights, making it much easier to correlate a sudden frame drop with a specific gameplay event.

7. Profile “Late” in the Frame

If you are investigating a frame hitch, look at the end of the frame in the Timing Insights view. Instrumentation often reveals that hitches are caused by “Stalls” where one thread is waiting for another (e.g., the Game Thread waiting for the Render Thread). Identifying these dependencies is key to the elimination of bottlenecking.

8. Strategic Elimination of Heavy Ticks

By using the instrumentation module to identify which Tick functions are taking the most time, you can prioritize which Actors need to be converted to Event-Driven logic or Significance Manager control. This data-driven approach is the most effective way to reach a stable 60 FPS.