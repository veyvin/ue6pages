---
layout: default
title: ConcurrencyVisualizer
---

<!-- ai-generation-failed -->

<h1>ConcurrencyVisualizer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/ConcurrencyVisualizer/ConcurrencyVisualizer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

een Unreal Engine and the Visual Studio Concurrency Visualizer extension. It acts as a wrapper that translates Unreal’s internal profiling events and thread activity into a format that the Windows Performance Toolkit and Visual Studio can interpret.

While Unreal Insights is the primary profiling tool for UE5, the ConcurrencyVisualizer module is used for low-level system analysis. It allows developers to see exactly how engine threads (Game, Render, RHI, Worker) interact with the Windows OS kernel, providing visibility into thread contention, core migration, and CPU scheduling that is not always visible in the engine’s internal profilers.

1. Enable for System-Level Analysis

Use this module when you suspect that performance hitches are being caused by the Operating System or external drivers rather than your Blueprint or C++ logic. It is ideal for identifying “Thread Starvation,” where the OS is parking engine threads because other applications or background processes are competing for the same CPU cores.

2. Required Build Configuration

The ConcurrencyVisualizer is a developer tool and is not available in Shipping builds.

Best Practice: Use Development or Test configurations when profiling. Ensure the module is included in your Build.cs only for the appropriate targets:
C#
	if (Target.Configuration != UnrealTargetPlatform.Shipping)

	{

	    PublicDependencyModuleNames.Add("ConcurrencyVisualizer");

	}
Copy code
3. Use Custom Markers in C++

You can inject your own “Markers” into the Visual Studio timeline using the macros provided by this module.

Tip: Use CONCURRENCY_VISUALIZER_MARKER to flag the start of a specific complex algorithm. When you view the trace in Visual Studio, these markers will appear as distinct flags, making it easy to correlate your code’s execution with the CPU’s physical thread transitions.
4. Differentiate from Unreal Insights
Unreal Insights: Best for “What is the engine doing?” (Task Graph, Load Times, Asset Bloat).
Concurrency Visualizer: Best for “What is the hardware doing?” (Context switches, Core affinity, Kernel-mode stalls).
Best Practice: Use Insights first to find the bottlenecked thread, then use the Concurrency Visualizer if that thread appears to be “stalling” for no apparent engine-related reason.
5. Identify Critical Section Contention

The module is excellent for finding locks that are being held too long across different threads.

Tip: In the Visual Studio Concurrency Visualizer “Execution” tab, look for red blocks on your Worker Threads. These indicate that a thread is ready to work but is blocked by a Mutex or CriticalSection. This module helps you trace that block back to the specific thread currently holding the resource.
6. Monitor Core Migration

Unreal Engine 5 performs best when threads stay on the same physical core to keep the L1/L2 caches “warm.”

Tip: Use the visualizer to see if the Windows Scheduler is frequently moving your Render Thread between different cores. If you see high migration, you may need to look into setting Thread Affinity or checking if the CPU is down-clocking due to thermal throttling.
7. Run with Administrative Privileges

Because this module interfaces with ETW (Event Tracing for Windows) to gather kernel-level data, the profiler (Visual Studio) usually requires Administrative privileges to collect the trace.

Best Practice: Always launch Visual Studio as an Administrator before starting a profiling session, or the ConcurrencyVisualizer module will fail to emit the necessary system events.
8. Use the -StatNamedEvents Flag

To get the most out of this module, launch your game or editor with the -StatNamedEvents command-line argument.

Insight: This forces the engine to emit string-based names for its internal stats, allowing the Concurrency Visualizer to label the blocks of time in Visual Studio with human-readable names like “Physics Simulation” or “Slate Tick” instead of generic thread IDs. This makes the resulting data significantly easier to interpret.