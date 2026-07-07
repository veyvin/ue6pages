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

ftware-based decompression logic for audio assets encoded with the Bink Audio codec. While the AudioFormatBink module handles the “cooking” (encoding) of assets, this module is responsible for the real-time playback and decoding of that data within the Unreal Audio Mixer.

Bink Audio is highly optimized for game development, offering a high-performance alternative to Ogg Vorbis or ADPCM. This module ensures that Bink-encoded sounds can be played back efficiently on any platform supported by Unreal Engine, including those with limited hardware decoding capabilities.

Practical Usage Tips and Best Practices
1. Add to Build Dependencies

If you are working with low-level audio streams or custom audio components that explicitly require Bink decoding, ensure the module is included in your Build.cs.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.Add("BinkAudioDecoder");
Copy code
2. Prioritize for CPU-Bound Platforms

Bink Audio is designed to be extremely “light” on the CPU compared to other high-compression formats.

Best Practice: Use Bink-encoded assets on mobile devices or older consoles. The BinkAudioDecoder will handle the stream with minimal overhead, helping to eliminate CPU spikes during intense scenes with high voice counts.
3. Achieve Platform Parity

One of the primary strengths of this module is its software-based nature, which provides consistent results across all hardware.

Tip: If you notice that your audio sounds different on Windows than it does on a console (due to different hardware codecs), switch those assets to Bink. Using this decoder across all targets will eliminate platform-specific audio artifacts.
4. Optimize Memory via High Compression

Bink Audio maintains high fidelity even at low bitrates.

Best Practice: For large, long-running files like background music or ambient loops, use Bink. The decoder is highly efficient at handling these compressed streams, which allows you to eliminate memory bloat in your resident audio bank.
5. Ensure Seamless Looping

The Bink decoder is specifically tuned to handle sample-accurate looping.

Tip: For musical segments that must loop perfectly, Bink is often superior to MP3 or Ogg Vorbis. The decoder correctly handles the metadata required to eliminate the “click” or gap often heard at the end of a compressed audio file.
6. Support Multi-Channel Output

The BinkAudioDecoder can efficiently handle multi-channel streams (like 5.1 or 7.1) without the complexity of hardware-specific routing.

Best Practice: For cinematic or environmental surround sound, use Bink. This decoder ensures that all channels remain perfectly in sync, eliminating the phasing issues that can occur with less robust software decoders.
7. Monitor Voice Decompression via Stats

To ensure the decoder is not being overtaxed by too many simultaneous streams:

Command: Use stat audio or stat audiomixer in the console.
Action: Look for the decompression time. If it is too high, consider reducing the number of concurrent Bink voices or increasing the compression ratio to eliminate performance bottlenecks on the audio thread.
8. Use with AudioLink for External Middleware

If you are using the AudioLink system to bridge Unreal audio to external tools like Wwise or FMOD:

Tip: You can decode Bink assets within Unreal using this module and then send the raw PCM data to the external engine. This allows you to use Bink’s excellent compression for your assets while still utilizing the mixing capabilities of your chosen middleware.