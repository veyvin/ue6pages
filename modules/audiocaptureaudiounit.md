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

end for Unreal Engine’s AudioCapture system on macOS and iOS. It serves as the bridge between the engine’s generic audio capture interface and Apple’s native AudioUnit and CoreAudio frameworks.

This module is responsible for initializing the hardware microphone, managing the input buffer callbacks, and feeding that raw PCM data into the Unreal audio mixer for processing, spatialization, or analysis.

Practical Usage Tips and Best Practices
1. Conditional Build Configuration

Because this module relies on Apple-specific system frameworks, it should only be referenced in your Build.cs when targeting those platforms. It is typically a dependency of the AudioCapture plugin.

C#
	if (Target.Platform == UnrealTargetPlatform.IOS || Target.Platform == UnrealTargetPlatform.Mac)

	{

	    // Usually managed by the AudioCapture plugin, but for custom backends:

	    PublicDependencyModuleNames.Add("AudioCaptureAudioUnit");

	}

	```

	 

	#### 2. Mandatory Info.plist Permissions

	On iOS and macOS, audio capture will fail silently without the proper privacy keys. Ensure your project's `Info.plist` includes the **NSMicrophoneUsageDescription**. Without this, the OS will terminate the application immediately upon attempting to initialize the `AudioUnit`.

	 

	#### 3. Manage iOS Audio Session Categories

	For iOS, this module's performance is tied to the `AVAudioSession` category. If your game requires recording while playing background music or other audio, ensure your project settings are configured to use a "PlayAndRecord" category with "MixWithOthers" to prevent the engine from silencing other apps.

	 

	#### 4. Latency and Buffer Size Tuning

	The `AudioCaptureAudioUnit` module is sensitive to the hardware's preferred buffer size. You can tune the latency vs. stability trade-off using the console variable `au.CaptureBufferFrameSize`. Lower values reduce latency for real-time applications (like voice-driven mechanics) but increase the risk of "crackling" due to buffer underruns.

	 

	#### 5. Match Engine and Hardware Sample Rates

	To avoid expensive software resampling, try to ensure your project's `Audio Callback Rate` (in Project Settings) matches the hardware's native rate (typically 48kHz or 44.1kHz). If the module has to resample inside the AudioUnit callback, it can significantly increase CPU overhead on mobile devices.

	 

	#### 6. Graceful Stream Elimination

	When a character is destroyed or a recording session ends, ensure you explicitly call `Stop()` and then allow the system to perform the **elimination** of the capture stream. On Apple platforms, failing to properly close an AudioUnit can leave the "Microphone in use" indicator (the orange dot) active even after the game logic has stopped using it.

	 

	#### 7. Handle Audio Session Interruptions

	On iOS, a phone call or an alarm can trigger an "Audio Session Interruption." While the module handles the basic resumption, you should listen for these interruptions in C++ to pause your game-side audio processing, as the `AudioUnit` callback will stop providing data until the interruption ends.

	 

	#### 8. Verify Device Names for Multi-Input macOS

	On macOS, unlike iOS, there may be multiple input devices (e.g., MacBook Mic, USB Headset, Audio Interface). Use the `FAudioCapture` factory to enumerate devices; the `AudioCaptureAudioUnit` module will use the "System Default" unless you explicitly provide the `DeviceID` found during enumeration.
Copy code
2. Mandatory Info.plist Permissions

On both iOS and macOS, the NSMicrophoneUsageDescription key must be present in your Info.plist. Without this, the OS will block the AudioUnit from initializing. On iOS, failing to provide this string will cause the application to terminate immediately upon attempting to open the audio stream.

3. Match Hardware Sample Rates

To avoid the CPU overhead of software resampling, try to match the engine’s audio processing rate to the hardware’s native rate (usually 48kHz). If the AudioCaptureAudioUnit module has to perform a sample rate conversion inside the high-priority audio callback, it can lead to performance hits on mobile devices.

4. Configure iOS Audio Session Category

On iOS, the microphone will only work if the AVAudioSession is set to a category that supports recording, such as PlayAndRecord. Ensure your project settings are configured to allow “Ambient” or “MixWithOthers” if you need the microphone to function while other system sounds are playing.

5. Handle Hardware Interruptions

Mobile devices are subject to interruptions like phone calls or alarms. When an interruption occurs, the AudioUnit stream is suspended. In C++, you should listen for these interruptions to pause any game-side audio analysis logic, as the module will stop providing new buffer data until the interruption is cleared.

6. Latency vs. Stability Tuning

You can adjust the input latency by changing the buffer size via the au.CaptureBufferFrameSize console variable. While smaller buffers provide lower latency for real-time voice features, setting them too low on older iOS hardware may cause “crackling” due to the CPU’s inability to keep up with the AudioUnit’s callback frequency.

7. Precise Stream Elimination

When an actor using a UAudioCaptureComponent is destroyed, ensure you call Stop() on the component. Properly closing the stream ensures the elimination of the AudioUnit instance. If not handled correctly, the “microphone in use” (orange dot) indicator on the OS may remain visible, draining the user’s battery even if the game logic is idle.

8. Verify Device IDs on macOS

Unlike iOS, macOS may have multiple input devices (e.g., Internal Mic, USB Headset). Use the FAudioCapture factory to enumerate devices. The AudioCaptureAudioUnit module defaults to the system’s “Default Input,” but you can specify a specific DeviceID if your tool requires a high-quality external interface.