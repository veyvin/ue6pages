---
layout: default
title: DX11Audio
---

<!-- ai-generation-failed -->

<h1>DX11Audio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/DX11/DX11Audio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">DirectX</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

is the Windows-specific audio backend for Unreal Engine. It serves as the hardware-abstraction layer that allows the Unreal Audio Engine to communicate with the Windows XAudio2 API to output sound to speakers and headphones.

What it is and What it’s used for

On Windows, Unreal Engine does not talk directly to your sound card. Instead, it uses the DX11Audio/XAudio2 module to hand off processed digital audio buffers to the operating system. This module is responsible for the final “render” pass of audio—taking the mixed sounds from MetaSounds or Sound Cues and sending them to the hardware.

Primary uses include:

Hardware Interface: Mapping Unreal’s internal audio channels to physical Windows output devices (Stereo, 5.1, 7.1).
Sample Rate Conversion: Ensuring the engine’s internal sample rate (typically 48kHz) matches the Windows playback device settings.
Device Management: Handling “hot-swapping” when a user plugs in a headset or changes the default playback device in Windows.
Low-Level Buffering: Managing the timing and latency of audio callbacks to prevent pops, clicks, or stuttering.
Practical Usage Tips and Best Practices
1. Configure Platform Headroom

Because this module interfaces with Windows XAudio2, it is susceptible to digital clipping if too many sounds play at once. In your WindowsEngine.ini, use the PlatformHeadroomDB setting (typically -3dB or -6dB). This provides a “safety gap” that prevents the final mix from distorting when hitting the Windows hardware limit.

2. Monitor for Audio Thread Starvation

If you hear “popping” or “crackling,” it often means the DX11Audio module is waiting too long for the engine to provide audio data. Use the console command stat audio and look for “Audio Callback Time.” If this value is inconsistent, it indicates that game thread hitches are starving the audio buffer.

3. Adjust Callback Buffer Sizes

For low-latency applications (like rhythm games), you can tune the buffer sizes in the Project Settings > Platforms > Windows > Audio.

Callback Buffer Size: Lowering this (e.g., to 256 or 512) reduces latency but increases the risk of underruns (crackling).
Number of Buffers To Enqueue: Increasing this provides a larger “safety net” for variable CPU performance at the cost of higher latency.
4. Handle Device Swapping Gracefully

In older versions of Unreal, switching audio devices (like unplugging headphones) could cause a deadlock or crash. Ensure you are using UE 5.0+ where the XAudio2 implementation has been modernized to handle device migration. If you encounter issues, verify that your Windows sound drivers are updated to support XAudio 2.9.

5. Use “Stat SoundWaves” to Audit Memory

Since this module manages the final playback buffers, use stat soundwaves to see which assets are currently resident in the audio memory managed by the DX11Audio backend. This helps identify massive uncompressed files that might be bloating your Windows memory footprint.

6. Optimize Source Worker Threads

The Windows audio backend can offload source processing to multiple CPU threads. In the Windows platform settings, set Number of Source Workers to match your target hardware (e.g., 4 for mid-range PCs). This parallelizes the audio decoding before the DX11Audio module performs the final mix.

7. Verify Spatialization Plugin Compatibility

If you are using 3rd-party spatializers (like Dolby Atmos or Oculus Audio), they must be compatible with the XAudio2 backend. Ensure your chosen spatialization plugin is selected in the Windows Audio settings to ensure the DX11Audio module correctly routes the 3D positioning data.

8. Strategic Elimination of Device Latency

If players report “audio lag” on Windows, check the Max Channels setting. Pushing too many voices (e.g., 128+) through the XAudio2 renderer on low-end CPUs can cause the module to fall behind. Capping your Max Channels to a reasonable number (32 or 64) for lower-tier Windows hardware ensures a snappy, synchronized audio experience.