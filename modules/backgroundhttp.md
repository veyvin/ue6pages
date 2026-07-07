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

ed for high-reliability, long-running file transfers that can persist even when the application is not in the foreground. Unlike the standard HTTP module, which is intended for fast request-response cycles (like REST APIs), BackgroundHttp leverages platform-specific APIs (such as iOS Background Fetch or Android WorkManager) to ensure large downloads—like patches, DLC, or telemetry—continue reliably in the background.

It provides a hardware-abstracted interface (IBackgroundHttpRequest) that handles the complexities of mobile task completion and OS-level download management.

Practical Usage Tips & Best Practices
1. Proper Build.cs Dependency

To use this module in C++, you must add it to your module’s dependencies. It is often used alongside the HTTP module for a complete networking solution:

C#
PublicDependencyModuleNames.AddRange(new string[] { "Http", "BackgroundHttp" });
Copy code
2. Use Primarily for Large Assets

Reserved for transfers that take significant time. For small JSON requests or quick metadata fetches, stick to the standard HTTP module. Using BackgroundHttp for tiny, frequent requests adds unnecessary overhead to the OS task scheduler and can lead to the elimination of battery efficiency.

3. Handle App Resumption via Delegates

Because a download might finish while the app is suspended, you must bind to OnProcessRequestComplete. When the user re-opens the app, the BackgroundHttpManager will flush the results of completed tasks, allowing your logic to resume exactly where it left off.

4. Platform-Specific Pathing

BackgroundHttp often downloads files directly to a temporary OS-managed location. Use GetDownloadedFileName() on the request object to find the actual local path. Always move these files to your permanent FPaths::ProjectSavedDir() immediately after completion, as the OS may “eliminate” temporary files to reclaim space.

5. Implement Progress UI with Throttling

Use OnProgress to update your loading bars. However, since large downloads generate many progress events, throttle your UI updates (e.g., only update the bar every 1% or every 0.5 seconds) to prevent the Game Thread from hitching during high-speed transfers.

6. Support for Resume and Retry

The module is designed to handle network interruptions gracefully. If a user loses Wi-Fi, the OS-level background service will pause the request and resume it once connectivity is restored. Do not manually cancel and restart requests on every minor error; let the manager handle the retry logic.

7. Mobile Task Completion Limits

Be aware that iOS and Android impose strict time limits on background tasks. If your download is massive (multiple gigabytes), the OS might suspend it if the device enters a low-power state. Always check the request status upon app startup to see if a transfer was “eliminated” by the OS and needs to be queued again.

8. Associate Requests with User IDs

When starting a background download, you can attach custom headers or metadata. It is a best practice to include a unique session or user ID in the request metadata so that if the download finishes after a user logs out and back in, your system can verify if the content is still relevant to the current session.