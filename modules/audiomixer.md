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

traction layer for audio rendering. It replaced the legacy platform-specific backends to provide a unified code base across Windows, consoles, and mobile. It functions as the “rendering engine” for sound, adding together all audio sources, applying Digital Signal Processing (DSP), and handling the final output to the speaker hardware.

By moving audio processing to its own dedicated Audio Render Thread, the AudioMixer ensures that game logic hitches do not cause audio stuttering and allows for advanced features like MetaSounds, Submix effects, and real-time audio analysis.

Practical Usage Tips and Best Practices
1. Offload Logic to the Audio Render Thread

The AudioMixer operates on a specialized thread that is separate from both the Game Thread and the standard Audio Thread. When writing custom C++ audio effects, perform your heavy math within the OnProcessAudio callback. This ensures that even if your game’s frame rate drops, the audio continues to render smoothly, resulting in the elimination of “buzzy” or “choppy” artifacts.

2. Utilize Submixes for Global Processing

Instead of applying effects to individual sounds, route your sounds into Sound Submixes. The AudioMixer can then apply effects (like Reverb, EQ, or Compression) to the entire group at once. This is significantly more performant and allows for professional-level “mastering” of your game’s soundscape.

3. Monitor for Buffer Underruns

If you hear “pops” or “clicks,” check your logs for “Waited [x] ms for audio thread.” This indicates a buffer underrun. To fix this without increasing latency, look for the elimination of blocking calls (like I/O or memory allocation) in your custom audio C++ code, as the Audio Render Thread must never be stalled.

4. Leverage Audio Modulation for Dynamic Mixing

The AudioMixer supports the Audio Modulation plugin, which replaces legacy Sound Classes and Mixes. Use Parameter Buses to control volumes or filter cutoffs globally. This is more efficient than ticking every active sound component to update their volume individually.

5. Implement Thread-Safe UObject Access

A common cause of crashes in the AudioMixer is accessing a UObject on the Render Thread after it has been garbage collected on the Game Thread. Always use TWeakObjectPtr or ensure your audio C++ classes hold a strong reference to the asset until the sound has finished playing.

6. Use Quartz for Sample-Accurate Timing

For music or rhythm games, do not use Blueprints or Timers to trigger sounds, as they are bound to the Game Thread’s variable frame rate. Use Quartz, a feature of the AudioMixer that schedules audio events with sample-accurate precision, ensuring your beats never drift.

7. Profile with the Audio Insights Tool

Use the Audio Insights dashboard (introduced in UE5) to visualize how the AudioMixer is working in real-time. It allows you to see active voices, submix hierarchies, and CPU usage per effect, making the elimination of performance bottlenecks much easier.

8. Adjust Platform Headroom

If your game sounds distorted even at low volumes, you may be clipping the AudioMixer’s output. In your BaseEngine.ini (under [Audio]), you can adjust PlatformHeadroomDB to provide more “space” for your sounds to mix together before they hit the hardware limit.