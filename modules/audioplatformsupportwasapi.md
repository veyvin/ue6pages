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

rn hardware abstraction layer for audio on Windows and Xbox. Introduced as the default backend in UE 5.8, it replaces the legacy XAudio2 system. It utilizes the Windows Audio Session API (WASAPI) to provide a direct, low-latency path between the Unreal Audio Mixer and the operating system’s audio drivers.

Its primary role is to handle device enumeration, stream management, and the high-priority callback loop that feeds mixed audio buffers to the hardware.

1. Module Configuration

As a core platform module, it is automatically loaded by the engine when running on Windows or Xbox. Developers typically do not link to it directly in gameplay code. However, you can control its behavior through the WindowsEngine.ini file:

ini
	[Audio]

	# Use this to revert to legacy if necessary, but WASAPI is the UE 5.8+ default

	AudioMixerModuleName=AudioMixerWasapi
Copy code
2. Practical Usage Tips & Best Practices
Seamless Device Swap Handling

The WASAPI module natively supports “Device Hot-Plugging.” This means if a player disconnects their USB headset or switches their default Windows audio device, the module handles the transition automatically. To support this in your UI, listen for the OnAudioDefaultDeviceChanged delegate in the AudioDevice class rather than polling for changes manually.

Optimize for Low Latency

WASAPI allows the engine to request specific buffer sizes from the OS. To “eliminate” audio lag in rhythm or VR games, you can adjust the CallbackBufferFrameSize in your project settings. Note that setting this too low may cause “crackling” if the CPU cannot fill the buffer in time.

Handle Exclusive Mode Considerations

While Unreal typically runs in “Shared Mode” (allowing other apps to make noise), WASAPI technically supports “Exclusive Mode” for bit-perfect audio. If your project requires audiophile-grade output, be aware that Exclusive Mode will “eliminate” audio from all other Windows applications (like Discord or web browsers) while the game is focused.

Verify Sample Rate Negotiation

The WASAPI module attempts to match the Windows “Default Format” (e.g., 48kHz, 24-bit). If there is a mismatch between the engine’s internal 48kHz processing and a user’s 44.1kHz hardware, the WASAPI backend performs a high-quality resample. Ensure your source assets are 48kHz to “eliminate” the need for this extra CPU overhead.

Monitor via LogAudioMixer

When debugging “no sound” issues on Windows, filter your Output Log for LogAudioMixer. The WASAPI module will print detailed information about the initialized device, including its channel count and supported bit depth. If a device fails to initialize, the log will specify the exact HRESULT error code from the Windows API.

Use “SoloAudio” for Multi-Instance Debugging

When running multiple client instances in the editor (PIE), the WASAPI backend can become crowded. Use the console command SoloAudio to focus the audio output only on the window currently in focus. This “eliminates” the overlapping noise from background clients, making it easier to mix your game.

Avoid Manual XAudio2 Fallbacks

Unless you encounter a specific driver bug on legacy hardware, avoid forcing the engine back to XAudio2. The WASAPI backend is built to support modern Windows features like Spatial Sound (Dolby Atmos/Windows Sonic) more robustly than the legacy XAudio2 implementation.

Manage Thread Priority

The WASAPI callback runs on a dedicated high-priority thread. To maintain audio stability, ensure that any custom MetaSounds or Submix effects are highly optimized. If a custom effect hitches, it can “eliminate” the WASAPI stream’s timing, resulting in a persistent “stutter” until the audio device is re-initialized.