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

e encoding and decoding of Ogg Vorbis audio data within Unreal Engine. While the engine stores imported audio as uncompressed PCM internally, it uses this module during the “cooking” process to compress assets for target platforms that utilize the Ogg Vorbis codec (such as PC, Linux, and certain Android configurations).

It acts as the bridge between Unreal’s abstract audio interfaces and the third-party libvorbis and libogg libraries.

1. Module Configuration

This is primarily a developer-tooling module used by the engine’s cookers. However, if you are writing custom tools that need to manipulate or inspect Ogg-compressed audio data directly, you must include it in your Build.cs:

C#
	// MyProject.Build.cs

	if (Target.Type == TargetType.Editor || Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PrivateDependencyModuleNames.Add("AudioFormatOgg");

	}
Copy code
2. Practical Usage Tips & Best Practices
Target Ogg-Vorbis for Cross-Platform Debugging

On many platforms, the default codec is proprietary (like xMA or opus). If you encounter platform-specific audio glitches, you can force the engine to use Ogg Vorbis by setting NAME_OGG in your platform’s TargetPlatform.cpp (for source builds). This helps “eliminate” the codec itself as the source of the bug by using a well-known, open-source standard across all devices.

Balance Quality vs. Memory

The Ogg Vorbis codec is lossy. In the Sound Wave asset details, the “Compression Quality” slider (1-100) directly affects how this module encodes the data.

Tip: For ambient sounds or UI clicks, a quality of 30-40 is often indistinguishable from 100 but significantly reduces the final package size and memory footprint.
Utilize Stream Caching

For long music tracks or ambient loops, enable Seekable Selection and Streaming in the Sound Wave. The AudioFormatOgg module supports chunked decoding, allowing the engine to load only small segments of the Ogg data into memory at a time. This “eliminates” the massive RAM spikes caused by loading large uncompressed audio files.

Monitor Cook-Time Performance

Because Ogg encoding is CPU-intensive, having thousands of uncompressed .wav files can slow down your project’s cook times. You can verify the efficiency of the encoding process by checking the “Cooker Statistics” in the Output Log. If encoding is the bottleneck, consider using the Derived Data Cache (DDC) to share compressed Ogg results across your team.

Validate Sample Rate Compatibility

While Ogg Vorbis supports various sample rates, the most stable results across different hardware back-ends are achieved at 44100Hz or 48000Hz. If this module encounters a non-standard rate, it may attempt to resample during compression, which can occasionally introduce “aliasing” or “ringing” artifacts.

Avoid Multi-Generation Compression

Always import your source audio as high-quality, uncompressed .wav files. If you import a file that was already compressed as an Ogg or MP3, and then the AudioFormatOgg module compresses it again during cooking, the “elimination” of data occurs twice, leading to significant “compression artifacts” and muddy audio.

Leverage Multichannel Ogg Support

Unlike some simpler codecs, Ogg Vorbis natively supports multichannel data (up to 255 channels, though UE typically limits this to 8 for 7.1). You can use this module to encode complex surround-sound ambisonics or multi-track stems into a single optimized asset, keeping your file management clean.

Debugging with “stat audio”

To see if your Ogg assets are correctly decompressing at runtime, use the console command stat audio. This display will show you how many “Decompressing” streams are active. If this number is high, your CPU may be struggling with the Ogg decoding overhead, suggesting you should switch some short, frequent sounds to “Realtime Decompression” or “ADPCM” instead.