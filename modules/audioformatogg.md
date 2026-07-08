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

n that provides Unreal Engine with the ability to encode and decode Ogg Vorbis compressed audio. Internally, it acts as a wrapper for the libvorbis and libogg libraries, allowing the engine’s cooking pipeline to convert raw PCM data into the .ogg format.

This module is primarily used during the Asset Cooking process to compress audio for platforms that support or require Ogg Vorbis as their runtime format (such as PC and some Android configurations). It is also utilized by the editor to import .ogg files and convert them into internal USoundWave assets.

Practical Usage Tips and Best Practices
1. Define Module Dependencies

If you are writing a custom tool that needs to programmatically compress audio or interface with the Ogg encoder, add this module to your [Project].Build.cs. Note that this is typically an Editor or Program module dependency.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AudioFormatOgg");

	}
Copy code
2. Target Ogg for Console Debugging

While consoles usually use proprietary hardware formats, you can force the engine to use Ogg Vorbis for debugging purposes. This is done by modifying the GetWaveFormat() function in your platform’s TargetPlatform.cpp to return NAME_OGG. This is useful for isolating whether an audio glitch is caused by a hardware codec or the engine logic.

3. Tune Quality via Sound Wave Settings

The Ogg encoder reacts to the Quality slider (1-100) in the USoundWave details panel. For Ogg, a quality of 40-60 is usually sufficient for most sound effects. High-quality music should stay around 70-80. Avoid 100 as it leads to diminishing returns and fails to provide significant elimination of file size compared to the original WAV.

4. Leverage Streaming for Long Files

Because Ogg is a compressed format, it must be decoded into PCM to be played. For long files (like background music), ensure Streaming is enabled in the Sound Wave settings. This allows the AudioFormatOgg module to decode small chunks of the file at a time, preventing a massive spike in memory usage that could lead to the elimination of your app’s memory budget.

5. Monitor Cooking Performance

Ogg encoding is CPU-intensive during the project cook process. If you have thousands of audio assets, ensure your build machine has a high core count. Unreal will use multiple threads to run the Ogg encoder in parallel, significantly reducing the time spent in the “Cooking Content” phase.

6. Use for Platform-Specific Overrides

In the Project Settings > Platforms, you can specify different compression formats. If you are targeting a platform with limited storage, using Ogg Vorbis (if supported) can offer a better balance of quality-to-ratio than ADPCM, effectively aiding in the elimination of unnecessary disk footprint.

7. Verify Runtime Decoding Support

Not all platforms use Ogg at runtime. Before assuming a device is using Ogg, check the AudioMixerDevice.cpp for the platform and look for FVorbisAudioInfo. If it is not present, the engine will likely decompress the Ogg to PCM during the cook or use a different format entirely (like Opus or Bink Audio).

8. Consistency in Sampling Rates

To prevent the Ogg encoder from having to perform extra work, try to import your original files at the sampling rate you intend to use in-game (typically 44.1kHz or 48kHz). This avoids an internal resampling step before the Ogg encoding begins, preserving higher audio fidelity.