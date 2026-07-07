---
layout: default
title: AudioPlatformConfiguration
---

<!-- ai-generation-failed -->

<h1>AudioPlatformConfiguration</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioPlatformConfiguration/AudioPlatformConfiguration.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nsible for managing platform-specific audio settings and hardware capabilities. It serves as the data bridge between the high-level Unreal Audio Engine and the specific constraints of the target hardware (PC, Console, or Mobile).

This module defines how audio should be cooked, compressed, and allocated for different platforms. It is the underlying logic that processes the settings found in Project Settings > Platforms > [Platform Name] > Audio, ensuring that the engine respects the memory and CPU limits of the device.

Practical Usage Tips and Best Practices
1. Optimize Max Channels per Platform

The module uses the Max Channels setting to determine how many simultaneous “voices” the engine will calculate.

Best Practice: Set lower values for mobile devices (e.g., 32) and higher for high-end PCs or consoles (e.g., 64 or 128). This helps eliminate CPU spikes caused by excessive concurrent sound calculations on weaker hardware.
2. Leverage Compression Overrides

Different platforms have different strengths regarding audio decoding.

Tip: Use the Compression Overrides section to specify different quality levels for different platforms. For example, you can set a higher compression ratio for mobile to save disc space while keeping high-fidelity audio on PC.
3. Coordinate Stream Caching

This module manages the configuration for Audio Stream Caching, which determines how much audio is kept in memory versus streamed from the disk.

Best Practice: Tune the Max Cache Size based on the available RAM of your target platform. Proper configuration will eliminate “out of memory” crashes caused by loading too many uncompressed .wav files into the resident memory.
4. Configure Source Workers

In the platform settings, you can define the number of Source Workers. This allows the audio engine to offload DSP processing to multiple CPU cores.

Tip: For modern multi-core consoles, increasing the number of source workers can significantly improve the performance of complex MetaSounds and real-time effects by distributing the workload.
5. Match Sample Rates to Eliminate Resampling

The module handles the target sample rate for the audio mixer.

Best Practice: Ensure your Project Settings match the native hardware sample rate (usually 48,000 Hz). This prevents the engine from performing a per-frame software resample, which can eliminate unnecessary CPU overhead.
6. Use Quality Levels to Scale Performance

You can define multiple quality levels within the platform configuration.

Tip: Link these quality levels to your game’s “Low/Medium/High” audio settings menu. This allows the player to manually eliminate expensive reverb or high-voice-count processing if they are running on an older machine.
7. Set ‘Override Compression Times’ for Faster Loads

There is a setting to determine at what duration a sound should be fully decompressed on load versus streamed.

Best Practice: For short, frequently used sounds (like UI clicks or footstep variations), set them to decompress on load. This eliminate the slight latency “pop” that can occur when the engine tries to stream a very short file from a slow hard drive.
8. Validate via Cooker Statistics

When you package your project, the AudioPlatformConfiguration settings determine the final size of your audio assets.

Tip: Check the Project/Saved/Logs after a cook to see the “Audio Cooker” output. If your audio size is too large, use this module’s settings to increase the compression of specific sound groups, helping to eliminate bloated package sizes.