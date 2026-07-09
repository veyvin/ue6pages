---
layout: default
title: AudioLinkEngine
---

<!-- ai-generation-failed -->

<h1>AudioLinkEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioLink/AudioLinkEngine/AudioLinkEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine to share its audio stream with external software, such as middleware (Wwise, FMOD) or digital audio workstations (DAWs). It provides the engine-side logic to capture PCM data from Sources, Submixes, or Audio Components and route it to an external consumer before it reaches the final hardware output.

This module is the “bridge” that enables developers to use Unreal-native features like MetaSounds while still utilizing the spatialization, mixing, or profiling tools of an external audio engine.

Practical Usage Tips and Best Practices
Implement IAudioLinkBlueprintInterface for Components For actor-based streaming, implement the IAudioLinkBlueprintInterface on your components. This provides a standardized API (SetLinkSound, PlayLink) that allows you to trigger sounds that are automatically “linked” to the external engine without manually writing data-buffer logic.
Configure via Sound Attenuation Assets Source-level transmission is managed through Sound Attenuation assets. Under the Attenuation (AudioLink) section, you can toggle “Enable Send to AudioLink.” This is the preferred way to “eliminate” the need for custom C++ when you want specific 3D sounds to be processed by external middleware.
Route Submixes for Group Processing Instead of linking every individual sound, route related sounds to a specific Submix and enable AudioLink on the submix itself. This is significantly more performant and allows you to apply external bus effects to entire categories of sounds (e.g., all “Elimination” sound effects) simultaneously.
Adjust Buffer Sizes to Balance Latency The module uses circular buffers (Producers/Consumers). If you experience “pops” or “clicks,” increase the buffer size in your AudioLink settings. However, keep the size as small as possible to “eliminate” latency between the Unreal gameplay event and the audio output from the external engine.
Use for Real-time Profiling AudioLink is a powerful debugging tool. By linking Unreal Audio to an external profiler, you can visually see where sounds are positioned in 3D space and audit their volume levels in real-time, helping you “eliminate” mixing issues that are difficult to diagnose in the standard Unreal viewport.
Add Module Dependencies in C++ When extending AudioLink or creating custom factories, you must include the module in your Build.cs.
C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "AudioLinkEngine", "AudioLinkCore" });
Copy code
Monitor “OnFormatKnown” Delegates When writing custom AudioLink implementations, always wait for the OnFormatKnown delegate to fire before starting playback. Since the audio format (sample rate/channel count) may not be available immediately upon link creation, this delegate ensures you “eliminate” initialization errors.
Avoid Double-Processing When sending a submix to an external engine via AudioLink, remember that the external engine is now responsible for the final output. Ensure you are not also playing that submix through the Unreal hardware output, or you will create a “doubling” effect that can lead to phase issues or uncomfortably loud audio.