---
layout: default
title: AudioFormatOgg
---

<!-- ai-generation-failed -->

<h1>AudioFormatOgg</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioFormatOgg/AudioFormatOgg.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine, VorbisAudioDecoder</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Ogg Vorbis audio codec. It provides the necessary logic to encode (during the cooking process) and decode (during runtime) audio assets using the Vorbis format. This module is essential for cross-platform audio compatibility, as Ogg Vorbis is a highly efficient, lossy compression format that offers a great balance between file size and audio fidelity.

It is primarily used to translate compressed Vorbis data from a project’s cooked content into raw PCM data that the Unreal Audio Mixer can process and play back.

Practical Usage Tips and Best Practices
1. Manual Targeting for Specific Platforms

While most platforms have a default codec, you can force a platform to use Ogg Vorbis for debugging purposes. In your platform’s TargetPlatform.cpp, you can set the return value of GetWaveFormat() to NAME_OGG to ensure the cooker uses this module for all audio assets.

2. Configure Quality vs. Size

The USoundWave asset has a Quality slider (1-100). For the Ogg Vorbis codec, this slider directly maps to the Vorbis bit-rate management. A setting of 40 is generally the “sweet spot” for high-fidelity game audio; setting it to 100 often provides diminishing returns while significantly increasing the memory footprint.

3. Use for Stream Caching

Ogg Vorbis is the primary format used when Audio Stream Caching is enabled. Because Vorbis is designed for seekable, packet-based streaming, this module allows the engine to load small “chunks” of audio data into memory on demand, which is critical for open-world games with massive audio libraries.

4. Leverage Seekable Decoding

Unlike some hardware-accelerated formats, the Ogg Vorbis implementation in Unreal is highly efficient at seeking. This makes it the preferred format for long ambient loops or music tracks where the game logic might need to jump to specific timestamps (e.g., dynamic music transitions).

5. Optimize CPU via Sample Rate

Decoding Ogg Vorbis is a CPU-intensive task compared to uncompressed PCM. To perform the elimination of unnecessary CPU overhead, ensure your source .wav files are imported at the same sample rate as your project’s output (usually 48kHz). This prevents the module from having to perform resampling and decoding simultaneously.

6. Monitor Memory with “stat soundwave”

Since Ogg Vorbis data must be decompressed into a real-time buffer, it can consume significant “Decompression” memory. Use the console command stat soundwave to see which assets are currently being managed by the Ogg decoder and identify if any long-form sounds should be switched to “Streaming” to save memory.

7. Ensure Module Inclusion in Build.cs

If you are writing custom low-level audio tools that need to interface directly with Vorbis data (such as a custom importer), you must include the module in your Build.cs.

C#
AddModuleDependencies(Target, new string[] { "AudioFormatOgg" });
Copy code
8. Verify Elimination of Silence

Vorbis encoding can sometimes add tiny amounts of padding at the start or end of a file. For perfectly seamless loops, ensure your source files are “sample-accurate.” If you notice clicks at loop points, the elimination of those artifacts is best handled by using the Looping checkbox in the Sound Wave settings, which tells the Ogg decoder to handle the wrap-around logic more cleanly.