---
layout: default
title: AudioCaptureAudioUnit
---

<!-- ai-generation-failed -->

<h1>AudioCaptureAudioUnit</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/IOS/AudioCaptureAudioUnit/AudioCaptureAudioUnit.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine audio capture interface designed for Apple platforms (iOS, macOS, and iPadOS). It bridges Unreal’s AudioCapture plugin with the native AudioUnit framework, allowing the engine to access hardware microphones and input devices.

It is primarily used to enable microphone input for features like real-time VOIP, spectral analysis (envelope following), and procedural audio effects on Apple devices.

1. Module Configuration

This module is a backend implementation. While you rarely call its classes directly, you must ensure the parent AudioCapture plugin is enabled in your .uplugin or .uproject. For C++ access to the underlying stream logic on Apple devices, include it in your Build.cs:

C#
	// MyProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.IOS || Target.Platform == UnrealTargetPlatform.Mac)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "AudioCapture", "AudioCaptureAudioUnit" });

	}
Copy code
2. Practical Usage Tips & Best Practices
Configure Info.plist Permissions

On iOS and macOS, audio capture will fail silently unless you provide a usage description. You must add the NSMicrophoneUsageDescription key to your project settings. Without this, the OS will “eliminate” the app process the moment it attempts to initialize the AudioUnit.

Handle Audio Session Interruptions

On iOS, the AudioUnit can be revoked by the OS (e.g., an incoming phone call). Use the FCoreDelegates::ApplicationWillDeactivateDelegate to stop your audio capture stream. Failing to handle interruptions can leave the AudioUnit in a zombie state, requiring a full app restart to recover microphone access.

Optimize Buffer Sizes for Latency

The AudioCaptureAudioUnit implementation is sensitive to the hardware’s preferred buffer size. If you need low-latency feedback (like a voice-reactive game mechanic), ensure your Audio Mixer settings in DefaultEngine.ini match the native sample rate of the device (usually 44.1kHz or 48kHz) to avoid costly resampling.

Check for Hardware “Elimination”

Users may disconnect headsets or Bluetooth mics during gameplay. Always check the return value of IsStreamOpen() before attempting to read audio data. If the hardware is disconnected, the AudioUnit backend will invalidate the stream, and you must re-initialize the component to detect the new default input.

Use Thread-Safe Enveloping

The native audio callback for AudioUnit runs on a high-priority system thread. If you are capturing audio to drive gameplay elements, do not perform logic inside the capture callback. Instead, use a thread-safe ring buffer or the built-in Audio Capture Component envelope follower to pass values to the Game Thread.

Manage Background Audio Modes

If your app needs to record audio while minimized (e.g., a background voice chat), you must enable the “Background Audio” capability in the iOS Project Settings. If this is disabled, the AudioCaptureAudioUnit module will be forced to stop the stream immediately upon the app entering the background.

Validate Mono vs. Stereo Input

Most Apple mobile devices provide mono input, but some Mac configurations provide stereo. Use GetCaptureDeviceInfo to query the channel count. Hard-coding a stereo buffer for a mono AudioUnit stream can result in “eliminated” audio data or silent channels in your submixes.

Monitor the Log for “Remote IO” Errors

If the microphone fails to start, check the Output Log for kAudioUnitErr_TooManyFramesToProcess or other Remote IO errors. These are specific to the Apple backend and usually indicate that the engine is requesting more data than the hardware buffer can provide, necessitating a change in your AudioBus settings.