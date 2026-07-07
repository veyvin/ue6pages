---
layout: default
title: AudioMixerAudioUnit
---

<!-- ai-generation-failed -->

<h1>AudioMixerAudioUnit</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Apple/AudioMixerAudioUnit/AudioMixerAudioUnit.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixerCore, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eal Engine’s modern Audio Mixer for the Apple ecosystem (macOS and iOS). It serves as the low-level hardware abstraction layer that interfaces between the engine’s platform-agnostic audio renderer and Apple’s AudioUnit API.

Its primary role is to initialize the hardware audio stream, manage the lifecycle of the AudioUnit (typically using the RemoteIO or VoiceProcessingIO subtypes), and provide a high-performance callback buffer where the engine’s mixed audio data is handed over to the OS for output.

Practical Usage Tips & Best Practices
1. Conditional Build.cs Inclusion

Since this module is strictly for Apple platforms, you must wrap its inclusion in a platform check within your Build.cs. Attempting to include it on Windows or Android targets will result in compilation errors.

C#
	if (Target.Platform == UnrealTargetPlatform.IOS || Target.Platform == UnrealTargetPlatform.Mac)

	{

	    PublicDependencyModuleNames.Add("AudioMixerAudioUnit");

	}

	```

	 

	#### 2. Configure for Background Audio (iOS)

	For iOS projects, the `AudioMixerAudioUnit` relies on your project's `Info.plist` settings to keep sound playing when the app is minimized. Ensure you have "App plays audio or streams audio/video using AirPlay" enabled in your **Project Settings > Platforms > iOS > Extra Background Modes**.

	 

	#### 3. Manage Sample Rate Mismatches

	Apple hardware often defaults to 44.1kHz or 48kHz depending on the device and connected peripherals (like AirPods). To minimize CPU overhead caused by OS-level resampling, set your project's sample rate to match the target device's native rate in `BaseEngine.ini`:

	```ini

	[/Script/Engine.AudioSettings]

	SampleRate=48000

	```

	 

	#### 4. Handle Audio Session Interruptions

	On iOS, the `AudioMixerAudioUnit` is subject to `AVAudioSession` interruptions (e.g., incoming phone calls). Use the engine’s `FCoreDelegates::ApplicationWillDeactivateDelegate` or audio-specific delegates to pause non-essential game logic when the AudioUnit is forcibly suspended by the OS.

	 

	#### 5. Optimization with Buffer Sizes

	You can tune the latency and stability of the Apple audio backend by adjusting the `CallbackBufferFrameSize` in your platform's `Engine.ini`. On iOS, smaller buffers (e.g., 256 or 512) provide lower latency for rhythm games but may cause "crackling" if the CPU hits 100%.

	```ini

	[Audio]

	CallbackBufferFrameSize=512

	```

	 

	#### 6. Utilize Voice Processing for VoIP

	If your game uses voice chat, the `AudioMixerAudioUnit` can be configured to use the `kAudioUnitSubType_VoiceProcessingIO`. This enables hardware-level echo cancellation and noise suppression provided by Apple, which is significantly more efficient than software-based solutions.

	 

	#### 7. Debugging via "stat audio"

	When running on a Mac or iOS device, use the console command `stat audio`. Look for the "Device" or "Backend" field; it should explicitly list **AudioUnit** as the active provider. If it shows "Null," the module failed to initialize, often due to missing microphone permissions or an occupied audio session.

	 

	#### 8. Monitor for "Waited X ms for Audio Thread"

	If you see these warnings in your Mac/iOS logs, it often means the `AudioMixerAudioUnit` callback is being starved. On Apple platforms, this is frequently caused by performing file I/O or heavy memory allocations on the main thread, which can occasionally block the high-priority audio callback thread in the Apple kernel.
Copy code
2. Configure for Background Audio (iOS)

The AudioMixerAudioUnit relies on your project’s Info.plist settings to maintain audio playback when the app is minimized. Ensure you have enabled “App plays audio or streams audio/video using AirPlay” in your Project Settings > Platforms > iOS > Extra Background Modes.

3. Match Hardware Sample Rates

Apple hardware defaults to 44.1kHz or 48kHz depending on the device. To minimize CPU overhead caused by OS-level resampling, set your project’s sample rate to match the target device’s native rate in BaseEngine.ini. This helps eliminate subtle audio artifacts and reduces latency.

ini
	[/Script/Engine.AudioSettings]

	SampleRate=48000
Copy code
4. Handle Audio Session Interruptions

On iOS, this module is subject to AVAudioSession interruptions (such as incoming phone calls). Use the engine’s FCoreDelegates::ApplicationWillDeactivateDelegate to pause non-essential audio logic when the AudioUnit is forcibly suspended by the OS to ensure a clean resume later.

5. Optimize Latency via Buffer Sizes

You can tune the latency and stability of the Apple audio backend by adjusting the CallbackBufferFrameSize in your platform’s Engine.ini. Smaller buffers (e.g., 256) provide lower latency for rhythm games but increase the risk of CPU underruns and “crackling” if the Game Thread is under heavy load.

ini
	[Audio]

	CallbackBufferFrameSize=512
Copy code
6. Utilize Voice Processing for VoIP

If your project requires voice chat, the module can be configured to use kAudioUnitSubType_VoiceProcessingIO. This enables hardware-level echo cancellation and noise suppression provided by Apple, which is significantly more efficient than software-based elimination of background noise.

7. Debugging via “stat audio”

When running on a Mac or iOS device, use the console command stat audio. Verify that the Device or Backend field explicitly lists AudioUnit as the active provider. If it shows “Null,” the module failed to initialize, often due to missing microphone permissions or an occupied audio session from another app.

8. Monitor for Audio Thread Starvation

If you see “Waited X ms for Audio Thread” warnings in your logs, the AudioUnit callback is being starved. On Apple platforms, this is frequently caused by performing heavy file I/O or memory allocations on the main thread, which can block the high-priority audio callback thread in the Apple kernel.