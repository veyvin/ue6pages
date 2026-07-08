---
layout: default
title: NonRealtimeAudioRenderer
---

<!-- ai-generation-failed -->

<h1>NonRealtimeAudioRenderer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NonRealtimeAudioRenderer/NonRealtimeAudioRenderer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, AudioMixerCore, Core, CoreUObject, Engine, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nreal Engine that operates independently of the system’s physical sound card and real-time clock. Instead of pushing audio buffers to speakers at a fixed 1:1 speed, this module allows the engine to “render” audio as fast as the CPU allows—or as slow as needed—to ensure every single sample is processed accurately.

This is primarily used for Render-to-Disk scenarios, such as exporting cinematics via the Movie Render Queue, automated testing (where you need to verify audio output without a human listening), and offline analytical processing. By decoupling audio from real-time constraints, it helps you eliminate audio dropouts, “crackling,” or desynchronization that can occur when the CPU is under heavy load during a high-quality render.

Practical Usage Tips and Best Practices
Use for Sample-Accurate Cinematic Exports
When rendering high-resolution videos, always use this renderer via the Movie Render Queue. Unlike the real-time audio path, which may skip samples if the frame rate dips, the Non-Realtime renderer waits for the engine to finish each frame, helping you eliminate the “audio drift” commonly seen in long cinematic sequences.
Configure via the Audio Device Module
In C++, you can instantiate this renderer by requesting a FNonRealtimeAudioDevice. This is useful for building custom commandlets that need to process sound files or generate “baked” audio data without opening the full Editor UI, which helps you eliminate unnecessary GPU overhead during batch processing.
Leverage for Deterministic Automation Testing
If you are writing Functional Tests to verify that a specific sound plays when an “elimination” event occurs, use this module to capture the output. Because it is deterministic, the audio result will be identical every time the test runs, helping you eliminate “flaky” tests caused by varying system latency.
Set Main and Submix Send Levels
Just like the real-time renderer, this module supports the full Submix Graph. Ensure your submixes are properly configured before starting an offline render; the Non-Realtime renderer will respect all effects (Reverb, EQ, Compression), helping you eliminate the need for post-production audio patching.
Monitor Buffer Underruns via Logs
Even though it is “non-realtime,” the module still tracks internal buffer health. If you are pushing the Signal Processing (DSP) too hard, check the logs for warnings. While it won’t “crackle” like a real speaker, extreme complexity can still lead to logic errors that you should eliminate by optimizing your MetaSounds or Sound Cues.
Sync with Fixed Frame Steps
When using this renderer in custom code, ensure the engine is running with a Fixed Time Step (-benchmarking or FApp::SetFixedDeltaTime). This ensures that the number of audio samples generated perfectly matches the duration of the visual frames, helping you eliminate jitter in interactive music or rhythm-based games.
Avoid Real-Time Input (Microphones)
Since this module does not follow the “wall clock,” it cannot be used with live microphone input or Live Link Audio. Attempting to mix real-time streams into an offline render will cause synchronization failure; you should eliminate any real-time input sources from your scene before starting a non-realtime render.
Properly Shutdown on Task Elimination
When your offline rendering task is finished (the “elimination” of the capture process), ensure you call Teardown on the audio device. This flushes the remaining samples to the output file (like a .wav or .m4a) and prevents file corruption, helping you eliminate incomplete or unplayable audio files.