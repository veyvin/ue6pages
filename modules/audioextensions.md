---
layout: default
title: AudioExtensions
---

<!-- ai-generation-failed -->

<h1>AudioExtensions</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioExtensions/AudioExtensions.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixerCore, Core, CoreUObject, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the standardized interfaces and base classes for expanding the Unreal Audio Engine. It provides the “contract” that allows third-party plugins and custom systems to hook into the engine’s audio pipeline.

What it is and What it’s used for

This module does not perform audio processing itself; instead, it provides the architecture for modular audio features. It defines how the engine communicates with external spatializers, reverb processors, and occlusion systems.

Primary uses include:

Defining Plugin Interfaces: Providing the base classes for IAudioSpatialization, IAudioReverb, and IAudioOcclusion.
Custom Settings Management: Enabling the creation of UAudioEndpointSettings and USoundfieldSettings which allow designers to configure third-party audio tools within the Unreal Editor.
Data Overrides: Utilizing the IAudioSourceDataOverride interface to modify sound source parameters (like position or volume) in real-time before they reach the renderer.
Audio Link Support: Providing the underlying structures for AudioLink, which facilitates sharing audio buffers between Unreal and external middleware (like FMOD or Wwise).
Practical Usage Tips and Best Practices
1. Implement IAudioSpatialization for Custom HRTFs

If you are developing a custom 3D audio solution or Head-Related Transfer Function (HRTF), inherit from IAudioSpatialization. This allows your plugin to receive raw audio buffers and listener/source positions directly from the engine, bypassing the default panning logic.

2. Use Source Data Overrides for Propagation

To implement advanced audio propagation (like sound traveling around corners), use the IAudioSourceDataOverride interface. This allows you to intercept a sound’s location and “virtualize” its position, making it sound as if it is coming from a doorway rather than directly through a wall.

3. Minimize Logic on the Audio Render Thread

When implementing the interfaces defined in this module, remember that the processing functions (like ProcessAudio) run on the Audio Render Thread. Avoid complex allocations, disk I/O, or heavy calculations here, as stalling this thread will cause audible pops and clicks.

4. Leverage Custom Settings Objects

If your audio plugin requires specific parameters (like “Room Size” or “Absorption”), create a class that inherits from UAudioExtensionPluginSettings. This automatically exposes those properties in the Sound Attenuation or Audio Volume settings in the editor, providing a seamless workflow for sound designers.

5. Thread-Safe Parameter Updates

Because audio parameters are set on the Game Thread but read on the Audio Render Thread, use a thread-safe “double buffering” or atomic approach when passing data. This ensures that your spatialization or occlusion logic doesn’t read partially updated data, which can eliminate jitter and crashes.

6. Optimize Per-Source vs. Submix Processing

For expensive effects like high-quality reverb, prefer implementing them at the Submix level rather than the Source level. The AudioExtensions module provides the hooks to apply effects to mixed buffers, which is significantly more performant than processing dozens of individual sound sources.

7. Use the Audio Link Factory

When integrating external audio middleware, use the IAudioLinkFactory interface provided by this module. This allows you to create a seamless bridge where Unreal’s MetaSounds or Sound Waves can be piped directly into external software for advanced processing.

8. Check Plugin Availability at Runtime

Before calling logic that depends on a specific audio extension, verify the plugin is active. You can query the AudioDevice to see which spatialization or occlusion plugin is currently selected in the Project Settings, preventing your code from calling into a null or inactive interface.