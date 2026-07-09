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

oding module that integrates RAD Game Tools technologies—specifically Bink Audio—into Unreal Engine. While Unreal uses standard codecs like Ogg Vorbis or XMA by default, this module allows the engine to handle the proprietary .bik audio format.

It is primarily used for high-performance audio playback within Bink Videos and as a highly optimized, low-CPU-overhead alternative for long-form audio streams (like cinematic soundtracks or ambient loops) that need to be decoded in real-time.

Practical Usage Tips and Best Practices
1. Use for Cinematic Synchronization

When playing a Bink Video, the AudioFormatRAD module ensures that the audio tracks remain perfectly synced with the video frames. If you encounter “drifting” audio in cinematics, verify that the Bink Media plugin is enabled, as it relies on this module to handle the underlying RAD audio streams.

2. Optimize for Multichannel Audio

Bink Audio is exceptionally efficient at handling multichannel data (5.1 or 7.1 surround sound). If you have a large cinematic with multiple language tracks, use the Bink encoder to pack them into a single file. The module can then selectively decode only the required tracks (e.g., the background music and the specific language center channel), reducing memory bandwidth.

3. Leverage for Low-End Hardware

The RAD audio codec is designed to have an extremely small CPU footprint during decompression. For mobile or console projects where CPU cycles are tight, using Bink Audio for long background music tracks can “eliminate” the performance hitch often caused by the more CPU-intensive Ogg Vorbis decoding.

4. Configure via Project Settings

You can manage how Bink audio behaves under Project Settings > Plugins > Bink Movie Player. Here, you can define the Bink Sound Track Start and Bink Sound Track Offset, which dictate which audio streams the AudioFormatRAD module will prioritize during playback.

5. Proper Naming for Automatic Detection

The module uses specific filename suffixes to determine speaker mapping. For 5.1 audio, ensure your source files end in _51. For localized 5.1 audio, use _51L. This allows the AudioFormatRAD logic to automatically route the audio channels to the correct speakers without manual Blueprint configuration.

6. Manage the “Stream Cache” Limit

Since Bink audio is typically streamed rather than pre-loaded, it interacts with the engine’s Audio Stream Cache. If your Bink audio stutters, check your Max Cache Size in the Audio Project Settings. If the cache is too small, other game sounds may “eliminate” the Bink audio buffer from memory, causing playback gaps.

7. Use the Standalone Bink 2 Encoder

To create compatible assets for this module, you must use the Bink2ForUnreal.exe tool located in Engine/Binaries/ThirdParty/Bink. This tool allows you to set the compression level. For most games, the default “Bink It!” settings provide the best balance between file size and audio fidelity.

Implementation & Setup

Because this is a low-level format module, you rarely call its functions directly in C++. Instead, you enable the plugin and configure your USoundWave or UBinkMediaPlayer to use it.

To enable support in your project:

Open the Plugins menu and enable Bink Media.
Restart the Editor.
Place your .bk2 or .bik files in the Content/Movies directory.
The AudioFormatRAD module will now automatically handle the audio decompression whenever these files are played via a Media Player or as a Startup Movie.
Performance & Best Practices
Module Dependency: If you are writing a custom media player that needs to handle RAD formats, add "AudioFormatRAD" to your Build.cs dependencies.
Memory Management: Use the Bink Buffer Mode setting to decide if the audio should be fully pre-loaded or streamed. For 4K cinematics with high-bitrate audio, “Stream” is highly recommended to avoid massive memory spikes.
Debugging: Use the console command stat bink to see real-time information about how much memory and CPU time the RAD audio and video decoding are consuming.