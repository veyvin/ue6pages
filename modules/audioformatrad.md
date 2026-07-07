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

provides support for Bink Audio, a high-performance audio compression technology developed by RAD Game Tools (now part of Epic Games). This module specifically implements the IAudioFormat interface, allowing the Unreal Editor to recognize, “cook” (compress), and decompress Bink Audio assets.

It is primarily used to facilitate the use of Bink Audio for both standalone sound assets and audio tracks embedded within Bink Video files, offering a specialized alternative to standard formats like Opus or ADPCM.

Practical Usage Tips & Best Practices
1. Module Dependency Requirements

Since AudioFormatRAD is an editor-only module used for asset compression, it should only be referenced in Editor-specific Build.cs files or within #if WITH_EDITOR blocks. For runtime playback, the engine uses the corresponding BinkAudioDecoder module.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AudioFormatRAD");

	}
Copy code
2. Utilize for Multi-Channel Audio

Bink Audio is highly efficient at handling multi-channel configurations (5.1 and 7.1 surround sound). Use this format via the AudioFormatRAD pipeline when you need high-fidelity cinematic audio that requires lower CPU overhead during decompression compared to standard multi-channel PCM.

3. Standardize with the .ba2 Extension

The module is designed to work with .ba2 (Bink Audio) files. When importing external audio specifically intended for the Bink pipeline, ensure your source files follow the conventions expected by the RAD encoder tools located in Engine/Binaries/ThirdParty/Bink.

4. Configure Bink Video Sound Tracks

This module handles the logic for the “Bink Sound Track” settings found in Project Settings > Bink Movies. If your cinematic audio sounds incorrect, verify that the Sound Track Start and Offset values match the multi-language or multi-channel configuration you authored in the Bink encoder.

5. Optimize via Compression Quality

In the USoundWave asset details, you can adjust the Quality slider. When the Bink codec is selected (facilitated by this module), the slider directly influences the bit-rate of the RAD compression. Test different values to find the “sweet spot” where you eliminate audible artifacts while minimizing the final package size.

6. Debugging with Console Commands

To verify if the RAD module is correctly processing audio at runtime, use the console command au.DumpActiveSounds 1. This will list all currently playing sounds and their associated codecs; Bink-compressed assets will clearly show their origin, helping you confirm the cook process worked as intended.

7. Placement in Content/Movies

While standard audio lives in the content tree, audio tightly coupled with Bink Video should be kept in the Content/Movies directory. This ensures that the AudioFormatRAD module and the Bink plugin can correctly resolve the file paths during the cooking process for different target platforms.

8. Prefer for Low-Latency Streaming

Bink Audio is architected for low-latency streaming. Use the settings provided by this module to enable “Stream Caching” on platforms with limited memory. This allows the engine to decode small chunks of RAD-compressed data on the fly, preventing the elimination of available RAM by large, uncompressed audio buffers.