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

at enables high-performance, low-latency audio bridging between the Unreal Audio Engine and external audio middleware (such as FMOD or Wwise).

Instead of forcing a choice between Unreal’s native systems and external tools, AudioLink allows both to run in parallel. It transmits raw Pulse-Code Modulation (PCM) data from Unreal’s submixes, sources, or audio components directly into the external engine’s environment. This allows you to use Unreal-specific features like MetaSounds while still utilizing the sophisticated mixing and profiling tools of your preferred middleware.

Practical Usage Tips and Best Practices
1. Include the Module in Your Build Script

To implement a custom AudioLink factory or interact with the system via C++, you must add the module to your Build.cs.

C++
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "AudioLinkEngine", "AudioLinkCore" });
Copy code
2. Avoid “Double-Mixing” and Volume Stacking

A common mistake is sending a Submix to AudioLink while also letting it play through the main Unreal output.

Best Practice: When sending a submix to an external engine, ensure the “Mute” or “Output to Bus Only” logic is handled correctly. If both engines play the same signal, it will cause “stacking,” which results in distorted, loud audio that can eliminate the clarity of your mix.
3. Use for MetaSound Integration

AudioLink is the primary way to use MetaSounds within a Wwise or FMOD project.

Tip: You can generate complex, procedural audio in MetaSounds and route that specific source to an external middleware’s event. This allows you to keep your procedural logic in Unreal while using the middleware for final spatialization and distance attenuation.
4. Register a Single Factory Object

The AudioLink architecture relies on the IAudioLinkFactory interface.

Best Practice: Only register one factory object for your specific implementation (e.g., the Wwise AudioLink Factory). Registering multiple factories for the same link type will trigger a fatal assert and eliminate your ability to boot the engine.
5. Leverage Sound Attenuation Assets for Routing

You can enable AudioLink on a per-source basis without touching C++ by using Sound Attenuation Assets.

Action: In the Sound Attenuation asset’s Details panel, look under Attenuation (AudioLink). Here you can toggle “Enable Send to AudioLink” and provide specific settings, allowing for granular control over which sounds are handled by Unreal and which are sent to the external engine.
6. Ensure Thread Safety in Custom Factories

AudioLink calls are often dispatched from the Audio Render Thread.

Best Practice: If you are writing a custom factory to bridge Unreal to a new third-party library, ensure your implementation is thread-safe and ideally lockless. Blocking the audio thread to wait for an external engine will cause “pops” and “stutters” in the final output.
7. Monitor Performance via the 3D Profiler

When using AudioLink with middleware like Wwise, the external engine’s profiler can often “see” Unreal’s sources as if they were native middleware objects.

Tip: Use the middleware’s 3D game profiler to verify the position and attenuation of Unreal sources. This is a highly efficient way to debug spatialization issues and eliminate bugs where a sound’s 3D position in Unreal doesn’t match its perceived location in the mix.
8. Use AudioLink for Virtual Production and DAWs

Beyond game middleware, AudioLink is designed to bridge audio to Digital Audio Workstations (DAWs).

Tip: Use AudioLink to render Unreal’s real-time audio directly into a DAW for recording or further processing. This is extremely useful in Virtual Production environments where you need to sync high-quality procedural audio with a live broadcast or film recording.