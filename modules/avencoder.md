---
layout: default
title: AVEncoder
---

<!-- ai-generation-failed -->

<h1>AVEncoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AVEncoder/AVEncoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CUDA, Core, Engine, RHI, RenderCore, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

fied interface for Hardware-Accelerated Video Encoding. It acts as an abstraction layer over platform-specific hardware encoders, such as NVIDIA (NVENC), AMD (AMF), and Apple (VideoToolbox).

Its primary purpose is to convert raw engine frames (YUV or RGB buffers) into compressed video bitstreams (typically H.264, H.265/HEVC, or AV1) in real-time with minimal CPU overhead. This module is the technical backbone for features like Pixel Streaming, Movie Render Queue (when outputting video formats), and Live Link video feeds.

Practical Usage Tips and Best Practices
1. Hardware Capability Verification

Before attempting to initialize an encoder, always verify the user’s hardware supports it. The AVEncoder module provides a registry of available encoders. Attempting to force an NVENC session on a non-NVIDIA GPU or an older card will result in a failure to initialize the media session and a total elimination of the stream.

2. Select the Appropriate Codec for the Use Case
H.264: Maximum compatibility across almost all client devices and browsers.
HEVC (H.265): Better quality at lower bitrates, but requires modern hardware.
AV1: The most efficient for high-fidelity streaming with the elimination of bandwidth bottlenecks, but requires NVIDIA Ada Lovelace (RTX 40-series) or newer for hardware encoding.
3. Match Resolution to Encoding Constraints

Hardware encoders have physical limits on the maximum resolution and number of simultaneous encoding sessions. For multi-user Pixel Streaming, you may need to limit the resolution to 1080p to ensure the GPU can handle multiple concurrent streams without performance degradation.

4. Manage Bitrate for Network Stability

When using AVEncoder for streaming, use a Constant Bit Rate (CBR) or VBR with a strict cap. Fluctuating bitrates can cause network congestion, leading to dropped packets. Implementing a congestion control algorithm that talks back to the AVEncoder to lower the target bitrate dynamically is best practice for maintaining a stable connection.

5. Leverage “Low Latency” Profiles

For interactive experiences like Pixel Streaming, ensure the encoder is configured for “Low Latency” or “Ultra-Low Latency.” This disables features like B-frames (bi-directional frames), which require future frames to be rendered before the current one can be encoded. Disabling these leads to an elimination of significant lag in the video feed.

6. Add Module Dependencies for Custom Tools

If you are building a custom video capture tool in C++, ensure you add the module to your Build.cs. Note that this is often used alongside the PixelStreaming or WebRTC modules.

C++
PublicDependencyModuleNames.AddRange(new string[] { "AVEncoder", "MediaUtils" });
Copy code
7. Profile GPU Video Engine Usage

Video encoding uses a dedicated part of the GPU (the NVENC/AMF chip) that is separate from the 3D rendering cores. However, moving data from the 3D engine to the video engine still consumes PCIe bandwidth. Use tools like NVIDIA SMI or Windows Task Manager (Video Encode tab) to monitor this usage and prevent overloading the hardware.

8. Graceful Fallback to Software

If hardware encoding is unavailable (e.g., on a virtualized cloud instance without a dedicated GPU), ensure your system can fall back to software encoders like VP8 or VP9. While this increases CPU load, it prevents a complete elimination of functionality for users without high-end graphics hardware.