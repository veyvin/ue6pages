---
layout: default
title: D3D12RHI
---

<!-- ai-generation-failed -->

<h1>D3D12RHI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/D3D12RHI/D3D12RHI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ASDCore, Engine, HeadMountedDisplay, WinPixEventRuntime, WindowsD3D</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

terface (RHI) in Unreal Engine. It acts as the low-level bridge between the engine’s high-level rendering commands (like those from Lumen, Nanite, and Niagara) and the Windows/Xbox graphics drivers.

As a modern, low-level API, this module enables advanced features like Hardware Ray Tracing (HWRT), Bindless Rendering, and Asynchronous Compute. It is designed to reduce CPU driver overhead by allowing the engine to manage memory and thread synchronization more directly than in DX11.

Practical Usage Tips and Best Practices
1. Enable via Project Settings

To utilize this module, go to Project Settings > Platforms > Windows > Default RHI and select DirectX 12. This is a requirement for using modern UE5 features like Lumen Hardware Ray Tracing and Nanite Programmable Rasterizer. Switching to DX12 is the primary step for the elimination of legacy rendering bottlenecks on modern GPUs.

2. Manage PSO Precaching (UE 5.3+)

DirectX 12 is prone to “shader stutter” because Pipeline State Objects (PSOs) must be compiled before they can be used. UE 5.3+ enables PSO Precaching by default. To ensure the elimination of hitches during gameplay, use the function FShaderPipelineCache::NumPrecompilesRemaining() to display a loading screen until all critical shaders are ready.

3. Utilize DRED for GPU Crash Debugging

If the game crashes with a “Device Removed” error, enable Device Removed Extended Data (DRED). Use the console command r.D3D12.DRED=1 or the launch argument -dred. This provides breadcrumbs that pinpoint exactly which draw call caused the GPU to hang, leading to the elimination of guesswork in rendering bug fixes.

4. Monitor the RHI Thread

DX12 relies heavily on an efficient RHI Thread to submit commands to the GPU. Use the command stat dispatch or stat rhi to monitor performance. If the RHI thread is saturated, consider simplifying your scene’s draw call count or using Instance Tooling to assist in the elimination of CPU-side command list submission overhead.

5. Configure Agility SDK Version

The D3D12RHI module uses the Microsoft DirectX 12 Agility SDK to support the latest features (like Work Graphs or Shader Model 6.6+) without requiring a specific OS build. Ensure your project is targeting a compatible Agility SDK version in the engine’s .ini files to ensure the elimination of compatibility issues on older versions of Windows 10.

6. Optimize Async Compute

This module supports Async Compute, allowing the GPU to process tasks like physics or lighting (Lumen) on a separate queue while the main graphics pass is running. Ensure r.AsyncCompute is enabled (usually 1 by default) to maximize GPU utilization and facilitate the elimination of idle GPU time during complex frames.

7. Profile with Pix or NSight

Because the D3D12RHI module provides a direct mapping to the hardware, standard engine profilers may not show the full picture. Use external tools like Microsoft PIX or NVIDIA Nsight. These tools hook into the D3D12 layer to show detailed memory allocation and pipeline stalls, aiding in the elimination of deep-level performance bottlenecks.

8. Implement SM6 for Advanced Shaders

Force the use of Shader Model 6 (SM6) in your Windows Target Settings. This allows the D3D12RHI to use more modern compiler features like wave intrinsics, which can significantly speed up compute shaders. This transition is essential for the elimination of inefficient shader code paths in high-end PC titles.