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

is kept small, and additional high-resolution assets or game modes are downloaded and “mounted” asynchronously while the user is playing.

Practical Usage Tips & Best Practices
1. Integrate with Primary Asset IDs

The InstallBundleManager works most effectively when your content is organized via the Asset Manager.

Best Practice: Assign your assets to specific Primary Asset Labels. This allows the manager to treat a group of assets as a single bundle, leading to the elimination of manual file tracking by using the engine’s built-in asset discovery logic.
2. Manage the Mounting Lifecycle

Downloading a bundle is only half the process; it must also be “mounted” into the engine’s virtual file system (VFS).

Tip: Always use the RequestInstallBundle function to handle both the download and the mount in one operation. This ensures the elimination of “file not found” errors that occur when the game tries to access an asset that has been downloaded but not yet registered with the engine.
3. Implement Persistent Storage Checks

Streaming installs can fail silently if the device runs out of storage space mid-download.

Best Practice: Use the GetBundleInstallState API to query disk space requirements before starting a download. This proactive check results in the elimination of corrupted installations and provides a better user experience by warning the player before they hit a storage limit.
4. Handle Cellular Data Confirmations

On mobile platforms, downloading large bundles over a cellular network can be expensive for the user.

Tip: Utilize the manager’s built-in hooks for network status. Use these to trigger a UI prompt for “Download over Cellular.” This ensures the elimination of accidental data cap overages, which is a requirement for many mobile storefront certifications.
5. Use Asynchronous Callbacks for UI Feedback

The process of downloading and mounting bundles is entirely asynchronous and can take several minutes.

Best Practice: Bind delegates to the OnInstallBundleComplete event. This allows your UI to show accurate progress bars and status text (e.g., “Mounting Content…”), leading to the elimination of player confusion during long background tasks.
6. Optimize via Priority-Based Downloading

Not all content is needed at the same time; a player in the tutorial doesn’t need the assets for Level 50.

Tip: Set appropriate priority levels for your bundles. High-priority bundles (like the current map) should be requested first to facilitate the elimination of long “waiting” screens, while low-priority bundles (like cosmetic skins) can download silently in the background.
7. Ensure Proper Unmounting and Clean-up

Keeping every bundle mounted simultaneously can lead to memory bloat and slowed asset lookups.

Best Practice: Call ReleaseBundle when a specific game mode or map is no longer needed. This results in the elimination of unnecessary memory overhead by unloading the associated pack files and freeing up the engine’s internal file cache.
8. Verify Manifest Versions

The manager relies on a manifest file (usually hosted on a CDN) to know which files belong to which bundle.

Tip: During the boot sequence, always check for a manifest update before attempting to load content. This ensures the elimination of version mismatches where the client tries to mount a bundle that is no longer compatible with the current game executable.