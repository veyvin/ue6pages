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

rformance software-based audio codec designed by RAD Game Tools (now part of Epic Games). Within Unreal Engine, this module acts as a specialized compressor/decoder that allows the engine to handle the Bink audio format for both standalone sound assets and audio tracks embedded within Bink Video files.

It is primarily used to provide a cross-platform, CPU-efficient alternative to Ogg Vorbis or ADPCM, offering high compression ratios with very low memory overhead and minimal latency during decompression.

Practical Usage Tips and Best Practices
Optimal Compression for Mobile and Console Bink Audio is exceptionally efficient on platforms with limited CPU resources. Use the Bink Audio compression setting in the SoundWave editor to “eliminate” the performance bottlenecks associated with heavier codecs like Ogg Vorbis on mobile devices or Nintendo Switch.
Multi-Channel Support The module supports multi-channel audio up to 7.1 surround sound. If your project includes high-fidelity cinematic sequences, use Bink Audio to maintain spatial clarity while “eliminating” the massive file sizes typically associated with uncompressed multi-channel PCM data.
Synchronize with Bink Video When using the Bink Media plugin for cinematics, the AudioFormatBink module ensures that the audio remains perfectly synced with the video frames. In the Project Settings > Bink Movies, use the “Snd Simple” setting to let the module automatically handle track offsets based on your filenames (e.g., files ending in _51 for surround).
Enable the Plugin for External Assets To use Bink Audio for standard SoundWaves, ensure the Bink Media plugin is enabled in the editor. Once active, “Bink” will appear as an option in the Loading Behavior and Compression settings of your SoundWave assets, allowing you to “eliminate” the need for external compression tools.
Manage Memory via Seeking Bink Audio supports fast seeking with very little CPU cost. This makes it ideal for long ambient tracks or music loops where you may need to jump to different timestamps. Using Bink allows you to “eliminate” the hitching that can occur when seeking through heavily encoded Ogg files.
Use the Bink 2 Encoder for Conversion For the highest quality results, use the Bink2ForUnreal.exe found in the Engine/Binaries/ThirdParty/Bink directory. Converting your source WAVE files here before importing ensures that the AudioFormatBink module receives data optimized for the engine’s specific implementation.
Identify Decoding Issues via Logs If Bink audio tracks fail to play or sound distorted, use the console command log LogAudioLink All or check for LogBinkMedia entries. This will help you “eliminate” errors related to unsupported sample rates or missing hardware decoder permissions on certain platforms.
Avoid Over-Compression While Bink is highly efficient, setting the quality level too low can introduce metallic artifacts. A best practice is to keep the quality setting at “4” or higher for music to “eliminate” audible compression noise, while lower settings can be used for simple sound effects to save space.