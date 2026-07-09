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

ine that defines the core interfaces and base classes for extending the audio engine’s capabilities. It provides the “hook points” for developers to create modular audio features such as custom spatialization, occlusion, reverb, and source data overrides.

By utilizing this module, developers can integrate third-party audio solutions (like Google Resonance, Oculus Audio, or Microsoft Project Acoustics) or write custom DSP (Digital Signal Processing) logic that operates directly within the Unreal audio pipeline without modifying the engine’s core source code.

Practical Usage Tips and Best Practices
1. Use for Plugin Interoperability

If you are developing a custom audio effect, inherit from the interfaces defined in this module (e.g., IAudioSpatialization, IAudioOcclusion). This ensures your plugin is compatible with the “Audio Plugin” dropdown menus in Project Settings, allowing users to swap between different spatialization backends easily.

2. Implement Source Data Overrides

One of the most powerful features in this module is the IAudioSourceDataOverride interface. Use this to intercept and modify raw source data before it reaches the renderer. This is ideal for advanced propagation systems where you need to change a sound’s position or volume based on complex geometric calculations (like portals or diffraction).

3. Favor Submix Effects for Efficiency

While the module allows for per-source effects, applying reverb or complex DSP through the IAudioReverb interface at the Submix level is generally more performant. Processing a mixed buffer of audio rather than dozens of individual sources prevents CPU “elimination” caused by excessive DSP overhead.

4. Create Custom Settings Assets

When implementing an audio extension, inherit from UAudioSpatializationSettings or UAudioOcclusionSettings. This allows you to create Data Assets that designers can use to tweak your plugin’s parameters (e.g., absorption coefficients or room dimensions) directly within the Unreal Editor.

5. Thread Safety is Mandatory

Logic within AudioExtensions classes often runs on the Audio Render Thread, not the Game Thread. Avoid accessing UObjects or AActor variables inside your DSP callbacks. Instead, cache the necessary numerical data into thread-safe structs during the initial setup or via the OnPostSourceInit callbacks.

6. Handle Hardware Changes Gracefully

Audio devices can be disconnected or swapped during a session. Ensure your implementation handles the OnListenerShutdown or OnListenerInitialize events. Failing to clean up resources when a listener is “eliminated” or reassigned can lead to memory leaks or stale audio pointers.

7. Leverage MetaSounds Integration

Modern audio workflows heavily utilize MetaSounds. When writing extensions, ensure they are compatible with the IAudioParameterInterface. This allows your custom spatialization or occlusion data to be driven dynamically by MetaSound nodes, providing a more expressive workflow for sound designers.

C++ Interface Example: Custom Spatialization

To create a custom spatialization plugin, you would implement the interface provided by this module:

C++
	#include "IAudioExtensionPlugin.h"

	 

	class FMySpatializationPlugin : public IAudioSpatialization

	{

	public:

	    // This is called for every source using this plugin

	    virtual void ProcessAudio(const FSoundSourceData& SourceData, FSinglePrecisionAudioBuffer& InSamples, FSinglePrecisionAudioBuffer& OutSamples) override

	    {

	        // 1. Analyze SourceData (Position, Velocity, Rotation)

	        // 2. Apply custom HRTF or Panning math to InSamples

	        // 3. Write processed audio to OutSamples

	    }

	    

	    virtual void OnSourceTerminated(const uint32 SourceId) override

	    {

	        // Clean up resources for this specific sound source

	    }

	};
Copy code
Performance & Best Practices
Module Dependency: Add "AudioExtensions" to your PrivateDependencyModuleNames in Build.cs.
Avoid Allocations: Never use new, malloc, or TArray::Add inside the ProcessAudio loop. Pre-allocate all buffers during initialization to ensure real-time performance.
Debugging: Use the console command au.Debug.Spatialization 1 to visualize how your extension is interacting with listeners and sources in the world.