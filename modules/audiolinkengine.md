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

of the AudioLink API. It serves as a hardware-abstraction bridge that allows the Unreal Audio Engine to share its audio data with external software or middleware (such as Wwise or FMOD) without requiring direct hardware access.

It acts as a “patch bay,” allowing you to route audio from Unreal’s native systems—like MetaSounds, Sound Cues, or Submixes—directly into an external engine’s environment. This enables developers to use Unreal’s procedural audio tools while maintaining a traditional middleware-based mixing and profiling workflow.

Practical Usage Tips and Best Practices
Understand the Three Link Types AudioLink can transmit data at different levels of the pipeline. You can send raw Sources (pre-attenuated data from Sound Waves), Submixes (mixed buffers from a group of sounds), or Audio Components. Choose the level that fits your needs to “eliminate” redundant processing; for example, send a Submix if you want to process a group of sounds as one unit in middleware.
Manage Module Dependencies If you are writing custom C++ factories or components that interface with AudioLink, you must include AudioLinkEngine and AudioLinkCore in your Build.cs.
C++
PublicDependencyModuleNames.AddRange(new string[] { "AudioLinkEngine", "AudioLinkCore" });
Copy code
Use Sound Attenuation for Source Routing To send a specific sound to AudioLink, you don’t always need a Blueprint node. You can enable the Send to AudioLink flag within a Sound Attenuation asset. This is a highly efficient way to “eliminate” manual setup for every actor, as the setting will apply to any sound using that attenuation profile.
Avoid Audio Stacking A common pitfall is sending both a Source and its parent Submix to AudioLink simultaneously. This causes the audio to “double up,” resulting in increased volume and potential clipping. Ensure your routing logic is clear to “eliminate” the risk of signal stacking in the external engine.
Leverage MetaSounds for Middleware AudioLink allows you to use MetaSounds as a powerful synthesizer or procedural generator while still using Wwise for spatialization. Route the MetaSound output to AudioLink, and the middleware will treat it like a standard input stream, “eliminating” the need to choose between one system or the other.
Implement Thread-Safe Factories If you are extending IAudioLinkFactory in C++, ensure your implementation is thread-safe and ideally lockless. The Audio Engine calls these functions on a high-priority audio thread; any blocking logic can “eliminate” the stability of your game’s frame rate and cause audio glitches.
Deep Linking with AudioComponent For specialized cases like ray-traced spatialization, use the AudioLinkBlueprintInterface. This standardized interface allows you to use SetLinkSound and PlayLink on components, giving you fine-grained control over when a specific component’s audio is “eliminated” or sent to the external backend.
Profile with the 3D Game Profiler When AudioLink is active (specifically with Wwise), you can often see Unreal’s sounds inside the middleware’s 3D profiler. Use this to “eliminate” spatialization bugs by verifying that the positions sent from Unreal match the expected coordinates in the middleware’s world space.