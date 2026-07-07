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

ing the Unreal Audio Engine’s capabilities. It provides the abstract base classes and interfaces—such as IAudioSpatialization, IAudioReverb, and IAudioOcclusion—that allow third-party plugins (like Steam Audio, Oculus Audio, or Project Acoustics) to override or enhance how sound is processed in 3D space.

It acts as the architectural “handshake” between the engine’s high-level audio mixer and specialized Digital Signal Processing (DSP) code, enabling custom solutions for acoustics, propagation, and spatial rendering.

Practical Usage Tips & Best Practices
1. Implement the Factory Pattern

When creating a custom audio plugin, you must inherit from the relevant factory class (e.g., IAudioSpatializationFactory). The engine uses these factories to discover your plugin and display it as an option in the Project Settings > Platforms > [Platform] > Audio dropdown. Without a factory implementation, the engine will not recognize your custom DSP logic.

2. Module Dependency Setup

To build a C++ audio extension, include AudioExtensions and AudioMixer in your Build.cs. AudioMixer is required because these extensions are designed to work with Unreal’s modern multi-threaded audio renderer.

C#
PublicDependencyModuleNames.AddRange(new string[] { "AudioExtensions", "AudioMixer" });
Copy code
3. Thread-Safety in ProcessAudio

The ProcessAudio function in your interface implementation is called on the Audio Render Thread, not the Game Thread. Avoid performing any heavy logic, memory allocations, or UObject manipulations here. Use thread-safe data structures to pass parameters from the game to the audio thread to prevent stalling the renderer.

4. Utilize Custom Settings Objects

Most interfaces in this module allow you to associate a custom USoundfieldEncodingSettings or UAudioSpatializationSettings object. This is the best practice for exposing plugin-specific parameters (like “Room Size” or “Wall Material”) to sound designers via the Details panel in the Editor.

5. Leverage Source Data Override

For complex acoustics projects, use the Source Data Override interface. This “kitchen-sink” approach provides a callback with access to the raw FWaveInstance data. This allows your plugin to completely control every parameter of a sound—including its position, volume, and pitch—based on your own baked propagation data.

6. Efficient Handle Management

The module uses unique IDs to track sound sources across the engine. In your OnInitSource implementation, create a local map to track these IDs. Always clean up your internal buffers in OnReleaseSource to ensure the elimination of memory leaks when sounds stop playing or actors are destroyed.

7. Combine with MetaSounds

Custom spatialization extensions work seamlessly with MetaSounds. If your plugin requires specific per-source data, you can pass parameters from a MetaSound graph to your C++ extension, allowing for a hybrid approach where high-level logic is handled in the graph and low-level DSP in C++.

8. Use AudioLink for External Engines

If you need to send audio to an external middleware or a separate process entirely, look into the AudioLink classes within this module. AudioLink provides a standardized way to “tap” into a Submix or a Source and stream that audio out of Unreal while maintaining synchronization with the engine’s clock.