---
layout: default
title: AMD_AGS
---

<!-- ai-generation-failed -->

<h1>AMD_AGS</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/AMD/AMD_AGS/AMD_AGS.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

yer that integrates the AMD AGS library into Unreal Engine 5. It allows the engine to communicate directly with AMD Radeon GPUs to access features and information that are not available through standard DirectX or Vulkan APIs.

It is primarily used for deep hardware identification, multi-GPU topology detection, and enabling AMD-specific shader extensions. These extensions allow for optimizations like specialized math intrinsics, barycentric coordinates, and advanced wave-front operations, which can significantly improve performance on Radeon hardware.

1. Enable Module in Build.cs

If you are writing custom shaders or low-level RHI code that requires AMD intrinsics, you must explicitly add the module to your project’s Build.cs. This ensures the necessary headers and linking for the AGS library are included.

C#
	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("AMD_AGS");

	}
Copy code
2. Verify Hardware Support at Runtime

Before calling any AGS-specific functions, always check if the AGS context was successfully initialized. Not all systems have the library or a compatible driver. Attempting to call AGS functions on non-AMD hardware without checking will lead to an immediate crash, effectively eliminating the stability of your build.

C++
	#if WITH_AMD_AGS

	    if (AMDAGS::GetContext() != nullptr) 

	    {

	        // Execute AMD specific logic

	    }

	#endif
Copy code
3. Accessing Shader Extensions

The module allows you to use AMD_EXT_ defines in your .usf or .ush shader files. These provide access to features like Wave Intrinsic Functions (GCN/RDNA architecture), which allow threads within a wave to share data without using local memory. This is critical for optimizing high-density compute shaders and reducing register pressure.

4. Hardware Topology and Memory Info

The amd_ags module provides more granular info than the standard RHI. Use it to detect the exact number of Physical GPUs (Crossfire/mGPU) and specific local memory (VRAM) sizes. This is particularly useful for automated graphics settings that need to scale based on specific hardware capabilities rather than generic “High/Ultra” presets.

5. Proper DLL Redistribution

When packaging your game, Unreal Engine generally handles the inclusion of amd_ags_x64.dll. However, if you are using a custom build pipeline or a non-standard installation, ensure this DLL is present in your Binaries/Win64 folder. If the DLL is missing, any code dependent on the module will fail to initialize, and AMD-specific optimizations will be disabled.

6. Use for Cross-Platform Parity

Because the PlayStation 5 and Xbox Series X/S use AMD RDNA-based hardware, using the amd_ags module on PC can help you achieve closer feature parity between PC and Console versions. By leveraging AGS intrinsics on PC, you can use the same optimized shader paths that the consoles use, rather than falling back to less efficient generic HLSL paths.

7. Monitor via Unreal Insights

When using AGS shader extensions, monitor your GPU timings carefully using Unreal Insights or stat gpu. While AGS intrinsics can improve performance, improper use of wave-level operations can lead to “hangs” or artifacts. Use these profiling tools to ensure your optimizations are actually reducing frame time and not introducing stalls.

8. Driver Version Sensitivity

AMD GPU Services often requires a minimum driver version to support specific extensions. It is a best practice to include a “Minimum Driver Version” check in your project’s startup logic. You can use AGS to query the current driver version and warn the user if an update is required to prevent the elimination of advanced rendering features like Ray Tracing or specific shader optimizations.