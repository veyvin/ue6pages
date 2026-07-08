---
layout: default
title: BackgroundHTTP
---

<!-- ai-generation-failed -->

<h1>BackgroundHTTP</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/BackgroundHTTP/BackgroundHTTP.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, BackgroundHTTPFileHash, BackgroundHttpIOS, Core, CoreUObject, Engine, HTTP</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eal Engine designed to handle large file downloads that persist even when the application is minimized or suspended. It is a more robust, platform-aware alternative to the standard HTTP module for long-running transfers.

What it is and What it’s used for

Unlike the standard HTTP module, which is generally used for short-lived REST API calls and can be interrupted if the application state changes, BackgroundHTTP leverages OS-specific background transfer services (such as NSURLSession on iOS or background download managers on Android/Consoles).

Primary uses include:

Large Content Downloads: Patching game data or downloading DLC while the user is not actively playing.
Persistent Transfers: Ensuring a download continues if the user switches to another app or the mobile device enters sleep mode.
Mobile Asset Delivery: Downloading OBB or PAK files post-install to minimize initial store download sizes.
Practical Usage Tips and Best Practices
1. Use for High-Volume Data Only

Do not use this module for standard gameplay API calls (like authentication or leaderboards). The overhead of registering a background task with the OS is significant; use it strictly for multi-megabyte files where the risk of interruption is high.

2. Check for Platform Support

Background HTTP is highly dependent on platform-specific implementations. Before initiating a request, verify that the current platform supports it by checking the IBackgroundHttpManager. If unsupported, you should have a fallback path to the standard HTTP module.

3. Implement Robust Delegate Handling

Because background downloads can finish while the application is in a different state, ensure your OnProcessRequestComplete delegates are thread-safe and can handle being called when the application resumes. Avoid hard-coding logic that assumes the local Game State is still identical to when the download started.

4. Manage Memory for Downloads

The BackgroundHTTP system often streams data directly to disk to prevent memory bloat. When configuring your IBackgroundHttpRequest, specify a destination file path. This is safer than keeping the entire download buffer in RAM, which could lead to the OS eliminating the app process for high memory usage.

5. Handle “Cellular Data” Constraints

On mobile platforms, the OS may pause background downloads if the user moves from Wi-Fi to a metered cellular connection. Listen for changes in the request status and provide UI feedback to the user if the OS has throttled the download due to data policies.

6. Use BackgroundHttp Notification Objects

To track progress across different parts of your C++ code, utilize the FBackgroundHttpNotificationObject. This allows multiple systems to “observe” a download’s progress without requiring direct access to the original request object.

7. Clean up Temporary Files

If a background download is canceled or fails, the module may leave partial files in the temporary directory. Implement a cleanup routine during your application’s StartupModule to eliminate any stale .tmp files left over from interrupted sessions to save user disk space.

8. Verify URL Persistence

The OS background manager often retries downloads automatically if the network drops. Ensure the URLs you provide to the BackgroundHTTP module are “long-lived” or signed with a generous expiration time. If a URL expires while the app is suspended, the OS-level retry will fail, and the download will be eliminated.