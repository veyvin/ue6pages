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

ine, primarily serving as a bridge to the older Microsoft DirectSound API.

Description and Purpose

This module provides a hardware-abstraction layer for audio playback on Windows systems. In earlier versions of Unreal Engine, it was a primary method for communicating with audio drivers. However, with the introduction of the AudioMixer (Unreal’s multi-platform native renderer), the DirectSound module has been moved to legacy status. It is now mainly used for backward compatibility on older Windows environments or as a fallback when the modern XAudio2-based mixer is unavailable. Its role is to handle basic sound buffering, mixing, and output to the system’s primary audio device.

Practical Usage Tips and Best Practices
Prioritize AudioMixer Over DirectSound
For all modern UE5 projects, ensure you are using the AudioMixerXAudio2 module instead of DirectSound. The modern mixer provides far superior performance and feature parity across platforms. Using the modern mixer will eliminate many of the synchronization and latency issues inherent in the legacy DirectSound path.
Identify Legacy Fallbacks via Logs
If you suspect your game is falling back to DirectSound, check the output log during startup for “Audio Device: DirectSound”. If found, investigate your Engine.ini settings. You should eliminate this fallback for shipping titles to ensure players get the intended spatialization and DSP effects.
Use for Compatibility Testing
The only practical reason to enable this module in UE5 is to test how your game performs on legacy hardware configurations or virtual machines with limited audio drivers. This helps you eliminate potential “no sound” bugs for players on highly restricted enterprise or legacy systems.
Monitor Buffer Underruns
DirectSound is prone to buffer underruns if the Game Thread hitches. If you hear “popping” during an intense character elimination sequence, it is likely due to the legacy backend struggling with CPU spikes. Moving to the modern AudioMixer will eliminate this by utilizing a dedicated high-priority audio thread.
Disable in Build.cs if Unused
If your project targets modern Windows 10⁄11 and consoles exclusively, you can eliminate the DirectSound module from your dependencies in ProjectName.Build.cs. This reduces your final executable size and prevents accidental initialization of the legacy API.
Avoid Using for Spatialization
The DirectSound module lacks support for modern spatialization plugins like Oculus Audio or Steam Audio. If your gameplay relies on precise audio cues—such as hearing a nearby elimination event—using DirectSound will eliminate your ability to provide accurate 3D positioning.
Verify Device Swap Handling
DirectSound does not handle modern Windows “Default Device” swaps (e.g., plugging in a headset) as gracefully as the modern AudioMixer. Testing with this module is a good way to identify if your code properly handles device disconnection, helping you eliminate crashes when the audio hardware state changes.
Check Platform Support in Engine.ini
If you must use it, check your WindowsEngine.ini under [Audio]. You can specify the AudioDeviceModuleName. By ensuring this is set to the modern mixer, you eliminate any ambiguity about which module the engine will load at runtime.