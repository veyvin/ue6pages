---
layout: default
title: AudioCaptureCore
---

<!-- ai-generation-failed -->

<h1>AudioCaptureCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureCore/AudioCaptureCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine that serves as the hardware abstraction layer for audio input devices. It provides the essential C++ interfaces required to open microphone streams, manage input buffers, and interface with platform-specific audio APIs (such as WASAPI on Windows, CoreAudio on macOS/iOS, and ALSA/PulseAudio on Linux).

Description

While the higher-level AudioCapture plugin provides UMG components and Blueprints for easy mic access, AudioCaptureCore is the underlying engine that does the heavy lifting. It is used to fetch raw PCM audio data from a physical device and feed it into the Unreal Audio Engine. This module is vital for features like real-time voice visualization, in-game VOIP systems, and audio-reactive gameplay mechanics.

Practical Usage Tips and Best Practices
1. Include Necessary Module Dependencies

To interface with microphone hardware in C++, you must add the module to your *.Build.cs file. It is often used in conjunction with AudioMixer for processing.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "AudioCaptureCore", "AudioMixer" });
Copy code
2. Handle Platform Permissions

On mobile and console platforms, the AudioCaptureCore will fail to initialize if the app lacks the proper microphone permissions.

Android: Ensure android.permission.RECORD_AUDIO is added in Project Settings.
iOS/macOS: You must provide a “Microphone Usage Description” in the plist settings, or the OS will immediately terminate the application process.
3. Use “Output to Bus Only” for Analysis

If you are capturing audio only to drive gameplay (e.g., a “blow-to-extinguish-fire” mechanic), ensure you set the output to an Audio Bus. This allows the engine to analyze the signal’s amplitude or frequency without playing the user’s own voice back through their speakers, which eliminates unpleasant feedback loops.

4. Monitor for Buffer Underruns

Audio input is time-sensitive. If your game thread hitches, the AudioCaptureCore may experience buffer underruns, leading to “crackling” or “popping” sounds. Use Unreal Insights to ensure your audio processing logic is not blocked by heavy game logic or synchronous file I/O.

5. Implement Device Swap Handling

Users frequently change audio devices (e.g., plugging in a USB headset). Use the delegates provided by the module to listen for device changes. When a device change is detected, you should re-initialize your capture stream to point to the new default device to ensure the audio stream is not lost.

6. Optimize Sample Rates

To reduce CPU overhead, verify that your capture sample rate matches your project’s default (usually 48kHz). Mismatched sample rates force the AudioCaptureCore to perform real-time sample rate conversion, which can be a hidden performance cost on mobile devices.

7. Clean Up Streams on Elimination

When an actor responsible for audio capture is eliminated or the level transitions, explicitly call CloseStream() or Stop(). Failing to close the hardware stream properly can leave the microphone “active” (indicated by the OS recording icon), which may lead to privacy concerns or prevent other applications from accessing the device.

8. Leverage Submix Analysis

Instead of processing raw PCM data manually, pipe the output from AudioCaptureCore into a Sound Submix. You can then use the StartAnalyzingOutput Blueprint or C++ nodes to get real-time FFT (Frequency) or Envelope (Amplitude) data, which is much more efficient than writing custom DSP code.