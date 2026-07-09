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

provides the standardized data structures and logic for platform-specific audio overrides. It acts as the “translator” between the high-level audio settings defined in the Unreal Editor and the specific .ini configuration files (like AndroidEngine.ini, WindowsEngine.ini, etc.) used during the cook and build process.

Its primary purpose is to allow developers to define unique audio constraints—such as maximum voice counts, compression qualities, and stream caching limits—for different hardware tiers without altering the core project-wide audio logic.

Practical Usage Tips and Best Practices
Override Max Channels per Platform
Use this module’s settings to “eliminate” CPU bottlenecks on mobile devices by lowering the Max Channels. While a PC might handle 64 or 128 concurrent voices, setting an Android or Switch target to 32 or lower ensures that the audio thread does not starve the game thread during intense combat or “elimination” sequences.
Leverage Audio Stream Caching
Enable Stream Caching within the platform-specific cook overrides managed by this module. This allows the engine to load only the beginning of a sound into memory, streaming the rest from disk as needed. This is essential for “eliminating” out-of-memory (OOM) crashes on consoles with limited RAM.
Configure Quality Level Scalability
The module allows you to map specific “Quality Levels” to different platforms. You can define a “Low” quality setting for older mobile devices that uses aggressive compression and a “Cinematic” quality for high-end PCs that uses uncompressed PCM or high-bitrate Ogg Vorbis.
Set Sample Rate for Hardware Native Alignment
Align your platform’s Sample Rate (e.g., 48000Hz vs 44100Hz) with the native hardware rate through this module. Matching the hardware’s native rate “eliminates” the CPU cost of real-time resampling, which is particularly beneficial for preserving battery life on mobile targets.
Use Compression Overrides for Package Size
If your project’s disk footprint is too large, use the Compression Quality slider in the platform audio settings. Lowering this value for mobile platforms can drastically reduce the size of your .pak or .obb files without requiring you to re-import every source .wav file.
Filter Random Nodes via Branch Culling
In the platform settings, use the Random Branch Limit to “eliminate” memory waste in Sound Cues. This tells the cook process to only include a specific number of random variations for a sound (like footstep variations) on that platform, saving significant storage space on smaller builds.
Standardize DSP for Performance
Use the module to disable expensive spatialization or reverb plugins on lower-end platforms. You can set the Spatialization Plugin to “Built-In” for mobile while using high-fidelity third-party plugins for PC/Console, ensuring a smooth frame rate across all devices.
Access via C++ for Custom Cook Rules
If you are building a custom build pipeline, you can access these settings via the FAudioPlatformSettings struct. This allows you to programmatically verify that “elimination” sound effects are always set to the highest priority before a build is finalized.