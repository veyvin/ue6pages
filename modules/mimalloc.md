---
layout: default
title: mimalloc
---

<!-- ai-generation-failed -->

<h1>mimalloc</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/mimalloc/mimalloc.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

neral-purpose memory allocator, into Unreal Engine. It is designed for high-performance multi-threaded applications and focuses on strong performance characteristics, including excellent memory locality and low internal fragmentation.

In Unreal Engine, it serves as a modern alternative to the default Windows allocator (TBB or MallocBinned). By providing a highly scalable allocation strategy, it facilitates the elimination of contention in the memory subsystem, particularly in CPU-intensive scenarios like world streaming, complex physics simulations, and massive agent counts.

Practical Usage Tips and Best Practices
1. Enable via BuildConfiguration.xml

To use mimalloc in your project, you must explicitly enable it in your BuildConfiguration.xml file located in AppData/Roaming/Unreal Engine/UnrealBuildTool/. Setting the memory allocator here leads to the elimination of the default allocator for your entire engine instance:

XML
	<Configuration xmlns="https://www.unrealengine.com/BuildConfiguration">

	    <WindowsPlatform>

	        <MemoryAllocator>Mimalloc</MemoryAllocator>

	    </WindowsPlatform>

	</Configuration>
Copy code
2. Leverage for Multi-Threaded Scalability

If your project utilizes many background worker threads (for tasks like Nanite building or procedural generation), mimalloc is a best practice. Its “free list” design avoids global locks, which facilitates the elimination of CPU thread synchronization stalls during frequent allocation and deallocation cycles.

3. Use in CPU-Bound Scenarios

Switching to mimalloc is most effective when your game is CPU-bound due to high memory churn (creating/destroying many actors or objects). Implementing it in these cases leads to the elimination of small but frequent frame-time spikes caused by memory fragmentation and management overhead.

4. Monitor with “Stat System”

After enabling mimalloc, use the console command stat system or stat memory to monitor the overhead. While mimalloc is fast, it may reserve more memory upfront than other allocators. Monitoring this assists in the elimination of unexpected “Out of Memory” errors on systems with limited physical RAM.

5. Verify Platform Compatibility

While mimalloc is highly optimized for Windows and Linux, ensure you test thoroughly if targeting mobile or console platforms. Using an unsupported allocator configuration on a specific platform leads to the elimination of the engine’s stability and can result in immediate boot crashes.

6. Combine with Unreal Insights

Use Unreal Insights (Memory Insights) to compare the performance of mimalloc against the default MallocBinned. Visualizing the allocation patterns leads to the elimination of guesswork when deciding which allocator provides the best throughput for your specific game’s memory footprint.

7. Maintain Engine Cleanliness

Avoid modifying the mimalloc module source code directly. Since it is a third-party integration, manual changes can lead to the elimination of your ability to easily upgrade the engine version later. Use MALLOC_MIMALLOC_API macros if you must interface with it from custom C++ code.

8. Evaluate for Large Projects

For massive open-world games using World Partition, mimalloc’s ability to handle large, varied allocation sizes is superior. Using it in these projects leads to the elimination of performance degradation that typically occurs as the application’s uptime increases and memory becomes fragmented.