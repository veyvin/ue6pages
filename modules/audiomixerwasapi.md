---
layout: default
title: AudioMixerWasapi
---

<!-- ai-generation-failed -->

<h1>AudioMixerWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/AudioMixerWasapi/AudioMixerWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, AudioMixerCore, AudioPlatformSupportWasapi, Core, CoreUObject, Engine, SignalProcessing, WindowsMMDeviceEnumeration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r Windows and Xbox platforms. Starting with Unreal Engine 5.8, it serves as the default audio renderer, replacing the legacy XAudio2 backend. It interfaces directly with the Windows Audio Session API (WASAPI) to communicate with the operating system’s audio drivers.

Its primary role is to manage the hardware-level audio stream, handle device-swap logic (like plugging in headphones), and provide the low-latency buffer management required for real-time spatialization and MetaSounds.

Practical Usage Tips & Best Practices
1. Native Device Swap Handling

One of the primary advantages of this module is its robust support for Default Device Switching. Unlike legacy backends, AudioMixerWasapi automatically detects when the Windows default playback device changes (e.g., switching from speakers to a USB headset) and migrates the active audio stream without requiring a game restart.

2. Tuning for Low Latency

You can control the audio latency on Windows by adjusting the CallbackBufferFrameSize. Smaller values result in tighter response times for gameplay events but increase the risk of CPU underruns (audible “popping”).

Location: Config/Windows/WindowsEngine.ini
Typical Value: 512 or 1024 (Lower to 256 for rhythm-critical games).
3. Handling Sample Rate Mismatches

The module performs its best when the engine’s sample rate matches the Windows “Advanced” sound properties of the device. If the OS is set to 44.1kHz and the engine to 48kHz, the WASAPI backend must resample, which adds minor CPU overhead. For high-fidelity projects, advise users to set their Windows hardware to 48kHz.

4. Opting Out (XAudio2 Fallback)

If you encounter hardware compatibility issues or specific driver bugs with the new backend, you can revert to the legacy XAudio2 driver. This is useful for debugging whether an audio issue is related to the engine’s mix logic or the platform’s communication layer.

In WindowsEngine.ini:
ini
	[Audio]

	AudioMixerModuleName=AudioMixerXAudio2
Copy code
5. Exclusive Mode Considerations

While the WASAPI module primarily operates in “Shared Mode” (allowing other apps to play sound), it is architecturally capable of “Exclusive Mode.” However, avoid forcing Exclusive Mode in shipped products, as it will eliminate audio from all other applications (like Discord or web browsers), leading to a poor user experience.

6. Debugging with Console Commands

To verify that the WASAPI backend is active and functioning correctly, use the command au.Debug.Device 1. This will print the active device’s details, including its native format, latency, and the specific AudioMixerWasapi instance being used.

7. Avoiding Audio Thread Starvation

The WASAPI callback expects a constant stream of data. If your Game Thread or Audio Thread hitches (due to heavy loading or complex Blueprint logic), the module will run out of samples, causing a “buffer underrun.” Monitor for “Waited [X] ms for audio thread” in your logs to identify performance bottlenecks.

8. C++ Module Dependency

If you are writing custom low-level audio extensions for Windows/Xbox, you may need to include the module in your Build.cs. Wrap it in a platform check to ensure cross-platform compatibility:

C#
	if (Target.Platform == UnrealTargetPlatform.Win64 || Target.IsInPlatformGroup(UnrealPlatformGroup.Microsoft))

	{

	    AddEngineNodeCoreConfigurations();

	    PrivateDependencyModuleNames.Add("AudioMixerWasapi");

	}
Copy code