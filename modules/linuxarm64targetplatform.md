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

nreal Engine to target the AArch64 (ARM 64-bit) architecture on Linux. While the standard Linux module handles x86_64 (Intel/AMD) systems, this specific module provides the settings, cook flavors, and deployment logic required for ARM-based hardware. It is the primary gateway for developing and packaging projects for ARM64 servers (like AWS Graviton), embedded Linux devices, and high-performance ARM workstations.

Practical Usage Tips & Best Practices
1. Configure the Cross-Compilation Toolchain

Since most developers work on Windows, you must install the specific “Multi-arch” Linux Cross-Compile Toolchain provided by Epic.

Best Practice: Ensure your LINUX_MULTIARCH_ROOT environment variable points to the correct version of the Clang toolchain. Setting this correctly ensures the elimination of “Platform not found” errors when attempting to package for Linux ARM64 from a Windows machine.
2. Select the Correct Cook Flavor (ASTC vs. DXT)

ARM-based hardware often uses different GPU architectures (like Mali or Adreno) compared to desktop NVIDIA/AMD cards.

Tip: Within the Project Settings, look for the Linux ARM64 section and choose the appropriate texture compression (e.g., ASTC or Multi). Utilizing the correct compression leads to the elimination of visual artifacts and significantly improves texture loading performance on mobile-derived ARM chipsets.
3. Optimize for AWS Graviton (Server-Side)

Many developers use Linux ARM64 for dedicated game servers to save on cloud costs.

Best Practice: When packaging a server build, select the LinuxArm64 target in the Project Launcher. This allows for the elimination of the higher overhead associated with x86_64 emulation and takes full advantage of the power-per-watt efficiency of ARM64 cloud instances.
4. Manage Architecture-Specific Dependencies

If your project uses third-party libraries (.so files), you must provide ARM64 versions of those binaries.

Tip: In your Build.cs, use Target.Architecture == "aarch64" to conditionally link the correct libraries. Proactive library management facilitates the elimination of linker errors that occur when the engine tries to bundle an x86_64 library into an ARM64 package.
5. Leverage Nanite and Lumen Considerations

While ARM64 hardware is becoming more powerful, not all Linux ARM64 devices support the latest SM6 features.

Best Practice: Test your rendering settings specifically on the target ARM hardware. If the device lacks hardware ray tracing, disabling these features for that specific platform results in the elimination of sub-par frame rates and GPU crashes.
6. Use Remote Deployment for Testing

Deploying to an ARM64 device (like a Raspberry Pi or an ARM Dev Kit) can be slow via manual file copying.

Tip: Use the Turnkey system or the “Device Manager” in Unreal to set up an SSH connection to your ARM64 target. This enables “Launch on Device” functionality, leading to the elimination of repetitive manual packaging and deployment steps.
7. Monitor Performance with Unreal Insights

ARM64 CPUs have different caching and execution characteristics than x86_64 CPUs.

Best Practice: Run Unreal Insights on your ARM64 target to identify bottlenecks. This specific data collection assists in the elimination of performance hitches that are unique to the ARM architecture’s memory model and branch prediction.
8. Verify glibc Compatibility

Linux ARM64 distributions vary widely in their glibc versions (e.g., Ubuntu vs. Alpine vs. Rocky Linux).

Tip: Use the Native Toolchain bundled with the engine whenever possible to compile against a fixed sysroot. This ensures the elimination of “version GLIBC_X.XX not found” errors when your packaged game is run on a different Linux distribution than the one it was built for.