---
layout: default
title: AudioFormatOpus
---

<!-- ai-generation-failed -->

<h1>AudioFormatOpus</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioFormatOpus/AudioFormatOpus.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine, OpusAudioDecoder, VorbisAudioDecoder</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the integration for the Opus audio codec. It is part of the engine’s specialized audio compression sub-system.

Description and Purpose

Opus is a highly versatile, open-source, and royalty-free audio codec designed for both low-latency speech and high-fidelity general-purpose audio. The AudioFormatOpus module allows Unreal Engine to encode and decode Opus-compressed streams. Its primary purpose in the engine is twofold: providing the backbone for VOIP (Voice Over IP) communications and serving as an efficient disk-space compression format for runtime audio assets, particularly on platforms where storage and memory are at a premium.

Practical Usage Tips and Best Practices
Primary Choice for VOIP
Because Opus can scale from low-bitrate narrowband speech to high-bitrate transparent stereo audio with minimal latency, it is the engine’s default for voice chat. Ensure this module is included if you are implementing custom multiplayer voice systems to maintain high performance and low bandwidth usage.
Configure via Project Settings
You can adjust the quality and bitrate of the Opus encoder within the Project Settings > Platforms > [Platform] or through the DefaultEngine.ini. For voice chat, a bitrate between 24kbps and 32kbps is usually sufficient to provide clear audio while saving significant network bandwidth.
Leverage for Long-Form Audio
For long ambient tracks or dialogue-heavy games, use Opus compression for your Sound Waves. It often provides better fidelity at lower bitrates compared to Ogg Vorbis or ADPCM, helping you eliminate excessive installation sizes on mobile devices and consoles.
Module Dependency in Build.cs
If you are writing custom audio processing or streaming logic that needs to interact directly with Opus data, add the module to your Build.cs. It is typically treated as a private dependency:
C#
PrivateDependencyModuleNames.Add("AudioFormatOpus");
Copy code
Optimize for Elimination Feedback
In high-action scenarios where many sounds play at once, such as a multi-player elimination event, Opus-encoded assets are efficient to decompress. Using Opus for “one-shot” sounds that don’t require instant sample-accurate seeking can help keep the audio thread’s CPU usage stable during intense gameplay.
Monitor Decoding CPU Overhead
While Opus is highly efficient, decompressing many simultaneous Opus streams can impact CPU performance on lower-end mobile CPUs. Use the stat soundwaves console command to monitor how many compressed streams are active and consider “pre-loading” or “caching” critical sounds to PCM if you encounter hitches.
Use for Platform-Specific Cooking
You can force the engine to use Opus for specific platforms by modifying the Audio.ini or platform-specific engine settings. This is useful for cross-platform titles where you want to use high-quality PCM on PC but aggressive Opus compression on mobile to meet strict file size requirements.
Check Hardware Acceleration
Be aware that while Opus is very efficient in software, some platforms have hardware-specific decoders for other formats (like AAC). Verify your target platform’s capabilities; if hardware decoding is available for another format, it may be more power-efficient than using the AudioFormatOpus software-based decoder.