---
layout: default
title: AudioMixerPlatformAudioLink
---

<!-- ai-generation-failed -->

<h1>AudioMixerPlatformAudioLink</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioLink/AudioMixerPlatformAudioLink/AudioMixerPlatformAudioLink.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioLinkEngine, AudioMixer, AudioMixerCore, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Unreal Audio Mixer designed to facilitate the “AudioLink” system. It provides the platform-level abstraction required to route Unreal’s internal audio buffers to external software or middleware (such as Wwise, FMOD, or custom VST-like environments) without bypassing the engine’s submix and source logic.

It is primarily used by developers who want to use MetaSounds or Unreal’s procedural audio features while still leveraging the advanced mixing and spatialization toolsets of external audio middleware.

1. Module Configuration

This module acts as a “bridge” between the engine’s hardware abstraction and external factories. To extend it or utilize it in a custom plugin, you must include it in your Build.cs:

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "AudioMixer", 

	    "AudioMixerPlatformAudioLink", 

	    "AudioLinkCore" 

	});
Copy code
2. Practical Usage Tips & Best Practices
Understand the Producer-Consumer Model

AudioLink operates using a Producer (Unreal) and a Consumer (External Software) pattern. The AudioMixerPlatformAudioLink manages a circular buffer of PCM data.

Best Practice: Ensure your external consumer drains the buffer at a rate that matches Unreal’s sample rate. If the consumer is too slow, it will cause a buffer overflow, “eliminating” the oldest audio data.
Match Sample Rates and Bitrates

AudioLink is highly sensitive to mismatched audio formats. When setting up an AudioLink factory, ensure the OnFormatKnown delegate is correctly handled. Most issues with “choppy” audio are caused by the external middleware attempting to consume at 48kHz when Unreal is outputting at 44.1kHz.

Use Submix Links for Hybrid Mixing

Instead of sending every individual source to AudioLink, send a specific Submix. This allows you to perform initial DSP (like MetaSound procedural effects) in Unreal, then send the “pre-mixed” group to external middleware for final environmental reverb or bus compression.

Manage Buffer Latency Carefully

The circular buffer size is a trade-off. A large buffer prevents underruns but adds latency.

Tip: For rhythmic gameplay (like a music game), aim for a 2:1 ratio of the consumer’s bitrate to keep latency low. If the buffer is too small, “elimination” of audio clarity will occur via stuttering.
Leverage the Shared Pointer Architecture

The module uses IAudioLink as an opaque type held by TUniquePtr. This ensures thread safety between the Audio Render Thread and the external middleware’s thread. Never attempt to manually manage the memory of the producer/consumer objects; let the shared pointers handle the “elimination” of the link when the source or submix is destroyed.

Use AudioLink for Virtual Production

In virtual production environments, you can use this module to stream Unreal’s audio directly into a Digital Audio Workstation (DAW). This allows a sound engineer to mix the game’s procedural audio in real-time alongside live-action dialogue, “eliminating” the need for complex patch-cables or hardware loops.

Validate with the “Send to AudioLink” Flag

In the Sound Attenuation or Submix settings, you must explicitly enable the “Send to AudioLink” flag. If you see active MetaSounds in the profiler but hear no output in your middleware, verify this flag first. It is the gatekeeper that tells the AudioMixerPlatformAudioLink to begin filling the circular buffer.

Monitor Performance with Middleware Profilers

When using this module, standard Unreal audio stats may not show the full picture. Use the external middleware’s profiler (like the Wwise 3D Game Profiler) to monitor the incoming streams. If the middleware reports “Starvation,” it indicates that the AudioMixerPlatformAudioLink is not being serviced fast enough by the engine’s main audio thread.