---
layout: default
title: AudioMixerWasapi
---

<!-- ai-generation-failed -->

<h1>AudioMixerWasapi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/AudioMixerWasapi/AudioMixerWasapi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, AudioMixerCore, AudioPlatformSupportWasapi, Core, CoreUObject, Engine, SignalProcessing, WindowsMMDeviceEnumeration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine 5.8, it is the default audio renderer for Windows and Xbox, replacing the legacy XAudio2 backend. It interfaces directly with the Windows Audio Session API (WASAPI) to communicate with the operating system’s audio drivers.

This module is responsible for the final stage of the audio pipeline: taking the mixed digital audio from the engine and delivering it to the hardware output (speakers/headphones). It provides superior device management and lower latency compared to older APIs.

Practical Usage Tips and Best Practices
1. Leverage Native Device Swapping

One of the primary strengths of this module is its robust handling of device changes. Unlike legacy backends that could crash or lose sound when a headset was unplugged, AudioMixerWasapi automatically handles “Default Device” changes. Ensure your game logic doesn’t manually force device resets, as the module now handles this “elimination” of old device paths natively.

2. Optimize Sample Rates (48kHz Standard)

For the best performance and to avoid the CPU cost of software resampling, set your Project Settings > Audio > Sample Rate to 48000. Most modern Windows hardware runs natively at 48kHz. If the engine and WASAPI match, the module can pass audio buffers more efficiently to the OS.

3. Tuning Buffer Sizes for Latency

If you are developing a rhythm or high-action game where audio latency is critical, you can tune the buffer sizes in your WindowsEngine.ini.

ini
	[Audio]

	CallbackBufferFrameSize=512

	NumStoppedSources=16
Copy code

Reducing CallbackBufferFrameSize to 256 or 128 lowers latency but increases the risk of “Audio Underruns” (buzzy/choppy sound) if the CPU is under heavy load.

4. Avoid Blocking the Audio Render Thread

The AudioMixerWasapi module relies on a high-priority callback thread to feed the OS audio data. If you are writing custom USoundSubmix effects or C++ audio logic, never perform file I/O or heavy memory allocations in the processing loop. Doing so will “eliminate” the thread’s ability to finish the buffer in time, causing audible pops and clicks.

5. Handle Exclusive Mode with Care

WASAPI supports “Exclusive Mode,” which allows the engine to bypass the Windows system mixer for the lowest possible latency. However, this prevents other apps (like Spotify or Discord) from making sound. Only enable this via specialized console variables if your project is for a pro-audio or VR-only application.

6. Use for Multi-Channel Debugging

This module is excellent at reporting hardware capabilities. Use the console command Log LogAudioMixer Verbose to see exactly how many channels WASAPI has detected. This is the fastest way to verify if your 5.1 or 7.1 surround sound configuration is actually being recognized by the hardware.

7. Fallback for Legacy Support

If you encounter a highly specific hardware compatibility issue on an older machine, you can opt-out of the WASAPI backend and revert to XAudio2 by adding this to your Config/Windows/WindowsEngine.ini:

ini
	[Audio]

	AudioMixerModuleName=AudioMixerXAudio2
Copy code

Note: This should only be used as a last resort, as WASAPI is the forward-looking standard.

Performance & Debugging
Audio Insights: Always use Unreal Insights with the Audio trace enabled. It will show you exactly how long the WASAPI callback is taking. If the time spent in the callback exceeds the buffer duration, you will experience audio “elimination” (stuttering).
Headroom Management: If your audio sounds distorted but the meters look fine, check the PlatformHeadroomDB setting in the [Audio] section of your Windows ini. Increasing this value provides more safety against digital clipping during the final WASAPI mix.
Thread Safety: When calling audio functions from C++, ensure you are using the Audio Device interface correctly. The AudioMixerWasapi module is thread-aware, but improper cross-thread UObject access can still cause crashes during device initialization.