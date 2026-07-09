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

esponsible for interfacing with hardware audio input devices. It acts as a hardware abstraction layer (HAL) that bridges platform-specific APIs—such as WASAPI (Windows), CoreAudio (Mac/iOS), and OpenSL ES/AAudio (Android)—with the Unreal Audio Engine. It is primarily used for capturing microphone data for real-time processing, VOIP, or environmental analysis.

Practical Usage Tips & Best Practices
1. Distinguish from the “AudioCapture” Plugin

It is important to understand the difference between these two:

AudioCaptureCore: The low-level API and logic for stream management.
AudioCapture: The UMG/Blueprint-facing plugin that includes the AudioCaptureComponent.
Best Practice: Use AudioCaptureCore if you are building a custom C++ backend for audio processing (like speech-to-text), but use the standard AudioCapture plugin if you simply need to play a player’s voice through a speaker in-game.
2. Manage Asynchronous Buffers

Audio capture operates on a high-priority hardware thread. When you override OnAudioCapture or use a callback, never perform heavy logic (like complex math or file I/O) directly in the callback.

Tip: Copy the incoming float* buffer data into a thread-safe ring buffer (or TCircularBuffer) and process it on a background worker thread to avoid “popping” or audio dropouts.
3. Handle Elimination of Audio Streams

Proper lifecycle management is critical. When your object is destroyed, you must explicitly stop and close the audio stream.

Best Practice: Call StopStream() and CloseStream() in your EndPlay or destructor. If you fail to do so, the hardware device may remain “in use,” preventing other applications or future instances of your game from accessing the microphone until a restart.
4. Add Module Dependency in Build.cs

To interface with the capture device via C++, you must add the module to your project’s dependencies. Note that since it interacts with hardware, it is a runtime module.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "AudioCaptureCore" 

	});
Copy code
5. Verify Sample Rate Compatibility

Different microphones support different sample rates (e.g., 44.1kHz vs 48kHz). Use GetCaptureDeviceInfo to query the hardware’s native sample rate before starting a stream. Attempting to force a mismatch without a proper resampler can lead to pitch-shifting or distorted audio.

6. Request Platform Permissions

Audio capture will fail silently if the OS permissions are not set.

Android: Ensure android.permission.RECORD_AUDIO is in your Project Settings.
iOS: Ensure NSMicrophoneUsageDescription is populated in your Info.plist settings.
Tip: Use the Application Lifecycle delegates to check for permission before attempting to initialize the IAudioCaptureStream.
7. Use for Real-Time “Elimination” Triggers

You can use the captured audio envelope (volume level) to trigger gameplay events. For example, a horror game might detect a player’s real-world scream via AudioCaptureCore and use that to trigger the player’s elimination by an in-game monster. Use the AudioMixer’s envelope follower for the most efficient implementation.

8. Thread Safety with UObjects

Because the capture callback occurs on a separate thread, you must not modify UObject properties directly within the audio callback. If a specific audio threshold is reached, use AsyncTask(ENamedThreads::GameThread, ...) to safely update game variables or trigger Blueprint events.