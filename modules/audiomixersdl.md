---
layout: default
title: AudioMixerSDL
---

<!-- ai-generation-failed -->

<h1>AudioMixerSDL</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Linux/AudioMixerSDL/AudioMixerSDL.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, AudioMixerCore, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

real Engine Audio Mixer that utilizes the Simple DirectMedia Layer (SDL) library. While platforms like Windows and macOS have dedicated backends (XAudio2 and AudioUnit, respectively), AudioMixerSDL serves as the primary audio renderer for Linux and was historically used for HTML5. It ensures that the engine’s high-level audio features—like MetaSounds and real-time DSP—function consistently on operating systems where specialized proprietary audio APIs are unavailable.

Practical Usage Tips & Best Practices
1. Transition to SDL3 in UE 5.7

With the release of Unreal Engine 5.7, the engine has migrated from SDL2 to SDL3. If you are writing custom C++ that interacts with this module, you must update your Build.cs dependencies to SDL3 and update your header includes from #include "SDL.h" to #include "SDL3/SDL.h".

2. Tune Buffer Sizes for Linux Performance

On Linux systems, audio “crackling” or “popping” is often caused by the OS being unable to keep up with the audio thread.

Best Practice: If you encounter glitches, increase the CallbackBufferFrameSize in your LinuxEngine.ini under the [Audio] section. A value of 1024 is generally safe for most Linux distributions, while 512 provides better latency for rhythm-heavy games.
3. Monitor “LogSDL3” for Hardware Issues

The AudioMixerSDL module hooks into Unreal’s logging system. If a user’s audio device fails to initialize, the details will be printed under the LogSDL3 category. Use this to identify if a failure is due to missing pulse-audio drivers or ALSA configuration issues on the host machine.

4. Debug with “au.Debug.AudioThread”

Because SDL acts as a middleman between Unreal and the Linux sound server (like PipeWire or PulseAudio), it can be susceptible to thread hitches. Use the console command au.Debug.AudioThread 1 to see if the engine is stalling while waiting for the SDL callback, which is a common sign of CPU starvation on the main game thread.

5. Handle Device Swapping Logic

SDL3 provides improved support for hot-swapping audio devices (e.g., plugging in a USB headset). The AudioMixerSDL module listens for these system events. Ensure your game UI responds to the OnAudioDeviceChange delegate to update the player’s settings menu without requiring a restart of the application.

6. Clean Up Resources for Elimination

When a game session ends or an audio-emitting actor undergoes elimination, ensure that active sound streams are properly stopped. On Linux, if the SDL audio device is not correctly released or if too many virtual voices remain active, it can lead to a “zombie” process that holds the hardware lock even after the game has closed.

7. Verify SDL Environment Variables

You can override SDL’s behavior without recompiling the engine by using environment variables. For example, if a user has issues with the default audio driver, they can set SDL_AUDIO_DRIVER=alsa or SDL_AUDIO_DRIVER=pulseaudio before launching the executable. This module will respect these overrides during initialization.

8. Use for Dedicated Server “Headless” Audio

While dedicated servers usually do not need audio, some logic (like audio-driven gameplay triggers) may still require an audio device to exist. The AudioMixerSDL module can be configured to use the “dummy” audio driver, allowing the engine to “play” sounds in a headless environment to ensure that elimination events triggered by sound analysis still fire correctly on the server.