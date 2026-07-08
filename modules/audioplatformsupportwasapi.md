---
layout: default
title: AudioPlatformSupportWasapi
---

<!-- ai-generation-failed -->

<h1>AudioPlatformSupportWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioPlatformSupport/Windows/WASAPI/AudioPlatformSupportWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rimary audio backend for Windows and Xbox in modern versions of Unreal Engine (standardized as the default in UE 5.8). It leverages the Windows Audio Session API (WASAPI) to communicate directly with the operating system’s audio stack, replacing the legacy XAudio2 implementation.

This module is responsible for device enumeration, sample-rate negotiation, and the actual pushing of processed audio buffers to the hardware. By using WASAPI, Unreal Engine achieves lower latency and more robust handling of modern audio hardware.

Practical Usage Tips and Best Practices
1. Leverage Native Device Swapping

The WASAPI backend is designed to handle “Device Swap” events automatically. In previous versions, unplugging headphones could sometimes hang the audio engine; with this module, the engine dynamically migrates the audio stream to the new default Windows device. You should rely on the engine’s built-in handling rather than writing custom C++ “re-initialization” logic.

2. Tune Latency via Callback Buffer Size

If your game requires ultra-low latency (e.g., rhythm or competitive shooters), you can adjust the buffer size in your WindowsEngine.ini. While the default is usually 1024 frames, lowering this to 512 or 256 can reduce delay, though it increases the risk of CPU hitches.

ini
	[Audio]

	CallbackBufferFrameSize=512
Copy code
3. Monitor for “Waited for Audio Thread” Logs

WASAPI requires the audio thread to deliver buffers on a strict schedule. If you see warnings in the log stating “Waited [x] ms for audio thread,” it means your game logic or a heavy MetaSound is stalling the pipeline. This leads to the elimination of audio continuity, resulting in audible pops or crackles. Use Unreal Insights to profile the audio thread.

4. Opt-Out Only for Legacy Support

If you encounter a project-specific bug with a niche piece of hardware, you can fallback to the legacy XAudio2 backend. However, this should only be a temporary measure for the elimination of a specific crash, as WASAPI is the forward-looking standard for the engine.

ini
	[Audio]

	AudioMixerModuleName=AudioMixerXAudio2
Copy code
5. Verify Sample Rate Negotiation

WASAPI usually operates in “Shared Mode,” meaning it must match the sample rate set in the Windows Sound Control Panel (e.g., 48kHz). If your source audio assets are 44.1kHz, the engine performs a high-quality resample. For maximum performance, try to match your source assets to the most common user hardware setting (48kHz).

6. Use for Multi-Output Debugging

WASAPI provides more detailed logging regarding available output channels. Use the console command au.ReportAudioDevices to see exactly how the WASAPI module sees your hardware. This is helpful for confirming if the engine is actually outputting in 7.1 surround or if it has been downmixed by Windows.

7. Handle Audio “Ducking” at the OS Level

WASAPI allows the OS to notify the engine when another application (like a VOIP call) wants priority. You can react to these events in Blueprints or C++ to implement your own in-game ducking logic, ensuring the elimination of clashing audio when a player receives an external notification.

8. Ensure Background Audio is Enabled

Because WASAPI is tightly integrated with the Windows session, audio may stop when the window loses focus. If you need audio to persist (e.g., for a social lounge or music player), ensure UnattendedBugCheck or “Allow Background Audio” is configured in your project’s platform-specific Windows settings.