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

acy Rendering Hardware Interface (RHI) module used to support Microsoft DirectX 9. It acted as the communication layer between Unreal Engine and older Windows graphics drivers, primarily those found on Windows XP and early Windows Vista systems.

In modern development, this module has been officially removed as of Unreal Engine 5.0, as the engine now requires a minimum of DirectX 11 (SM5) or DirectX 12 (SM6). Historically, it was responsible for translating the engine’s high-level draw commands into API calls that older GPUs could understand, though it lacked support for modern features like Nanite, Lumen, or complex Compute Shaders.

Practical Usage Tips and Best Practices
1. Plan for API Migration

If you are maintaining a legacy project that still utilizes the dx9 module, prioritize upgrading to DirectX 11 or 12. Modern versions of Unreal Engine no longer support SM3 hardware. Transitioning to a newer RHI is the primary step for the elimination of compatibility crashes on modern Windows 10⁄11 operating systems.

2. Verify Legacy Hardware Targets

For developers targeting very old hardware (e.g., Windows XP systems), you must remain on Unreal Engine 4.x (specifically versions prior to 4.27 where deprecation began). Continuing with older versions is the only way to ensure the elimination of “Feature Level Not Supported” errors for end-users on legacy devices.

3. Standardize on DirectX 11 for “Low” Settings

Rather than relying on the legacy dx9 module for performance, use the DirectX 11 (SM5) RHI and adjust the Scalability Settings. Lowering resolutions and disabling post-processing in SM5 provides better stability and performance than the old dx9 module ever could, aiding in the elimination of visual artifacts.

4. Avoid DX9 in Command-Line Arguments

Older tutorials may suggest launching the editor or game with the -dx9 flag. In UE5, using this flag will result in the elimination of the application launch process entirely, as the engine will fail to find the required RHI module. Always use -dx11 or -dx12 for modern builds.

5. Remove Stale Shader Code

If your project contains custom shaders (.usf or .ush files) with legacy DirectX 9 hacks or SM3-specific workarounds, remove them. Modern compilers optimized for DX12/Vulkan may struggle with these legacy paths. Cleaning up this code facilitates the elimination of shader compilation warnings during the cook process.

6. Transition to Vulkan for Cross-Platform “Low End”

If you were previously using DX9 to target low-spec Windows machines, consider the Vulkan RHI as a modern alternative. Vulkan provides high-performance access to hardware while maintaining modern feature sets, leading to the elimination of the overhead associated with the aging Direct3D 9 framework.

7. Audit Material Nodes for SM5/SM6

Many features available in the Material Editor today (like certain Texture Gradients or Advanced Math nodes) were never compatible with the dx9 module. When upgrading an old project, audit your materials to ensure they are fully utilizing SM5 nodes, which assists in the elimination of “Material Failed to Compile” errors.

8. Check for Legacy DLL Dependencies

If you are porting an old project to a new engine version, check your Binaries folder for d3d9.dll or similar redistributables. These are no longer needed by Unreal Engine and should be removed to ensure the elimination of bloat and potential library conflicts in your final packaged build.