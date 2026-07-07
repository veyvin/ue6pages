---
layout: default
title: nvDecode
---

<!-- ai-generation-failed -->

<h1>nvDecode</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/nvDecode/nvDecode.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

NVDEC) within Unreal Engine. It provides a dedicated hardware-accelerated path for decoding video streams directly on NVIDIA GPUs.

While general media playback often uses the CPU or generic Windows Media Foundation (WMF) paths, the nvdecode module allows the engine to offload the heavy lifting of decompressing high-resolution video (H.264, HEVC/H.265) to the GPU’s dedicated SIP blocks. This is particularly critical for applications involving high-bitrate video textures, real-time 360-degree video, and the Pixel Streaming infrastructure.

Practical Usage Tips and Best Practices
1. Hardware Requirements and Fallbacks

The nvdecode module requires an NVIDIA GPU that supports hardware decoding.

Best Practice: Always implement a software-based fallback (like the Electra player or WMF) in your project. If a user runs your application on an AMD or Intel GPU, the nvdecode module will be unavailable; having a fallback helps you eliminate the risk of a “black screen” or application crash.
2. Enable via Plugin and Build Configuration

This module is usually leveraged through the NVIDIA Video Codec SDK plugin.

Action: Ensure the plugin is enabled in your .uproject file. If you are working in C++, add "NVDecode" to your PrivateDependencyModuleNames in the *.Build.cs file. This ensures the engine correctly links against the necessary .dll or .so files, eliminating linker errors during the build process.
3. Optimize for 4K and 8K Playback

Software decoding of 8K video can easily overwhelm even high-end CPUs, causing the game’s frame rate to tank.

Tip: Use nvdecode for high-resolution video textures. Because the decoding happens on a dedicated chip on the GPU, it leaves the CPU free to handle gameplay logic and the GPU’s CUDA cores free for rendering, effectively eliminating performance hitches during playback.
4. Minimize CPU-to-GPU Memory Transfers

One of the main advantages of nvdecode is that decoded frames can stay in GPU memory.

Best Practice: Use the MediaTexture system to ensure that decoded frames are passed directly as GPU resources rather than being copied back to system RAM. Keeping the data on the GPU helps you eliminate the massive bandwidth bottleneck associated with “Read-Back” operations.
5. Leverage for Pixel Streaming

The nvdecode module is a key component for the receiving end of low-latency video streams in high-performance setups.

Action: When using Pixel Streaming, ensure your server-side environment has the latest NVIDIA drivers installed. Proper driver support allows the nvdecode module to handle incoming streams with sub-millisecond latency, which helps you eliminate input lag for the end-user.
6. Handle Color Space in Shaders

NVDEC often outputs data in specialized YUV formats (like NV12) to save bandwidth.

Tip: When writing custom shaders to display video decoded via nvdecode, ensure you are using the correct YUV-to-RGB conversion matrix. Using the GPU to handle this conversion in the pixel shader helps you eliminate the heavy CPU cost of color-space conversion.
7. Monitor GPU Video Engine Load

Windows Task Manager and specialized profiling tools (like NVIDIA Nsight) can show “Video Decode” as a separate category.

Action: If your game is stuttering, check if the “Video Decode” graph is at 100%. If so, you may need to reduce the bitrate or resolution of your video files. Monitoring this specific metric helps you eliminate guesswork when profiling GPU-related performance issues.
8. Verify Supported Codec Profiles

Not every NVIDIA GPU supports every profile (e.g., 10-bit HEVC or AV1).

Best Practice: Check the NVIDIA Video Codec Support Matrix for your target hardware. If you target older GPUs, stick to 8-bit H.264. Choosing a widely supported profile helps you eliminate compatibility issues across different generations of NVIDIA hardware.