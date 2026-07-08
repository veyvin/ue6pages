---
layout: default
title: GeForceNOW
---

<!-- ai-generation-failed -->

<h1>GeForceNOW</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/GeForceNOW/GeForceNOW.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

optimize Unreal Engine applications for NVIDIA’s cloud gaming platform. It provides a C++ and Blueprint interface to the NVIDIA GeForce NOW (GFN) SDK, allowing the game to communicate directly with the cloud streaming environment.

Its primary purpose is to handle cloud-specific logic such as session signaling, identifying if the game is running in a streaming context, and managing “Cloud Saves” or user authentication state. By utilizing this module, developers can eliminate common friction points in cloud gaming, such as incorrect display settings or abrupt session terminations.

Practical Usage Tips and Best Practices
Detect the Cloud Environment
Use the module’s API to check if the game is currently running on a GFN server. Knowing this allows you to eliminate unnecessary local settings (like “Ultra” disk-heavy texture streaming) and instead focus on settings optimized for a high-bandwidth video stream.
Automate Graphics Scaling
When the GeForceNow module confirms a cloud session, you should automatically apply a “Cloud” scalability profile. This helps eliminate visual artifacts caused by aggressive motion blur or film grain, which can often look poor when processed through a video encoder.
Synchronize Cloud Saves Early
GFN sessions are ephemeral. Use the module’s callbacks to ensure that game state and player progress are synchronized with your backend as soon as a milestone is reached. This practice helps eliminate data loss if the user’s internet connection drops and the cloud instance is recycled.
Monitor Session Status
Subscribe to session lifecycle events to detect when a user is being timed out due to inactivity. You can use these events to trigger an auto-save or display a custom UI warning, which helps eliminate player frustration during forced session closures.
Optimize for Latency-Sensitive Input
If the GFN module is active, consider enabling “Low Latency” input modes or reducing internal frame buffering. This helps eliminate the “floaty” feeling that can occur when network latency is added on top of engine render latency.
Handle Multi-User Login Flow
The GFN module can provide information about the user’s platform (e.g., Steam, Epic, or GOG). Use this data to automatically skip redundant login screens, helping to eliminate extra clicks and get the player into the game as quickly as possible.
Adjust UI for Small Streamed Screens
Many GFN users play on mobile devices or tablets. Use the detection logic from this module to trigger a “Large Text” or “Touch Optimized” UI layout. This helps eliminate readability issues caused by streaming a 1080p or 4K desktop interface to a 6-inch phone screen.
Include in Build.cs Dependencies
To access the GFN features in C++, you must add "GeForceNow" to your PublicDependencyModuleNames. Ensure you wrap your calls in #if WITH_GEFORCENOW (or a similar project-defined macro) to eliminate linker errors when building for platforms where the NVIDIA SDK is not supported.