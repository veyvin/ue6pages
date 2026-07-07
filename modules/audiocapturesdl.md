---
layout: default
title: AudioCaptureSDL
---

<!-- ai-generation-failed -->

<h1>AudioCaptureSDL</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/Linux/AudioCaptureSDL/AudioCaptureSDL.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

layer that utilizes the Simple DirectMedia Layer (SDL) library to capture audio input (microphones or line-in). It provides the engine with a standardized way to access audio hardware across different operating systems, acting as a bridge between the physical audio device and Unreal’s internal audio processing.

This module is particularly critical for Linux and Steam Deck development, as it serves as the primary audio input backend for those platforms. It allows developers to implement features like voice-driven gameplay or local microphone monitoring in a way that remains consistent even when the underlying OS audio drivers differ.

1. Enable the Audio Capture Plugin

The AudioCaptureSDL module is part of the broader Audio Capture system. Before use, ensure the Audio Capture plugin is enabled in your project. On Linux/Unix platforms, the engine will automatically prefer the SDL implementation provided by this module over other backends.

2. Verify Device Permissions

On Linux and mobile platforms, the hardware detection depends on OS permissions.

Tip: Ensure your application has the necessary “Record Audio” permissions. If permissions are missing, the SDL module will report zero available devices, effectively eliminating your ability to capture input even if a microphone is physically connected.
3. SDL2 to SDL3 Transition

Be aware of the engine version you are using. Unreal Engine 5.7+ has migrated to SDL3. If you are writing custom C++ that interfaces with this module or the underlying SDL library, you must update your Build.cs and include paths to target SDL3 instead of SDL2 to maintain compatibility with modern engine builds.

4. Manage Latency via Buffer Sizes

Audio latency is a common challenge with SDL-based capture.

Best Practice: If you notice a delay in microphone playback, check your AudioSettings or your platform’s .ini files to adjust the Callback Buffer Size. Smaller buffers reduce latency but increase CPU load and the risk of “crackling” if the CPU cannot keep up.
5. Utilize Submixes for Processing

Captured audio from this module is typically sent to an Audio Bus or a Sound Submix.

Tip: Route your microphone input into a Submix where you can apply real-time effects like EQ, Compression, or Noise Gates. This is a highly efficient way to clean up raw SDL input before using it for visualization or localized playback.
6. Single-Player vs. Networked Voice

This module is intended for local audio capture.

Important: While it works perfectly for local mechanics (like blowing into a mic or rhythm detection), it is not a replacement for a networked voice-over-IP (VoIP) solution. For multiplayer voice chat, utilize specialized services like Epic Online Services (EOS) Voice or the built-in Steam VOIP.
7. Check Device Sample Rates

SDL may struggle if there is a mismatch between the hardware’s native sample rate (e.g., 48kHz) and the engine’s internal audio rate.

Best Practice: When querying device capabilities through the AudioCapture component, verify the supported sample rate. Forcing a mismatched rate can cause pitch-shifting or “speed-up” effects in the captured audio.
8. Handling Device Disconnection

If a player unplugs their headset while the SDL capture stream is active, the module needs to handle the event to prevent a crash.

Tip: Bind to the OnAudioCaptureDeviceChange delegates. This allows your game to gracefully stop the capture or prompt the user to select a new input device, preventing the elimination of the audio feature during a session.