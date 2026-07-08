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

ixer.

Unlike heavier codecs like Ogg Vorbis or Opus, ADPCM uses a simple predictive compression scheme that requires significantly less CPU overhead to decode, making it ideal for mobile devices, consoles (like Nintendo Switch), and high-concurrency sound effects.

Practical Usage Tips and Best Practices
Module Dependency Configuration To reference ADPCM decoding logic in C++, include the module in your project’s Build.cs file. While the engine handles this automatically for standard assets, custom audio tools require this dependency.
C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "Engine", 

	    "ADPCMAudiodecoder" // Include for low-level audio manipulation

	});

	```

	 

	#### 2. Choose ADPCM for Short, Frequent Sounds

	Use ADPCM for short sound effects (e.g., footsteps, UI clicks, gunshots) that trigger frequently. Because it is a low-complexity codec, it avoids the CPU "spikes" associated with initializing more complex decoders like Vorbis for every sound instance.

	 

	#### 3. Optimize for Nintendo Switch and Mobile

	On platforms with limited CPU resources (like the Nintendo Switch), ADPCM is often the preferred "hardware-friendly" format. Many mobile and console platforms have dedicated hardware paths or highly optimized SIMD instructions for ADPCM decoding that this module leverages.

	 

	#### 4. Balancing Compression Ratio vs. CPU

	*   **Vorbis/Opus:** High compression (smaller files), higher CPU usage.

	*   **ADPCM:** Moderate compression (approx. 4:1 ratio), very low CPU usage.

	*   **PCM:** No compression (large files), zero CPU usage.

	**Best Practice:** Use ADPCM as the "middle ground" for assets where memory is a concern but CPU budget is tight.

	 

	#### 5. Verify Decoding with Console Commands

	You can verify if your sounds are correctly using the ADPCM decoder at runtime by using the console command:

	`stat soundwaves`

	Look for the "Format" or "Codec" column in the debug overlay. If the asset was cooked correctly for ADPCM, it will show as such in the active sound instance list.

	 

	#### 6. Control Compression via Sound Wave Settings

	You don't typically interact with the `ADPCMAudiodecoder` API directly. Instead, you control its behavior in the **Sound Wave** editor:

	*   Set **Compression Quality** to a value that triggers ADPCM (usually lower values on certain platforms).

	*   Use **Platform Overrides** in the Project Settings to force ADPCM for specific platforms while keeping Vorbis for PC/PS5.

	 

	#### 7. Avoid ADPCM for Music or Ambient Loops

	Due to the nature of 4-bit ADPCM, "quantization noise" can become audible in high-fidelity audio or long, quiet loops. Avoid using this module/codec for orchestral music or subtle ambient beds; stick to Ogg Vorbis or Opus for those categories to maintain audio transparency.

	 

	#### 8. Use with the Audio Mixer (Multi-stream)

	The `ADPCMAudiodecoder` is fully compatible with the Unreal Audio Mixer. It supports efficient multi-stream decoding, meaning you can have dozens of ADPCM-encoded sounds playing simultaneously without threatening the audio thread's frame budget.
Copy code
Prioritize for Short, Frequent Sounds Use ADPCM for short sound effects such as footsteps, UI clicks, or “elimination” confirmation sounds. Because it is a low-complexity codec, it avoids the CPU spikes associated with initializing more complex decoders for every rapid sound instance.
Optimize for CPU-Constrained Platforms On platforms like Nintendo Switch or older mobile devices, ADPCM is often the preferred format. It leverages optimized software paths that allow for high voice counts without hitting the CPU ceiling.
Understand the Compression Trade-off ADPCM typically offers a fixed 4:1 compression ratio. While Ogg Vorbis can compress files much further, ADPCM’s predictable and low CPU cost makes it superior for sounds that need to be triggered and “eliminated” from memory quickly.
Verify Active Streams via Debugging You can verify if your sounds are correctly utilizing the decoder at runtime by using the console command: stat soundwaves This overlay will display the format of every active sound. Ensure your high-frequency effects are showing as ADPCM to save on your CPU budget.
Configure via Platform Overrides Use the Target Platform settings in the Project Settings to force ADPCM for specific platforms. This allows you to maintain high-fidelity Vorbis or PCM on PC/PS5 while automatically switching to ADPCM for mobile builds.
Avoid Usage for Music or Ambient Loops ADPCM can introduce “quantization noise” in quiet or high-fidelity segments. Avoid using this module for orchestral music or subtle ambient beds; stick to Ogg Vorbis or Bink Audio for those categories to maintain audio transparency.
Leverage for High Voice Counts If your game features large-scale battles where dozens of sounds trigger at once, converting those specific assets to ADPCM is the most effective way to prevent audio-related frame drops and buffer underruns.