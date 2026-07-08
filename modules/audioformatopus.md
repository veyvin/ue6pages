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

ion in Unreal Engine that integrates the Opus codec into the engine’s asset cooking pipeline. Opus is a highly versatile, open-source audio format designed specifically for low-latency interactive audio and high-quality speech.

Description

This module is primarily responsible for encoding raw PCM audio data into the Opus format during the project “cooking” process. In Unreal Engine, Opus is the standard codec used for VOIP (Voice Over IP) and is an excellent choice for long-form audio like radio tracks or ambient soundscapes. It provides a superior balance between low bitrate and high fidelity, outperforming older codecs like Ogg Vorbis in both quality and latency.

Practical Usage Tips and Best Practices
1. Ideal for Voice and Dialogue

Because Opus was engineered for speech, use this module for character dialogue and VOIP. It excels at maintaining clarity at very low bitrates (as low as 16–32 kbps), which is essential for reducing network bandwidth in multiplayer games when players communicate via a microphone.

2. Manage Bitrate for Mobile Optimization

In your Project Settings under Windows/Android/iOS, you can configure the default audio compression. For mobile platforms with limited storage and memory, using Opus allows you to significantly reduce the size of your audio assets. This helps to eliminate unnecessary “bloat” in your final APK or IPA package.

3. Use for Long Ambient Tracks

Avoid using PCM or ADPCM for long background music or ambient loops, as these formats consume massive amounts of memory. Opus is a “streaming-friendly” codec; by using the AudioFormatOpus module to compress these tracks, you can keep the memory footprint low while maintaining a high dynamic range for your game’s soundtrack.

4. Configure Platform-Specific Quality

The module respects the “Compression Quality” slider in the Sound Wave asset details.

Quality 1–20: High compression, best for VOIP and radio-style effects.
Quality 40–60: Balanced, ideal for most dialogue and music.
Quality 80+: Transparent quality, use only for critical, high-fidelity audio.
5. Understand the Latency Benefits

Opus has a much lower algorithmic delay compared to other codecs. This makes it the preferred choice for real-time applications. If you are building a custom system that requires audio to be sent across a network (e.g., a shared musical instrument or a walkie-talkie feature), the AudioFormatOpus module ensures the encoding process adds minimal delay.

6. Verify Asset Cooking via Logs

When cooking your project, monitor the Output Log for “AudioFormatOpus.” This will show you the compression ratios achieved. If a specific asset is not compressing as expected, verify that the source file is a standard 16-bit mono or stereo WAV file, as the encoder is optimized for these inputs.

7. Handle Audio on Elimination

For “one-shot” sound effects that trigger during high-action moments, such as a player’s elimination, consider using a less CPU-intensive codec like Bink Audio or ADPCM if performance is tight. While Opus is efficient, it requires more CPU cycles to decompress than ADPCM. Reserve Opus for instances where file size and speech quality are the primary concerns.

8. Ensure Module Inclusion in Build.cs

If you are writing a custom tool or a plugin that needs to programmatically compress audio into the Opus format, you must include the module in your editor-target dependencies. This is generally only required for technical artists or pipeline engineers building custom asset importers:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AudioFormatOpus");

	}
Copy code