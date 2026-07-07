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

of the Unreal Engine Audio Capture interface. It utilizes the Windows Audio Session API (WASAPI) to interface directly with the operating system’s audio endpoint devices.

Starting with Unreal Engine 5.8, WASAPI has become the default audio backend for Windows (replacing the legacy XAudio2 implementation). This module is responsible for capturing low-latency microphone input, handling device swaps (like plugging in a USB headset), and managing sample rate negotiation between the OS and the engine’s audio mixer.

Practical Usage Tips and Best Practices
1. Configure Module Dependencies

If you are developing custom C++ components for microphone processing on Windows, you must link the module in your Build.cs. Always wrap this in a platform check to ensure the project remains cross-platform compatible.

C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("AudioCaptureWASAPI");

	}
Copy code
2. Handle Dynamic Device Swaps

WASAPI is more robust than legacy APIs at handling hardware changes.

Best Practice: Do not hardcode device IDs. Rely on the engine’s default device handling. If a user unplugs their microphone during a session, the WASAPI module will attempt to fail over to the next available system default, preventing the capture session from being eliminated.
3. Match Hardware Sample Rates

To eliminate CPU-intensive software resampling and reduce latency, ensure your project’s audio settings match the Windows “Default Format” (usually 48kHz).

Tip: Check the Project Settings > Platforms > Windows > Audio > Callback Buffer Size. For pro-audio or rhythm games, a smaller buffer (e.g., 256 or 512) paired with WASAPI provides the fastest response time.
4. Respect Exclusive vs. Shared Mode

By default, Unreal uses Shared Mode, allowing other applications (like Discord or a browser) to use the microphone simultaneously.

Best Practice: Avoid trying to force “Exclusive Mode” via custom code unless you are building a specialized professional audio tool. Forcing exclusive mode will eliminate audio from all other applications on the user’s system, leading to a poor user experience.
5. Use Submix Recording for Validation

If you are experiencing “buzzy” or “distorted” audio captured via WASAPI, use Submix Recording.

Tip: Route your AudioCapture component to a specific Submix and use the StartRecordingOutput node. This allows you to inspect the raw .wav file to determine if the distortion is happening at the OS capture level (WASAPI) or within your in-game effect chain.
6. Optimize for Windows 10⁄11 Audio Enhancements

Windows often applies “Signal Enhancements” (like noise suppression or echo cancellation) at the driver level.

Best Practice: If your game relies on high-fidelity audio analysis, advise users to disable “Enable audio enhancements” in their Windows Sound Settings, as these processing layers can interfere with the raw data received by the module.
7. Prevent Feedback Loops

Because WASAPI is highly sensitive, capturing and immediately playing back audio on the same device can cause rapid acoustic feedback.

Tip: When testing in the editor, ensure your AudioCapture component is set to Output to Bus Only. This allows the engine to “hear” the microphone for gameplay logic while eliminating the audio signal from the speakers.
8. Monitor for Buffer Underruns

If your logs show WASAPI buffer underrun or Audio device starved, it usually means the Game Thread is blocking the Audio Render Thread.

Best Practice: Move complex audio analysis or gameplay logic out of the OnAudioEnvelopeValue event and into a separate thread or use the MetaSounds system to handle real-time signal processing, ensuring the capture stream remains steady.