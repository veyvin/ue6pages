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

of the Unreal Engine Audio Capture interface. It serves as the bridge between the engine’s generic audio capture system and the native Android audio hardware. This module handles the low-level initialization of microphone input streams, buffer management, and sample rate conversion specifically for Android devices.

In modern versions of Unreal Engine (5.x), this module typically utilizes the Oboe library (replacing legacy OpenSL ES) to provide high-performance, low-latency audio input across the diverse Android hardware ecosystem.

Practical Usage Tips and Best Practices
Handle Android Permission Requests The module cannot capture audio until the RECORD_AUDIO permission is granted. You must call the Request Android Permission node (or the C++ equivalent) at runtime before activating the Audio Capture component. Failure to do so will “eliminate” the audio stream and return silent buffers.
Optimize for Latency vs. Battery In the Project Settings > Android, you can adjust the Audio Callback Buffer Size. Lowering this value reduces the latency of the microphone input—critical for “elimination” sounds or voice-reactive gameplay—but increases the CPU load on the mobile processor.
Manage Background State On Android, the OS may reclaim the microphone if the app is put in the background. Use the OnApplicationSuspend and OnApplicationResume delegates to stop and restart the Audio Capture component. This prevents the module from entering an error state that could “eliminate” audio functionality until the app is fully restarted.
Match Hardware Sample Rates To “eliminate” the CPU cost of software resampling, the module attempts to match the device’s native sample rate (often 48kHz). When processing this audio via MetaSounds or the Audio Bus, ensure your submixes are configured to handle the incoming sample rate efficiently to avoid stuttering.
Use the Audio Capture Component for Testing The easiest way to verify the module is working is to add an Audio Capture Component to a Pawn. Ensure Auto Activate is true, but check the Output to Bus Only setting. This allows you to visualize the microphone’s amplitude or frequency without causing a painful feedback loop in the user’s speakers.
Avoid Feedback with Echo Cancellation Android devices often have built-in Acoustic Echo Cancellation (AEC). However, this is not always exposed directly through the generic capture module. For games requiring high-quality voice, consider using the EOS Voice plugin which leverages this module but adds specialized noise and echo “elimination” logic.
Monitor Buffer Underruns If the device is under heavy load (e.g., during intense combat or complex Niagara effects), the audio capture buffer may underrun, causing “pops” or “clicks.” Use the console command stat audio on the device to monitor if the Android audio thread is keeping up with the hardware demands.
Verify Manifest Requirements Ensure that the Audio Capture Plugin is enabled in the editor. Enabling this plugin automatically instructs the Unreal Build Tool (UBT) to include the AudioCaptureAndroid module and inject the necessary android.permission.RECORD_AUDIO tag into the generated Android Manifest.