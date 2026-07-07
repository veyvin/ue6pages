---
layout: default
title: AudioMixerCore
---

<!-- ai-generation-failed -->

<h1>AudioMixerCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioMixerCore/AudioMixerCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, SignalProcessing, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine 5 audio system. It defines the low-level architecture for the native audio renderer (the “Audio Mixer”), providing the interfaces and base logic needed to mix multiple audio sources, apply DSP effects, and output the final buffer to hardware.

Unlike legacy systems that relied on platform-specific APIs (like XAudio2 for Windows or OpenAL for others), this module ensures feature parity across all platforms. It allows next-generation features like MetaSounds, Quartz, and Submix Effects to function identically whether the game is running on a PC, console, or mobile device.

1. Verify Audio Mixer Status

The Audio Mixer is enabled by default in modern UE5 versions. However, if you suspect your project is falling back to a legacy backend, you can verify it in the log. Look for LogAudioMixer: Display: Using Audio Mixer. If this is missing, ensure your BaseEngine.ini or platform-specific .ini is not overriding the AudioMixerModuleName.

2. Manage the Audio Render Thread

The AudioMixerCore operates on its own high-priority Audio Render Thread, separate from the Game Thread.

Best Practice: Never perform heavy game logic, file I/O, or complex Blueprint calls within custom audio processor callbacks. Doing so will block the audio thread, leading to buffer underruns and the elimination of smooth audio playback (manifesting as pops or clicks).
3. Handle C++ UObject Safety

If you are writing custom C++ audio code, be extremely careful with UObject pointers on the audio thread.

Tip: Audio UObjects can be eliminated by Garbage Collection while the audio thread is still trying to access them. Always use TSharedPtr or ensure you are holding a strong reference on the Game Thread until the audio thread confirms it is finished with the asset.
4. Optimize Buffer Sizes for Latency vs. Stability

You can tune the mixer’s performance in Project Settings > Platforms > [Platform] > Audio.

Best Practice: Lowering the Callback Buffer Size reduces latency (the time between an event and its sound), which is vital for rhythm games. However, setting it too low on mobile or weak hardware can cause the audio thread to “starve,” resulting in distorted sound. Test thoroughly on target hardware to find the balance.
5. Transition from Sound Cues to MetaSounds

AudioMixerCore was designed to power MetaSounds. While Sound Cues are still supported, MetaSounds operate as native DSP graphs within the mixer.

Tip: Use MetaSounds to move logic-heavy audio (like procedural wind or complex engine sounds) into the mixer. This is significantly more efficient than using Blueprints to update parameters every frame, as it reduces Game Thread overhead.
6. Utilize Submixes for Signal Processing

The mixer uses a hierarchical Submix system. Use this module’s capability to group sounds (e.g., “Explosions,” “Voice”) into specific submixes.

Best Practice: Apply “Mastering” effects like compressors or limiters to the Submix level rather than individual sounds. This prevents clipping when many sounds play at once and allows for much easier overall mix control.
7. Troubleshooting Buffer Underruns

If you hear “stuttering” or “crackling,” check the Output Log for warnings like “Waited [x] ms for audio thread.”

Tip: This usually indicates the CPU is too busy with rendering or physics to feed the audio mixer’s buffers. Use the console command stat audio to see which sounds or effects are consuming the most time and consider reducing your max voice count or lowering DSP quality.
8. Use for Real-Time Analysis

The mixer allows for real-time analysis of any submix. By attaching an Audio Analyzer to a submix, you can pull frequency or amplitude data back to the Game Thread for visuals.

Tip: Use this for UI pulses or environmental reactivity. Since it’s built into the core mixer, the data is synchronized with what the player actually hears, ensuring visual and audio alignment.