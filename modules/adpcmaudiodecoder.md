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

ble for decoding ADPCM (Adaptive Differential Pulse Code Modulation) compressed audio data.

ADPCM is a lossy compression format that provides a fixed 4:1 compression ratio. In Unreal Engine 5, this module provides the ICompressedAudioInfo implementation (specifically FADPCMAudioInfo) required for the engine’s audio mixer to expand compressed ADPCM blocks into PCM samples for playback. It is primarily used as a high-performance, low-CPU alternative to more complex codecs like Ogg Vorbis or Opus.

Practical Usage Tips and Best Practices
1. Configure Build Dependencies

To utilize ADPCM decoding interfaces or manually handle ADPCM streams in a C++ project, you must include the module in your Project.Build.cs file.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "Engine", 

	    "AudioMixer", 

	    "Adpcmaudiodecoder" // Include the decoder module here

	});

	```

	 

	#### 2. Prioritize for Low-Latency/High Voice Counts

	Because ADPCM decoding is computationally "cheap" compared to Vorbis, use it for short, repetitive sounds (like UI clicks or footstep variations) where you need many simultaneous voices to play without impacting the CPU's audio thread budget.

	 

	#### 3. Managing the 4:1 Fixed Ratio

	Unlike Vorbis or Opus, which have variable bitrates, ADPCM always compresses at a 4:1 ratio.

	*   **Best Practice:** Do not use ADPCM for long background music tracks or cinematic dialogue. The file size on disk/memory will be significantly larger than a high-quality Vorbis file, even though the CPU usage is lower.

	 

	#### 4. Platform-Specific Cooking

	ADPCM is often the "fallback" or preferred format for certain platforms (like mobile or specific console builds). You can force a `USoundWave` to use ADPCM by setting its **Loading Behavior Override** or using **Target Column** settings in the Project Settings under **Audio -> Platforms**.

	 

	#### 5. Runtime Decoding Interface

	If you are writing a custom audio procedural generator or streaming system, use `FADPCMAudioInfo` to decode raw bytes.

	 

	```cpp

	#include "ADPCMAudioInfo.h"

	 

	// Example: Checking if a SoundWave is using ADPCM

	void CheckAudioFormat(USoundWave* InSoundWave)

	{

	    if (InSoundWave && InSoundWave->GetRuntimeFormat() == FName("ADPCM"))

	    {

	        UE_LOG(LogTemp, Log, TEXT("Sound is using ADPCM compression."));

	    }

	}

	```

	 

	#### 6. Avoid Double Compression

	Ensure you are not importing already-compressed ADPCM files into Unreal. Always import high-fidelity **uncompressed .WAV** (PCM) files and let Unreal’s cook process handle the conversion to ADPCM. This prevents "generation loss" and ensures the module handles the bit-depth conversion correctly.

	 

	#### 7. Debugging via Console

	If you suspect performance issues with the decoder or want to verify its usage at runtime, use the following console commands:

	*   `stat soundwaves`: Displays all active sound waves and their compression formats.

	*   `au.Debug.ListDecoders`: (If available in your build) Lists currently active hardware/software decoders.

	 

	#### 8. Memory vs. CPU Trade-off

	Use ADPCM when your project is **CPU-bound** on the audio thread but has available **RAM/Disk space**. If your project is memory-constrained (e.g., mobile), Vorbis is usually superior despite the higher CPU cost.
Copy code
2. Prioritize for High Voice Counts

Because ADPCM decoding is computationally inexpensive compared to Vorbis, use it for scenarios requiring high voice concurrency. It is ideal for short, repetitive sounds—such as UI clicks, weapon casings, or environmental debris—where the goal is to eliminate CPU bottlenecks on the audio thread.

3. Strategic Format Selection

Understand the 4:1 fixed ratio. While ADPCM saves CPU cycles, it results in a larger memory footprint than Vorbis or Opus.

Best Practice: Reserve ADPCM for short clips. Avoid using it for long background music or cinematic dialogue to prevent excessive memory usage.
4. Platform-Specific Overrides

ADPCM is often the preferred format for mobile or specific console platforms where hardware resources are limited. You can force a USoundWave to use ADPCM by adjusting the Loading Behavior Override or modifying the Target Column settings in Project Settings > Audio > Platforms.

5. Handle Decoding in C++

If you are developing a custom audio procedural generator or a specialized streaming system, use FADPCMAudioInfo to decode raw byte streams into PCM data that the Audio Mixer can process.

C++
	#include "ADPCMAudioInfo.h"

	 

	// Example: Checking for ADPCM format at runtime

	void ValidateAudioFormat(USoundWave* InSoundWave)

	{

	    if (InSoundWave && InSoundWave->GetRuntimeFormat() == FName("ADPCM"))

	    {

	        UE_LOG(LogTemp, Log, TEXT("Audio source validated for ADPCM decoding."));

	    }

	}
Copy code
6. Import High-Quality Source Assets

Always import uncompressed .WAV (PCM) files into the editor. Allow the engine’s cooking process to handle the ADPCM conversion. Importing pre-compressed ADPCM files can lead to “generation loss” and artifacts, which the decoder module cannot eliminate during playback.

7. Monitor Decoder Performance

Use the Unreal Insights tool or console commands to verify that the decoder is not being overtaxed.

stat soundwaves: Use this to see which sounds are currently active and confirm they are using the expected ADPCM format.
stat audio: Monitors the overall CPU cost of the audio thread.
8. Manage Memory vs. CPU Trade-offs

Select ADPCM only when your project is CPU-bound on the audio thread. If your project is memory-bound (typical in mobile development), the higher compression of Vorbis or Bink Audio is generally superior, despite the increased CPU cost required to decode those formats.