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

the Unreal Audio Mixer designed to facilitate the Audio Link framework. It acts as the platform-agnostic bridge that allows Unreal Engine to share its rendered audio data with external audio middleware or software (such as Wwise or FMOD) in real-time.

Instead of outputting audio directly to the system hardware, this module hooks into the Audio Mixer’s output stage and routes the pulse-code modulation (PCM) data to a “Link” interface, enabling hybrid workflows where Unreal handles some sounds (like MetaSounds) while external middleware handles others.

Practical Usage Tips and Best Practices
1. Use for Middleware Coexistence

The primary use case for this module is the elimination of the “either/or” choice between Unreal Audio and third-party middleware. If you want to use MetaSounds for procedural music but Wwise for environmental spatialization, this module provides the pipeline to feed MetaSound output directly into the Wwise mix.

2. Manage Buffer Latency Carefully

Because Audio Link involves passing buffers between two different audio engines, latency can accumulate. Use the Audio Link Settings asset to tune the buffer size. Smaller buffers reduce latency but increase the risk of “underrun” (audio pops). Aim for a 2:1 ratio relative to your consumer’s bitrate for the best stability.

3. Enable via Sound Attenuation

Transmission of individual sources via this module is typically toggled within a Sound Attenuation asset. Look for the AudioLink section in the attenuation settings. This allows you to selectively choose which sounds are sent to the external link and which remain internal to Unreal.

4. Avoid “Double Mixing”

Be careful not to send a sound to a Submix that is already being sent to Audio Link. If both the Submix and the individual Source are linked, the audio will “stack,” resulting in doubled volume and potential phase issues. Perform a manual elimination of redundant send paths in your submix hierarchy.

5. Leverage the OnFormatKnown Delegate

When implementing a custom consumer for the Audio Link data in C++, always wait for the OnFormatKnown delegate. Since the link is often established before the audio format (sample rate, channel count) is finalized, starting playback too early can lead to corrupted audio or crashes.

6. Profile with “Stat Audio”

Use the stat audio console command to monitor the overhead of the Audio Link. Sending dozens of high-fidelity sources to an external engine via this module increases CPU usage on the audio thread. If performance dips, consider sending a single combined Submix to the link instead of multiple individual sources.

7. Clean Up Link Instances

When a source or submix is no longer needed, the AudioMixerPlatformAudioLink module relies on smart pointers to manage the lifetime of the producer and consumer. Ensure your external middleware handles the elimination of the link instance correctly when it receives a null or terminated signal to prevent memory leaks.

8. Verify Channel Agnostic Settings

Audio Link is designed to be channel-agnostic, but your external middleware may not be. Ensure that the channel count being sent from the Unreal Audio Mixer (e.g., 5.1 or 7.1) matches the configuration expected by your external software to avoid dropped channels or incorrect spatial positioning.