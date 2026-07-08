---
layout: default
title: GPUDirect
---

<!-- ai-generation-failed -->

<h1>GPUDirect</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/GPUDirect/GPUDirect.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e’s Media IO and Virtual Production framework, specifically designed to leverage NVIDIA GPUDirect RDMA (Remote Direct Memory Access) technology. Its primary purpose is to allow high-bandwidth data—such as SMPTE 2110 video streams—to be transferred directly from a supported Network Interface Card (NIC) to the GPU’s memory, completely bypassing the CPU and system RAM.

This module is essential for high-fidelity virtual production environments (like LED volumes), facilitating the elimination of the latency and CPU bottlenecks traditionally caused by copying large video buffers through the system’s main memory.

Practical Usage Tips and Best Practices
1. Enable via Environment Variables

For the module to function with Rivermax and RDMA, you must set the system environment variable RIVERMAX_ENABLE_CUDA to 1. Without this, the engine will default to standard system memory copies, resulting in the elimination of the performance benefits provided by the GPUDirect path.

2. Verify Hardware Compatibility

GPUDirect RDMA requires specific enterprise-grade hardware, such as NVIDIA Mellanox ConnectX-6 or BlueField-2 NICs. Using consumer-grade networking hardware will lead to the elimination of GPUDirect support, as these devices lack the necessary peer-to-peer DMA capabilities.

3. Use for Single-Stream Performance

Currently, GPUDirect in Unreal Engine is highly optimized for single, high-bandwidth streams. If you are receiving multiple simultaneous streams, monitor performance closely, as there is a global CVAR (Rivermax.UseGPUDirect) that may need to be toggled if multi-stream synchronization issues occur. Managing this correctly assists in the elimination of frame jitter.

4. Configure PTP for Accurate Timing

In the Project Settings under Plugins - NVIDIA Rivermax, set the Time Source to PTP (Precision Time Protocol) when using a BlueField-2 card. This ensures the GPUDirect module aligns video frames with the grandmaster clock, leading to the elimination of tearing on LED walls.

5. Monitor CUDA External Memory Handles

When developing custom implementations using this module, ensure you are not leaking CUDA handles during deinitialization. A common pitfall is a memory leak in the video stream handoff; resolving these leaks is vital for the elimination of crashes during prolonged playback sessions.

6. Disable “Receivers Apply OCIO” for 10-bit Streams

When using GPUDirect to ingest 10-bit RGB or YUV422 streams, it is a best practice to disable the “Receivers Apply OCIO” feature in the media source settings. This facilitates the elimination of color clipping and ensures the raw 10-bit data reaches the GPU correctly for high-dynamic-range (HDR) processing.

7. Use Block on Reservation for Frame Locking

To ensure that the GPUDirect buffer is always ready for the next frame, set the Frame Locking mode to Block on Reservation. This forces the engine to synchronize its presentation rate with the incoming stream, aiding in the elimination of dropped frames in live broadcast scenarios.

8. Check Peer-to-Peer (P2P) Topology

Ensure that your NIC and GPU are connected to the same PCIe root complex (typically the same CPU socket). If the data must cross the QPI/UPI link between two different CPUs, the latency increases, which can lead to the elimination of the sub-frame latency advantages that GPUDirect is meant to provide.