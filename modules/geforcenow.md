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

gration that provides a bridge between the engine and the NVIDIA GeForce NOW (GFN) SDK. This module is essential for developers looking to optimize their games for NVIDIA’s cloud gaming service, as it allows the game to communicate directly with the GFN infrastructure.

Its primary purposes include session signaling, checking for “Cloud Save” requirements, and detecting if the game is currently running in a virtualized cloud environment. This enables the game to automatically adjust its settings to provide the best possible experience for cloud-streamed players.

Practical Usage Tips and Best Practices
1. Use Conditional Logic for Cloud Environments

When your game is running on GFN, it is effectively running on high-end hardware with a high-bandwidth connection, but it is displayed on a remote device.

Best Practice: Use IGeForceNOWWrapperModule::Get().IsRunningOnGFN() to detect the environment. Use this check to eliminate “Auto-Detect Settings” prompts, as the cloud instance should already be locked to its optimal configuration.
2. Scale UI for Diverse Devices

GFN users frequently stream to mobile phones, tablets, or low-resolution laptops.

Tip: When the GeForceNOW module detects an active session, automatically increase the Global UI Scale or swap to a “Touch-Friendly” HUD layout. This helps eliminate readability issues for players on smaller screens where standard 1080p/4K text would be illegible.
3. Optimize Latency with Reflex

The GeForceNOW module works in tandem with the NVIDIA Reflex plugin to minimize “input-to-display” lag.

Action: Ensure that NVIDIA Reflex is enabled when running on GFN. Reducing the rendering pipeline latency is critical for cloud gaming to eliminate the “heavy” feeling that players sometimes experience during streamed gameplay.
4. Handle Entitlements for “One-Click” Launch

GFN relies on “one-click” functionality to get players into the game as fast as possible.

Tip: Use the module to pass session and authentication tokens back to the GFN SDK. This allows the service to verify that the user owns the game, eliminating redundant login screens or manual password entry during the cloud session.
5. Prioritize Cloud Save Synchronization

In a GFN environment, the local file system is wiped as soon as the session ends.

Action: Ensure your game triggers a save-game sync via your Online Subsystem (Steam, Epic, etc.) immediately after any major progress. Using the GeForceNOW module hooks to signal a “Safe Shutdown” helps eliminate the risk of data loss if a user’s internet connection drops.
6. Disable Resource-Heavy Non-Essentials

Cloud instances are often shared across many users on a single server rack.

Best Practice: If GFN is detected, disable features like “Background Downloading” or “Shader Pre-Caching” that might saturate the VM’s disk I/O. This helps eliminate micro-stutters that can occur when the game and the streaming encoder compete for system resources.
7. Monitor Session Termination

The GeForceNOW SDK can send signals when the user is about to be disconnected (e.g., due to inactivity or session time limits).

Tip: Listen for these signals via the module and force a “Quick Save.” This proactive approach helps eliminate player frustration by ensuring their progress is secured before the instance is shut down by the GFN manager.
8. Customize Graphics for Video Encoding

Video streaming can cause “color banding” or “macro-blocking” in dark or highly detailed areas.

Action: When running on GFN, consider slightly increasing the Film Grain or reducing the intensity of Motion Blur. These minor adjustments help the video encoder maintain a clearer image, which works to eliminate visual artifacts in the final stream sent to the player.