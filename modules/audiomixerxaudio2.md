---
layout: default
title: AudioMixerXAudio2
---

<!-- ai-generation-failed -->

<h1>AudioMixerXAudio2</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/AudioMixerXAudio2/AudioMixerXAudio2.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, AudioMixerCore, Core, CoreUObject, Engine, WindowsMMDeviceEnumeration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd for Unreal Engine’s native Audio Mixer on Windows and Xbox. It implements the low-level communication between Unreal’s cross-platform audio engine and Microsoft’s XAudio2 API.

While the core audio logic (mixing, MetaSounds, effects) is handled by the AudioMixer module, AudioMixerXAudio2 is the “last mile” that sends the final mixed audio buffers to the sound card. It handles device discovery, speaker configuration (Stereo, 5.1, 7.1), and hardware-level sample rate conversion.

1. Verify Backend Activation

On Windows, this module should be the active audio renderer by default. You can confirm this in your log files by looking for: LogAudioMixer: Display: Using Audio Mixer: AudioMixerXAudio2. If your project is accidentally using a legacy backend, you will lose access to modern features like MetaSounds and real-time submix effects.

2. Tuning Latency and Buffer Stability

You can adjust the performance of this module in the project’s WindowsEngine.ini file under the [Audio] section.

Best Practice: Adjust AudioCallbackBufferFrameSize. Smaller values (e.g., 256 or 512) reduce the delay for input-driven sounds like gunshots, but values that are too low can cause “crackling” if the CPU hits a spike. 1024 is the standard balance for most desktop games.
3. Handle Device Swapping Gracefully

XAudio2 is sensitive to “Device Lost” events (e.g., a player unplugging a USB headset).

Tip: Unreal’s implementation via this module handles most reconnections automatically, but you should still bind logic to the OnAudioDeviceChange delegate in your game’s UI to prompt the user or pause the game if the primary output device is eliminated.
4. Speaker Configuration and Spatialization

This module automatically detects the Windows speaker settings. If a user has “Windows Sonic” or “Dolby Atmos for Headphones” enabled, AudioMixerXAudio2 will pass the audio data accordingly.

Best Practice: Ensure your Sound Attenuation assets are set to “Spatialization Method: Panning” for standard surround, or use a binaural plugin (like Microsoft Spatial Sound) for a 3D HRTF experience.
5. Managing Platform Headroom

To prevent digital clipping when many loud sounds play at once, you can set the PlatformHeadroomDB in your Windows platform settings (managed by this module).

Tip: Setting this to a value like -3.0 provides a small buffer that prevents the final mix from distorting at peak volumes, effectively eliminating harsh digital “clipping” artifacts.
6. Debugging with “stat audio”

Because this module sits at the end of the chain, it is the best place to monitor final output health. Use the console command stat audio or au.Debug.Graph 1.

Insight: Monitor the “CPU Time” and “Active Voices.” If the CPU time for the Audio Thread exceeds your buffer window (e.g., ~21ms for a 1024 buffer at 48kHz), the XAudio2 backend will stutter.
7. Coordinating Sample Rates

Windows usually defaults to 48,000Hz. If your source assets are 44,100Hz, this module must perform a sample rate conversion.

Best Practice: To minimize CPU overhead and maintain the highest quality, import your audio assets at 48kHz to match the native rate of the XAudio2 backend on most modern Windows systems.
8. Use for Virtual Production and nDisplay

In virtual production environments using nDisplay, this module manages how audio is routed across multiple nodes.

Tip: Ensure that only the “Primary” node is outputting audio through the XAudio2 device to avoid echoing or phasing across different machines in the volume. This can be toggled via command-line arguments when launching the engine.