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

nterface (RHI) for Microsoft’s DirectX 12 API. It acts as the low-level translation layer that converts platform-agnostic engine rendering commands into specific DX12 API calls, managing modern graphics features like asynchronous compute, ray tracing (DXR), and resource binding.

This module is essential for high-end Windows and Xbox development, enabling the use of Nanite, Lumen, and Hardware Ray Tracing.

Practical Usage Tips and Best Practices
1. Enable DRED for Crash Debugging

If your project is experiencing intermittent GPU hangs, enable Device Removed Extended Data (DRED). This DX12 feature helps identify the exact command that caused the crash. Use the following console variables to gain deep insights into the state of the GPU at the moment of failure: r.D3D12.DRED=1 r.GPUCrashDebugging=1 This facilitates the elimination of guesswork when diagnosing “Device Removed” errors.

2. Manage PSO Precaching

DX12 is prone to “shader stutter” during the first run. Unreal Engine uses a PSO (Pipeline State Object) precaching system to compile shaders in the background. You can optimize this by adjusting the thread pool size to match your target hardware’s CPU core count: r.pso.PrecompileThreadPoolSize=8 Properly tuning this ensures the elimination of runtime hitches when new effects appear on screen.

3. Use the D3D12 Debug Layer

When developing custom shaders or RDG (Render Graph) passes in C++, run the editor with the -d3ddebug command-line argument. This activates the official DirectX 12 validation layer, which will log detailed warnings to the Output Log if you violate API rules. This is the most effective way to ensure the elimination of subtle memory corruption in your rendering code.

4. Monitor Memory with “stat D3D12RHI”

DirectX 12 gives the engine more control over memory management than DX11. Use the console command stat D3D12RHI to view real-time statistics on video memory (VRAM) usage, including allocated textures and buffers. Monitoring this helps in the elimination of VRAM over-budgeting, which can lead to aggressive texture streaming or crashes.

5. Leverage Async Compute

The D3D12RHI module supports Async Compute, allowing the GPU to process compute shaders (like those used for lighting or physics) in parallel with the main graphics queue. Ensure r.AsyncCompute is enabled to maximize GPU utilization. This results in the elimination of idle GPU cycles while waiting for heavy draw calls to finish.

6. Clear Driver Cache for Clean Testing

When testing the “first-time player experience” regarding shader compilation, use the command-line argument -clearPSODriverCache. This forces the DX12 driver to delete its local shader cache, ensuring you see the true performance impact of your PSO setup and allowing for the elimination of false-positive performance results from previous runs.

7. Understand the RHI Thread

D3D12RHI heavily utilizes the RHI Thread, which parallels the translation of commands from the Render Thread to the GPU. To see if your game is “RHI Thread Bound,” use stat unit. If the RHI time is higher than the GPU time, you may need to simplify your scene’s draw call count or optimize your material complexity to assist in the elimination of CPU-side rendering bottlenecks.

8. Direct Module Interaction in C++

If you must access the raw DX12 Device or Command Queue for third-party library integration (like NVIDIA DLSS or specialized plugins), include the module in your Build.cs. However, always wrap this in platform checks to avoid breaking cross-platform builds:

C#
	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("D3D12RHI");

	}
Copy code

Access the device via ID3D12DynamicRHI::GetNativeDevice(), but only as a last resort to maintain the elimination of platform-specific code in your high-level logic.