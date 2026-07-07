---
layout: default
title: InstallBundleManager
---

<!-- ai-generation-failed -->

<h1>InstallBundleManager</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/InstallBundleManager/InstallBundleManager.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, IoStoreOnDemandCore, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

signed to handle the asynchronous downloading, patching, and mounting of game content “bundles” on mobile and consoles.

Description and Purpose

This module acts as a robust coordinator for Background Downloads and On-Demand Content. While the lower-level ChunkDownloader focuses on the raw retrieval of files, the InstallBundleManager provides a unified API for managing the entire lifecycle of a content bundle—from checking for updates and verifying disk space to the final mounting of .pak files. It is specifically built to handle the complexities of mobile platforms (iOS/Android) and modern consoles, where games often download a small “initial” executable and then stream the remaining high-resolution assets in the background.

Practical Usage Tips and Best Practices
Implement “Initial” and “On-Demand” Bundles
Divide your game into an “Initial” bundle (required to reach the main menu) and several “On-Demand” bundles (specific levels or characters). This allows the user to start playing quickly while the manager works in the background to eliminate long waiting periods during the first launch.
Check Connectivity and Disk Space First
Before initiating a large download, use the manager’s built-in query functions to check for a Wi-Fi connection and sufficient storage. Informing the user of a storage shortage before starting helps you eliminate failed download attempts and corrupted partial files.
Use Bundle Priority for Seamless Gameplay
The manager allows you to set priorities for different bundles. If a player selects “Level 5” while other assets are downloading, increase the priority of the Level 5 bundle. This helps you eliminate loading hitches by ensuring the most relevant data is processed first.
Handle Background Suspend Gracefully
On mobile devices, the OS may suspend your app during a download. Use the InstallBundleManager delegates to save the current progress state. This ensures that when the app resumes, the manager can pick up exactly where it left off to eliminate redundant data usage.
Utilize the Persistent Content Cache
The module manages a local cache for downloaded bundles. Instead of re-downloading every update, the manager can perform delta-patching. This efficiency helps you eliminate unnecessary bandwidth costs for both the developer (CDN fees) and the end-user.
Bind to Lifecycle Delegates
Always bind to the OnInstallBundleComplete and OnInstallBundleProgress delegates. This allows your UI to provide accurate progress bars and error messages, which helps you eliminate player confusion during large content updates.
Clean Up Old Bundles Regularly
Use the manager to track which bundles are no longer needed (e.g., assets from a previous seasonal event). Calling the delete functions for these specific bundles helps you eliminate “storage creep” and keeps your game’s footprint small on the user’s device.
Validate Manifests for Content Integrity
The manager uses manifest files to track bundle versions. Always verify the manifest version against your server before allowing the game to proceed. This synchronization is the best way to eliminate “version mismatch” crashes where the game tries to load assets that don’t match the executable’s logic.