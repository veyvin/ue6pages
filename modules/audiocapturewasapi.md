---
layout: default
title: AudioCaptureWasapi
---

<!-- ai-generation-failed -->

<h1>AudioCaptureWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/Windows/AudioCaputureWasapi/AudioCaptureWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, AudioPlatformSupportWasapi, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine’s audio capture interface using the Windows Audio Session API (WASAPI). It provides the low-level communication between the engine and Windows audio input devices (microphones, line-ins, etc.).

Since Unreal Engine 5.8, WASAPI has become the default audio backend for Windows, replacing the legacy XAudio2 path. This module is responsible for initializing input streams, managing hardware buffers, and handling device-specific sample rates to ensure high-quality, low-latency audio capture for features like voice-reactive gameplay or real-time submix recording.

Practical Usage Tips and Best Practices
Handle Device Swapping and “Elimination” The WASAPI backend is designed to handle “Hot Swapping.” If a user unplugs their primary microphone during gameplay, the module will attempt to migrate the stream to the new Windows default device. Always listen for the OnAudioDeviceDefaultChanged delegate in C++ to ensure your UI updates when a device is “eliminated” or changed.
Match Sample Rates for Performance WASAPI often operates in “Shared Mode,” meaning it uses the sample rate defined in the Windows Sound Control Panel (typically 48kHz). To “eliminate” the CPU overhead of resampling, ensure your project’s default sample rate matches the hardware’s native rate whenever possible.
Avoid Audio Buffer Underruns If the CPU is under heavy load, the WASAPI callback may not receive data in time, leading to “pops” or “clicks.” If you encounter this, increase the Callback Buffer Frame Size in the Windows platform settings. While this increases latency slightly, it prevents the “elimination” of audio quality during frame rate dips.
Use Audio Buses for Routing Instead of playing captured audio directly to the master output (which causes feedback), route the output of the AudioCapture component to an Audio Bus. You can then use this bus as a source for Niagara visualizers or MetaSounds, effectively “eliminating” unwanted feedback loops.
Verify Exclusive Mode Requirements By default, WASAPI runs in Shared Mode. If your application requires ultra-low latency (e.g., a professional audio tool), you might consider Exclusive Mode, but be aware this will “eliminate” the ability of other Windows applications (like Discord or Spotify) to use that specific audio device.
Debug with LogAudioMixer If the microphone is not picking up sound, check the Output Log for LogAudioMixer entries. The AudioCaptureWasapi module will log the specific hardware format it has negotiated with Windows, which is essential for identifying “invalid format” errors.
Check Windows Privacy Settings A common “elimination” of audio input is the Windows 10⁄11 “Microphone Privacy” setting. If “Allow desktop apps to access your microphone” is toggled off, the WASAPI module will initialize successfully but will only receive silent buffers (zero voltage).
Leverage MetaSounds for Processing Capture raw input via this module and pipe it into a MetaSound using the AudioCapture node. This allows you to apply real-time filters, gates, or “elimination” of background noise before the audio is used for gameplay logic or recorded to disk.