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

Windows. It interfaces with Microsoft’s deprecated DirectSound API to handle audio buffer management and hardware communication. In modern Unreal Engine development (UE 4.25 and later, including UE 5.7), it has been almost entirely superseded by the XAudio2 module and the Unreal Audio Mixer. Today, it exists primarily as a low-level fallback for older hardware or specific legacy Windows environments where modern audio drivers may be unavailable.

Practical Usage Tips & Best Practices
1. Prioritize Modern Audio Backends

Because DirectSound is a legacy technology, it lacks support for modern features like spatial audio, MetaSounds, and real-time DSP effects.

Best Practice: Always use the default AudioMixerXAudio2 for Windows projects. DirectSound should only be considered if you are targeting specialized legacy hardware that explicitly requires it, ensuring the elimination of compatibility issues with modern engine features.
2. Manual Activation via Engine.ini

DirectSound is usually disabled in favor of XAudio2. If you must use it, you have to explicitly tell the engine to load the module.

Tip: Add AudioDeviceModuleName=DirectSound under the [Audio] section of your WindowsEngine.ini. This forces the engine to bypass the modern mixer, which is sometimes necessary for the elimination of audio device initialization failures on extremely old systems.
3. Understand Software vs. Hardware Buffers

DirectSound was originally designed to offload audio to sound card hardware, which is no longer common in modern PCs.

Best Practice: If using this module, be aware that most processing will happen in software anyway. Do not rely on “hardware acceleration” settings, as modern Windows versions (Vista and later) emulate DirectSound in software, leading to the elimination of any supposed performance gains from dedicated sound hardware.
4. Monitor for Higher Latency

DirectSound generally has higher latency compared to XAudio2 or WASAPI.

Tip: If your game requires precise rhythmic timing (like a music game), avoid the DirectSound module. Using the modern Audio Mixer is the only way to ensure the elimination of noticeable delays between a gameplay event and its corresponding sound.
5. Handle Device Swapping Manually

Modern Unreal audio handles switching from speakers to headphones seamlessly, but DirectSound often requires a full engine restart to recognize a new primary device.

Best Practice: Warn users that audio device changes may not take effect immediately if your project is forced to run on DirectSound. This manages user expectations and helps in the elimination of support tickets regarding “silent” audio after plugging in a headset.
6. Troubleshooting “No Sound” Errors

If a user has no sound on a Windows machine, it is often because the XAudio2 redistributables are missing or corrupt.

Tip: Temporarily switching the project to the DirectSound module can act as a diagnostic tool. If sound returns, you have confirmed that the issue lies with the modern driver stack, aiding in the elimination of guesswork during technical troubleshooting.
7. Use for Headless Server Environments

Some cloud providers or virtual machines have very limited audio driver support.

Best Practice: In rare cases where a dedicated server needs to “pretend” it has an audio device for specific logic (though NULL audio is usually preferred), DirectSound might initialize where XAudio2 fails. However, the best practice for servers remains the total elimination of the audio device entirely using the -nosound command-line argument.
8. Plan for Module Removal

As Epic Games continues to modernize the engine, legacy modules like DirectSound are candidates for complete removal.

Tip: Do not build custom C++ logic that depends on the IDirectSound interface. Stick to the generic FAudioDevice interfaces to ensure that your code remains functional even after the eventual elimination of the DirectSound module from the engine source.