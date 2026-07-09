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

on of Unreal Engine’s audio capture interface for the Android OS. It acts as the bridge between the engine’s internal audio mixer and the Android hardware abstraction layer, typically utilizing the Oboe library or OpenSL ES backends.

This module is primarily used to enable microphone input on mobile devices. It is the backbone for features like real-time voice chat (VOIP), gameplay mechanics based on sound analysis (e.g., blowing into the mic to interact with the environment), and recording user-generated audio content on Android.

Practical Usage Tips and Best Practices
Configure Module Dependencies
If you are implementing custom audio capture logic in C++, you must add the module to your Build.cs specifically for the Android target.
C#
	    // In YourProject.Build.cs

	    if (Target.Platform == UnrealTargetPlatform.Android)

	    {

	        PublicDependencyModuleNames.Add("AudioCaptureAndroid");

	    }

	    ```

	 

	*   **Request the RECORD_AUDIO Permission**

	    Unreal's project settings allow you to add permissions, but for Android API 23+, you must request the `android.permission.RECORD_AUDIO` permission at runtime before starting capture. Use the `UAndroidPermissionFunctionLibrary` in C++ or the "Request Android Permission" node in Blueprints to ensure the OS doesn't "eliminate" your microphone stream.

	 

	*   **Leverage Oboe for Low Latency**

	    Modern versions of Unreal use the **Oboe** library within this module to minimize audio input latency. Ensure that your **Project Settings > Android > Audio > Audio Mixer** is set to use the Android Audio Mixer (default in 5.x) to take full advantage of these optimizations.

	 

	*   **Manage App Lifecycle (Pause/Resume)**

	    Android may forcibly revoke microphone access when an app enters the background. It is a best practice to bind to the `FCoreDelegates::ApplicationWillEnterBackgroundDelegate` and `ApplicationHasEnteredForegroundDelegate` to manually stop and restart your audio capture components, preventing crashes or "silent" capture bugs.

	 

	*   **Use AudioCaptureComponent for Gameplay Logic**

	    Instead of writing raw JNI bridge code, use the `UAudioCaptureComponent`. It inherits from `USynthComponent`, allowing you to route microphone input through the engine’s **Submix** system. This allows you to perform real-time envelope following or frequency analysis (FFT) on the player's voice directly on the device.

	 

	*   **Route to a Silent Submix for Analysis**

	    If you only need to analyze the player's voice (e.g., for a "clap to jump" mechanic) without the player hearing their own voice echoed back, send the `AudioCaptureComponent` output to a specific **Sound Submix** and set that submix’s **Output Volume** to 0.0. This allows the analysis logic to work while "eliminating" the feedback loop.

	 

	*   **Check Device Sample Rates**

	    Android devices vary wildly in hardware capabilities. Use the `FAudioCaptureDeviceInfo` struct in C++ to query the device's native sample rate. While Unreal performs resampling, aligning your processing logic with the device's native rate can reduce CPU overhead on lower-end mobile chipsets.

	 

	*   **Monitor Battery Impact**

	    Continuous audio capture is a heavy drain on mobile batteries and can cause thermal throttling on older Android devices. Only activate the `AudioCaptureAndroid` logic when strictly necessary (e.g., during a specific gameplay sequence or when the push-to-talk button is held) to preserve the player's device health.
Copy code
Request the RECORD_AUDIO Permission
Unreal’s project settings allow you to add permissions, but for Android API 23+, you must request the android.permission.RECORD_AUDIO permission at runtime before starting capture. Use the UAndroidPermissionFunctionLibrary in C++ or the “Request Android Permission” node in Blueprints to ensure the OS does not “eliminate” your microphone stream.
Leverage Oboe for Low Latency
Modern versions of Unreal (5.x) use the Oboe library within this module to minimize audio input latency. Ensure that your Project Settings > Android > Audio > Audio Mixer is set to use the Android Audio Mixer (enabled by default) to take full advantage of these optimizations.
Manage App Lifecycle (Pause/Resume)
Android may forcibly revoke microphone access when an app enters the background. It is a best practice to bind to the FCoreDelegates::ApplicationWillEnterBackgroundDelegate and ApplicationHasEnteredForegroundDelegate to manually stop and restart your audio capture components, preventing crashes or “silent” capture bugs.
Use AudioCaptureComponent for Gameplay Logic
Instead of writing raw JNI bridge code, use the UAudioCaptureComponent. It inherits from USynthComponent, allowing you to route microphone input through the engine’s Submix system. This allows you to perform real-time envelope following or frequency analysis (FFT) on the player’s voice directly on the device.
Route to a Silent Submix for Analysis
If you only need to analyze the player’s voice (e.g., for a “clap to jump” mechanic) without the player hearing their own voice echoed back, send the AudioCaptureComponent output to a specific Sound Submix and set that submix’s Output Volume to 0.0. This allows the analysis logic to work while “eliminating” the feedback loop.
Check Device Sample Rates
Android devices vary widely in hardware capabilities. Use the FAudioCaptureDeviceInfo struct in C++ to query the device’s native sample rate. While Unreal performs resampling, aligning your processing logic with the device’s native rate can reduce CPU overhead on lower-end mobile chipsets.
Monitor Battery Impact
Continuous audio capture is a heavy drain on mobile batteries and can cause thermal throttling on older devices. Only activate the AudioCaptureAndroid logic when strictly necessary (e.g., during a specific gameplay sequence) to preserve the player’s device health and “eliminate” unnecessary power consumption.