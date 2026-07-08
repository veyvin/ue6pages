---
layout: default
title: nvEncode
---

<!-- ai-generation-failed -->

<h1>nvEncode</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/nvEncode/nvEncode.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

vides a wrapper for the NVIDIA Video Codec SDK. It enables the engine to utilize dedicated hardware-accelerated video encoding (NVENC) found on NVIDIA GPUs. By offloading video compression from the CPU to the GPU’s dedicated encoding chips, it allows for high-quality, real-time video capture and streaming with minimal impact on game performance.

This module is primarily used by Pixel Streaming, the Movie Render Queue (MRQ), and the Replay system to generate H.264, HEVC (H.265), or AV1 bitstreams. Its implementation facilitates the elimination of CPU bottlenecks during high-resolution video output, making it essential for cloud gaming and virtual production.

Practical Usage Tips and Best Practices
1. Verify Hardware and Driver Requirements

To utilize this module, the host machine must have a supported NVIDIA GPU (Kepler architecture or newer). Always ensure the latest Production Branch or Studio Drivers are installed. This practice leads to the elimination of “Encoder failed to initialize” errors that occur with outdated or generic display drivers.

2. Configure for Pixel Streaming

When using the Pixel Streaming plugin, the NVEncode module is often the default choice for Windows-based NVIDIA servers. Use the command-line argument -PixelStreamingEncoderCodec=H264 to explicitly target NVENC. This setup assists in the elimination of latency by leveraging the GPU’s fixed-function hardware instead of software-based encoding.

3. Optimize with h264_nvenc in Movie Render Queue

If you are exporting videos via the Command Line Encoder in MRQ, specify h264_nvenc as your video codec. This facilitates the elimination of long render times for video files, as the GPU can encode frames significantly faster than standard CPU encoders like libx264.

4. Balance Latency vs. Quality via Rate Control

For interactive applications like cloud gaming, set the rate control to CBR (Constant Bit Rate) or Low Latency. This configuration leads to the elimination of “stuttering” or “hitching” in the stream caused by sudden spikes in network bandwidth requirements during complex high-motion scenes.

5. Be Aware of Max Encoding Sessions

Consumer-grade NVIDIA GeForce GPUs have a strict limit on the number of simultaneous encoding sessions (often 3 to 5). If your project requires “Multi-tenancy” (multiple engine instances on one GPU), moving to NVIDIA RTX (Quadro) or Tesla GPUs facilitates the elimination of these session limits, allowing for more concurrent streams.

6. Leverage AV1 for Superior Bitrates

On newer NVIDIA hardware (Ada Lovelace architecture and later), the NVEncode module supports AV1 encoding. Switching to AV1 leads to the elimination of blocky artifacts at lower bitrates, providing significantly higher visual fidelity compared to H.264 at the same bandwidth.

7. Use Coupled Mode for Critical Latency

By default, Pixel Streaming and NVEncode work in “Coupled” mode, where the streamer attempts to match the engine’s frame rate. This leads to the elimination of input lag, as the frame is encoded and sent immediately after being rendered, rather than waiting for a separate encoding clock.

8. Monitor via Console Commands

Use the console command Stat PixelStreaming or Stat GPU to monitor the encoding overhead. Seeing the “Encoder Latency” in milliseconds assists in the elimination of performance guesswork, allowing you to downscale resolution or adjust bitrate if the hardware encoder becomes saturated.