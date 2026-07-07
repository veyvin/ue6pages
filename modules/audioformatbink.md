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

gration that allows Unreal Engine to utilize Bink Audio. While Bink is traditionally associated with video (Bink Video), Bink Audio is a highly optimized, high-fidelity perceptual audio codec specifically designed for games.

This module provides the “cooker” logic and runtime decompression required to use Bink as an alternative to Ogg Vorbis or ADPCM. It is particularly valuable for cross-platform development because it offers consistent performance and quality across PC, consoles, and mobile devices without relying on platform-specific hardware decoders.

Practical Usage Tips and Best Practices
1. Use for Memory-Intensive Projects

Bink Audio typically offers better compression ratios than Ogg Vorbis at the same perceived quality level.

Best Practice: If your project is hitting disc space or memory limits, switch your long-form ambient tracks or music to the Bink codec. This helps eliminate memory bloat while maintaining high-quality stereo or 5.1 output.
2. Configure via Sound Wave Settings

You don’t need C++ to activate Bink Audio; it is integrated directly into the USoundWave asset properties.

Action: Open a Sound Wave asset, locate the Format or Compression section, and select Bink from the dropdown menu. You can then adjust the quality slider to find the perfect balance between file size and clarity.
3. Prioritize Bink for Multi-Channel Audio

Hardware decoders on many platforms struggle with more than two channels.

Tip: For 5.1 or 7.1 surround sound assets, use the Bink Audio codec. The AudioFormatBink module handles the multi-channel mapping efficiently in software, ensuring that complex spatial mixes are not eliminated or downmixed due to hardware limitations.
4. Leverage Low CPU Overhead

Unlike some modern high-compression codecs, Bink Audio is designed to be extremely “cheap” to decode on the CPU.

Best Practice: Use Bink for sounds that need to start instantly. Because the decoding is lightweight, it reduces the latency between a “Play” command and the actual audio output, which is critical for synchronized UI sounds or weapon effects.
5. Coordinate with the Bink Media Plugin

The AudioFormatBink module works in tandem with the Bink Video plugin.

Tip: When playing Bink Videos, ensure the audio track is encoded using the Bink Audio format within the .bk2 file. This allows the engine to use a unified decoding path for both the video’s sound and your standard game sound effects.
6. Optimize Seek Times for Looping

Bink Audio supports very fast seeking and seamless looping.

Best Practice: For music tracks that require perfect sample-accurate looping, Bink is often more reliable than standard MP3 or Ogg. It avoids the “gap” or “pop” often found at the loop point, eliminating the need for complex cross-fading logic in Blueprints.
7. Validate Platform Compatibility

While Bink is cross-platform, always verify your “Cook Override” settings.

Action: Go to Project Settings > Windows/Android/Console > Audio. You can set Bink as the default compression format for specific platforms. This allows you to use Bink on mobile (to save space) while keeping uncompressed PCM on high-end consoles if disc space is not an issue.
8. Monitor via ‘stat soundwave’

To verify that the AudioFormatBink module is active and working correctly during gameplay:

Command: Use the console command stat soundwave. This overlay will show you which codecs are currently being used by active voices. Ensure your intended assets show “Bink” to confirm that the software decoder is handling the stream.