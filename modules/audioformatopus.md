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

the Opus audio codec for Unreal Engine. It provides the logic required to encode raw PCM audio into the .opus format during the asset cooking process. Because Opus is a highly versatile, low-latency, and high-compression codec, this module is the primary driver for voice-over-IP (VOIP) systems and high-fidelity mobile audio in Unreal Engine.

Practical Usage Tips & Best Practices
1. Prioritize for VOIP and Communication

Opus is specifically designed for speech and low-latency communication. If your project includes multiplayer voice chat, ensure your build utilizes this module’s output. In the Project Settings > Engine > Audio, check the VOIP section to ensure Opus is the designated codec for capturing and transmitting voice data.

2. Manage Bitrate for Performance

The quality of Opus audio is highly dependent on the bitrate.

Best Practice: For clear speech in a VOIP setting, a bitrate of 16kbps to 24kbps is usually sufficient. For background music or high-fidelity environmental sounds on mobile, consider 64kbps or higher. Use the SoundWave asset settings to override quality per-platform.
3. Restrict to Editor/Cooker Modules

The AudioFormatOpus module handles the encoding (compression) of assets, which typically happens during the “Cook” phase in the Editor. You should only include this module as a dependency in Editor or Program (Cooker) build targets. The runtime decompressor is handled by separate platform-specific audio mixer modules.

4. Optimize Mobile Package Size

If you are targeting mobile platforms with strict storage limits, use the AudioFormatOpus module to aggressively compress non-essential sound effects. Opus often maintains higher perceived quality at lower bitrates compared to Ogg Vorbis or ADPCM, allowing for a significant elimination of unnecessary file size in your final APK or IPA.

5. Use for Long-Duration Ambient Tracks

Because Opus is excellent at handling variable bitrates (VBR), it is ideal for long ambient background loops (e.g., wind, rain, or city hum). Using the Opus encoder via this module allows you to keep multi-minute audio files in memory with a much smaller footprint than standard .wav files.

6. Coordinate with Elimination Sound Cues

When designing the audio for a character’s elimination, use the Opus encoder settings to ensure the “Death Cry” or impact sound is high-priority. In the SoundWave details panel, you can specify if the asset should be “Decompress on Load” or “Stream from Disk.” For critical gameplay cues like elimination, “Decompress on Load” is preferred to avoid the slight latency of Opus streaming.

7. Verify Sample Rate Support

Opus natively supports sample rates up to 48kHz. Ensure your source .wav files are recorded at 48kHz for the best encoding results through this module. If you import files at 44.1kHz, the encoder will perform a resample, which can occasionally introduce minor artifacts or increase cook times.

8. Debugging Encoding Failures

If an audio asset fails to cook, check the Output Log for LogAudioFormatOpus. Common failures include attempting to encode files with unsupported channel counts (Opus supports up to 255 channels, but Unreal typically expects Mono or Stereo) or corrupt source headers that prevent the encoder from initializing.