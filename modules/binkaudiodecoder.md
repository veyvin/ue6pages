---
layout: default
title: BinkAudioDecoder
---

<!-- ai-generation-failed -->

<h1>BinkAudioDecoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/BinkAudioDecoder/Module/BinkAudioDecoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or Bink Audio within Unreal Engine. While the AudioFormatBink module handles the high-level asset integration and “cook” settings, this module contains the actual implementation of the Bink Audio codec’s decoding algorithms.

It is responsible for taking compressed bitstream data—either from a standalone SoundWave or an audio track embedded in a Bink Video—and converting it into raw PCM samples that the Unreal Audio Mixer can play. It is designed to be highly performant, utilizing software-based decoding that is optimized for simultaneous multi-threaded execution across all supported platforms.

Practical Usage Tips and Best Practices
Prioritize Software Decoding on Consoles Bink Audio uses a software-based decoder rather than hardware-specific chips. This is a best practice to “eliminate” contention for hardware decoding resources (like those on PS5 or Xbox) that might be reserved for system-level audio or other proprietary formats.
Leverage Multi-Threaded Decompression The decoder is designed to run on the engine’s audio worker threads. To “eliminate” hitches on the Game Thread, ensure your Project Settings allow for multiple Audio Worker Threads. This module will then spread the decoding workload across available CPU cores.
Monitor Memory with Bink-Specific SoundWaves When a SoundWave is set to use Bink, the decoder only requires a tiny memory footprint for the decompression state. Use this for long ambient loops or background music to “eliminate” the massive RAM usage required by uncompressed PCM (Wave) files.
Avoid Real-Time Decoding for Tiny SFX For sounds shorter than a few hundred milliseconds (like UI clicks), the overhead of initializing the Bink decoder can outweigh the memory savings. In these cases, “eliminate” the decoder’s CPU cost by using “PCM” or “ADPCM” instead of Bink.
Verify Module Inclusion in Build.cs If you are building a custom audio engine extension or a specialized media player in C++, you may need to explicitly include this module to handle Bink streams.
C++
	if (Target.Type == TargetType.Editor || Target.Platform == UnrealTargetPlatform.Win64)

	{

	    AddEngineThirdPartyPrivateStaticDependencies(Target, "BinkAudioDecoder");

	}
Copy code
Check for Seeking Latency While the decoder is fast, seeking to a random point in a Bink stream requires the decoder to find the nearest “seek point.” To “eliminate” audible delays when jumping around a track, ensure your source files were encoded with frequent seek frames using the Bink 2 compressor tools.
Use with MetaSounds for Dynamic Mixing The Bink Audio Decoder works seamlessly as a source for MetaSounds. By using Bink-encoded assets within a MetaSound graph, you can “eliminate” storage space concerns while still applying complex, real-time DSP effects to the decoded output.
Debug via LogBinkMedia If audio fails to play from a Bink-encoded source, check the logs for LogBinkMedia. This module will report if the bitstream is corrupted or if the sample rate is unsupported by the current hardware, allowing you to “eliminate” asset-related issues quickly.