---
layout: default
title: oneAPILevelZero
---

<!-- ai-generation-failed -->

<h1>oneAPILevelZero</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Intel/oneAPILevelZero/oneAPILevelZero.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

egrates Intel’s Level Zero API into Unreal Engine. Level Zero is a core component of the Intel oneAPI rendering and compute stack, designed to provide fine-grained, direct-to-metal access to Intel GPU hardware (such as Intel Arc and Data Center GPUs).

In Unreal Engine, this module primarily serves as a bridge for high-performance compute tasks and ray tracing acceleration on Intel hardware. It allows the engine to bypass higher-level API overhead for specific tasks like XeSS (Xe Super Sampling) and specialized compute kernels. By utilizing this direct interface, the engine can eliminate translation latency between the Unreal RHI and Intel’s hardware execution units.

Practical Usage Tips and Best Practices
Ensure Proper Driver Support
Level Zero functionality requires the latest Intel Graphics Drivers that include the oneAPI runtime. Without these, the module will fail to initialize. Verifying driver compatibility during your project’s prerequisite check helps you eliminate “Graphics Device Lost” errors on Intel-based systems.
Optimize XeSS Performance
If your project uses Intel XeSS for upscaling, this module often handles the low-level execution of the machine-learning kernels. Enabling the “Hardware” path (which uses Level Zero) on Intel Arc GPUs helps you eliminate the performance penalty of the generic HLSL fallback path used on other vendors.
Use for Compute-Heavy Plugins
For developers writing custom plugins that perform heavy GPGPU (General-Purpose GPU) calculations, the OneApiLevelZero module provides the necessary headers to interact with Intel’s compute command queues. This is the best way to eliminate CPU-bound bottlenecks for complex mathematical simulations on Intel hardware.
Monitor via Intel Graphics Performance Analyzers (GPA)
Because Level Zero provides low-level hardware metrics, you should use Intel GPA alongside Unreal Insights. This allows you to see exactly how command buffers are being processed, helping you eliminate “bubbles” or idle periods in the GPU pipeline.
Verify RHI Compatibility
This module is most effective when the engine is running in DirectX 12 or Vulkan mode. Ensure your RHI settings are correctly configured in the Project Settings to allow the Level Zero bridge to communicate with the primary renderer, which helps you eliminate texture-sharing synchronization issues.
Leverage for Ray Tracing Hardware Acceleration
On Intel hardware, the OneApiLevelZero module assists in managing the ray tracing acceleration structures (BVH). Using the specialized Intel path helps you eliminate jitter and performance drops in scenes with high ray counts and complex lighting.
Implement Vendor-Specific Fallbacks
Always remember that this module is specific to Intel hardware. When writing C++ logic that touches this module, wrap your code in vendor checks (if (IsIntel())). This practice helps you eliminate crashes or “Undefined Symbol” errors when your game is running on NVIDIA or AMD hardware.
Clean Up Compute Contexts on Elimination
When a compute task is finished or the associated actor is removed (the “elimination” of the compute instance), ensure all Level Zero handles and buffers are properly released. Proper resource management within this module helps you eliminate VRAM leaks that could eventually lead to a full system hang.