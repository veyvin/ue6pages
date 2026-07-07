---
layout: default
title: AudioMixerCoreAudio
---

<!-- ai-generation-failed -->

<h1>AudioMixerCoreAudio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Apple/AudioMixerCoreAudio/AudioMixerCoreAudio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixerCore, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

on of the Unreal Audio Mixer for Apple platforms, specifically macOS. It serves as the low-level interface between Unreal Engine’s internal audio renderer and the Core Audio framework provided by Apple.

While the module AudioMixerAudioUnit handles the higher-level “Audio Unit” graph (common to both iOS and macOS), AudioMixerCoreAudio manages the specific hardware endpoint interactions, device enumeration, and sample-rate negotiation for Mac desktops and laptops.

Practical Usage Tips and Best Practices
1. C++ Build Configuration

If you are writing low-level audio tools or hardware-specific extensions for Mac, you must include this module in your Build.cs. Always wrap it in a platform check to prevent build failures on Windows or Linux.

C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Mac)

	{

	    PublicDependencyModuleNames.Add("AudioMixerCoreAudio");

	}
Copy code
2. Synchronize Sample Rates

Core Audio on macOS is highly sensitive to sample rate mismatches between the OS and the application.

Best Practice: Check your Project Settings > Platforms > Mac > Audio > Sample Rate. To eliminate the CPU cost of software resampling, ensure this matches the “Default Output” setting in the macOS Audio MIDI Setup utility (typically 48000 Hz).
3. Optimize Buffer Sizes for Latency

Mac hardware is capable of very low-latency audio, which is critical for rhythm or action games.

Tip: Adjust the Callback Buffer Frame Size in the Mac platform settings. A value of 256 or 512 frames is usually the “sweet spot” for macOS. Setting it too high increases latency; setting it too low may cause “crackling” if the Game Thread hitches.
4. Handle System-Level Device Changes

Users on Mac frequently switch between built-in speakers, AirPods, and external thunderbolt interfaces.

Best Practice: The Core Audio module is designed to handle “Hot Plugging.” However, you should listen for the OnAudioDeviceDefaultDeviceChanged delegate in your C++ code to ensure that any custom submix effects or spatialization settings are re-validated when the hardware endpoint changes.
5. Debugging with Stat Commands

To verify that the Core Audio backend is performing correctly without dropped frames:

Command: Use stat audio or stat audiomixer in the console.
What to look for: Look at the “Buffer Generation Time.” If this value frequently exceeds the hardware buffer duration, the audio thread is being starved, and you will need to optimize your MetaSounds or DSP effects to eliminate the stuttering.
6. Support for Multi-Channel Aggregate Devices

Pro-audio users on Mac often use “Aggregate Devices” to combine multiple interfaces.

Tip: The AudioMixerCoreAudio module supports these virtual devices. If your game or tool requires more than standard stereo (e.g., for a 7.1 installation), ensure your Max Channels setting in the Project Settings is high enough to accommodate the aggregate device’s output.
7. Manage “Exclusive Mode” Behavior

Unlike Windows (WASAPI), macOS Core Audio handles mixing at the system level very efficiently.

Best Practice: Do not attempt to bypass the system mixer for “Exclusive Mode” on Mac unless you are building a dedicated DAW-like tool. Keeping the audio in “Shared Mode” allows system alerts and other apps to function, which is the expected behavior for Mac users.
8. Prevent Audio Clipping at the Driver Level

Core Audio has a very transparent but strict ceiling for digital signals.

Tip: Use the Platform Headroom DB setting in the MacEngine.ini file. Setting this to -3dB or -6dB provides a safety margin that helps eliminate digital clipping (distorted “crunchy” sounds) when many loud sound effects play simultaneously during intense gameplay.