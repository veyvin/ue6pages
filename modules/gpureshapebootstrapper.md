---
layout: default
title: GPUReshapeBootstrapper
---

<!-- ai-generation-failed -->

<h1>GPUReshapeBootstrapper</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/GPUReshape/Source/GPUReshapeBootstrapper/GPUReshapeBootstrapper.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ization module primarily utilized in Unreal Engine’s Linux and Unix-based environments.

Description and Purpose

This module serves as a critical bridge during the early engine startup phase, specifically for managing the transition between the operating system’s environment and the Vulkan or OpenGL Rendering Hardware Interface (RHI). Its primary purpose is to handle the “reshaping” or reconfiguration of the GPU process environment. It ensures that required drivers, library paths (such as ld_library_path), and hardware-specific environment variables are correctly mapped before the main rendering thread initializes. This is essential for maintaining stability in containerized environments (like Docker) or on varied Linux distributions where driver locations can differ.

Practical Usage Tips and Best Practices
Use for Linux Deployment Debugging
If your Linux build fails to initialize the RHI or crashes immediately on launch, check the logs for GPUReshape entries. This module is responsible for finding the correct Vulkan driver (ICD); misconfigured paths here will eliminate the engine’s ability to communicate with the GPU.
Validate glibc Compatibility
For Linux development, ensure your target system uses glibc 2.35 or newer. The bootstrapper interacts with the system loader, and older versions can cause significant delays during the dlopen calls, which might eliminate the performance benefits of a fast-loading game.
Leverage -gpucrashdebugging for Driver Issues
Because this module handles early driver attachment, passing the -gpucrashdebugging command-line argument is vital. If a crash occurs during the bootstrapper’s execution, the resulting log will help you eliminate hardware-specific driver conflicts as a potential cause.
Configure Environment Variables via Shell
Since the bootstrapper reads the environment to configure the GPU, you can use shell scripts to set variables like ENABLE_VULKAN_RENDERDOC_CAPTURE=1 before launching the binary. This allows the bootstrapper to prepare the RHI for external tools, helping you eliminate rendering bugs.
Manage Containerized RHI Initialization
When deploying Unreal Engine in a cloud or pixel-streaming container, the bootstrapper must find the NVIDIA or AMD drivers mapped into the container. Ensure your LD_LIBRARY_PATH includes the driver mount points to eliminate “Device Not Found” errors during the bootstrap phase.
Utilize -vulkanbestpractices for RHI Validation
When the bootstrapper is initializing the Vulkan RHI, passing -vulkanbestpractices enables validation layers. This is a best practice during development to eliminate non-compliant API calls that could lead to an eventual GPU elimination or hang.
Check Vulkan ICD Profiles
On systems with multiple GPUs (like an integrated Intel chip and a discrete NVIDIA card), the bootstrapper follows the system’s Vulkan ICD profile. Use the VK_ICD_FILENAMES environment variable to force the bootstrapper to choose the discrete GPU, which will eliminate the accidental use of low-power integrated graphics.
Monitor Early Memory Allocations
The bootstrapper is active before the full Unreal Insights system is live. For early-phase memory issues, use the -llm (Low Level Memory) flag. This tracks memory used by the RHI during the bootstrap process, helping you eliminate memory leaks that occur before the game even reaches the “BeginPlay” state.