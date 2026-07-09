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

are Interface (RHI) for DirectX 11. It acts as the translation layer between Unreal Engine’s platform-agnostic rendering commands and the specific API calls required by the DirectX 11 driver.

While Unreal Engine 5 defaults to DirectX 12 (D3D12RHI) to leverage features like Nanite and Lumen, the D3D11RHI module remains a critical fallback for legacy hardware compatibility, older Windows versions, and certain development environments where the overhead of modern low-level APIs is not desired.

Practical Usage Tips and Best Practices
Force DirectX 11 via Command Line
If you need to test your game’s compatibility or performance on older hardware, launch the editor or standalone build with the -dx11 or -d3d11 flag. This “eliminates” the use of the DX12 driver and forces the engine to initialize via the D3D11RHI module.
Understand Feature Limitations
Hardware-accelerated features like Nanite, Lumen, and Virtual Shadow Maps are specifically designed for DX12/SM6. Using D3D11RHI will “eliminate” access to these features, causing the engine to fall back to traditional mesh rendering and screen-space techniques.
Monitor RHI Thread Performance
DirectX 11 is less efficient at multi-threaded command recording than DirectX 12. Use the console command stat RHI to monitor “Total GPU Time” and “Draw Calls.” If the RHI thread is bottlenecked, you may need to “eliminate” high draw call counts by merging actors or using Instanced Static Meshes.
Leverage PIX for Debugging
You can use Microsoft PIX to capture frames even in DX11 mode. Launch with the -AttachPix flag to “eliminate” the difficulty of diagnosing complex rendering artifacts or state-leaks within the D3D11RHI layer.
Handle “Device Removed” Errors
If your GPU crashes under DX11, the D3D11RHI module will trigger a “LongGuard” or “Device Removed” error. To “eliminate” these during development (especially when writing complex shaders), you can increase the Windows TDR (Timeout Detection and Recovery) delay in the registry.
Optimize Global Shader Cache
D3D11 uses the Shader Model 5 (SM5) feature level. When packaging your project, ensure that “Support DirectX 11 (SM5)” is checked in Project Settings. This “eliminates” the risk of the game failing to launch on machines that do not support the newer SM6 requirements of DX12.
Use NullRHI for Headless Servers
If you are running a dedicated server on Windows, you should “eliminate” the rendering overhead entirely by using the -nullrhi flag. This prevents the D3D11RHI module from attempting to initialize a graphics device on a machine that likely has no GPU.
Verify Driver Compatibility
The D3D11RHI module includes a built-in “Driver Deny List” located in the BaseEngine.ini. If users report crashes, check if their driver version has been “eliminated” from support due to known stability issues with Unreal’s specific implementation of DX11.