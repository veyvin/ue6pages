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

r Hardware Interface (RHI). It acts as the abstraction layer that translates platform-independent rendering commands into specific DirectX 11 API calls for Windows-based systems.

While UE5 has transitioned to Direct3D 12 as the default for modern features (like Nanite and Lumen), the D3D11RHI remains a critical legacy module for maintaining compatibility with older hardware, ensuring stability on lower-end Windows machines, and providing a fallback for projects that do not require high-end DX12 features.

Practical Usage Tips and Best Practices
1. Forced RHI Command Line Argument

During development or testing, you may need to force the engine to run in DX11 mode to verify compatibility or performance.

Action: Launch the editor or game with the -dx11 command-line argument. This bypasses the default DX12 initialization and forces the engine to use the D3D11RHI, helping you eliminate driver-specific issues occurring only in newer APIs.
2. Enable GPU Crash Debugging

DX11 is historically difficult to debug when a “Device Removed” error occurs because it lacks the advanced diagnostic tools of DX12.

Tip: Use the command line -gpucrashdebugging or set r.GPUCrashDebugging=1 in ConsoleVariables.ini. This enables additional breadcrumbs within the D3D11RHI that help eliminate guesswork when tracking down which draw call caused the GPU to hang.
3. Utilize NVIDIA Aftermath

If you are developing on NVIDIA hardware, the D3D11RHI supports NVIDIA Nsight Aftermath.

Action: Ensure Aftermath is enabled in your logs. When a crash occurs, the D3D11RHI will output a status dump showing exactly which shader pass was active at the time of elimination. This is invaluable for identifying infinite loops in custom HLSL code.
4. Monitor Feature Level Constraints

DirectX 11 cannot support UE5’s flagship features like Nanite, Lumen, or Virtual Shadow Maps.

Best Practice: If your project must support DX11, you must provide fallback content (LODs and baked lighting). Use the “Preview Rendering Level” in the editor to switch to “Shader Model 5 (DX11)” to eliminate visual discrepancies that players on older hardware might see.
5. Handle “Device Removed” Gracefully

In a C++ RHI context, the D3D11RHI may encounter a DXGI_ERROR_DEVICE_REMOVED if the GPU driver crashes or the hardware is disconnected.

Tip: Check the engine logs for the “Reason” code. If the reason is DXGI_ERROR_DEVICE_RESET, it usually indicates a different application caused the crash. Understanding these codes helps you eliminate false reports of engine bugs that are actually caused by external software.
6. Profile with ‘profilegpu’

The built-in GPU profiler works seamlessly with the D3D11RHI to give you a breakdown of the frame.

Command: Press Ctrl + Shift + , (Comma) or type profilegpu in the console. This provides a detailed view of the rendering pipeline. Use this to find expensive draw calls and eliminate bottlenecks in your material instructions or transparency density.
7. Use for “Internal” Standalone Tools

Many internal studio tools (like commandlets or custom asset builders) do not need the overhead of DX12 or ray-tracing.

Best Practice: Configure non-graphical or low-fidelity internal tools to use DX11 via the project’s Target.cs or App.ini. This can eliminate the longer “Pipeline State Object” (PSO) caching times associated with DX12, leading to faster tool startup.
8. Avoid Over-Reliance on Legacy Tessellation

The D3D11RHI supported hardware tessellation, which has been deprecated in UE5 in favor of Nanite.

Action: If you are migrating a project from UE4 to UE5 while staying on DX11, manually audit your materials for tessellation nodes. Since Nanite doesn’t run on DX11, you must eliminate legacy tessellation and replace it with standard LODs to ensure the project remains performant.