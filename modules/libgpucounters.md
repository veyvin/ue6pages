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

sed by Unreal Engine to interface with vendor-specific GPU performance monitoring libraries.

Description and Purpose

This module acts as a wrapper for third-party SDKs provided by hardware vendors, such as NVIDIA (NVAPI), AMD (AGP/AGS), and Intel (Metrics Framework). Its primary purpose is to retrieve high-frequency hardware metrics—such as GPU clock speeds, memory bandwidth utilization, temperature, and shader unit activity—that are not exposed through standard graphics APIs like DirectX or Vulkan. By using this module, the engine can feed detailed telemetry into tools like Unreal Insights and the GPU Visualizer, helping developers eliminate performance bottlenecks that occur at the silicon level.

Practical Usage Tips and Best Practices
Enable Vendor-Specific Plugins
The functionality of this module often depends on platform plugins (e.g., the NVIDIA Performance Library plugin). Ensure these are enabled in your project settings to eliminate “null” or “zero” readings when attempting to profile hardware-specific metrics.
Use stat hardware for Quick Checks
You can access the data provided by this module in-game using the console command stat hardware. This displays real-time GPU frequency and temperature data, allowing you to eliminate heat-related thermal throttling as a potential cause of sudden frame rate drops.
Monitor VRAM Bandwidth via Unreal Insights
When capturing a trace with Unreal Insights, look for the “GPU Counters” track. This module provides the data necessary to see if the GPU is “bandwidth bound.” Identifying saturated memory buses helps you eliminate excessive texture resolutions or unoptimized buffer layouts.
Verify Hardware Support in C++
Before calling functions that rely on this module, check the return value of IGpuProfiler::IsAvailable(). Hardware counters are not supported on all mobile or integrated GPUs; checking for availability helps you eliminate crashes or log spam on unsupported devices.
Profile Shader Core Utilization
Use the metrics provided by this module to determine if your GPU bottleneck is “Computational” (ALU) or “Texture” (TEX) bound. This distinction allows you to eliminate unnecessary shader complexity rather than wasting time optimizing meshes that are not the actual cause of the slowdown.
Keep Drivers Updated for Metric Accuracy
Hardware vendors frequently update their metric SDKs through driver releases. If you notice inaccurate or missing counters, updating your GPU drivers is the best way to eliminate reporting errors and ensure the LibGpuCounters module is receiving valid data from the hardware.
Limit High-Frequency Sampling in Shipping Builds
Accessing hardware counters via this module incurs a small CPU overhead for each request. For maximum performance, ensure that high-frequency hardware polling is disabled or gated behind #if !UE_BUILD_SHIPPING to eliminate unnecessary performance tax on the end-user.
Analyze Power Draw on Mobile/Laptops
This module can often report the power consumption (TDP) of the GPU. Monitoring this during long playtests helps you eliminate power-hungry rendering features that would cause a mobile device to overheat or drain the battery too quickly.