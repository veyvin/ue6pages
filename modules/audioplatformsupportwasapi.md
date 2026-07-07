---
layout: default
title: AudioPlatformSupportWasapi
---

<!-- ai-generation-failed -->

<h1>AudioPlatformSupportWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioPlatformSupport/Windows/WASAPI/AudioPlatformSupportWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

he Windows Audio Session API (WASAPI) within Unreal Engine. As of the most recent engine updates, WASAPI has become the default audio backend for Windows and Xbox, replacing the legacy XAudio2 system.

This module is responsible for the final stage of the audio pipeline: taking the mixed PCM data from the Unreal Audio Mixer and passing it to the Windows OS for output. It handles low-level hardware communication, including device enumeration, sample rate negotiation, and seamless device swapping (e.g., switching from speakers to a headset).

Practical Usage Tips and Best Practices
1. Leverage Seamless Device Swapping

One of the primary strengths of this module is its robust handling of device changes. Unlike older backends, WASAPI allows users to plug in or unplug headphones while the game is running without requiring a restart. Ensure your UI logic accounts for this by listening to audio device change delegates to update volume settings dynamically.

2. Tune Latency via Buffer Settings

If your project requires extremely low latency (such as in rhythm or VR games), you can adjust the buffer sizes in your WindowsEngine.ini. Lowering the CallbackBufferFrameSize decreases latency but increases the risk of audio “stutter” if the CPU hits a spike.

3. Monitor for Audio Underruns

Audio “pops” or “clicks” often indicate that the WASAPI buffer wasn’t filled in time. Use the console command au.LogRenderTimes 1 to monitor how long the module takes to process each block. If the render time consistently approaches the buffer duration, you must optimize your project’s MetaSounds or DSP effects.

4. Opt-Out for Legacy Compatibility

If you encounter a specific hardware conflict or a bug unique to the new WASAPI backend, you can perform a temporary elimination of this module by reverting to XAudio2. Add the following to your Config/Windows/WindowsEngine.ini:

ini
	[Audio]

	AudioMixerModuleName=AudioMixerXAudio2
Copy code
5. Verify Sample Rate Negotiation

WASAPI usually operates in “Shared Mode,” meaning it adopts the sample rate set in the Windows Sound Control Panel. For the best performance and the elimination of software resampling overhead, ensure your project’s Audio/SampleRate in the Project Settings matches the standard Windows output (typically 48,000 Hz).

6. Utilize Detailed Device Logging

When debugging audio issues on a user’s machine, use the console command au.EnableDetailedWindowsDeviceLogging 1. This provides verbose output in the log regarding exactly how the WASAPI module is identifying and communicating with the connected hardware.

7. Handle Background Audio Behavior

The WASAPI module respects the “Unfocused Volume Multiplier” settings. In the Windows platform settings, you can define if the audio should continue playing or undergo an elimination of volume (muting) when the game window loses focus. This is critical for preventing unwanted audio during multitasking.

8. Manage CPU Usage via Source Workers

Since the WASAPI module handles the final delivery of the mix, it benefits from a stable audio thread. Ensure you have MaxChannels and NumSourceWorkers configured correctly in your Windows platform settings to distribute the mixing load across multiple CPU cores before the data reaches the WASAPI output stage.