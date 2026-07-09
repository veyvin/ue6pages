---
layout: default
title: AudioFormatBink
---

<!-- ai-generation-failed -->

<h1>AudioFormatBink</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioFormatBink/AudioFormatBink.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ink Media plugin within Unreal Engine. It provides the engine with the ability to decode and play back high-performance compressed audio tracks encoded with the Bink Audio codec.

This module is primarily used in conjunction with Bink Video (.bk2 files) to handle complex audio configurations, such as multi-language tracks and 5.1⁄7.1 surround sound, which are common in pre-rendered cinematics. It is highly optimized for performance, allowing for software-based decompression with very low CPU overhead across all platforms.

Practical Usage Tips and Best Practices
Prioritize for Cinematics and Startup Movies
Bink Audio is the engine’s preferred choice for fullscreen pre-rendered movies. Because it uses an efficient software decoder, it “eliminates” the common compatibility issues found with hardware-dependent codecs like H.264/AAC, especially during the early initialization phases of the engine.
Utilize Language Overrides for Localized Audio
The module supports a “Language Override” feature. You can encode multiple audio tracks into a single Bink file and use the Bink Sound Track settings in the Project Settings to swap between them at runtime. This allows you to “eliminate” the need for separate video files for every supported language.
Configure Surround Sound via Filename Suffixes
The AudioFormatBink logic can automatically detect speaker configurations based on file naming. If your movie file ends in _51 or _71, the module will automatically route the six or eight mono tracks to the correct surround sound channels without manual configuration.
Adjust Bitrate for Mobile Platforms
While Bink is efficient, high-bitrate multi-channel audio can still impact performance on low-end mobile devices. When encoding your files using the Bink Video Tool (Bink2ForUnreal.exe), aim for the lowest acceptable bitrate to “eliminate” potential audio stuttering on older hardware.
Check Module Dependencies in C++
If you are building a custom media player or cinematic tool, ensure that the BinkMediaPlayer and its associated audio modules are enabled. In your Build.cs, you typically depend on the higher-level media modules which utilize AudioFormatBink internally.
Verify Playback via the Bink Media Player Asset
When importing a Bink file, always open the Bink Media Player asset and check the “Audio” tab. This confirms that the AudioFormatBink module has correctly parsed the tracks. If the track list is empty, the audio may have been encoded with an unsupported sample rate or bit depth.
Synchronize Audio with Video Seek
Because Bink Audio is tightly interleaved with video frames, seeking to a specific timestamp is much faster and more accurate than other formats. Use this to your advantage when creating interactive “elimination” replays or branching cinematic sequences where the player might skip segments.
Avoid Overlap with Standard Audio Engine
Bink Audio typically bypasses the standard Unreal Audio Engine (MetaSounds/Sound Cues) and plays directly to the system output. If you need to apply real-time reverb or spatialization to a cinematic’s audio, you may need to route the Bink audio through a specialized Submix if supported by your version of the Bink plugin.