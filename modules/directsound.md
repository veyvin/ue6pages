---
layout: default
title: DirectSound
---

<!-- ai-generation-failed -->

<h1>DirectSound</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/DirectSound/DirectSound.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">DirectX</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ows Unreal Engine to interface with the Microsoft DirectSound API for audio playback.

Description

In modern Unreal Engine development (UE 4.24 and later), the engine has largely transitioned to the Audio Mixer (XAudio2 on Windows). However, the DirectSound module remains in the codebase as a legacy fallback or compatibility layer for older Windows hardware and specific software environments. It handles the low-level communication between the engine’s audio thread and the Windows sound driver, managing basic buffer mixing and output. Because it lacks support for modern features like Submixes, Real-time DSP effects, and MetaSounds, it is rarely used as the primary driver in modern projects.

Practical Usage Tips and Best Practices
1. Identify the Active Audio Backend

To check if your project is accidentally using the legacy DirectSound path instead of the modern Audio Mixer, check your Output Log at startup. Search for LogAudioMixer or LogAudio. If you see references to “DirectSound,” you are likely running on a legacy path that will prevent you from using modern features like Niagara-Audio integration.

2. Force Migration to XAudio2

For all modern Windows projects, ensure your BaseEngine.ini or WindowsEngine.ini is configured to use the modern mixer. A best practice is to explicitly define the mixer module:

ini
	[Audio]

	AudioMixerModuleName=AudioMixerXAudio2
Copy code

This ensures that the DirectSound module is bypassed in favor of the more performant and feature-rich XAudio2 backend.

3. Use as a Compatibility Fallback

If you are developing for specialized industrial hardware or very old “thin client” Windows environments that do not support XAudio2 or WASAPI, the DirectSound module can serve as a vital fallback. In these rare cases, you must avoid using Sound Submixes, as they will not process correctly through this legacy module.

4. Monitor Latency and Performance

Legacy backends like DirectSound often exhibit higher latency (the delay between a gameplay event and the sound being heard) compared to the modern Audio Mixer. If you notice a “lag” in sound effects during weapon fire or UI clicks, it is a sign that the elimination of the legacy module in favor of XAudio2 is necessary for your project.

5. Be Aware of Buffer Limitations

DirectSound operates on a simpler buffering system than modern mixers. If your game plays hundreds of sounds simultaneously, the DirectSound module may struggle with “voice stealing” or crackling audio more quickly than the modern multi-threaded audio mixer. Keep your concurrency settings low if you are forced to use this module.

6. Avoid Using for Multi-Platform Development

DirectSound is strictly a Windows-only technology. If you are developing a cross-platform game (e.g., PC, Xbox, PS5), relying on DirectSound-specific behaviors will lead to inconsistent audio levels and quality across platforms. Always use the Audio Mixer to ensure feature parity.

7. Handle Audio Device Elimination

The DirectSound module is less robust at handling “hot-plugging” (switching from headphones to speakers while the game is running). If a user disconnects their primary audio device, the legacy module may fail to hand off the stream, leading to a total loss of sound. Testing for “Device Elimination” is a critical best practice if supporting this legacy path.

8. Disable for Third-Party Middleware

If you are using Wwise or FMOD, you should typically disable Unreal’s native audio modules (including DirectSound) to prevent resource conflicts. These third-party tools provide their own low-level drivers, and the elimination of the native Unreal audio backend via .ini settings is the recommended way to prevent crashes and free up CPU cycles.