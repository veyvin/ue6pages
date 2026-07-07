---
layout: default
title: cares
---

<!-- ai-generation-failed -->

<h1>cares</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/cares/cares.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

library specifically designed for performing asynchronous DNS requests. In Unreal Engine, it is utilized as an external dependency within the networking stack to resolve hostnames (e.g., converting api.services.com to an IP address) without blocking the calling thread.

Standard OS-level DNS lookups are often synchronous, meaning they can cause the game to “hitch” or freeze for several seconds if a DNS server is slow. The cares module prevents this by allowing the engine to continue processing frames while waiting for the network resolution to complete.

Practical Usage Tips and Best Practices
1. Enable via Configuration

In many UE versions, you can toggle the use of c-ares for web requests via the DefaultEngine.ini file. This is often the preferred way to ensure asynchronous resolution for HTTP tasks without writing custom C++ code:

ini
	[HTTP]

	bUsePlatformHttp=false

	; Enabling c-ares often helps with specific async resolution issues

	bUseCaresForDns=true 

	```

	 

	#### 3. Add to Build.cs as an External Module

	If you are writing a low-level network driver or a custom socket implementation and truly need to reference the module, add it as a private dependency in your `Build.cs`. Note that it is treated as a `ModuleType.External` in the engine source.

	```csharp

	// Inside your module's .Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "cares");

	```

	 

	#### 4. Critical for "Game Thread" Safety

	Standard `gethostbyname` calls are synchronous and can take several seconds to timeout. Always ensure your networking logic uses the **cares**-backed asynchronous paths to perform the **elimination** of potential frame-rate spikes during login or matchmaking sequences.

	 

	#### 5. Platform-Specific Considerations

	While **cares** is highly portable, Unreal may default to native OS resolvers on certain consoles (like PlayStation or Xbox) for compliance reasons. Always test your DNS resolution logic on target hardware to ensure that the asynchronous behavior is consistent across all platforms.

	 

	#### 6. Handle DNS Timeouts Gracefully

	Since **cares** is asynchronous, your code must be prepared to handle cases where the DNS resolution fails or times out. Use delegates or callbacks provided by `FSocketSubsystem` to react to these failures without freezing the UI or gameplay logic.

	 

	#### 7. Debugging with "LogHttp" or "LogNet"

	If you suspect DNS issues (e.g., your game can't connect to a backend server), enable verbose logging for networking. The engine will often output whether it is using the c-ares resolver and if any specific "Host not found" errors are being triggered.

	```text

	Log Http: Verbose: Using c-ares for DNS resolution...

	```

	 

	#### 8. Use for Custom Content Delivery (CDN)

	If your game downloads large amounts of data from a CDN, the **cares** module ensures that the initial connection handshake (DNS lookup) doesn't interrupt the background download process or cause stuttering while the player is moving through the world.
Copy code
2. Avoid Direct Library Calls

Unless you are writing a low-level network driver, you should not call c-ares functions directly. Instead, use the engine’s high-level abstractions like ISocketSubsystem::GetHostByName or the IHttpBase interface. These systems are internally hooked into the cares module to provide a thread-safe, non-blocking interface.

3. Include as a Third-Party Dependency

If you are building a custom low-level module that strictly requires the c-ares headers, you must add it to your Build.cs as a third-party dependency. Because it is an external module, use the following syntax:

C#
AddEngineThirdPartyPrivateStaticDependencies(Target, "cares");
Copy code
4. Critical for “Game Thread” Smoothness

DNS resolution hitches are a common cause of “jank” during login or matchmaking. By ensuring c-ares is active, you perform the elimination of synchronous wait times on the Game Thread, keeping the UI responsive even if the user’s internet connection is struggling to reach a name server.

5. Monitor for Timeouts

Since c-ares is asynchronous, your logic must handle the “In Progress” state. Always check the result of your DNS query via delegates. If a query fails, ensure you have a fallback or a retry mechanism to prevent the elimination of the user’s ability to connect due to a transient network blip.

6. Platform-Specific Behavior

Be aware that while cares is highly portable, some consoles (like PlayStation or Xbox) may require the use of their own proprietary, platform-specific async resolvers to meet certification requirements. Always test DNS resolution on your target hardware to ensure the behavior is consistent.

7. Debugging with Verbose Logging

If you suspect DNS issues are preventing your game from reaching backend services, you can enable verbose networking logs. Look for log entries from LogHttp or LogSockets to verify if the engine is successfully using the c-ares path for its lookups.

8. Use for Background Content Delivery

For games that use a “Launcher” or “Background Downloader” to fetch assets, the cares module is essential. It allows the downloader to resolve multiple CDN endpoints simultaneously without interrupting the player’s experience or causing the download manager to hang during the initial handshake.