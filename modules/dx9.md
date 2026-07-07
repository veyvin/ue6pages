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

tion that provided support for Microsoft’s DirectX 9.0c API. Historically, this module allowed Unreal Engine 3 and early versions of Unreal Engine 4 to run on Windows XP and older hardware.

In the context of modern development, DX9 support has been removed from Unreal Engine (as of version 4.23 and later). Modern versions of the engine, including UE5, focus exclusively on DX11, DX12, Vulkan, and Metal to support advanced rendering features.

Practical Usage Tips and Best Practices
1. Transition to Modern APIs

If you are maintaining a very old project that still references the DX9 module, your primary goal should be the elimination of this dependency. Modern hardware and Windows 10⁄11 are optimized for DX11 and DX12. Moving to DX11 is usually a seamless transition for legacy assets and provides much better stability.

2. Avoid Using Legacy Materials

DirectX 9 relied on an older shader model (SM3.0). Modern Unreal Engine materials are built for SM5 or SM6. Using legacy DX9-era logic can cause rendering artifacts. Upgrading your materials to use modern PBR (Physically Based Rendering) standards ensures the elimination of visual “flatness” associated with older rendering tech.

3. Legacy Asset Cleanup

When migrating from an older engine version that utilized DX9, check for “Fixed Function” textures or specialized shaders that were DX9-specific. Replacing these with standard Texture Samples in the modern Material Editor results in the elimination of “Material Error” warnings during the cooking process.

4. Compatibility with Nanite and Lumen

Be aware that features like Nanite and Lumen require DX12 (SM6) or specific Vulkan features. These systems are fundamentally incompatible with anything related to the old DX9 pipeline. To use modern UE5 features, you must ensure the elimination of any legacy rendering constraints in your project settings.

5. Check Project Settings for RHI Targets

In the Unreal Editor, navigate to Project Settings > Platforms > Windows. Ensure that “DirectX 9” is not selected (if using a version where it still appears) and that DX11 or DX12 is the default. This prevents the engine from trying to initialize a non-existent or deprecated RHI, leading to the elimination of startup crashes on modern GPUs.

6. Handling Older Hardware

If your target audience uses extremely old integrated graphics that do not support DX11, consider using the Mobile Renderer (Vulkan/ES3.1) on PC rather than searching for DX9 workarounds. This provides a modern code path for low-end hardware and ensures the elimination of security vulnerabilities found in older APIs.

7. Remove Deprecated Module References

If you are upgrading a C++ project and encounter errors regarding DX9, D3D9, or the dx9 module in your Build.cs files, delete those strings. Since the module is no longer in the engine source, its removal is required for the elimination of linker errors during compilation.

8. Use Emulation for Testing

If you must see how your game looks on “retro” hardware, do not use DX9. Instead, use the Mobile Previewer or the Active Target Previewer set to a lower Feature Level (like ES3.1). This emulates the constraints of older hardware while staying on a supported API, facilitating the elimination of bugs that would only appear on obsolete systems.