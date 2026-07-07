---
layout: default
title: AudioCaptureAndroid
---

<!-- ai-generation-failed -->

<h1>AudioCaptureAndroid</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioCaptureImplementations/Android/AudioCaptureAndroid/AudioCaptureAndroid.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioCaptureCore, Core, GoogleOboe</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

on of the Unreal Engine IAudioCapture interface for Android devices. It acts as the bridge between the engine’s audio systems and the Android hardware, specifically utilizing the Oboe library (and formerly OpenSL ES) to handle low-latency microphone input.

This module is what allows components like the AudioCaptureComponent to function on mobile hardware, enabling features such as voice-driven gameplay, environmental reactivity, or local recording.

Practical Usage Tips and Best Practices
1. Configure Mandatory Permissions

The module will fail to initialize if the correct Android permissions are not requested.

Project Settings: Add android.permission.RECORD_AUDIO to the Extra Permissions array in Project Settings > Platforms > Android.
Runtime Check: For Android 6.0+, you must use the AndroidPermission library in Blueprints or C++ to request this permission from the user at runtime before attempting to start the capture.
2. C++ Module Dependency Setup

If you are interacting with the capture system via code, you must include the module in your build script. Wrap it in a platform check to avoid compilation errors on non-Android targets.

C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { 

	        "AudioCapture", 

	        "AudioCaptureAndroid" 

	    });

	}

	```

	 

	#### 3. Match Hardware Sample Rates

	Recording at a sample rate that differs from the Android device's native rate can cause expensive software resampling, increasing latency and CPU usage.

	*   **Tip:** Use the **AudioCapture** plugin’s `GetAudioCaptureDeviceInfo` to determine the device's native sample rate (usually 44100Hz or 48000Hz) and initialize your stream using that value to **eliminate** unnecessary overhead.

	 

	#### 4. Tune Callback Buffer Sizes

	Android audio is sensitive to buffer sizes. Small buffers reduce latency but increase the risk of "underruns" (audio glitches/pops).

	*   **Best Practice:** Adjust the **Audio Callback Buffer Size** in **Project Settings > Platforms > Android > Audio**. A value of 512 or 1024 is generally safe for stable recording, while 128 or 256 is better for real-time interactive voice features if the hardware supports it.

	 

	#### 5. Handle Audio Focus and Interruptions

	Android applications can lose "Audio Focus" if a phone call comes in or another app plays sound.

	*   **Tip:** Implement logic to call `Stop` on your audio capture when the application moves to the background (handled via `FCoreDelegates::ApplicationWillDeactivateDelegate`). This prevents the Android OS from force-killing your audio session.

	 

	#### 6. Use for Envelope Following (Visualizers)

	One of the most practical uses for this module on Android is driving visual elements via the player's voice.

	*   **Best Practice:** Route the `AudioCapture` component to a **Submix**. Apply a **Submix Envelope Follower** or **Submix FFT Analysis**. This allows you to create "voice-reactive" environments without the complexity of full voice-chat networking.

	 

	#### 7. Prefer Oboe for Lower Latency

	Unreal Engine 5 increasingly defaults to the Oboe backend for Android.

	*   **Tip:** If you experience high latency, ensure that `Android.UseOboe` is enabled in your `BaseEngine.ini` or via Console Variables. Oboe is designed specifically to **eliminate** the high-latency paths present in older Android OpenSL implementations.

	 

	#### 8. Prevent Echo and Feedback

	If you are playing back the captured audio through the device speakers while recording, you will likely create a feedback loop.

	*   **Best Practice:** Check **"Output to Bus Only"** on the `AudioCapture` component. This allows you to analyze the audio data (e.g., for gameplay triggers) while **eliminating** the microphone audio from the final speaker output, preventing painful acoustic feedback.
Copy code
3. Match Hardware Sample Rates

To eliminate high CPU overhead caused by software resampling, always try to initialize your audio capture using the device’s native sample rate (typically 48000Hz or 44100Hz). You can query the device defaults using the AudioCapture plugin’s C++ API.

4. Manage Audio Focus

Android is a multi-tasking environment where other apps (like phone calls) can take control of the microphone.

Best Practice: Listen for the ApplicationWillDeactivateDelegate. When your app loses focus, explicitly stop the audio capture to release the hardware resource. This prevents the OS from force-closing your app to reclaim the microphone.
5. Use “Output to Bus Only” for Feedback Prevention

If you are capturing microphone input to analyze it (e.g., for a “blow into the mic” mechanic), ensure you do not play the audio back through the device speakers.

Tip: Check the Output to Bus Only setting on your AudioCapture component. This allows you to send the signal to a Submix for analysis while eliminating the risk of a painful acoustic feedback loop.
6. Optimize Buffer Sizes for Latency

Mobile devices are sensitive to audio buffer sizes.

Best Practice: In Project Settings > Platforms > Android > Audio, tune the Audio Callback Buffer Size. Lower values (e.g., 256 or 512) reduce latency for interactive tasks but increase the risk of “crackling” if the CPU is under heavy load.
7. Prefer Oboe for Modern Devices

Unreal Engine 5 uses Google’s Oboe library within this module. Oboe is designed to automatically select the best path (AAudio or OpenSL ES) for the specific device.

Tip: Ensure Android.UseOboe is set to 1 in your BaseEngine.ini. Oboe helps eliminate the high-latency issues found on older Android audio paths.
8. Implement Silence Detection

Continuous microphone polling can drain mobile batteries.

Best Practice: If your gameplay only requires intermittent microphone input, use the Stop function when the input is not needed. Implement a simple amplitude threshold check so the game only processes audio data when the user is actually speaking, saving significant processing power.