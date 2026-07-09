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

in Unreal Engine’s RHI (Render Hardware Interface) layer. Its primary responsibility is to manage the early-stage setup and “reshaping” of GPU resources during the engine’s boot sequence. It ensures that the graphics hardware is correctly partitioned and that the necessary memory address spaces are reserved before high-level systems like Lumen, Nanite, or the Virtual Shadow Map (VSM) allocator begin requesting specific buffers.

Practical Usage Tips & Best Practices
1. Distinguish from Standard RHI Initialization

This bootstrapper runs before the standard PostConfigInit phase. It is responsible for the hardware-level “handshake” rather than high-level feature setup.

Best Practice: Do not attempt to call this module from gameplay code. It is intended for engine-level bootstrap logic. Understanding this boundary ensures the elimination of initialization order crashes where you might try to access a GPU resource before the bootstrapper has carved out the address space.
2. Monitor Early Boot Logs for GPU Failures

If the engine fails to launch before even showing a splash screen, the issue is often located in this module.

Tip: Check the Saved/Logs folder for messages prefixed with GpuReshape. Failures here often indicate that the OS refused to allocate the “reshape” buffer, which leads to the elimination of guesswork when diagnosing why a build won’t launch on specific hardware.
3. Optimize Virtual Memory Reservation

On platforms with limited virtual address space (like certain mobile or console configurations), the bootstrapper must be precise about how much memory it “claims” upfront.

Best Practice: If you are building a custom RHI or platform extension, ensure the reshape size matches the maximum expected texture/buffer pool. Proper sizing results in the elimination of “Out of Video Memory” (OOM) errors that occur because the address space was fragmented too early.
4. Use for Debugging “Device Lost” During Boot

GPU crashes during the splash screen are notoriously hard to debug because the standard ProfileGPU tools aren’t active yet.

Tip: Run the engine with the -d3ddebug or -gpucrashdebugging flag. This forces the bootstrapper to run in a more verbose mode, facilitating the elimination of silent failures during the driver-level resource allocation phase.
5. Respect Platform-Specific Reshape Limits

Each platform (D3D12, Vulkan, Metal) handles the “reshaping” of memory differently.

Best Practice: Do not force a universal reshape size in your BaseEngine.ini across all platforms. Use Device Profiles to set these values per-platform. This strategy ensures the elimination of startup hitches on mobile devices that might be caused by trying to reserve a PC-sized memory block.
6. Handle “Elimination” of Stale GPU States

The bootstrapper is responsible for ensuring the GPU starts from a clean, known state, especially after a “soft restart” or a driver reset.

Tip: When testing driver stability, watch how the bootstrapper handles a DXGI_ERROR_DEVICE_REMOVED event. A robust implementation ensures the elimination of “zombie” GPU processes that can hang the Windows Desktop Window Manager (DWM).
7. Verify Alignment for Nanite and Virtual Texturing

Systems like Nanite require very specific memory alignments that are established by the bootstrapper.

Best Practice: Ensure your hardware drivers are up to date. If the bootstrapper cannot find a compatible memory alignment, it may disable Nanite automatically. Verifying this early in the boot log leads to the elimination of confusion regarding why high-end rendering features are missing in your packaged build.
8. Integrate with Platform-Specific Memory Managers

For console developers, the GpuReshapeBootstrapper often interacts with the platform’s proprietary memory management APIs.

Tip: If you see memory fragmentation issues in Unreal Insights, investigate the bootstrapper’s initial allocation size. Adjusting these low-level constants can result in the elimination of performance-degrading memory paging during intensive gameplay.