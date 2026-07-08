---
layout: default
title: AudioCaptureRtAudio
---

<!-- ai-generation-failed -->

<h1>AudioCaptureRtAudio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/AudioCaptureRtAudio/AudioCaptureRtAudio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

of the Unreal Engine audio capture interface. It utilizes the RtAudio library, a cross-platform C++ API for realtime audio input and output, to provide microphone and line-in functionality.

What it is and What it’s used for

This module acts as a “hardware abstraction layer” for audio input. While the generic AudioCapture plugin provides the Blueprint nodes and components developers use, AudioCaptureRtAudio is the backend worker that communicates with the actual sound drivers on specific platforms.

Primary uses include:

Cross-Platform Input: Providing a consistent audio capture backend for platforms where native backends (like XAudio2 or WASAPI) are not used exclusively.
Low-Latency Capture: Fetching raw PCM audio data from a microphone for use with MetaSounds, amplitude envelopes, or spectral analysis.
Developer Tooling: Enabling audio input in the editor for testing VOIP systems or reactive audio environments without needing a full platform SDK setup.
Practical Usage Tips and Best Practices
1. Module Dependency Management

If you are developing a C++ plugin that requires direct access to the RtAudio-based capture backend, you must include it in your *.Build.cs. However, since it is a platform-specific implementation, wrap it in a conditional check to ensure it doesn’t try to load on unsupported platforms:

C#
	if (Target.Platform == UnrealTargetPlatform.Win64 || Target.Platform == UnrealTargetPlatform.Mac)

	{

	    PublicDependencyModuleNames.Add("AudioCaptureRtAudio");

	}
Copy code
2. Match Sample Rates to Avoid Resampling

To eliminate CPU overhead and potential audio artifacts, ensure your AudioCapture settings match the hardware’s native sample rate (usually 44.1kHz or 48kHz). This prevents the RtAudio backend from having to perform costly software resampling before passing the data to the engine.

3. Handle Permission Lifecycles

On platforms like macOS or Android (where RtAudio might be utilized), simply enabling the module is not enough. You must ensure the application has been granted microphone permissions. Use the CoreDelegates or platform-specific wrappers to check for permission before calling Start() on an Audio Capture Component to prevent silent failures.

4. Configure Buffer Sizes via .ini

You can tune the latency and stability of the RtAudio backend by adjusting the AudioMixer settings in your DefaultEngine.ini. A smaller CallbackBufferFrameSize reduces latency but increases the risk of “pops” or “clicks” if the CPU cannot keep up with the audio thread.

5. Output to Bus for Analysis

To use the captured audio for gameplay logic without the player hearing their own voice (which can cause feedback loops), set the Audio Capture Component to Output to Bus Only. You can then use the signal from that Audio Bus to drive MetaSounds or Niagara VFX while keeping the audio itself silent to the user.

6. Debugging via LogAudio

When troubleshooting why a microphone isn’t being detected, check the Output Log for the LogAudioCapture and LogAudioMixer categories. The RtAudio backend will log the specific hardware device name it is attempting to open and the exact error code if the stream fails to initialize.

7. Use for Local-Only Logic

The RtAudio capture backend is intended for local processing. It is not a networking module. If you need to send audio across a network (VOIP), use this module to capture the raw data, but pass it to an optimized networking framework like EOS Voice or the Online Subsystem for transmission and elimination of jitter.

8. Verify Device Availability

Before starting a capture session, use the GetAudioCaptureDeviceInfo nodes or C++ functions. The RtAudio backend can report how many input channels are available. Validating that a device is actually connected before attempting to capture will prevent the audio stream from timing out.