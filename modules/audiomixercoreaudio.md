---
layout: default
title: AudioMixerCoreAudio
---

<!-- ai-generation-failed -->

<h1>AudioMixerCoreAudio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Apple/AudioMixerCoreAudio/AudioMixerCoreAudio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixerCore, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ace for the Unreal Audio Engine. It provides the low-level implementation required to communicate with the Core Audio framework on macOS and iOS. This module acts as the final stage of the audio pipeline, responsible for opening audio streams, managing hardware output buffers, and ensuring that the mixed digital signal from Unreal is correctly delivered to the device’s speakers or headphones.

In the modular architecture of the Unreal Audio Mixer, this module handles platform-specific tasks like sample rate negotiation and hardware callback management for all Apple devices.

Practical Usage Tips and Best Practices
Handle iOS Audio Session Interruptions On iOS, the system can “eliminate” your audio stream if a phone call or alarm occurs. Use the OnAudioComponentFinished or system-level delegates to handle these interruptions. It is a best practice to pause the game or mute non-essential sounds during these events to ensure the Core Audio session resumes correctly.
Configure Background Audio Permissions If your app needs to play sound while the screen is locked or while another app is in the foreground, you must enable “Audio, AirPlay, and Picture in Picture” in the Xcode project settings. Without this, the OS will “eliminate” the audio process as soon as the app loses focus.
Match Native Sample Rates Apple devices typically favor a 44.1kHz or 48kHz sample rate depending on the hardware (e.g., AirPods vs. built-in speakers). To “eliminate” the CPU cost of software resampling within the engine, set your Project Settings > Platforms > iOS/Mac > Audio > Default Sample Rate to match the target device’s most common hardware rate.
Manage Latency via Buffer Sizes In the platform-specific project settings, you can adjust the Callback Buffer Size. For rhythm games on iOS, lowering this value reduces latency but increases the risk of CPU spikes. Finding the right balance is the only way to “eliminate” audible “pops” while maintaining responsive gameplay.
Monitor Device Changes (Hot Swapping) Core Audio is highly dynamic. When a user connects Bluetooth headphones, the hardware sample rate and channel count may change instantly. The AudioMixerCoreAudio module handles this transition, but you should verify that your submix effects (like specialized reverbs) don’t cause an “elimination” of audio stability during the handover.
Check for Microphone Privacy (iOS) If you are using audio capture features, ensure the NSMicrophoneUsageDescription is filled out in your Info.plist. If this is missing, the Core Audio capture stream will be “eliminated” by the OS security layer, and your app may crash upon trying to initialize the input device.
Optimize for Silent Mode By default, Unreal respects the physical “Silent/Mute” switch on iPhones. If your game is a media-heavy experience where audio is required (like a music player), you can override this behavior in the IOSRuntimeSettings to ensure audio is not “eliminated” when the hardware switch is active.
Debug with LogAudioMixer If you encounter audio issues on Mac or iOS, use the console command log LogAudioMixer Verbose. This will output the specific Core Audio hardware parameters, such as the AudioUnit type being used, helping you “eliminate” bugs related to unsupported hardware formats.