---
layout: default
title: AudioCaptureWasapi
---

<!-- ai-generation-failed -->

<h1>AudioCaptureWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/Windows/AudioCaputureWasapi/AudioCaptureWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, AudioPlatformSupportWasapi, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

f Unreal Engine’s audio input system. It utilizes the Windows Audio Session API (WASAPI) to interface directly with the operating system’s audio hardware. As of Unreal Engine 5.8, WASAPI has replaced XAudio2 as the default audio backend for Windows and Xbox.

This module is responsible for capturing microphone input and system audio on Windows platforms. It provides a low-latency, high-performance path for real-time audio analysis, VOIP, and recording, offering superior device-swap handling and stability compared to legacy APIs.

Practical Usage Tips and Best Practices
Handle Automatic Device Swapping Starting with UE 5.8, the WASAPI backend natively handles device changes. You no longer need to write complex manual listeners for when a player unplugs a headset or switches the Windows default device; the module handles this “hot-swapping” automatically to ensure the audio stream is not lost.
Route Through Submixes for Muting To analyze microphone input (e.g., for a voice-activated mechanic) without the player hearing themselves, send the AudioCapture component output to a specific Sound Submix. Set that Submix’s Output Volume to zero in the details panel. This allows the frequency analysis logic to function while “eliminating” the auditory feedback.
Prioritize the Audio Render Thread When writing custom DSP or analysis code in C++ using WASAPI data, perform your signal processing on the Audio Render Thread. Avoid placing blocking calls, I/O operations, or complex mutexes here, as they can cause buffer underruns, resulting in “clicks” or “pops” in the captured audio.
Configure Module Dependencies To use WASAPI-specific capture logic in C++, add the module to your Build.cs. However, for cross-platform compatibility, it is usually better to depend on the generic AudioCapture module, which will call AudioCaptureWasapi internally on Windows.
C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("AudioCaptureWasapi");

	}
Copy code
Manage Windows Privacy Settings The WASAPI backend will fail to initialize if the user has disabled microphone access in Windows Privacy Settings. Always implement a check or a graceful failure message if the audio stream returns null, as the engine cannot override OS-level security restrictions.
Optimize for Latency with WASAPI Exclusive Mode While Unreal generally uses Shared Mode for compatibility, if you are building a professional audio tool or a rhythm game requiring the lowest possible latency, you can investigate WASAPI Exclusive Mode settings. Note that this will “eliminate” the ability for other applications to play or record sound simultaneously.
Use the Audio Capture Component for Envelopes For gameplay triggers, use the OnAudioEnvelopeValue event from the AudioCapture component. You can adjust the Envelope Follower Attack and Release times in the component settings to smooth out the microphone data, which is useful for “eliminating” jittery input when a player is speaking.
Verify Backend via Logs If you suspect audio issues on Windows, check the logs for LogAudioMixer. You should see “AudioMixerWasapi” initialized. If you need to revert to the legacy backend for troubleshooting, you can add AudioMixerModuleName=AudioMixerXAudio2 to your WindowsEngine.ini.