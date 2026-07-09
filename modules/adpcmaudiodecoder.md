---
layout: default
title: AdpcmAudioDecoder
---

<!-- ai-generation-failed -->

<h1>AdpcmAudioDecoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AdpcmAudioDecoder/Module/AdpcmAudioDecoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

provides the logic for decoding audio data compressed with the ADPCM (Adaptive Differential Pulse Code Modulation) algorithm. Unlike complex codecs like Ogg Vorbis or Opus, ADPCM uses a simple predictive scheme to achieve a fixed 4:1 compression ratio.

Its primary purpose is to provide a low-CPU-cost audio solution for performance-critical scenarios. It is most commonly used on mobile platforms, the Nintendo Switch, or in any situation where high voice counts would otherwise cause CPU bottlenecks.

Practical Usage Tips and Best Practices
Add Module Dependencies If you are writing custom audio processing or low-level sound management in C++, you must include the module in your Build.cs file. Standard sound assets handle this internally, but custom systems require the reference.
C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "ADPCMAudioDecoder" });

	```

	 

	#### 2. Target High-Frequency, Short SFX

	Use ADPCM for sounds that trigger frequently and rapidly, such as:

	*   Footsteps and foley.

	*   UI clicks and feedback sounds.

	*   Weapon shell casings or small debris impacts.

	ADPCM’s low-complexity decoding prevents the CPU spikes often seen when initializing multiple Vorbis/Opus decoders simultaneously.

	 

	#### 3. Use for Platform-Specific Overrides

	ADPCM is often the "goldilocks" format for platforms with weaker CPUs (like mobile or Switch). You can maintain high-quality Ogg Vorbis on PC/PS5 while forcing ADPCM for mobile in your Project Settings:

	*   Go to **Project Settings** > **Platforms** > **[Platform Name]** > **Audio**.

	*   Configure the **Compression Quality** and default formats to prioritize ADPCM for that specific target.

	 

	#### 4. Monitor Memory vs. CPU Trade-offs

	Remember that ADPCM is a "fat" compression (4:1) compared to Ogg Vorbis (~10:1 or better). 

	*   **Best Practice:** Use ADPCM to save **CPU** at the cost of **Memory**. 

	*   **Best Practice:** Use Ogg Vorbis/Opus to save **Memory** at the cost of **CPU**.

	 

	#### 5. Verify via Console Commands

	You can confirm if the ADPCM decoder is being used at runtime by using the console command:

	`stat soundwaves`

	Look for the **Format** column; it will explicitly list the codec being used by every active sound wave.

	 

	#### 6. Include the Correct Headers

	When working with ADPCM data structures in C++, you will likely interact with `FADPCMAudioInfo`. Extract the exact includes from the engine source:

	```cpp

	#include "ADPCMAudioInfo.h"

	 

	// Example: Initializing ADPCM info for a raw data buffer

	FADPCMAudioInfo AdpcmInfo;

	FSoundQualityInfo QualityInfo;

	if (AdpcmInfo.ParseHeader(CompressedDataPtr, DataSize, &QualityInfo))

	{

	    // Ready to decode or query format tags

	}

	```

	 

	#### 7. Avoid for Music or Ambient Beds

	ADPCM can introduce "quantization noise," particularly in quiet passages or complex orchestral music. Because it only achieves 4:1 compression, a 5-minute music track in ADPCM would be prohibitively large for memory. Stick to **Bink Audio** or **Ogg Vorbis** for music.

	 

	#### 8. Leverage for Simultaneous Voice Count

	If your game logic requires 60+ simultaneous voices (e.g., a large-scale battlefield), ensure the majority of those sounds are encoded in ADPCM. The linear decoding logic allows the Audio Mixer to process these streams with significantly less latency and overhead than more sophisticated codecs.
Copy code
Target Short, Rapid-Fire SFX Use ADPCM for sounds that trigger frequently and in high numbers, such as footsteps, UI clicks, or “elimination” confirmation bleeps. Because the decoding logic is simple, it avoids the CPU spikes associated with spinning up multiple Vorbis decoders simultaneously.
Platform-Specific Overrides Use ADPCM as a “Platform Override” for mobile or Switch builds. In the Sound Wave asset editor, you can specify different compression formats per platform. This allows you to keep high-fidelity Ogg Vorbis on PC/PS5 while saving CPU on mobile.
Balance Memory vs. CPU Remember that ADPCM is “fat” (4:1) compared to Ogg Vorbis (often 10:1 or better). Use ADPCM when you have spare RAM but are CPU-bound. If your project is hitting memory limits, prioritize Ogg Vorbis or Opus instead.
Monitor Performance with Console Commands Verify that the decoder is being utilized correctly during gameplay. Use the console command: stat soundwaves This will show a list of active sound instances and their compression format. Ensure that your high-frequency sound effects are properly showing the ADPCM format tag.
Avoid for Music and Ambient Beds ADPCM can introduce “quantization noise,” which is audible as a slight hiss or graininess in quiet or complex audio. Avoid using it for long music tracks or subtle wind loops; these assets are better suited for Bink Audio or Ogg Vorbis.
Use for Voice Count Scalability If your game logic requires a high number of simultaneous voices (e.g., a large-scale battle), encoding those specific sounds in ADPCM allows the Audio Mixer to “eliminate” the risk of buffer underruns and audio stuttering by reducing the per-voice processing cost.
Leverage FADPCMAudioInfo in C++ When handling raw compressed buffers in C++, use the FADPCMAudioInfo struct (found in ADPCMAudioInfo.h) to parse headers and query format tags. This ensures your custom code remains compatible with the engine’s internal audio pipeline.