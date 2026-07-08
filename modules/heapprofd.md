---
layout: default
title: heapprofd
---

<!-- ai-generation-failed -->

<h1>heapprofd</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/heapprofd/heapprofd.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

on in Unreal Engine designed specifically for the Android platform. It acts as a bridge between the engine and the native Android heapprofd system daemon (part of the Perfetto suite). Its primary purpose is to capture high-frequency native memory allocation data directly from the system’s heap, including allocations made by third-party libraries and the Android system itself.

This module is essential for the elimination of memory leaks and “Out of Memory” (OOM) crashes on mobile devices, providing a deeper level of visibility than standard LLM (Low-Level Memory) tracking by capturing the full native allocation life cycle.

Practical Usage Tips and Best Practices
1. Use for Native Heap Analysis

While Unreal’s Memory Insights tracks engine-level allocations, use the heapprofd module to identify memory consumed by external Android plugins or GPU drivers. This facilitates the elimination of “hidden” memory overhead that doesn’t appear in standard Unreal stats.

2. Enable via Perfetto Config

The module is triggered by a Perfetto trace session. You must provide a configuration file that targets the game’s package name. Correctly scoping the trace to your specific PID (Process ID) leads to the elimination of noise from other background Android processes.

3. Monitor System-Wide Allocations

Unlike internal engine profilers, heapprofd can track allocations in libc and other system libraries. This is a best practice for the elimination of memory bloat caused by Android’s asset management or OS-level media playback during gameplay.

4. Optimize for Production Builds

Native heap profiling can introduce significant overhead. Use this module primarily on Development or Test builds. For shipping builds, ensure the profiling hooks are disabled to assist in the elimination of performance hitches on lower-end mobile hardware.

5. Leverage Callstack Sampling

Configure the module to sample callstacks at a specific interval (e.g., every 4KB or 16KB). This statistical sampling approach allows you to find large memory consumers while facilitating the elimination of the massive CPU cost associated with tracking every single tiny allocation.

6. Symbolicate Traces for Readability

To make sense of the data, you must provide the non-stripped versions of your .so (shared object) libraries to the Perfetto UI. Properly symbolicating the trace leads to the elimination of cryptic memory addresses, turning them into readable C++ function names.

7. Combine with “Elimination” Event Tracking

Use heapprofd to verify the elimination of memory when an Actor or Level is destroyed. If the heap does not shrink after an “Elimination” event, it indicates a reference leak that standard Blueprint debugging might miss.

8. Analyze with the Perfetto Web UI

After capturing a trace, upload the resulting file to ui.perfetto.dev. This tool provides a powerful flame-graph view of the heap, aiding in the elimination of complex memory fragmentation issues by visualizing how memory is distributed across the life of the process.