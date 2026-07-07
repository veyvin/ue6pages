---
layout: default
title: BackgroundHTTPFileHash
---

<!-- ai-generation-failed -->

<h1>BackgroundHTTPFileHash</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/BackgroundHTTPFileHash/BackgroundHTTPFileHash.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BuildSettings, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

real Engine’s Background HTTP system designed to perform high-performance file verification for data downloaded in the background. It provides a standardized way to calculate and verify hashes (typically MD5 or SHA1) of files that have been retrieved while the application is in the background or minimized.

This module is essential for mobile platforms (iOS/Android) where large content updates are common. It ensures that data downloaded via the BackgroundHttp module is complete and uncorrupted before the engine attempts to mount or use it, preventing crashes or logic errors caused by partial downloads.

1. Integrate with BackgroundHttp Requests

The primary use for this module is as a post-download verification step. After a FBackgroundHttpRequest completes, use this module to generate a hash of the file on disk. Compare this result against the hash provided by your server’s manifest to ensure the integrity of the update.

2. Offload Hashing to Background Threads

Calculating a hash for a multi-gigabyte file is computationally expensive.

Best Practice: Always use the asynchronous hashing functions provided by this module. Performing a hash on the Game Thread will cause the UI to freeze, leading to a poor user experience or the OS watchdog eliminating the process for being unresponsive.
3. Verify Before Mounting Chunks

If you are using the ChunkDownloader or a custom patching system, use this module to verify the .pak or .utoc files immediately after they are written to the persistent download directory. This prevents the engine from attempting to mount a corrupted archive, which is a common cause of “missing file” errors or hard crashes.

4. Utilize MD5 for Fast Integrity Checks

While the module supports multiple algorithms, MD5 is generally preferred for file integrity checks in Unreal. It offers the best balance between calculation speed and collision resistance for non-security-critical tasks like verifying game assets. Use SHA1 only if your backend specifically requires it or for higher security requirements.

5. Match Server-Side Hashing Logic

The most common cause of verification failure is a mismatch between how the server calculates the hash and how this module does.

Tip: Ensure your CDN or manifest generator calculates the hash based on the raw binary file. If your server hashes a compressed version but the BackgroundHttp module hashes the decompressed result, the verification will fail.
6. Clean Up Corrupted Downloads

When a hash check fails, it indicates a corrupted or intercepted download.

Best Practice: If the hash does not match, your logic should immediately eliminate the local file and re-queue the download. Never allow the game to proceed with a file that failed its BackgroundHttpFileHash check.
7. Handle Low-Power States

Since this module is often used while the app is in the background, be mindful of mobile OS power management. On iOS, background execution time is limited. If the hashing process takes too long, the OS may suspend the app. Keep your download chunks small enough that hashing can complete within the OS-allotted background window.

8. Use for Cache Validation

Beyond new downloads, use this module to validate existing cached content on startup. If a user’s local storage becomes corrupted or a file is accidentally modified, a quick hash check can identify the damaged file and trigger a repair, ensuring the stability of the game environment.