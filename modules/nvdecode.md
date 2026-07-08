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

Engine that integrates the NVIDIA Video Codec SDK (specifically NVDEC). It provides a high-performance path for decoding compressed video streams (such as H.264 and HEVC/H.265) directly on the GPU’s dedicated hardware decoder.

In Unreal Engine, this module is primarily utilized by the Electra Media Player and the WMF (Windows Media Foundation) media player plugins. By offloading the heavy computational task of video decompression from the CPU to the NVIDIA GPU, it helps you eliminate CPU bottlenecks, allowing for the playback of high-resolution 4K or 8K video alongside complex game logic without dropping frames.

Practical Usage Tips and Best Practices
Enable Hardware Acceleration in Media Player
To leverage this module, you must ensure that “Hardware Accelerated Video Decoding” is enabled in your Media Player settings or the Electra Player plugin configuration. Using the GPU’s dedicated silicon for decoding helps you eliminate “stuttering” in high-bitrate cinematics.
Verify NVIDIA Driver Version
Because this module relies on specific entry points in the NVIDIA driver, ensure your target hardware has updated drivers. Older drivers may lack support for newer HEVC profiles; keeping them current helps you eliminate decoding errors or “black screen” issues during video playback.
Monitor VRAM Usage for Multiple Streams
NVDEC uses a portion of the GPU’s video memory (VRAM) for frame buffers. If you are playing back multiple high-resolution videos simultaneously (e.g., in a security camera room scene), monitor your VRAM usage. Proper management helps you eliminate crashes caused by exceeding the GPU’s memory limits.
Use Supported Codec Profiles
The NVDecode module is highly efficient with standard H.264 (AVC) and H.265 (HEVC) profiles. Avoid using “High” profiles with non-standard bit depths (like 12-bit) unless the specific hardware supports it. Sticking to 8-bit or 10-bit standard profiles helps you eliminate compatibility issues across different NVIDIA card generations.
Optimize for 4K/8K Playback
If your project features a “Movie Theatre” or massive screens, the NVDecode module is essential. It can handle 8K streams that would typically cause a 100% CPU load. Using this module allows you to eliminate the need for pre-rendered frames or lower-quality proxies for your largest textures.
Check for DirectX 12 Compatibility
When using modern RHI (Rendering Hardware Interface) settings like DX12, ensure your Media Player is set to use the “Electra” player, which interfaces well with the NVDecode backend. This ensures the decoded texture is shared efficiently with the renderer, helping you eliminate the latency of copying data from the GPU to the CPU and back.
Handle Fallback Scenarios
Not all users will have an NVIDIA GPU (e.g., AMD or Intel users). Always ensure you have a software decoding fallback or an alternative player configuration. Testing on non-NVIDIA hardware helps you eliminate “Missing Codec” errors for a portion of your player base.
Clean Up Media Resources on Elimination
When a video finishes or the Actor containing the Media Plate is destroyed (the “elimination” of the media instance), ensure you call Close on the Media Player. This signals the NVDecode module to release the hardware decoder session, which helps you eliminate “Resource Busy” errors when attempting to start the next video.