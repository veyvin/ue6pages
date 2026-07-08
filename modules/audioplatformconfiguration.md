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

real Engine designed to handle the per-platform serialization and management of audio settings. It provides the data structures and logic required to define how audio behaves differently across various target hardware, such as PC, consoles, and mobile devices.

This module is responsible for the “Cook Overrides” and “Compression Overrides” systems. It ensures that when you package your game, the audio assets are compressed and optimized specifically for the target platform’s memory and CPU constraints without requiring you to manually duplicate assets.

Practical Usage Tips and Best Practices
Implement Platform-Specific Max Channels Use the settings provided by this module to “eliminate” CPU bottlenecks on mobile by capping the Max Channels. While a high-end PC might handle 128 simultaneous voices, you should often limit Android or iOS devices to 32 or 24 to preserve processing power for gameplay logic.
Configure Quality Compression Overrides Instead of manually setting the quality for every SoundWave, use this module’s ability to set a Global Compression Quality scale. For example, you can set a scale of 0.5 for mobile platforms to “eliminate” unnecessary file size bloat while keeping high-fidelity audio for the PC build.
Utilize Override Compression Times For mobile platforms, use the Override Compression Times setting to define a duration threshold (e.g., 5 seconds). Any sound shorter than this will be fully decompressed on load. This is a best practice to “eliminate” the CPU hit of real-time decompression for frequent, short sounds like footsteps or UI clicks.
Standardize Stream Caching Enable Stream Caching via this module’s configuration for platforms with limited RAM. This allows the engine to load audio in small “chunks” rather than keeping the entire file in memory. This is the most effective way to “eliminate” Out Of Memory (OOM) crashes on memory-constrained devices.
Target Native Sample Rates Configure the Sample Rate settings to match the native hardware of your primary target platform. If the hardware runs at 48kHz, setting your configuration to 48kHz will “eliminate” the need for the engine to perform software resampling, saving valuable CPU cycles.
Cull Sound Cue Branches Use the Max Random Branches setting in the platform configuration to “eliminate” memory waste. On consoles or mobile, you can limit a Random Node in a Sound Cue to only preload a subset of its variations, ensuring that memory isn’t consumed by audio clips that might never be played.
Manage Audio Thread Priority For platforms prone to hitching (like mobile), ensure the Audio Worker Thread count is configured correctly. Providing enough workers ensures that audio calculations are not “eliminated” or delayed by the game thread, which prevents audible pops and stutters.
Automate via Device Profiles While AudioPlatformConfiguration handles the project-wide platform settings, you can further refine these using Device Profiles. This allows you to “eliminate” audio quality issues on specific low-end Android devices by overriding the values defined in this module for that specific hardware model.