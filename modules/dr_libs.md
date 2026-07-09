---
layout: default
title: dr_libs
---

<!-- ai-generation-failed -->

<h1>dr_libs</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/dr_libs/dr_libs.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine with high-performance, single-header C libraries for audio decoding. Specifically, it includes the dr_wav, dr_mp3, and dr_flac libraries created by David Reid. Unreal Engine utilizes these libraries as the primary low-level backend for importing and real-time decoding of compressed audio files, converting them into raw PCM data that the Unreal Audio Mixer can process.

Practical Usage Tips & Best Practices
1. Use for Runtime Audio Loading

While Unreal prefers assets to be imported as USoundWave, you may need to load audio from an external folder (like a “Music” folder on the user’s desktop).

Best Practice: Utilize the dr_wav or dr_mp3 headers directly in C++ for “runtime file IO.” These libraries are extremely lightweight and allow for the elimination of the heavy overhead associated with the full Unreal Media Framework for simple audio playback.
2. Wrap Includes with Third-Party Macros

Because dr_libs are third-party C headers, they do not follow Unreal’s coding standards and can cause “shadow variable” or “missing macro” warnings.

Tip: Always wrap your #include "dr_wav.h" statements with THIRD_PARTY_INCLUDES_START and THIRD_PARTY_INCLUDES_END. This prevents the Unreal Header Tool from throwing errors and ensures the elimination of compiler warnings during your build.
3. Manage Memory via Unreal’s Allocators

By default, dr_libs uses standard C malloc. In Unreal, you want all memory tracked by the engine’s memory profiler.

Best Practice: Define DR_WAV_MALLOC and DR_WAV_FREE to point to FMemory::Malloc and FMemory::Free. This ensures that any memory used for audio decoding is visible in Unreal Insights, aiding in the elimination of “untracked” memory leaks.
4. Prefer FLAC for High-Fidelity/Small-Size Balance

The dr_flac implementation in this module is highly efficient at decoding.

Tip: If you have high-quality orchestral tracks that are too large for uncompressed WAV but require better quality than MP3, use FLAC. The dr_flac decoder provides lossless quality with a significant elimination of disk space compared to raw PCM.
5. Implement IWYU Compliance

When using these libraries in your own module, do not include them in your public header files.

Best Practice: Keep all dr_libs includes in your .cpp (Private) files. This follows the “Include What You Use” (IWYU) standard and prevents the third-party C logic from “leaking” into other modules, which facilitates the elimination of circular dependency issues.
6. Handle Sampling Rate Conversion

The dr_libs decoders output the “native” sampling rate of the file (e.g., 44.1kHz or 48kHz).

Tip: If the source file rate doesn’t match the Unreal Audio Mixer’s output rate (usually 48kHz), you must pass the resulting buffer through an Audio::FResampler. Failure to do so will result in pitch shifts, so proper resampling is key to the elimination of playback speed bugs.
7. Use for Procedural Sound Generation

If you are building a MetaSound node or a custom USoundWaveProcedural, you can use dr_libs to “bake” or “stream” binary data into the buffer.

Best Practice: Use the dr_wav_read_pcm_frames_f32 function to get floating-point data directly. This matches Unreal’s internal 32-bit float audio pipeline, leading to the elimination of unnecessary integer-to-float conversion steps.
8. Monitor for “Malicious” File Headers

Loading external files at runtime carries risks if the files are corrupted or malformed.

Tip: Always check the return value of the dr*_init_* functions. These libraries are robust, but validating the header before attempting to decode a massive buffer ensures the elimination of potential application crashes caused by reading “garbage” data from a corrupt file.