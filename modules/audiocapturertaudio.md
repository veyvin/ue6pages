---
layout: default
title: AudioCaptureRtAudio
---

<!-- ai-generation-failed -->

<h1>AudioCaptureRtAudio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/AudioCaptureRtAudio/AudioCaptureRtAudio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

f a real-time audio capture backend powered by the RtAudio library.

While Unreal Engine uses platform-native backends by default (like WASAPI on Windows or CoreAudio on macOS), AudioCaptureRtAudio provides a cross-platform alternative. It is primarily used when developers require a consistent audio input interface across multiple operating systems—particularly Linux—or when specific low-level control over audio device streams is needed that platform-specific wrappers might abstract away.

Practical Usage Tips and Best Practices
1. Conditionally Include in Build.cs

Since this is a platform-specific implementation module, you typically interact with the high-level AudioCapture module. However, if you are building custom audio tools for Linux or cross-platform environments, ensure your module dependencies are wrapped correctly:

C#
	if (Target.Platform == UnrealTargetPlatform.Linux || Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("AudioCaptureRtAudio");

	}

	```

	 

	#### 2. Force the Backend via Command Line

	If you want to ensure the engine uses the RtAudio backend instead of the default platform driver (like WASAPI), you can launch your project or standalone build with the following command-line argument:

	`-audiocapturebackend=RtAudio`

	 

	#### 3. Match Sample Rates to Avoid Resampling

	RtAudio performs best when the requested sample rate matches the hardware's native rate. In your C++ setup, query the device info first and use the hardware's `PreferredSampleRate`. Attempting to capture at 44.1kHz on a 48kHz device can introduce "clicks" or "pops" due to the internal resampling overhead.

	 

	#### 4. Manage Latency vs. Stability

	RtAudio allows you to configure the buffer size. A smaller buffer (e.g., 256 or 512 samples) provides lower latency for vocal effects but increases the risk of **Audio Underruns**. If you hear "buzzing" or "choppy" audio, increase the buffer size in your `FAudioCaptureDeviceParams`.

	 

	#### 5. Handle Device "Elimination" (Disconnection)

	Mobile or USB microphones are frequently disconnected during gameplay. The RtAudio backend can sometimes hang if a device is removed while a stream is active. Always implement a check using `GetCaptureDevicesAvailable()` before attempting to restart a stream after a device change event.

	 

	#### 6. Utilize the Audio Render Thread

	Avoid performing complex signal processing (like heavy FFT analysis) on the Game Thread. The `AudioCaptureRtAudio` backend provides data through a callback; process this data on the **Audio Render Thread** to ensure the Game Thread remains responsive and doesn't "hitch" during high-frequency audio analysis.

	 

	#### 7. Thread-Safe Data Snapping

	If you need to pass captured audio data from the RtAudio callback to your game logic (e.g., for a visualizer), use a thread-safe circular buffer or an atomic "triple buffer" pattern. Never use a standard `TArray` to store incoming samples without a lock, as the audio thread will write while your game thread reads, causing memory corruption.

	 

	---

	 

	### C++ Implementation Recipe

	 

	To interact with the underlying capture system in C++, you generally use the `IAudioCapture` interface which `AudioCaptureRtAudio` implements.

	 

	**Header Includes:**

	```cpp

	#include "AudioCapture.h"

	#include "AudioCaptureDeviceInterface.h"

	```

	 

	**Implementation Logic:**

	```cpp

	void UMyAudioCaptureSystem::InitializeRtCapture()

	{

	    FAudioCapture AudioCapture;

	    TArray<FCaptureDeviceInfo> DeviceList;

	    

	    // Retrieve list of devices available to the RtAudio backend

	    AudioCapture.GetCaptureDevicesAvailable(DeviceList);

	 

	    if (DeviceList.Num() > 0)

	    {

	        FAudioCaptureDeviceParams Params;

	        Params.DeviceIndex = 0; // Use default

	        Params.NumChannels = 2;

	        Params.SampleRate = 48000;

	 

	        // Start the stream. RtAudio will now begin calling its internal callback.

	        AudioCapture.OpenCaptureStream(Params, [this](const float* AudioData, int32 NumSamples)

	        {

	            // PRO TIP: This lambda runs on the Audio Render Thread.

	            // Do NOT perform UObject operations or heavy logic here.

	            ProcessRawAudio(AudioData, NumSamples);

	        });

	        

	        AudioCapture.StartStream();

	    }

	}

	```

	 

	### Performance & Debugging

	*   **Logs:** Monitor your output log for `LogAudioCapture`. If RtAudio fails to initialize, it will report specific API errors (e.g., "RtAudio Error: No devices found").

	*   **Profiling:** Use **Unreal Insights** to monitor the Audio thread. If you see large spikes in the audio callback, your processing logic is too heavy for the chosen buffer size.

	*   **Linux Setup:** On Linux, RtAudio typically defaults to ALSA or PulseAudio. Ensure the corresponding developer libraries (e.g., `libasound2-dev`) are installed on your build machine.
Copy code
2. Force the Backend via Command Line

If you want to ensure the engine uses the RtAudio backend instead of the default platform driver (like WASAPI), you can launch your project or standalone build with the following command-line argument: -audiocapturebackend=RtAudio

3. Match Sample Rates to Avoid Resampling

RtAudio performs best when the requested sample rate matches the hardware’s native rate. In your C++ setup, query the device info first and use the hardware’s PreferredSampleRate. Attempting to capture at 44.1kHz on a 48kHz device can introduce “clicks” or “pops” due to the internal resampling overhead.

4. Manage Latency vs. Stability

RtAudio allows you to configure the buffer size. A smaller buffer (e.g., 256 or 512 samples) provides lower latency for vocal effects but increases the risk of Audio Underruns. If you hear “buzzing” or “choppy” audio, increase the buffer size in your FAudioCaptureDeviceParams.

5. Handle Device “Elimination” (Disconnection)

Mobile or USB microphones are frequently disconnected during gameplay. The RtAudio backend can sometimes hang if a device is removed while a stream is active. Always implement a check using GetCaptureDevicesAvailable() before attempting to restart a stream after a device change event.

6. Utilize the Audio Render Thread

Avoid performing complex signal processing (like heavy FFT analysis) on the Game Thread. The AudioCaptureRtAudio backend provides data through a callback; process this data on the Audio Render Thread to ensure the Game Thread remains responsive and doesn’t “hitch” during high-frequency audio analysis.

7. Thread-Safe Data Snapping

If you need to pass captured audio data from the RtAudio callback to your game logic (e.g., for a visualizer), use a thread-safe circular buffer or an atomic “triple buffer” pattern. Never use a standard TArray to store incoming samples without a lock, as the audio thread will write while your game thread reads, causing memory corruption.

C++ Implementation Recipe

To interact with the underlying capture system in C++, you generally use the IAudioCapture interface which AudioCaptureRtAudio implements.

Header Includes:

C++
	#include "AudioCapture.h"

	#include "AudioCaptureDeviceInterface.h"
Copy code

Implementation Logic:

C++
	void UMyAudioCaptureSystem::InitializeRtCapture()

	{

	    FAudioCapture AudioCapture;

	    TArray<FCaptureDeviceInfo> DeviceList;

	    

	    // Retrieve list of devices available to the RtAudio backend

	    AudioCapture.GetCaptureDevicesAvailable(DeviceList);

	 

	    if (DeviceList.Num() > 0)

	    {

	        FAudioCaptureDeviceParams Params;

	        Params.DeviceIndex = 0; // Use default

	        Params.NumChannels = 2;

	        Params.SampleRate = 48000;

	 

	        // Start the stream. RtAudio will now begin calling its internal callback.

	        AudioCapture.OpenCaptureStream(Params, [this](const float* AudioData, int32 NumSamples)

	        {

	            // PRO TIP: This lambda runs on the Audio Render Thread.

	            // Do NOT perform UObject operations or heavy logic here.

	            ProcessRawAudio(AudioData, NumSamples);

	        });

	        

	        AudioCapture.StartStream();

	    }

	}
Copy code
Performance & Debugging
Logs: Monitor your output log for LogAudioCapture. If RtAudio fails to initialize, it will report specific API errors (e.g., “RtAudio Error: No devices found”).
Profiling: Use Unreal Insights to monitor the Audio thread. If you see large spikes in the audio callback, your processing logic is too heavy for the chosen buffer size.
Linux Setup: On Linux, RtAudio typically defaults to ALSA or PulseAudio. Ensure the corresponding developer libraries (e.g., libasound2-dev) are installed on your build machine.