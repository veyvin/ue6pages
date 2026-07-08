---
layout: default
title: AudioMixerAudioUnit
---

<!-- ai-generation-failed -->

<h1>AudioMixerAudioUnit</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Apple/AudioMixerAudioUnit/AudioMixerAudioUnit.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixerCore, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

re abstraction layer for Apple devices. It bridges Unreal Engine’s multi-threaded Audio Mixer to the CoreAudio/AudioUnit framework used by macOS and iOS.

What it is and What it’s used for

This module acts as the “backend” for the Unreal Audio Engine on Apple hardware. While the engine handles high-level logic (like MetaSounds or Reverb), this module is responsible for the final stage: handing the mixed audio buffers to the operating system to be played through speakers or headphones.

Primary uses include:

Hardware Interface: Opening and managing the RemoteIO or HAL Audio Units on iOS and macOS.
Buffer Delivery: Feeding the final audio mix from Unreal’s audio thread into the Apple system’s callback thread.
Sample Rate Conversion: Ensuring the engine’s internal sample rate matches the device’s hardware sample rate.
Input/Output Routing: Managing microphone input and speaker output streams.
Practical Usage Tips and Best Practices
1. Match Engine and Hardware Sample Rates

To eliminate CPU-intensive resampling, ensure your project’s sample rate matches the Apple device (typically 48,000 Hz). You can set this in your IOS or Mac platform settings. If the rates don’t match, the AudioMixerAudioUnit must perform a software conversion, which adds latency and CPU overhead.

2. Tune Buffer Sizes for Latency

On iOS, you can adjust the CallbackBufferFrameSize in the Project Settings > Platforms > iOS > Audio. A value of 256 or 512 is common for low-latency gameplay. However, setting this too low can lead to “buffer underruns,” causing audible crackling or “buzzy” distortion if the CPU hits a hitch.

3. Handle iOS Background Audio

iOS will often suspend audio when the app moves to the background. Ensure you have the “Background Audio” capability enabled in your Xcode project settings if your app needs to maintain a connection. The AudioMixerAudioUnit module relies on these permissions to restart the audio stream gracefully when the app is resumed.

4. Monitor via LogAudioMixer

When debugging silent audio on a Mac or iPhone, look for the LogAudioMixer category in the logs. This module will report exactly which Apple device it initialized and if it successfully created the Audio Unit. Errors like kAudioUnitErr_InvalidPropertyValue often indicate a mismatch in configuration.

5. Respect the iOS Silent Switch

By default, Unreal respects the physical silent switch on iPhones. If you need your game to play audio even when the switch is on (e.g., for a media player app), you must configure the Audio Session Category in the Project Settings to “Playback” or “Ambient” to override the default behavior.

6. Use for Local Microphone Input

If you are using the AudioCapture plugin on a Mac or iOS device, this module handles the input Audio Unit. Ensure your Info.plist has the NSMicrophoneUsageDescription key; otherwise, the AudioMixerAudioUnit will fail to initialize the input stream, and the process will be eliminated by the OS.

7. Performance Profiling with Unreal Insights

If you notice “pops” or “clicks,” use Unreal Insights to check the Audio Thread. If the time spent in the audio callback exceeds the time allowed by your buffer size (e.g., ~5.3ms for a 256-frame buffer at 48kHz), you must optimize your MetaSounds or increase the buffer size.

8. Avoid Blocking the Audio Callback

The code inside this module runs on a high-priority system thread. If you are writing custom C++ audio code that interacts with this backend, never perform disk I/O, memory allocations, or complex logic in the callback. Stalling this thread will immediately result in audio “underrun” and poor user experience.