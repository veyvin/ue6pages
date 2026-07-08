---
layout: default
title: AudioMixerWasapi
---

<!-- ai-generation-failed -->

<h1>AudioMixerWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/AudioMixerWasapi/AudioMixerWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, AudioMixerCore, AudioPlatformSupportWasapi, Core, CoreUObject, Engine, SignalProcessing, WindowsMMDeviceEnumeration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

kend for Unreal Engine. Introduced to replace the legacy XAudio2 path, it utilizes the Windows Audio Session API (WASAPI) to provide a more direct and robust connection between the engine and the operating system’s audio hardware.

What it is and What it’s used for

Starting with Unreal Engine 5.8, AudioMixerWasapi is the default audio mixer module on Windows. It is responsible for the low-level tasks of initializing audio devices, managing audio streams, and delivering the final mixed buffers from the engine to the system’s DAC (Digital-to-Analog Converter).

Primary uses include:

Low-Latency Output: Providing high-performance audio streaming with better control over buffer scheduling than legacy APIs.
Dynamic Device Swapping: Handling hardware changes, such as plugging in a headset or changing the default Windows playback device, without requiring a game restart.
Format Negotiation: Automatically matching the engine’s output to the native sample rate and channel configuration of the user’s hardware.
Xbox Parity: Using a unified backend architecture across both Windows PC and Xbox consoles.
Practical Usage Tips and Best Practices
1. Leverage Automatic Device Swapping

One of the primary advantages of this module is its robust handling of “Device Swaps.” You no longer need to write custom logic to detect when a user unplugs their headphones; the WASAPI backend handles the re-routing of the audio stream automatically, ensuring the audio experience is never interrupted.

2. Match Sample Rates for Performance

To eliminate the CPU overhead of software resampling, ensure your project’s sample rate (defined in DefaultEngine.ini under [Audio]) matches your target hardware—typically 48000 Hz. WASAPI performs best when it can pass buffers directly to the hardware without intermediate conversion.

3. Tune Buffer Sizes for Latency

In your project’s Windows platform settings, you can adjust the Callback Buffer Frame Size. A smaller buffer (e.g., 512) results in lower latency, which is critical for rhythm games or shooters. However, be cautious: if the buffer is too small, you may experience “underruns” (audible pops/clicks) if the CPU hits a momentary hitch.

4. Monitor via LogAudioMixer

When troubleshooting audio issues on Windows, filter your Output Log for LogAudioMixer. This module provides detailed feedback on which WASAPI device was initialized, the detected channel count (e.g., Stereo vs. 7.1), and whether it is running in “Shared” or “Exclusive” mode.

5. Handle Audio “Underruns”

If you hear “buzzy” or “choppy” audio, it is often due to an underrun. This happens when the WASAPI backend requests a buffer before the engine has finished rendering it. Use Unreal Insights to profile the Audio Thread and ensure your MetaSounds or complex Sound Cues aren’t exceeding the time allotted by your buffer size.

6. Opt-Out Fallback (If Necessary)

If you encounter a specific hardware compatibility issue with the new backend, you can revert to the legacy XAudio2 mixer by adding the following to your Config/Windows/WindowsEngine.ini:

ini
	[Audio]

	AudioMixerModuleName=AudioMixerXAudio2
Copy code

Note: This should only be used as a temporary troubleshooting step, as WASAPI is the intended future-proof standard.

7. Use for Procedural Audio Analysis

Because WASAPI provides a stable, low-latency stream, it is ideal for games using real-time spectral analysis (FFT). You can capture the output from a Submix and use it to drive Niagara VFX or gameplay logic with minimal delay between the sound occurring and the visual reaction.

8. Verify Exclusive Mode Settings

While Unreal typically runs in “Shared Mode” to allow other applications to play sound, WASAPI supports “Exclusive Mode” for ultra-low latency. Be aware that Exclusive Mode will eliminate the ability for other apps (like Discord or web browsers) to play audio simultaneously, so it should only be used in specialized professional or VR applications.