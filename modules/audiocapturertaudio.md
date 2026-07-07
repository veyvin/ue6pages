---
layout: default
title: AudioCaptureRtAudio
---

<!-- ai-generation-failed -->

<h1>AudioCaptureRtAudio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/AudioCaptureRtAudio/AudioCaptureRtAudio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

of the Unreal Engine Audio Capture interface that utilizes the RtAudio library. It is primarily used as the audio input backend for desktop platforms (Windows, Linux, and macOS) to facilitate real-time microphone capture.

While the high-level AudioCapture plugin provides the user-facing Blueprint nodes, AudioCaptureRtAudio handles the low-level communication with the hardware drivers, ensuring that raw PCM data is successfully streamed from the physical input device into the engine’s audio mixer.

Practical Usage Tips & Best Practices
1. Module Dependency and Activation

If you are building a custom C++ audio tool that needs to interact directly with the RtAudio backend, you must include the module in your Build.cs. Additionally, ensure the Audio Capture plugin is enabled in the Editor, as it acts as the primary wrapper for this module.

C#
PrivateDependencyModuleNames.AddRange(new string[] { "AudioCapture", "AudioCaptureRtAudio" });
Copy code
2. Configure Hardware Sample Rates

RtAudio is sensitive to sample rate mismatches between the OS settings and the Engine. For the most stable performance, ensure your Windows/Mac microphone settings match the Engine’s project sample rate (typically 48kHz). Mismatches can lead to pitch-shifting artifacts or the total elimination of the audio signal.

3. Manage Buffer Latency

The module relies on a hardware buffer size to stream data. You can influence the latency of the capture by adjusting the AudioCallbackBufferFrameSize in your BaseEngine.ini. Lower values reduce latency for real-time applications (like voice-reactive VFX) but increase the risk of CPU underruns and “popping” sounds.

4. Monitor Device Availability

On desktop platforms, users often unplug or switch microphones. The AudioCaptureRtAudio module generates log warnings if the selected device becomes unavailable. Use the OnAudioCaptureDeviceInfo functions in C++ to verify a device is valid before attempting to call Start() to prevent null-pointer crashes.

5. Output to Bus Only for Analysis

If you are using the microphone for frequency analysis (e.g., a “blow to light a fire” mechanic) rather than voice chat, check Output to Bus Only on your Audio Capture component. This sends the signal to an AudioBus for processing while preventing the raw microphone input from being played back through the speakers, which eliminates unpleasant feedback loops.

6. Use Submixes for Effects and Recording

The data captured via this module can be routed to any standard Sound Submix. This allows you to apply real-time EQ, Reverb, or Compression to the microphone stream. It also enables the use of the Start Recording Output node to save the captured microphone data into a .wav file or a Sound Wave asset.

7. Verify Linux Dependencies

When deploying to Linux, the AudioCaptureRtAudio module often depends on system-level libraries like ALSA or PulseAudio. Ensure your target environment has these libraries installed, as the module will fail to initialize without a valid platform audio API to hook into.

8. Implement “Push-to-Talk” Logic

Because this module keeps the microphone “hot” once activated, it can consume unnecessary CPU cycles and bandwidth. Use the Start and Stop functions on the component to toggle the capture. This effectively implements a push-to-talk system and ensures the hardware is only being polled when gameplay requires it.