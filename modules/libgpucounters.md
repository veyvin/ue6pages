---
layout: default
title: libGPUCounters
---

<!-- ai-generation-failed -->

<h1>libGPUCounters</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/libGPUCounters/libGPUCounters.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gine 5 that acts as a bridge to hardware-specific GPU performance counters. Primarily utilized on ARM Mali (Android) platforms, it allows developers to extract granular hardware metrics—such as shader core cycles, stall reasons, texture pipe utilization, and memory bandwidth—directly from the GPU silicon.

Unlike standard RHI profiling (stat gpu), which provides high-level timestamps for rendering passes, libgpucounters exposes the “why” behind a bottleneck (e.g., Is the GPU slow because of math complexity or memory latency?).

Practical Usage Tips & Best Practices
1. Conditional Build.cs Inclusion

The module is platform-specific and should never be included in desktop or shipping builds. Attempting to link it on Windows or in a Shipping target will result in build failures.

Best Practice: Wrap the dependency in an Android platform check within your MyProject.Build.cs file:
C#
	    if (Target.Platform == UnrealTargetPlatform.Android)

	    {

	        PublicDependencyModuleNames.Add("libgpucounters");

	    }

	    ```

	 

	#### 2. Enable the GpuProfiler Trace Channel

	To see these hardware counters in **Unreal Insights**, you must enable the `gpu` trace channel. Hardware counters are typically funneled through the `GpuProfilerTrace` system.

	*   **Tip:** Launch your Android build with the following command-line argument:

	    ```bash

	    -trace=gpu,cpu,frame

	    ```

	    Once captured, these will appear in the **Counters** or **Timing Insights** view under a "Mali GPU" or "GPU Hardware" category.

	 

	#### 3. Use for "Boundness" Analysis

	Standard profilers tell you if you are GPU bound. `libgpucounters` tells you *how* you are bound.

	*   **Tip:** Look for **Stall Rate** vs. **Active Cycles**. If `LS_STALL` (Load/Store Stall) is high, your shaders are waiting for memory; if `VARYING_STALL` is high, your bottleneck is likely vertex-to-fragment interpolation. Use this data to decide between optimizing texture fetches or simplifying vertex data.

	 

	#### 4. Manage Profiling Overhead

	Hardware counters are not "free." Accessing these registers requires frequent interrupts that can slightly degrade frame rate, potentially skewing your results.

	*   **Best Practice:** Use `libgpucounters` for targeted optimization sessions rather than keeping it active during general QA. Proactive **elimination** of profiling overhead is key to getting an accurate representation of "real-world" performance.

	 

	#### 5. Verify Driver and Hardware Support

	This module relies on the vendor’s driver (specifically ARM’s user-space drivers on Android). Not all Android devices support these counters.

	*   **Tip:** Check the `UE_LOG` output during startup. If the module fails to initialize, it will usually log a `LogRHI` or `LogAndroid` error stating that the Mali counter library could not be loaded. This ensures the **elimination** of guesswork when metrics appear blank in Insights.

	 

	#### 6. Combine with RHI Scoped Stats

	To correlate hardware counters with specific draw calls, you should still use standard C++ profiling macros.

	*   **Best Practice:** Use `SCOPED_GPU_STAT` in your C++ code. The hardware counters provided by `libgpucounters` will be sampled during these intervals, allowing you to see exactly which rendering pass is causing specific hardware stalls.

	    ```cpp

	    #include "GpuProfilerTrace.h"

	    // ... inside a rendering function

	    SCOPED_GPU_STAT(RHICmdList, MyCustomRenderPass);

	    ```

	 

	#### 7. Use Command Line to Toggle at Runtime

	You can often toggle the sampling rate or the specific counters being tracked via console variables if the module is active.

	*   **Tip:** Use `r.GpuStatsEnabled 1` to ensure the underlying RHI system is ready to receive data from the hardware counter library.

	 

	#### 8. Target Mali-Specific Optimization (Mobile)

	Since this module is heavily tied to ARM Mali, use it to validate mobile-specific features like **Forward Pixel Killing (FPK)**.

	*   **Best Practice:** Monitor the `FRAGMENT_JOBS` counter. If you see high fragment work but low FPK efficiency, it indicates your Z-prepass or draw order is inefficient, leading to wasted GPU cycles on occluded pixels.
Copy code
2. Enable the GpuProfiler Trace Channel

To see these hardware counters in Unreal Insights, you must enable the gpu trace channel. Hardware counters are typically funneled through the GpuProfilerTrace system.

Tip: Launch your Android build with the following command-line argument:
C#
	    if (Target.Platform == UnrealTargetPlatform.Android)

	    {

	        PublicDependencyModuleNames.Add("libgpucounters");

	    }

	    ```

	 

	#### 2. Enable the GpuProfiler Trace Channel

	To see these hardware counters in **Unreal Insights**, you must enable the `gpu` trace channel. Hardware counters are typically funneled through the `GpuProfilerTrace` system.

	*   **Tip:** Launch your Android build with the following command-line argument:

	    ```bash

	    -trace=gpu,cpu,frame

	    ```

	    Once captured, these will appear in the **Counters** or **Timing Insights** view under a "Mali GPU" or "GPU Hardware" category.

	 

	#### 3. Use for "Boundness" Analysis

	Standard profilers tell you if you are GPU bound. `libgpucounters` tells you *how* you are bound.

	*   **Tip:** Look for **Stall Rate** vs. **Active Cycles**. If `LS_STALL` (Load/Store Stall) is high, your shaders are waiting for memory; if `VARYING_STALL` is high, your bottleneck is likely vertex-to-fragment interpolation. Use this data to decide between optimizing texture fetches or simplifying vertex data.

	 

	#### 4. Manage Profiling Overhead

	Hardware counters are not "free." Accessing these registers requires frequent interrupts that can slightly degrade frame rate, potentially skewing your results.

	*   **Best Practice:** Use `libgpucounters` for targeted optimization sessions rather than keeping it active during general QA. Proactive **elimination** of profiling overhead is key to getting an accurate representation of "real-world" performance.

	 

	#### 5. Verify Driver and Hardware Support

	This module relies on the vendor’s driver (specifically ARM’s user-space drivers on Android). Not all Android devices support these counters.

	*   **Tip:** Check the `UE_LOG` output during startup. If the module fails to initialize, it will usually log a `LogRHI` or `LogAndroid` error stating that the Mali counter library could not be loaded. This ensures the **elimination** of guesswork when metrics appear blank in Insights.

	 

	#### 6. Combine with RHI Scoped Stats

	To correlate hardware counters with specific draw calls, you should still use standard C++ profiling macros.

	*   **Best Practice:** Use `SCOPED_GPU_STAT` in your C++ code. The hardware counters provided by `libgpucounters` will be sampled during these intervals, allowing you to see exactly which rendering pass is causing specific hardware stalls.

	    ```cpp

	    #include "GpuProfilerTrace.h"

	    // ... inside a rendering function

	    SCOPED_GPU_STAT(RHICmdList, MyCustomRenderPass);

	    ```

	 

	#### 7. Use Command Line to Toggle at Runtime

	You can often toggle the sampling rate or the specific counters being tracked via console variables if the module is active.

	*   **Tip:** Use `r.GpuStatsEnabled 1` to ensure the underlying RHI system is ready to receive data from the hardware counter library.

	 

	#### 8. Target Mali-Specific Optimization (Mobile)

	Since this module is heavily tied to ARM Mali, use it to validate mobile-specific features like **Forward Pixel Killing (FPK)**.

	*   **Best Practice:** Monitor the `FRAGMENT_JOBS` counter. If you see high fragment work but low FPK efficiency, it indicates your Z-prepass or draw order is inefficient, leading to wasted GPU cycles on occluded pixels.
Copy code
Once captured, these will appear in the Counters or Timing Insights view under a “Mali GPU” or “GPU Hardware” category.
3. Use for “Boundness” Analysis

Standard profilers tell you if you are GPU bound. libgpucounters tells you how you are bound.

Tip: Look for Stall Rate vs. Active Cycles. If LS_STALL (Load/Store Stall) is high, your shaders are waiting for memory; if VARYING_STALL is high, your bottleneck is likely vertex-to-fragment interpolation. Use this data to decide between optimizing texture fetches or simplifying vertex data.
4. Manage Profiling Overhead

Hardware counters are not “free.” Accessing these registers requires frequent interrupts that can slightly degrade frame rate, potentially skewing your results.

Best Practice: Use libgpucounters for targeted optimization sessions rather than keeping it active during general QA. Proactive elimination of profiling overhead is key to getting an accurate representation of “real-world” performance.
5. Verify Driver and Hardware Support

This module relies on the vendor’s driver (specifically ARM’s user-space drivers on Android). Not all Android devices support these counters.

Tip: Check the UE_LOG output during startup. If the module fails to initialize, it will usually log a LogRHI or LogAndroid error stating that the Mali counter library could not be loaded. This ensures the elimination of guesswork when metrics appear blank in Insights.
6. Combine with RHI Scoped Stats

To correlate hardware counters with specific draw calls, you should still use standard C++ profiling macros.

Best Practice: Use SCOPED_GPU_STAT in your C++ code. The hardware counters provided by libgpucounters will be sampled during these intervals, allowing you to see exactly which rendering pass is causing specific hardware stalls.
C#
	    if (Target.Platform == UnrealTargetPlatform.Android)

	    {

	        PublicDependencyModuleNames.Add("libgpucounters");

	    }

	    ```

	 

	#### 2. Enable the GpuProfiler Trace Channel

	To see these hardware counters in **Unreal Insights**, you must enable the `gpu` trace channel. Hardware counters are typically funneled through the `GpuProfilerTrace` system.

	*   **Tip:** Launch your Android build with the following command-line argument:

	    ```bash

	    -trace=gpu,cpu,frame

	    ```

	    Once captured, these will appear in the **Counters** or **Timing Insights** view under a "Mali GPU" or "GPU Hardware" category.

	 

	#### 3. Use for "Boundness" Analysis

	Standard profilers tell you if you are GPU bound. `libgpucounters` tells you *how* you are bound.

	*   **Tip:** Look for **Stall Rate** vs. **Active Cycles**. If `LS_STALL` (Load/Store Stall) is high, your shaders are waiting for memory; if `VARYING_STALL` is high, your bottleneck is likely vertex-to-fragment interpolation. Use this data to decide between optimizing texture fetches or simplifying vertex data.

	 

	#### 4. Manage Profiling Overhead

	Hardware counters are not "free." Accessing these registers requires frequent interrupts that can slightly degrade frame rate, potentially skewing your results.

	*   **Best Practice:** Use `libgpucounters` for targeted optimization sessions rather than keeping it active during general QA. Proactive **elimination** of profiling overhead is key to getting an accurate representation of "real-world" performance.

	 

	#### 5. Verify Driver and Hardware Support

	This module relies on the vendor’s driver (specifically ARM’s user-space drivers on Android). Not all Android devices support these counters.

	*   **Tip:** Check the `UE_LOG` output during startup. If the module fails to initialize, it will usually log a `LogRHI` or `LogAndroid` error stating that the Mali counter library could not be loaded. This ensures the **elimination** of guesswork when metrics appear blank in Insights.

	 

	#### 6. Combine with RHI Scoped Stats

	To correlate hardware counters with specific draw calls, you should still use standard C++ profiling macros.

	*   **Best Practice:** Use `SCOPED_GPU_STAT` in your C++ code. The hardware counters provided by `libgpucounters` will be sampled during these intervals, allowing you to see exactly which rendering pass is causing specific hardware stalls.

	    ```cpp

	    #include "GpuProfilerTrace.h"

	    // ... inside a rendering function

	    SCOPED_GPU_STAT(RHICmdList, MyCustomRenderPass);

	    ```

	 

	#### 7. Use Command Line to Toggle at Runtime

	You can often toggle the sampling rate or the specific counters being tracked via console variables if the module is active.

	*   **Tip:** Use `r.GpuStatsEnabled 1` to ensure the underlying RHI system is ready to receive data from the hardware counter library.

	 

	#### 8. Target Mali-Specific Optimization (Mobile)

	Since this module is heavily tied to ARM Mali, use it to validate mobile-specific features like **Forward Pixel Killing (FPK)**.

	*   **Best Practice:** Monitor the `FRAGMENT_JOBS` counter. If you see high fragment work but low FPK efficiency, it indicates your Z-prepass or draw order is inefficient, leading to wasted GPU cycles on occluded pixels.
Copy code
7. Use Command Line to Toggle at Runtime

You can often toggle the sampling rate or the specific counters being tracked via console variables if the module is active.

Tip: Use r.GpuStatsEnabled 1 to ensure the underlying RHI system is ready to receive data from the hardware counter library.
8. Target Mali-Specific Optimization (Mobile)

Since this module is heavily tied to ARM Mali, use it to validate mobile-specific features like Forward Pixel Killing (FPK).

Best Practice: Monitor the FRAGMENT_JOBS counter. If you see high fragment work but low FPK efficiency, it indicates your Z-prepass or draw order is inefficient, leading to wasted GPU cycles on occluded pixels.