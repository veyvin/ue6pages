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

nreal Engine’s native Audio Mixer for systems that use the Simple DirectMedia Layer (SDL) as their hardware abstraction layer.

Description and Purpose

This module serves as the bridge between Unreal Engine’s digital signal processing (DSP) graph and the audio hardware via the SDL library. In Unreal Engine 5.6 and 5.7, it is the primary audio backend for Linux and the Valve Steam Deck. Its purpose is to handle the initialization of audio devices, manage hardware buffer callbacks, and ensure that mixed audio data is delivered to the system’s audio server (such as PulseAudio or PipeWire) with high fidelity and cross-platform consistency.

Practical Usage Tips and Best Practices
SDL Version Awareness (UE 5.7)
With the release of Unreal Engine 5.7, the Linux backend has transitioned to SDL3. If you are writing custom extensions for this module or linking third-party audio libraries, ensure you update your Build.cs to reference the SDL3 module and update your include paths (e.g., #include "SDL3/SDL.h").
Standardize for Steam Deck Development
Since the Steam Deck utilizes this module, use it as your primary testing ground for Linux audio performance. Because the Audio Mixer is software-based, it ensures that your submix effects and spatialization sound identical on the Steam Deck as they do on Windows.
Configure via Linux Engine.ini
You can explicitly define the audio mixer module in your project’s LinuxEngine.ini to ensure it initializes correctly:
ini
	[Audio]

	AudioMixerModuleName=AudioMixerSDL
Copy code
Optimize for PipeWire/PulseAudio Latency
On Linux, the AudioMixerSDL performance depends on the underlying system’s audio daemon. Use the environment variable SDL_AUDIO_DRIVER=pulse or SDL_AUDIO_DRIVER=pipewire to force SDL to use the most efficient driver for your specific Linux distribution, which helps eliminate audio stuttering or crackling.
Leverage SDL Logging
In UE 5.7, SDL logging is hooked directly into the Unreal Engine log system. You can monitor audio-related issues by looking for the LogSDL3 (or LogSDL2 in older versions) category in your output log to debug device initialization failures or sample rate mismatches.
Match Hardware Sample Rates
Linux audio servers often run at 48,000Hz. To avoid the CPU overhead of software resampling within the AudioMixerSDL module, set your project’s audio sample rate to 48kHz. This reduces the workload on the Steam Deck’s APU, preserving battery life for gameplay.
Handle Audio Device Hotplugging
SDL provides robust support for device changes (e.g., plugging in USB headphones). The AudioMixerSDL module handles these events, but you should verify your game’s UI responds correctly to the “Audio Device Changed” delegate to ensure the player isn’t left without sound during a critical gameplay moment.
Reliable Feedback for Elimination Events
In competitive Linux/Steam Deck titles, audio clarity is vital. Ensure that critical SFX, such as an elimination notification, are routed through a high-priority Sound Class. The AudioMixerSDL module will prioritize these mixed streams, ensuring the elimination sound is never “crushed” by the OS-level audio compression during high-intensity scenes.