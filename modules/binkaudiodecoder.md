---
layout: default
title: BinkAudioDecoder
---

<!-- ai-generation-failed -->

<h1>BinkAudioDecoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/BinkAudioDecoder/Module/BinkAudioDecoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

amework that provides the low-level software decoding logic for Bink Audio streams. Unlike the higher-level AudioFormatBink module which handles asset management, this module is responsible for the heavy lifting: transforming compressed Bink audio packets into raw PCM data that the Unreal Audio Engine can process.

It is primarily used as the audio backend for the Bink Media Player, ensuring that sound from .bk2 video files is decoded with high fidelity and low CPU latency across all supported platforms.

Practical Usage Tips and Best Practices
Software Decoding Advantage Because this module performs software-based decoding, it is not subject to the hardware sharing limitations often found on mobile devices or consoles. You can use it to “eliminate” issues where a hardware audio decoder is already in use by another system process, ensuring consistent playback.
Optimization for Multi-Core CPUs The Bink Audio Decoder is designed to be highly thread-safe. To “eliminate” hitches on the Game Thread, ensure your Bink Media Player is configured to allow asynchronous decoding. This allows the BinkAudioDecoder to run on worker threads, preventing audio processing from impacting your frame rate.
Match Sample Rates to the Audio Mixer For the best performance, encode your Bink files at the same sample rate as your project’s target platform (typically 48kHz). This “eliminates” the need for the engine to perform additional resampling after the BinkAudioDecoder has finished its work, saving CPU cycles.
Manage Stream Buffering If you experience audio dropouts in high-action scenes (such as an intense “elimination” sequence with many sound effects), increase the Bink Buffer Mode in your Project Settings. This gives the decoder more breathing room to handle momentary CPU spikes without starving the audio buffer.
Monitor Memory via LLM Use Low-Level Memory (LLM) tracking to monitor the memory footprint of the decoder. While the code itself is small, the buffers required for high-channel-count audio (like 7.1 surround) can add up. Use this data to “eliminate” memory leaks in long-running cinematic sequences.
Use for Precise Audio/Video Sync The BinkAudioDecoder is tightly coupled with the Bink video frame clock. This makes it superior to using separate .wav files for cinematics, as it “eliminates” the drift that often occurs between independent audio and video streams over long durations.
Verify Backend Initialization If your Bink videos have no sound, check your log for LogBinkMediaPlayer. If the decoder fails to initialize due to a missing module dependency or an unsupported audio format, the log will report it. Ensure the Bink Media Player plugin is fully enabled to “eliminate” initialization failures.
Coordinate with AudioLink If you are using the AudioLink module to send sound to external middleware (like Wwise), be aware that the BinkAudioDecoder output can be routed through the Unreal Submix system. This is a best practice for applying global bus effects or “elimination” filters to your cinematic audio.