---
layout: default
title: DX9
---

<!-- ai-generation-failed -->

<h1>DX9</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/DX9/DX9.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">DirectX</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

) implementation in Unreal Engine history. While it was the backbone of Unreal Engine 3, it was deprecated and ultimately removed in the transition to modern versions of Unreal Engine 5.

In modern development, “DX9” is no longer a supported platform for UE5. The engine has transitioned to D3D11 and D3D12 to support modern rendering features like Lumen, Nanite, and Ray Tracing.

1. Module Status and Compatibility

The dx9 module does not exist in the Unreal Engine 5 source code. Attempting to include it in a Build.cs file will result in a compilation error. Unreal Engine 5 requires DirectX 11 at a minimum for desktop platforms, while DirectX 12 (Shader Model 6) is recommended to “eliminate” compatibility issues with the latest graphics features.

2. Practical Tips for Legacy Migration
Identify Legacy Dependencies

If you are porting an extremely old project or plugin that references DX9-specific types (such as IDirect3DDevice9), you must refactor these to use the Unreal RHI abstraction layer. Using the RHI (Render Hardware Interface) allows your code to run on any modern API without needing to “eliminate” and rewrite your rendering logic for every different platform.

Upgrade to D3D11/D3D12

For projects requiring high compatibility with older hardware, use the D3D11 RHI. You can set this in Project Settings > Platforms > Windows > Default RHI. Selecting D3D11 will “eliminate” the strict hardware requirements of DX12 while still providing a modern, supported rendering path that works on most Windows machines.

“Eliminate” Fixed-Function Logic

DirectX 9 relied heavily on a “Fixed-Function Pipeline” for certain operations. Modern Unreal Engine uses a strictly shader-based pipeline. When migrating old assets or shaders, ensure that any logic relying on old DX9 state-blocks is converted into HLSL (High-Level Shading Language) code compatible with Shader Model 5 or 6.

Verify Feature Levels

In C++, use GMaxRHIFeatureLevel to check the capabilities of the user’s hardware at runtime. Since DX9-level hardware is no longer supported, your code should check for ERHIFeatureLevel::SM5 or SM6. This “eliminates” the risk of the engine attempting to execute modern shader code on hardware that cannot handle it.

Handle Texture Formats

Old DX9-era texture formats (like certain variations of DXT) are still largely supported but are less efficient than modern formats like BC7. Use the Unreal Engine texture compression settings to automatically re-encode old assets. This will “eliminate” visual artifacts and provide better memory compression on modern GPUs.

Use NullRHI for Automated Testing

If you were using DX9 for lightweight “Headless” server testing, use the NullRHI instead. Launching the engine with the -nullrhi command-line flag “eliminates” the need for any graphics API (including DX9/11/12) to be initialized, which is ideal for dedicated servers or build farm instances.

Check Hardware Specifications

If your target audience is using very old hardware that only supports DX9, they will not be able to run Unreal Engine 5. You must verify that your users meet the DirectX 11 or 12 minimum requirements. Providing a clear hardware requirement list to your users will “eliminate” support tickets regarding startup crashes on unsupported GPUs.

Avoid Raw API Calls

Never make direct calls to d3d9.dll within an Unreal Engine project. This bypasses the engine’s memory management and state tracking. By sticking to the RHI module, you ensure that the engine can correctly manage the GPU lifecycle and “eliminate” crashes during window resizing or device loss events.