---
layout: default
title: AudioMixerAndroid
---

<!-- ai-generation-failed -->

<h1>AudioMixerAndroid</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Android/AudioMixerAndroid/AudioMixerAndroid.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixerCore, Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

of Unreal Engine’s multi-platform Audio Mixer (the “native” audio renderer) for the Android operating system. It serves as the interface between the engine’s high-level audio systems and the low-level Android audio drivers.

Description

This module is responsible for the final stage of audio production on Android devices: it takes the mixed digital audio buffers from the engine and feeds them into the device’s hardware. It primarily utilizes the AAudio API for modern, low-latency performance on newer devices, while maintaining a fallback to OpenSL ES for older hardware. It handles the critical tasks of hardware-specific sample rate conversion, buffer management, and device-level volume control.

Practical Usage Tips and Best Practices
1. Prioritize AAudio for Low Latency

Modern Android devices support the AAudio backend, which is designed for high-performance, low-latency audio. In your DefaultEngine.ini under the [Audio] section, ensure the audio mixer is enabled. The AudioMixerAndroid module will automatically attempt to use AAudio on supported devices (Android 8.1+) to eliminate the “audio lag” often associated with mobile gaming.

2. Configure Callback Buffer Sizes

To balance performance and latency, you can tune the buffer sizes in Project Settings > Platforms > Android > Audio.

Lower values (e.g., 512 or 1024): Decrease latency but increase the risk of “crackling” or “popping” if the CPU hitches.
Higher values: Increase stability on low-end devices at the cost of slight audio delay.
3. Match Hardware Sample Rates

The AudioMixerAndroid module performs best when the engine’s sample rate matches the device’s native hardware rate (usually 48kHz). Mismatched rates force the module to perform software resampling, which increases CPU usage. Check the logs on a test device; the module will report the “Native Sample Rate”—ensure your project settings align with this value.

4. Manage Background and Suspend States

On Android, apps are frequently moved to the background. This module handles the suspension of the audio hardware to save battery and release resources to the OS. Ensure your gameplay logic accounts for this by using the OnApplicationSuspend delegates to pause any time-sensitive audio logic when the mixer is silenced by the OS.

5. Optimize for ARM Neon

Starting in version 5.4, the audio mixer includes significant optimizations for ARM Neon intrinsics (SIMD). When building your project, ensure you are targeting the arm64-v8a architecture. This allows the AudioMixerAndroid module to process audio blocks much faster, helping to eliminate performance bottlenecks during intense combat scenes.

6. Monitor for “Waited X ms for Audio” Warnings

If you see “Waited for audio thread” warnings in your logcat, it indicates that the game thread is stalling the audio mixer’s ability to fill its buffers. Because the AudioMixerAndroid module runs on a high-priority thread, you must ensure your Game Thread remains performant to avoid audio dropouts.

7. Handle Audio on Elimination Events

When many sound effects trigger simultaneously—such as during a massive team fight or a sudden player elimination—the mixer’s CPU cost spikes. Use Sound Concurrency settings to limit the number of active voices. This ensures the Android mixer isn’t overwhelmed, which would otherwise result in distorted sound or a crash.

8. Use Unreal Insights for Mobile Profiling

To specifically profile the AudioMixerAndroid module, use Unreal Insights with the Audio trace channel enabled while running on a physical device. This will show you the exact cost of the “AudioMixer Render Thread,” allowing you to see if specific submix effects (like reverb) are too heavy for your target mobile hardware.