---
layout: default
title: AudioMixer
---

<!-- ai-generation-failed -->

<h1>AudioMixer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioMixer/AudioMixer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioExtensions, AudioLinkCore, AudioLinkEngine, AudioMixerCore, AudioPlatformConfiguration, Core, CoreUObject, Engine, HeadMountedDisplay, SignalProcessing, SoundFieldRendering, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or Unreal Engine. It replaced the legacy platform-specific audio backends with a unified, multi-platform architecture that performs all digital signal processing (DSP) in software.

This module is the “brain” of the audio system, responsible for source generation, distance attenuation, spatialization, and the processing of the submix graph. It allows for sample-accurate timing, procedural audio via MetaSounds, and real-time audio analysis.

Practical Usage Tips and Best Practices
1. Prioritize MetaSounds over Sound Cues

For all new development, use MetaSounds. The AudioMixer module is optimized specifically for MetaSounds’ DSP-graph architecture, offering far superior performance and sample-accurate control compared to the legacy Sound Cue system.

2. Manage the Submix Graph Efficiently

Think of submixes as a “flowing river.” Group sounds into submixes (e.g., “Ambience,” “Weapons,” “UI”) to apply effects like reverb or compression to multiple sources at once. This is significantly more performant than applying individual effects to every single sound source.

3. Use Quartz for Musical Accuracy

If your game requires audio to be perfectly synchronized with gameplay (like a rhythm game or procedural music), use the Quartz system. Quartz bypasses the Game Thread’s frame-rate fluctuations and schedules audio events directly on the AudioMixer’s render clock.

4. Monitor Audio Thread Performance

Audio glitches like “pops” or “clicks” are usually caused by the CPU being unable to fill the audio buffer in time. Use the console command stat audio or Unreal Insights to monitor the audio thread. If you see “Waited [x] ms for audio thread” warnings in the log, you need to optimize your DSP complexity.

5. Implement Distance-Based Effect Elimination

To save CPU cycles, perform the elimination of expensive real-time effects on sound sources that are far away. Use Sound Attenuation settings to drive Low-Pass Filters (LPF) or to stop the sound entirely when it falls outside the max attenuation radius.

6. Leverage Audio Modulation

Replace the legacy Sound Class/Sound Mix system with Audio Modulation. This allows you to create “Parameter Buses” that can dynamically control volume, pitch, or effect parameters via Blueprints or C++ without the overhead of the older, static Sound Class hierarchy.

7. Profile with Real-time Analysis

The AudioMixer allows for real-time FFT (Fast Fourier Transform) and envelope following. Use these tools to drive Niagara visual effects or gameplay logic. Always ensure you perform the elimination of these delegates when the visual effect is no longer active to reclaim CPU resources.

8. Adjust Platform Headroom

If your audio sounds distorted or clipped, it might be due to a lack of digital headroom. You can adjust the PlatformHeadroomDB in your project’s BaseEngine.ini under the [Audio] section to provide more “space” for the AudioMixer to sum multiple loud sounds without clipping.