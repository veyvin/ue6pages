---
layout: default
title: GoogleGameSDK
---

<!-- ai-generation-failed -->

<h1>GoogleGameSDK</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/GoogleGameSDK/GoogleGameSDK.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

cated in Engine/Source/ThirdParty/GoogleGameSDK, this module provides a suite of low-level tools that help developers optimize the “Android experience.” While the standard Android plugins handle high-level features like achievements, this module focuses on technical performance and hardware-level communication.

Primary uses include:

Frame Pacing (Swappy): Synchronizing the engine’s render loop with the Android display’s refresh rate to eliminate visual stutter and reduce input latency.
Performance Monitoring (Tuning Fork): Reporting detailed frame-time data and quality settings back to the Google Play Console for real-world performance analysis.
Game Mode API: Allowing the game to communicate its state (e.g., “Loading,” “Gameplay”) to the OS so Android can optimize CPU/GPU resources or silence notifications.
Memory Management: Providing tools to better monitor and handle the strict memory constraints of various Android devices.
Practical Usage Tips and Best Practices
1. Enable Swappy for Consistent Frame Delivery

The Swappy library is the most critical part of this module. It should be enabled in your Project Settings under Android > Frame Pacing. By default, it helps in the elimination of “micro-stutter” by ensuring the engine doesn’t push frames faster than the screen can display them, which also helps prevent the device from overheating.

2. Use CVars to Fine-Tune Pacing

You can control the Google Game SDK frame pacer at runtime using console variables. Use a.UseSwappyForFramePacing 1 to ensure it is active. If you notice input lag on high-end devices, you can experiment with r.setframepace to lock the framerate to exactly half the refresh rate (e.g., 60fps on a 120Hz screen) for maximum stability.

3. Implement the Game Mode API

In your C++ or via Blueprint nodes, use the Game Mode API to signal when the player is in a loading screen versus active gameplay. When you signal “Loading,” the OS can temporarily boost clock speeds to shorten load times, which is a best practice for improving the user’s perceived performance.

4. Configure Tuning Fork for Real-World Data

If you are shipping on the Google Play Store, integrate the Tuning Fork component. It allows you to define “Quality Levels” in your project that match your Device Profiles. This provides you with a dashboard in the Play Console showing exactly where users are experiencing frame drops, helping you target specific devices for optimization.

5. Optimize Input Latency

Swappy works by predicting when the next frame will be displayed. To get the most out of this, ensure your Enhanced Input logic is not throttled. The Google Game SDK helps synchronize input sampling with the start of the frame, leading to the elimination of the “spongy” feel often associated with mobile touch controls.

6. Audit Memory with AGDK Tools

Android is aggressive about closing background apps that consume too much memory. Use the memory tools within this SDK to monitor your “Resident Set Size” (RSS). Setting up alerts for when your game approaches the “low memory” threshold allows you to proactively clear textures or purge the C++ object cache.

7. Profile with Android GPU Inspector (AGI)

The Google Game SDK enables deeper integration with the Android GPU Inspector. When this module is active, AGI can provide more granular data about your Vulkan or OpenGL ES draw calls, allowing you to identify bottlenecks in your shaders or Nanite-proxy meshes on mobile hardware.

8. Update Device Profiles Regularly

The effectiveness of the Google Game SDK often relies on correct Device Profiles. Ensure your BaseDeviceProfiles.ini accurately reflects the capabilities of popular Android chipsets (Snapdragon, Exynos, etc.). Proper profiling ensures the SDK can apply the correct frame pacing and thermal throttling logic for each specific device.