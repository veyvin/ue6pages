---
layout: default
title: AudioFormatRad
---

<!-- ai-generation-failed -->

<h1>AudioFormatRad</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioFormatRad/AudioFormatRad.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

in Unreal Engine that integrates technology from RAD Game Tools (now part of the Epic Games family). It specifically provides the engine with the ability to encode and decode Bink Audio, a high-performance audio codec designed for games.

What it is and What it’s used for

This module implements the IAudioFormat interface, allowing the Unreal Engine “Cooker” to recognize and process Bink Audio data. It is the backend responsible for transforming standard PCM wave data into the proprietary Bink Audio format during the project’s cooking phase.

Primary uses include:

High-Efficiency Compression: Providing an alternative to Ogg Vorbis or ADPCM that offers a better balance between CPU usage and file size.
Bink Video Synchronization: Handling the audio tracks embedded within .bk2 (Bink Video) files to ensure perfect lip-sync and multi-track audio playback.
Multi-Platform Support: Delivering a consistent audio codec across various platforms (PC, Console, Mobile) with hardware-aware optimization.
Practical Usage Tips and Best Practices
1. Use for Memory-Constrained Platforms

Bink Audio is highly efficient. If you are struggling with audio memory budgets on mobile or older console hardware, consider switching your primary compression format to Bink via the AudioGroup settings. It often achieves similar quality to Ogg Vorbis but with a smaller memory footprint during playback.

2. Optimize Bink Video Audio Tracks

When importing Bink Videos into Unreal, the AudioFormatRAD module manages the multi-track data. If your video has localized dialogue, you can use the Bink Media Player to select specific audio tracks (e.g., Track 0 for English, Track 1 for French) without needing to load separate video files.

3. Manage Quality vs. Bitrate

In the USoundWave settings, you can adjust the “Quality” slider. For RAD-based compression, this value directly influences the bitrate. For background music, a setting of 40-60 is usually sufficient, while UI sounds and dialogue should remain around 70-80 to eliminate compression artifacts.

4. Pre-bake for Faster Loading

Bink Audio is designed to be streamed or pre-loaded efficiently. Ensure that your SoundGroup settings in DefaultEngine.ini are configured to allow Bink-compressed assets to use “Stream from Disk” for long tracks. This prevents large audio files from bloating the resident memory (RAM) of your game.

5. Verify Module in Build.cs

If you are writing custom editor tools that involve audio manipulation or manual cooking, ensure you include AudioFormatRAD in your Editor module dependencies. Without this, the editor will be unable to “cook” or preview assets that are set to use RAD-specific compression.

6. Synchronize with MetaSounds

While MetaSounds are procedural, they can still trigger Bink-compressed SoundWave assets. Use the AudioFormatRAD module’s high-speed decoding to ensure that complex MetaSound patches utilizing many Bink-compressed samples do not cause CPU spikes or frame-rate hitches.

7. Handle Multi-Channel (5.1 / 7.1) Audio

Bink Audio is excellent at handling multi-channel surround sound data. When importing 5.1 or 7.1 WAV files, the AudioFormatRAD module ensures that the channel mapping remains intact during the compression process, which is critical for cinematic experiences.

8. Eliminate Redundant Decompressors

Be mindful of how many different audio formats you use in a single project. Mixing Bink, Ogg, and ADPCM requires the engine to keep multiple decompressor libraries in memory. Sticking to Bink for most assets (via this module) can streamline the runtime memory overhead.