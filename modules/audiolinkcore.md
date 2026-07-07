---
layout: default
title: AudioLinkCore
---

<!-- ai-generation-failed -->

<h1>AudioLinkCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioLink/AudioLinkCore/AudioLinkCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

igned to bridge the Unreal Audio Engine with external audio middleware and software. It functions similarly to how “Live Link” works for animation, allowing Unreal to “stream” its audio data to an external renderer (like Wwise, FMOD, or a Digital Audio Workstation) rather than outputting it directly to the hardware.

This module is primarily used by technical sound designers and middleware developers to create hybrid audio pipelines. It enables projects to use the strengths of both engines—for example, using MetaSounds for procedural sound generation within Unreal while using an external middleware for complex spatialization, mixing, and profiling.

1. Understand the Transmission Types

AudioLink can transmit data at different levels of the signal chain. You should choose the level that fits your workflow:

Sources: Sends raw PCM data from Sound Waves, Sound Cues, or MetaSounds.
Submixes: Sends the summed audio of a specific Submix (e.g., all “Footsteps”).
Audio Components: Sends data specifically from an individual component, often used for specialized spatialization.
2. Configure via Sound Attenuation

For individual sound sources, AudioLink settings are managed through Sound Attenuation assets. Inside the asset, look for the Attenuation (AudioLink) section. Here you can toggle “Enable Send to AudioLink” and override specific settings. This allows you to selectively choose which sounds are processed by Unreal and which are sent to the external middleware.

3. Prevent Stacking and Volume Spikes

A common mistake is sending both a Source and its parent Submix to AudioLink simultaneously. This can cause the same audio data to be received twice by the external software, leading to “stacking,” which results in phasing or dangerously loud volume levels. Ensure your routing logic is clean to eliminate these artifacts.

4. Leverage MetaSounds for External Processing

AudioLink allows you to use MetaSounds as a powerful synthesizer or procedural generator that outputs directly into your middleware of choice. This is excellent for games that require the dynamic, logic-driven capabilities of MetaSounds but need to maintain the professional mixing environment of an external tool like Wwise.

5. Utilize the IAudioLinkFactory for Custom Tools

If you are a C++ developer building a custom audio tool or integration, you must derive from IAudioLinkFactory. This is the entry point for the module. Note that you can only register a single factory object per implementation; attempting to register multiple factories will result in a fatal error during engine startup.

6. Optimize with Submix Isolation

To save CPU and bandwidth, don’t send every sound to AudioLink. Instead, route only the sounds that require external processing into a specific Submix. In that Submix’s details panel, enable the “Send to Audio Link” flag. This keeps your external middleware project clean and focused only on the sounds that truly benefit from it.

7. Performance and Thread Safety

AudioLink is designed to be high-performance, but it requires thread-safe implementations. When writing custom C++ logic for AudioLink, ensure that all calls dispatched to the external engine are lockless where possible. Blocking the audio thread to wait for an external middleware response will eliminate the smoothness of your game’s audio and potentially cause hitches.

8. Use for Digital Audio Workstation (DAW) Workflows

Beyond middleware, AudioLink can be used to route Unreal’s audio into a DAW for real-time recording or cinematic mixing. This is a powerful feature for virtual production, allowing a sound engineer to mix the game’s live output using professional-grade hardware and plugins as if it were a traditional studio session.