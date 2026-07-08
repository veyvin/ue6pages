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

on of the Unreal Engine Audio Capture interface for Apple platforms (macOS and iOS). It bridges the engine’s generic audio capture system with Apple’s Audio Unit framework, specifically utilizing the Remote I/O unit to access hardware microphone inputs.

This module is primarily used to enable real-time microphone input on iPhones, iPads, and Macs, allowing for features like voice-driven gameplay mechanics, real-time spectral analysis, or local voice recording.

Practical Usage Tips and Best Practices
1. Configure Info.plist Permissions

On iOS and macOS, the AudioCaptureAudioUnit will fail to initialize if the app does not have explicit permission to access the microphone. You must add the NSMicrophoneUsageDescription key to your project settings under Platforms > iOS > Additional Plist Data. Failure to do this will result in an immediate crash upon attempting to start audio capture.

2. Match Hardware Sample Rates

Apple devices often default to a 44.1kHz or 48kHz sample rate. To avoid expensive software resampling and potential latency, configure your Audio Capture Component or C++ logic to request the hardware’s native sample rate. You can query the preferred hardware rate via the AVAudioSession on iOS to ensure the capture buffer aligns with the hardware’s output.

3. Handle Audio Session Interruptions

On mobile devices, a phone call or an alarm can interrupt the Audio Unit. In C++, listen for FCoreDelegates::ApplicationWillDeactivateDelegate. When the app loses focus, you should call Stop on your audio capture logic to release the Audio Unit, then restart it once the app returns to the foreground to prevent the audio stream from becoming “stale” or silent.

4. Optimize Buffer Sizes for Latency

The module relies on the Apple hardware’s callback buffer size. If your game requires low-latency response (like a rhythm game), you can suggest a smaller IO duration via the iOS platform settings. However, be cautious: setting the buffer too small can lead to “crackling” if the CPU cannot process the audio data in time, leading to a total elimination of audio clarity.

5. Manage Background Audio Modes

If your project requires recording audio while the app is in the background, you must enable the “Audio, AirPlay, and Picture in Picture” background mode in the iOS project settings. Without this, the AudioCaptureAudioUnit will be silenced by the operating system the moment the user switches apps.

6. Use for Local Logic Only

As with the general Audio Capture system, this module is intended for local processing (e.g., getting the amplitude of a player’s shout). It is not a replacement for a networked VOIP solution like Epic Online Services (EOS) Voice. Using it for networking requires manual encoding and packet transmission logic.

7. Elimination of Echo via Ducking

When the microphone is active on a device with speakers (like an iPhone), feedback is a major risk. Use Audio Modulation or Sound Mixes to “duck” (lower the volume of) the game’s master output when the capture component is active. This helps in the elimination of feedback loops where the microphone picks up and amplifies the game’s own sound effects.

8. Verify Device Compatibility in C++

Always check if a valid input device exists before activating the capture unit. Use AudioCapture.GetCaptureDeviceInfo() to ensure the hardware is actually available. On some Mac configurations or older iOS devices, the capture device might be restricted or missing, and attempting to initialize the Audio Unit on a null device will log errors and fail silently.