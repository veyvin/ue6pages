---
layout: default
title: D3D11RHI
---

<!-- ai-generation-failed -->

<h1>D3D11RHI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/D3D11RHI/D3D11RHI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">HeadMountedDisplay, WindowsD3D</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

der Hardware Interface (RHI) for DirectX 11. It serves as a translation layer that converts platform-independent engine rendering commands into native D3D11 API calls.

While Unreal Engine 5 heavily favors DirectX 12 (D3D12RHI) to support modern features like Nanite and Lumen, the D3D11RHI remains a critical fallback for older hardware, specialized enterprise applications, and debugging. It provides a stable, mature backend that handles the creation of buffers, textures, shaders, and state objects for GPUs that do not fully support the DX12 feature set.

Practical Usage Tips and Best Practices
Understand Feature Limitations
D3D11 cannot support modern UE5 features like Nanite, Lumen, or Hardware Ray Tracing. If your project defaults to D3D11RHI, the engine will “eliminate” these features and fallback to standard mesh rendering and baked/screen-space lighting. Ensure your project settings are configured for your target hardware’s capabilities.
Leverage the D3D Debug Layer
When troubleshooting rendering crashes or “Device Removed” errors, launch the editor with the -d3ddebug command-line argument. This enables the DirectX Debug Layer within the D3D11RHI, providing detailed output in the log that can help you “eliminate” invalid API calls or resource state mismatches.
Manage Draw Call Overhead
DirectX 11 has a much higher CPU overhead per draw call compared to DirectX 12 or Vulkan. To maintain performance, use Instanced Static Meshes or the Actor Merging tool to “eliminate” excessive draw calls that would otherwise bottleneck the Render Thread.
Use for Legacy Hardware Compatibility
If you are targeting low-end PCs or integrated GPUs, D3D11RHI is often more stable than D3D12. You can force the engine to use this module by setting DefaultGraphicsRHI=DefaultGraphicsRHI_DX11 in your DefaultEngine.ini or by passing the -dx11 argument at startup to “eliminate” compatibility issues on older drivers.
Monitor GPU Memory (VRAM) Manually
Unlike DX12, which gives the engine more control over memory management, DX11 relies heavily on the driver to manage resources. Use the stat memory and stat d3d11rhi commands to monitor usage. If you hit VRAM limits, the driver may start swapping memory to system RAM, which you must “eliminate” by reducing texture resolutions or mesh complexity.
Validate Shader Complexity
Some complex shaders written for modern UE5 might fail to compile or perform poorly on the D3D11 backend due to register limits or older shader models (SM5 vs SM6). Always test your materials in the SM5 Preview Mode in the editor to “eliminate” visual discrepancies between development and the final D3D11 build.
Avoid Async Compute on D3D11
The D3D11RHI does not support true asynchronous compute. Any dispatch() calls intended for an async queue will be executed synchronously on the main graphics context. If your logic depends on parallel execution for performance, consider moving to DX12 to “eliminate” the performance penalty of serial execution.
Properly Handle Device Resets
DirectX 11 is susceptible to “TDR” (Timeout Detection and Recovery) if a shader takes too long to execute. To “eliminate” these crashes, optimize your heavy compute shaders and ensure you aren’t blocking the GPU for more than a few milliseconds per frame, as DX11 is less graceful than DX12 at recovering from these events.