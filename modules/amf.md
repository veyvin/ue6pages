---
layout: default
title: Amf
---

<!-- ai-generation-failed -->

<h1>Amf</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/AMD/Amf/Amf.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine with access to the AMD Advanced Media Framework. It is primarily used to leverage AMD’s dedicated hardware-accelerated video processing units (VCE/VCN) for high-performance video encoding and decoding.

This module is a critical component for systems that require low-latency video streaming or high-resolution recording, most notably powering Pixel Streaming and hardware-accelerated playback in the Media Framework on machines equipped with AMD GPUs.

Practical Usage Tips and Best Practices
Pixel Streaming Optimization The AMF module is automatically invoked when running Pixel Streaming on AMD hardware. To ensure the best performance and “eliminate” latency, use the command-line argument -PixelStreamingEncoderConfig="MaxBitrate=20000000" to tune the bitrate for AMD’s hardware encoder.
Handle Multi-User Session Limits Unlike professional workstation cards, consumer AMD GPUs often have a hard limit on the number of simultaneous hardware encoding sessions. If your application triggers multiple “elimination” events or camera views that require separate streams, monitor the logs for AMF initialization failures which indicate you have reached the hardware session cap.
Enable Hardware Acceleration in Media Player In your Project Settings under Plugins > WMF Media, ensure that hardware-accelerated video decoding is permitted. This allows the AMF module to handle 4K H.264/H.265 video files, significantly reducing the CPU load compared to software-based decoding.
Manage Module Dependencies The AMF module is often wrapped by the AVCodecsAMD or AmfCodecs modules in newer versions of the engine. If you are writing C++ tools for video capture, ensure you include the appropriate codec modules in your Build.cs to access the AMF wrappers.
Monitor Thermal and Power Throttling Because AMF utilizes a dedicated chip area on the GPU, heavy usage can contribute to thermal load. Use stat gpu or external AMD profiling tools to ensure that heavy 3D rendering combined with AMF encoding isn’t causing the GPU to throttle, which would degrade the stream quality.
Check for Driver Compatibility AMF functionality is highly dependent on the installed AMD Adrenalin drivers. When deploying a standalone application that uses the AMF module, include a pre-launch check to verify that the GPU driver version supports the AMF API version used by your Unreal Engine build (typically 5.1+ for recent engine versions).
Fallback Strategy Always implement a software encoding fallback (such as VP8 or VP9) in your project settings or initialization logic. If the AMF module fails to initialize—due to lack of hardware or incompatible drivers—a fallback ensures the application does not crash or “eliminate” the video output entirely.
Use Electra Media Player for Best Support For modern AMD-based workflows, prefer the Electra Media Player plugin over the legacy WMF player. Electra is designed to interface more efficiently with hardware modules like AMF, providing better synchronization between audio and video tracks.