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

library, a specialized C library used by Unreal Engine to perform asynchronous DNS lookups.

In network programming, standard DNS resolution functions (like gethostbyname) are “blocking,” meaning they pause the entire thread until the DNS server responds. If this occurs on the Game Thread, the game will freeze. The cares module allows Unreal to resolve domain names (like dedicated server URLs) in the background, ensuring the elimination of network-related hitches during the connection process.

Practical Usage Tips and Best Practices
1. Include as an Engine Dependency

If you are building a custom low-level networking plugin that requires manual DNS resolution, you must add the module to your Build.cs. Since it is an External module, use the third-party helper:

C#
	AddEngineThirdPartyPrivateStaticDependencies(Target, "cares");

	```

	 

	#### 2. Avoid Direct c-ares API Calls

	Unless you have a highly specialized use case, do not call the `ares_*` functions directly. Instead, use the engine's abstraction layer, **`ISocketSubsystem`**. The engine internally uses `cares` when you call `GetHostByName`, provided the platform supports it. This ensures your code remains cross-platform and GC-safe.

	 

	#### 3. Monitor for "Hanging" DNS Lookups

	If a player's internet connection is unstable, DNS lookups can take several seconds. Even though `cares` is asynchronous, the engine might be waiting for the result before proceeding with a connection. Use the console command `net.IpConnectionDisableResolution 1` during local testing to bypass DNS and use direct IPs, which helps in the **elimination** of DNS-related connection delays.

	 

	#### 4. Check for Platform Support

	Not all platforms use `cares`. Windows and Linux commonly use it, but consoles (PS5, Xbox) often use their own proprietary, non-blocking OS-level resolvers. Always wrap your custom networking code in `#if WITH_LIBCARES` to ensure it compiles on all target platforms.

	 

	#### 5. Debugging with "net.DebugAppendResolverAddress"

	If you suspect DNS resolution is failing or pointing to the wrong IP, use the console variable `net.DebugAppendResolverAddress [Address]`. This allows you to force the resolver to use a specific DNS server, which is invaluable for the **elimination** of "Server Not Found" bugs in complex network environments.

	 

	#### 6. Use IPv6-Compatible Lookups

	The `cares` module supports both IPv4 and IPv6. When resolving addresses for modern platforms (especially mobile), ensure your networking logic doesn't assume a 32-bit IP address. The engine's `FInternetAddr` class handles this gracefully when backed by the `cares` resolver.

	 

	#### 7. Prefer IPs for Dedicated Servers

	While `cares` makes DNS lookups asynchronous, it still adds latency to the initial connection. For competitive dedicated server environments, it is a best practice to provide the client with the direct IP address via your Matchmaking/Master Server API. This results in the total **elimination** of the DNS resolution step for the client.

	 

	#### 8. Verify initialization in logs

	If you suspect the module isn't working, check your startup logs for "cares" or "c-ares". The engine will log an error if the third-party library fails to initialize (usually due to missing system permissions or a restricted network environment). Correcting these early ensures the **elimination** of silent network failures.
Copy code
2. Utilize via SocketSubsystem

For most gameplay needs, do not call ares_* functions directly. Instead, use ISocketSubsystem::Get()->GetHostByName(). When the cares module is active on supported platforms, the engine internally uses it to handle the request asynchronously, leading to the elimination of complex manual thread management.

3. Monitor for DNS Latency Hitches

Even though cares is asynchronous, a slow DNS response can delay the transition to a new level or match. Use the console command net.IpConnectionDisableResolution 1 during development to bypass DNS and use direct IP addresses. This helps in the elimination of variables when debugging slow connection times.

4. Wrap with Platform Macros

The cares module is not available on all platforms (some consoles use proprietary OS-level resolvers). Always wrap your code in #if WITH_LIBCARES to ensure your project compiles across different architectures without missing symbol errors.

5. Debug with Name Resolution Flags

If your game is failing to connect to a server via URL, use the console variable net.DebugAppendResolverAddress [ServerIP]. This forces the resolver to use a specific address, allowing you to test if the issue lies with the cares implementation or a specific ISP’s DNS settings.

6. Support for Dual-Stack (IPv4/IPv6)

The cares module is compliant with modern networking standards. Ensure your C++ logic uses FInternetAddr to store the results of a lookup rather than a raw integer or string. This allows the engine to handle both IPv4 and IPv6 addresses correctly, ensuring the elimination of compatibility issues on mobile networks.

7. Verify Thread Safety

If you are performing hundreds of manual lookups (e.g., in a master server browser), do not share a single ares_channel across threads. While the engine’s wrapper is safe, raw c-ares calls are not. Creating local instances within your worker threads allows for the elimination of race conditions and crashes.

8. Check Initialization Logs

Upon startup, the engine logs the status of its network subsystems. Search your log for “c-ares” to verify the module has initialized correctly. If it fails to load due to system permissions or firewall restrictions, the engine may fallback to blocking calls, which you should address to ensure the elimination of potential frame-rate drops during matchmaking.