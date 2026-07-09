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

of Unreal Engine’s multi-platform Audio Mixer (the native audio renderer) for the Android OS. It acts as the final stage of the audio pipeline, responsible for taking the mixed digital audio buffers from the engine and sending them to the Android hardware. It handles the low-level interfacing with Android’s audio backends, specifically supporting both OpenSL ES and the modern, low-latency AAudio API.

Practical Usage Tips & Best Practices
1. Leverage AAudio for Low Latency

On modern devices (Android 8.1+), this module defaults to the AAudio backend. AAudio is designed for high-performance audio and significantly reduces the “round-trip” latency compared to the older OpenSL ES. Ensure your project is targeting a minimum SDK level that supports AAudio to give your players the most responsive experience.

2. Tune “Audio Callback Buffer Size”

In Project Settings > Platforms > Android > Audio, you can adjust the “Audio Callback Buffer Size.”

Best Practice: Lower values (e.g., 256 or 512) reduce the delay between a gameplay event and its sound. However, setting this too low on budget devices can cause CPU starvation, leading to “crackling” or “popping.” Test on mid-range hardware to find a stable balance.
3. Optimize with ARM NEON SIMD

The AudioMixerAndroid module is optimized for ARM processors. Starting in UE 5.4+, many hot-path functions (like Float-to-PCM conversion and buffer mixing) utilize ARM NEON instructions to process multiple audio samples simultaneously. This reduces the total CPU time spent on audio, which is critical for maintaining high frame rates on mobile.

4. Manage Audio Interruptions (Phone Calls)

This module handles Android system events like incoming phone calls or alarms. It is a best practice to use the OnApplicationWillDeactivateDelegate in your game logic to pause non-essential audio. The module will automatically handle the elimination of the audio stream when the OS takes focus and resume it when the user returns to the game.

5. Monitor “Waited [x] ms for audio thread”

If you see “Waited [x] ms for audio thread” warnings in your logcat while debugging an Android device, it means the hardware is consuming audio faster than the engine can provide it. To fix this, increase the Number of Buffers to Enqueue in the Android Audio settings to create a larger safety margin against performance spikes.

6. Handle Permissions for Capture

If your game uses microphone input (via AudioCaptureCore), this module works in tandem with the Android permissions system. You must ensure android.permission.RECORD_AUDIO is enabled in your Android Runtime Settings, or the audio mixer will be unable to initialize the input stream, resulting in silent VOIP.

7. Synchronize Elimination SFX with Haptics

For a premium feel on mobile, synchronize the audio of an elimination event with Android’s haptic feedback. Since this module provides the final timing for audio playback, using Force Feedback Assets triggered alongside sound ensures that the vibration and the “thud” of a character’s elimination reach the player’s hands at the exact same moment.

8. Use “Background Audio” Settings

By default, Android may kill audio when the app is backgrounded. If your game requires audio to persist (e.g., a music player or persistent world sounds), check the “Allow Background Audio” toggle in the Project Settings. Note that this will increase battery consumption and may be subject to stricter OS power-management rules.