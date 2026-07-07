---
layout: default
title: AudioCaptureCore
---

<!-- ai-generation-failed -->

<h1>AudioCaptureCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureCore/AudioCaptureCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

n Unreal Engine. It serves as the hardware abstraction layer (HAL) that interfaces directly with a device’s operating system audio APIs.

Description and Purpose

While the AudioCapture plugin provides high-level Blueprint components for developers, AudioCaptureCore handles the actual communication with backends like WASAPI (Windows), CoreAudio (macOS/iOS), and ALSA/PulseAudio (Linux). Its purpose is to open audio input streams, manage hardware buffer callbacks, and feed raw PCM sample data into the Unreal Audio Mixer. It is essential for features requiring real-time microphone access, such as VOIP, gameplay-driven audio analysis, and in-editor recording tools.

Practical Usage Tips and Best Practices
Explicit Module Dependency
If you are writing custom C++ classes to process microphone data, you must add the module to your Build.cs file. Note that it is often required alongside AudioMixer:
C#
PublicDependencyModuleNames.AddRange(new string[] { "AudioCaptureCore", "AudioMixer" });
Copy code
Handle Platform Permissions
On mobile platforms (Android/iOS), simply including the module is not enough. You must ensure the “Microphone Permission” is requested in the Project Settings. Without this, AudioCaptureCore will fail to initialize the hardware stream, often returning a silent buffer without an explicit error message.
Avoid the Game Thread for Processing
Audio buffers are provided via a high-priority hardware callback. Never perform heavy calculations or modify UObjects directly inside these callbacks. Instead, use a thread-safe circular buffer (like TCircularQueue) to pass data from the AudioCaptureCore thread to a worker thread or the Game Thread.
Use Submixes for “Silent” Analysis
If you want to analyze microphone input (e.g., for lip-syncing) without the player hearing their own voice echoed back, route the audio capture to a specific Sound Submix. Set that Submix’s output volume to zero but attach an Audio Analysis delegate to it to extract the frequency data.
Account for Sample Rate Mismatches
Different hardware devices operate at different sample rates (typically 44.1kHz or 48kHz). Always query the hardware’s preferred sample rate via the IAudioCaptureStream interface before initializing your buffers to eliminate pitch-shifting issues or expensive software resampling.
Threading and Thread Safety
Be aware that OnAudioCapture callbacks originate from a dedicated audio thread. If an event in your game—such as a player elimination—needs to trigger a change in how audio is captured (like stopping the stream or changing gains), ensure you use thread-safe atomics or the TaskGraph system to communicate these state changes.
Minimize Buffer Latency
For gameplay mechanics that rely on timing (e.g., a “blow into the mic” mechanic), keep your buffer sizes small. However, extremely small buffers increase the risk of “crackling” if the CPU is under heavy load. Test on your target hardware to find the “sweet spot” where latency is low but the stream remains stable.
Clean Up Streams on EndPlay
Always explicitly stop and close the audio capture stream when an Actor is destroyed or the level changes. Leaving a hardware stream open via AudioCaptureCore can prevent other applications from accessing the microphone and can cause the Unreal Editor to hang during shutdown.