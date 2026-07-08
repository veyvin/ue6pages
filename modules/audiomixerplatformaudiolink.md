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

Engine’s internal Audio Mixer and the AudioLink abstraction layer. It provides the platform-specific implementation required to intercept audio buffers from the engine’s renderer and “link” them to external software, such as third-party audio middleware (Wwise, FMOD) or Digital Audio Workstations (DAWs).

Instead of outputting directly to hardware, this module allows UE to act as an audio producer, sending PCM (Pulse Code Modulation) data across a thread-safe circular buffer to an external consumer. This is the technology that enables features like MetaSounds to play inside a Wwise-driven project.

Practical Usage Tips and Best Practices
1. Handle the OnFormatKnown Delegate

AudioLink often initializes before the incoming audio format (sample rate, channel count) is fully determined. Always bind to the OnFormatKnown delegate in your implementation. You should only begin playback or data draining once this delegate fires to ensure the elimination of pitch-shifting or “speed-up” glitches caused by mismatched sample rates.

2. Configure Sound Attenuation for Routing

To send a specific sound to an external link, you must use a Sound Attenuation asset. In the details panel under Attenuation (AudioLink), enable “Enable Send to AudioLink.” This allows the module to route that specific source through the AudioLink pipeline rather than the standard spatialization path.

3. Manage Buffer Sizes Carefully

The circular buffer used by this module requires a balance between latency and stability. A buffer that is too large introduces audible delay, while one that is too small leads to underruns (silence or popping). It is best practice to set your buffer size to at least a 2:1 ratio relative to the consumer’s bitrate to maintain a steady stream.

4. Use Submix AudioLink for Group Routing

If you want to send an entire category of sounds (like all “Footsteps”) to an external engine, set the AudioLink on the Sound Submix level rather than individual sources. The AudioMixerPlatformAudioLink module will then capture the mixed output of that submix, which is much more CPU-efficient than managing dozens of individual source links.

5. Implement the AudioLinkBlueprintInterface

When dealing with Audio Components, you should implement the AudioLinkBlueprintInterface. This provides a standardized API (SetLinkSound, PlayLink) that allows your Blueprints to communicate with the C++ module logic, ensuring that your audio triggers are synchronized between UE and the external platform.

6. Monitor Thread Safety

The “Producer” (UE) and “Consumer” (External Engine) operate on different threads. The IAudioLink interface handles this via shared pointers, but if you are writing custom extensions, ensure you are using atomic operations or the provided thread-safe circular buffers to avoid the elimination of data integrity.

7. Avoid Redundant Spatialization

If you are sending audio to an external middleware like Wwise to handle 3D positioning, ensure that UE’s internal spatialization is disabled for those sources. Otherwise, the sound may be processed twice (once in UE and once in the middleware), leading to “doubling” artifacts and unnecessary CPU usage.

8. Verify Factory Registration

For AudioLink to function, the implementer must register an AudioLink Factory during the engine’s startup phase. If your links are not appearing or working, check the log to ensure the factory for your specific middleware (e.g., WwiseAudioLink) was correctly initialized by this module.