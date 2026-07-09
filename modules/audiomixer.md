---
layout: default
title: AudioMixer
---

<!-- ai-generation-failed -->

<h1>AudioMixer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioMixer/AudioMixer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioExtensions, AudioLinkCore, AudioLinkEngine, AudioMixerCore, AudioPlatformConfiguration, Core, CoreUObject, Engine, HeadMountedDisplay, SignalProcessing, SoundFieldRendering, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

thin Unreal Engine. Historically, Unreal relied on platform-specific backends (like XAudio2 for Windows or CoreAudio for Mac), which led to inconsistent features across devices. The AudioMixer replaces these with a unified C++ renderer that performs all decoding, mixing, and DSP (Digital Signal Processing) in a platform-agnostic way.

It is used to drive the engine’s most advanced audio features, including MetaSounds, Quartz (sample-accurate timing), and the Submix graph system.

1. Module Configuration

To interact with the audio renderer in C++, you must include AudioMixer in your Build.cs. If you are creating custom DSP effects, you should also include SignalProcessing.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "AudioMixer", 

	    "SignalProcessing", 

	    "AudioExtensions" 

	});

	```

	 

	To access the audio device in code:

	```cpp

	#include "AudioDevice.h"

	#include "AudioMixerDevice.h"

	 

	// Retrieve the current audio device and cast to mixer

	if (FAudioDevice* AudioDevice = GetWorld()->GetAudioDeviceRaw())

	{

	    Audio::FAudioMixerDevice* MixerDevice = static_cast<Audio::FAudioMixerDevice*>(AudioDevice);

	}

	```

	 

	---

	 

	### 2. Practical Usage Tips & Best Practices

	 

	#### Use Submixes for Grouped DSP

	Instead of applying effects to every individual `AudioComponent`, route sounds to a **Sound Submix**. This allows you to apply a single "Master Reverb" or "Global EQ" to hundreds of sounds simultaneously, significantly "eliminating" CPU overhead by processing a single mixed buffer rather than dozens of individual ones.

	 

	#### Leverage Audio Buses for Side-Chaining

	Use **UAudioBus** to create "patch cables" between sounds. For example, send your music to an Audio Bus and use that bus as an external "Key Source" in a compressor on your SFX Submix. This creates a professional "ducking" effect where the music automatically gets quieter when a character speaks or an explosion occurs.

	 

	#### Implement Quartz for Sample-Accurate Events

	For rhythm-based games or procedural music, do not use `SetTimer` or `Tick`. Use **Quartz** (`UQuartzSubsystem`). Quartz schedules audio events directly on the AudioMixer's render thread, "eliminating" the latency jitter caused by the Game Thread's variable frame rates.

	 

	#### Optimize with Submix Effect Presets

	When creating custom DSP in C++, derive from `USoundEffectSubmix`.

	*   **Best Practice:** Keep the `OnProcessAudio` function as lean as possible. It runs on the high-priority Audio Render Thread. Any blocking calls or heavy memory allocations here will cause audible "pops" or system-wide hitches.

	 

	#### Control Dynamic Headroom

	If your game has many overlapping loud sounds, they may "clip" (distort). Use the `PlatformHeadroomDB` setting in your `DefaultEngine.ini` under `[Audio]` to give the AudioMixer more "space" to mix without hitting the digital ceiling.

	 

	#### Use MetaSounds for Procedural Logic

	"Eliminate" the need for complex C++ state machines for simple audio logic by using **MetaSounds**. Since MetaSounds are a native part of the AudioMixer's graph, they support sample-accurate control and can be updated via the **Audio Modulation** plugin to change parameters (like pitch or volume) with zero zipper noise.

	 

	#### Monitor Performance with "stat audio"

	Use the console command `stat audio` to monitor the AudioMixer's health. Watch the **"Mixer Render Time"**; if it exceeds your audio buffer length (usually ~10-20ms), you are over-processing and need to simplify your submix graph or reduce the number of active `Source Effects`.

	 

	#### Handle Garbage Collection Carefully

	Audio objects (like `USoundWave` or `USoundSubmix`) used in C++ must be tracked via `UPROPERTY()`. If an object is garbage collected while the AudioMixer is still trying to process its buffer, the engine will crash. Always ensure your sound references remain valid until the `AudioComponent` has finished playing.
Copy code
2. Practical Usage Tips & Best Practices
Leverage Submixes for Grouped Processing

Instead of applying effects to individual sounds, route them to a Sound Submix. The AudioMixer processes a submix as a single mixed buffer. Applying a “Master Reverb” to a submix “eliminates” the CPU overhead of running separate reverb instances for every active sound source.

Use Quartz for Rhythm-Critical Logic

Standard Blueprints and Timers are bound to the Game Thread, which has variable latency. For music or rhythmic gameplay, use Quartz (UQuartzSubsystem). Quartz schedules events directly on the AudioMixer’s render thread, providing sample-accurate timing and “eliminating” jitter.

Minimize “Main Thread” Calls in DSP

If you are writing custom USoundEffectSubmix classes, never perform heavy logic, file I/O, or memory allocation inside the OnProcessAudio function. This function runs on the high-priority Audio Render Thread; any delay here will “eliminate” audio stability, causing pops, clicks, or system-wide hitches.

Control Dynamic Headroom

When many loud sounds play simultaneously, they can exceed the digital maximum and “clip.” You can prevent this by adjusting the PlatformHeadroomDB setting in your DefaultEngine.ini under the [Audio] section. This gives the mixer more “room” to sum loud signals without distortion.

Utilize Audio Buses for Side-Chaining

Use Audio Buses to send the output of one submix into the “Key Source” of another’s compressor. This is ideal for “ducking” music when a character speaks or an explosion occurs, ensuring important gameplay sounds are never “eliminated” by background tracks.

Implement Distance-Based LODs

The AudioMixer supports Concurrency and LOD Thresholds. For complex procedural sounds, set a distance threshold to disable the actual DSP processing when the player is too far away. This ensures the CPU is not wasted on audio that the player cannot hear.

Monitor Health with “stat audio”

Use the console command stat audio to monitor the AudioMixer’s performance in real-time. Keep an eye on the “Mixer Render Time”; if this value approaches the buffer length (typically 10-20ms), your project’s audio complexity is too high and requires optimization.

Efficient Variable Modulation

When changing parameters like Pitch or Volume at runtime, use the Audio Modulation plugin. This allows the AudioMixer to smoothly interpolate values between frames, “eliminating” the “zipper noise” or artifacts caused by immediate value jumps in traditional Blueprint updates.