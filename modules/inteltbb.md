---
layout: default
title: IntelTBB
---

<!-- ai-generation-failed -->

<h1>IntelTBB</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Intel/TBB/IntelTBB.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Located in Engine/Source/ThirdParty/Intel/TBB, this module is a core dependency for the engine’s performance layer. It is used to distribute heavy computational workloads—such as physics, animation skinning, and texture compression—across all available CPU cores.

Primary uses include:

ParallelFor: Powering the ParallelFor() function used to run loops in parallel.
Task Scheduling: Acting as the backend for the Task Graph and the newer Tasks System, managing how threads are “stolen” from idle cores to maximize throughput.
MallocTBB: Providing a high-performance memory allocator (FMallocTBB) designed specifically to prevent lock contention when multiple threads allocate memory simultaneously.
Scalability: Ensuring the engine scales linearly with high core-count CPUs (e.g., Threadripper or Xeon).
Practical Usage Tips and Best Practices
1. Prefer ParallelFor for Heavy Loops

When you have a large array of data to process (e.g., updating 10,000 AI states), use ParallelFor. It uses the TBB backend to automatically chunk the data and distribute it. This ensures the elimination of “long frames” caused by serial processing on the Game Thread.

C++
	// Example: Processing a large data set in parallel

	ParallelFor(DataArray.Num(), [&](int32 Index) {

	    DoExpensiveWork(DataArray[Index]);

	});

	```

	 

	#### 2. Fine-tune with "Grain Size"

	A common TBB pitfall is creating too many small tasks, which adds overhead. If your loop body is very light, use the `ParallelFor` overload that allows for a "Batch Size." This tells TBB to process items in groups (e.g., 100 at a time), which leads to the **elimination** of scheduling overhead.

	 

	#### 3. Use `FMallocTBB` for Multi-threaded Memory Stress

	If your project performs heavy allocations from multiple threads (common in procedural generation), ensure you are using the TBB allocator. You can check this in your log at startup; it should say `Using MallocTBB`. It is significantly faster than the default system allocator for concurrent `New` and `Delete` operations.

	 

	#### 4. Avoid Nested Parallelism

	While TBB supports it, nesting `ParallelFor` inside another `ParallelFor` can lead to "oversubscription," where the CPU spends more time switching contexts than doing work. A best practice is to parallelize only the outermost loop or use the **Tasks System** to define a dependency graph instead.

	 

	#### 5. Leverage `TAtomic` for Thread-Safe Counters

	TBB-backed systems work best with lock-free logic. Instead of using `FCriticalSection` (which can stall the TBB scheduler), use `TAtomic<int32>` for simple counters or flags. This ensures the **elimination** of thread stalls during high-concurrency operations.

	 

	#### 6. Profile with "Thread" View in Unreal Insights

	To see TBB in action, use **Unreal Insights** and look at the "Worker Threads" track. If you see many "gaps" between tasks, your grain size may be too large. If you see massive "Task Overhead" markers, your tasks are too small and frequent.

	 

	#### 7. Set Core Affinity for Console Stability

	On consoles (PS5/Xbox), TBB’s ability to use every core can sometimes interfere with the OS or Audio threads. Use the `FThreadManager` or specific console variables (like `TaskGraph.NumWorkerThreads`) to reserve specific cores for the Game and Render threads, ensuring the **elimination** of micro-stutter.

	 

	#### 8. Strategic Elimination of Blocking Calls

	The TBB scheduler assumes that worker threads are always "doing work." If you call a blocking function (like `FPlatformProcess::Sleep` or a synchronous file read) inside a parallel loop, you effectively "kidnap" a TBB worker thread, reducing the total throughput of the engine. Always use asynchronous I/O when working within parallelized code.
Copy code
2. Fine-tune with “Grain Size” or “Batch Size”

A common TBB pitfall is creating too many small tasks, which adds overhead. If your loop body is very light, use the ParallelFor overload that allows for a “Batch Size.” This tells TBB to process items in groups (e.g., 100 at a time), which leads to the elimination of scheduling overhead.

3. Use FMallocTBB for Multi-threaded Memory Stress

If your project performs heavy allocations from multiple threads (common in procedural generation), ensure you are using the TBB allocator. You can check this in your log at startup; it should say Using MallocTBB. It is significantly faster than the default system allocator for concurrent New and Delete operations.

4. Avoid Nested Parallelism

While TBB supports it, nesting ParallelFor inside another ParallelFor can lead to “oversubscription,” where the CPU spends more time switching contexts than doing work. A best practice is to parallelize only the outermost loop or use the Tasks System to define a dependency graph instead.

5. Leverage TAtomic for Thread-Safe Counters

TBB-backed systems work best with lock-free logic. Instead of using FCriticalSection (which can stall the TBB scheduler), use TAtomic<int32> for simple counters or flags. This ensures the elimination of thread stalls during high-concurrency operations.

6. Profile with “Thread” View in Unreal Insights

To see TBB in action, use Unreal Insights and look at the “Worker Threads” track. If you see many “gaps” between tasks, your grain size may be too large. If you see massive “Task Overhead” markers, your tasks are too small and frequent, requiring optimization.

7. Set Core Affinity for Console Stability

On consoles (PS5/Xbox), TBB’s ability to use every core can sometimes interfere with the OS or Audio threads. Use the FThreadManager or specific console variables (like TaskGraph.NumWorkerThreads) to reserve specific cores for the Game and Render threads, ensuring the elimination of micro-stutter.

8. Strategic Elimination of Blocking Calls

The TBB scheduler assumes that worker threads are always “doing work.” If you call a blocking function (like FPlatformProcess::Sleep or a synchronous file read) inside a parallel loop, you effectively “kidnap” a TBB worker thread, reducing the total throughput of the engine. Always use asynchronous I/O when working within parallelized code.