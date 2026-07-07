---
layout: default
title: LinuxArm64TargetPlatform
---

<!-- ai-generation-failed -->

<h1>LinuxArm64TargetPlatform</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Linux/LinuxArm64TargetPlatform/LinuxArm64TargetPlatform.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopPlatform, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nreal Engine platform abstraction layer, specifically designed to handle the AArch64 (ARM64) architecture on Linux.

Description and Purpose

This module provides the implementation of the ITargetPlatform interface for the Linux ARM64 target. Its primary purpose is to define the capabilities, settings, and packaging rules for applications intended to run on ARM64-based Linux hardware, such as AWS Graviton servers, NVIDIA Jetson devices, and various ARM-based edge computing modules. It manages architecture-specific details including shader compilation (targeting Vulkan), asset cooking flavors, and the generation of appropriate binary formats. By utilizing this module, developers can eliminate the complexity of manually configuring cross-compilation toolchains when targeting high-performance ARM servers or embedded systems.

Practical Usage Tips and Best Practices
Configure the Cross-Compile Toolchain
To use this module from a Windows host, you must install the specific “Linux ARM64” cross-compilation toolchain provided by Epic Games. Setting the LINUX_MULTIARCH_ROOT environment variable correctly is the only way to eliminate “Platform not found” errors during the packaging process.
Target Vulkan for Rendering
Linux ARM64 typically relies on Vulkan for hardware-accelerated graphics. Within the project settings managed by this module, ensure that Vulkan Desktop or Vulkan Mobile is selected as the targeted RHI. This ensures the cooker generates the correct bytecode to eliminate rendering failures on ARM-based GPUs.
Optimize for Server-Side ARM (Graviton)
If you are packaging a dedicated server for ARM64 cloud instances, use the LinuxArm64Server target. This allows the engine to eliminate unnecessary graphical dependencies, resulting in a smaller binary footprint and lower memory overhead on the server.
Select Appropriate Texture Compression
ARM64 devices often prefer ASTC or ETC2 texture compression. Use the Multi-Cook flavors supported by this module to package textures in multiple formats. This allows the target device to select the most efficient format at runtime and helps you eliminate visual artifacts caused by incompatible compression.
Verify GLIBC Compatibility
Ensure your target Linux distribution meets the minimum glibc requirements (typically 2.28 or newer). Using a toolchain that matches your target OS version helps you eliminate “Version ‘GLIBC_X.XX’ not found” errors when trying to run the packaged binary on the device.
Use -ClientArchitecture=arm64 for UAT
When using the Unreal Automation Tool (RunUAT) to build via command line, explicitly pass -ClientArchitecture=arm64. This tells the module to bypass the default x86_64 logic and helps you eliminate accidental compilation of the wrong binary architecture.
Leverage Remote Debugging via GDB
Because you are often cross-compiling, use a remote GDB session to debug the ARM64 binary on the target hardware. This allows you to step through C++ code in real-time and eliminate the guesswork involved in diagnosing architecture-specific crashes.
Monitor Thermal Throttling on Edge Devices
For embedded ARM64 hardware (like the Jetson), monitor the GPU/CPU clock speeds using the engine’s stat commands. High-fidelity Unreal projects can quickly reach thermal limits; adjusting the scalability settings within this module’s configuration helps you eliminate performance drops caused by hardware throttling.