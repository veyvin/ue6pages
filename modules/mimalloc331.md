---
layout: default
title: mimalloc331
---

<!-- ai-generation-failed -->

<h1>mimalloc331</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/mimalloc/mimalloc331.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

me-malloc”), a compact, high-performance, and scalable general-purpose memory allocator. In Unreal Engine, it serves as a modern alternative to the standard system allocator and other binned allocators.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/mimalloc331, this module provides a memory allocation strategy designed for high concurrency. It uses “free lists” and specialized page structures to handle memory requests with extremely low overhead.

Primary uses include:

Performance Optimization: Reducing the time spent in malloc and free calls, especially in multi-threaded environments where lock contention can slow down the CPU.
Memory Efficiency: Minimizing fragmentation through a design that returns memory to the OS more aggressively than traditional allocators.
Build System Acceleration: mimalloc is often the default allocator for Unreal Build Accelerator (UBA), ensuring that massive parallel compilation tasks don’t bottleneck on memory management.
Practical Usage Tips and Best Practices
1. Enable via BuildConfiguration.xml

To use mimalloc for your engine builds, you can configure it in your BuildConfiguration.xml. Setting the allocator to mimalloc can lead to the elimination of significant overhead during long C++ compilation sessions or complex asset cooks.

2. Leverage for Multi-Threaded Heavy Logic

If your project uses the Task Graph or Mass Entity to process data across dozens of threads, mimalloc is highly recommended. Its design focuses on thread-local heaps, which results in the elimination of “stop-the-world” lock contention that often occurs with the default Windows allocator (TBB or msvcrt).

3. Monitor for UBA Bottlenecks

When using the Unreal Build Accelerator (UBA), mimalloc is typically enabled by default to speed up remote process execution. If you encounter strange memory-related crashes during a distributed build, you can set bDisableCustomAlloc=true in your UBA settings to perform the elimination of mimalloc as a potential variable during troubleshooting.

4. Use for Large World Coordinate (LWC) Tasks

Projects with massive amounts of double-precision data (LWC) often involve high-frequency allocations of small structs. Mimalloc’s “binned” approach to small objects ensures the elimination of memory “bloat” by packing these small allocations into contiguous pages efficiently.

5. Verify Platform Compatibility

While mimalloc is excellent for Windows and Linux, be aware that certain platforms (like iOS) have strict virtual memory subsystem limitations that may require the use of FMallocBinned instead. Always check your target platform’s memory requirements to ensure the elimination of “Out of Memory” errors caused by incompatible allocation strategies.

6. Profile with Memory Insights

When mimalloc is active, you can still use Unreal Insights (Memory Insights) to track allocations. If you notice a high “Fragmentation” stat in Insights, switching to mimalloc can sometimes result in the elimination of those gaps in your memory map due to its superior page management.

7. Debugging with Memory Stomping Checks

If you suspect a memory stomp (where one piece of code writes into another’s memory), mimalloc includes “secure” features that can help detect these issues. While these features add overhead, enabling them during a debug build leads to the elimination of difficult-to-track corruption bugs by crashing the engine the moment a stomp occurs.

8. Strategic Elimination of Allocation Latency

In high-action games where “hitches” must be avoided, mimalloc’s predictable performance is a major asset. By replacing the default allocator with mimalloc, you are performing a strategic elimination of non-deterministic latency spikes during runtime memory management, resulting in a smoother frame rate for the end-user.