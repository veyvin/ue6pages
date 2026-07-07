---
layout: default
title: NVAftermath
---

<!-- ai-generation-failed -->

<h1>NVAftermath</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/NVaftermath/NVaftermath.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rary, providing specialized GPU crash analysis for Windows-based developers using NVIDIA GeForce GPUs.

Description and Purpose

GPU crashes (such as TDR events) are notoriously difficult to debug because the standard CPU callstack often only shows where the CPU was when it noticed the GPU had already failed. The NVAftermath module addresses this by inserting lightweight markers into the GPU command stream and generating a “GPU dump” when a crash occurs. Its primary purpose is to provide “Breadcrumbs” that reveal exactly which draw call or compute shader was being executed at the moment of the crash. This allows developers to eliminate the guesswork involved in fixing “D3D Device Lost” or “DXGI_ERROR_DEVICE_HUNG” errors.

Practical Usage Tips and Best Practices
Enable via Console Variables
To activate Aftermath, add r.GPUCrashDebugging=1 to your ConsoleVariables.ini or launch the engine with the -gpucrashdebugging command-line argument. This is the first step to eliminate the lack of visibility during a GPU hang.
Check the Log for Status Markers
Once enabled, look for LogD3D12RHI: [Aftermath] Aftermath enabled and primed in your output log. When a crash occurs, the log will output a “GPU Stack Dump” showing a hierarchy of passes (e.g., Scene -> ComputeLightGrid -> Compact). Use this hierarchy to eliminate non-relevant systems and focus on the failing shader.
Avoid Using with -d3ddebug Simultaneously
Epic recommends not running -gpucrashdebugging and -d3ddebug at the same time, as they can interfere with one another. To eliminate potential conflicts and performance noise, run tests with each flag separately to gather different types of diagnostic data.
Use for TDR Troubleshooting
If you encounter a Timeout Detection and Recovery (TDR) crash, Aftermath can tell you if the GPU was truly hung or just taking too long on an expensive pass (like high-resolution Ray Traced Global Illumination). This helps you eliminate TDRs by identifying which specific pass needs to be optimized or broken into smaller tiles.
Identify Out of Memory (OOM) Conditions
The Aftermath integration can report if a crash was caused by a memory allocation failure. If the logs indicate an OOM status, you can eliminate the crash by simplifying textures or reducing the render resolution of the specific pass identified in the breadcrumbs.
Safe for Distribution to Testers
Unlike heavy profiling tools, Aftermath is lightweight enough to be included in Development builds sent to external testers. This is a best practice to eliminate “unreproducible” GPU crashes that only happen on specific hardware configurations outside of your internal office environment.
Locate Dump Files for NVIDIA Nsight
When a crash occurs, Aftermath may generate a .nv-gpudmp file in your [Project]/Saved/Logs or [Project]/Saved/Crashes folder. You can open these files in the standalone NVIDIA Nsight Graphics tool to eliminate any ambiguity regarding the state of the GPU pipelines and active warps at the time of the failure.
Monitor Nanite and Compute Passes
Aftermath is particularly effective at debugging modern UE5 systems like Nanite and virtual shadow maps. Because these systems rely heavily on compute shaders, the breadcrumb trail is the best way to eliminate bugs in custom material shaders that might be causing GPU exceptions in the Nanite rasterizer.