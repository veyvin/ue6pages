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

es a C++ wrapper for asynchronous DNS requests. While the standard SocketSubsystem in Unreal often performs DNS lookups synchronously (which can hitch the game thread), the cares module allows the engine to resolve domain names into IP addresses in the background.

It is primarily used by the Online Subsystem (OSS) and backend service modules to “eliminate” the blocking latency associated with connecting to game servers, matchmaking APIs, or telemetry endpoints.

1. Module Configuration

To utilize the cares module in your C++ project for custom network logic, include it in your Build.cs. It is typically used in conjunction with NetCore.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "NetCore", "cares" });
Copy code
2. Practical Usage Tips & Best Practices
Prevent Game Thread Hitches

Standard gethostbyname calls can take several seconds if a DNS server is slow or unreachable, freezing your game’s UI. Use the cares module to perform these lookups asynchronously. This “eliminates” frame-rate drops during the initial connection phase when a player is logging in or searching for a match.

Utilize the Unreal Wrapper Classes

Avoid calling raw c-ares C functions. Instead, look for Unreal’s internal wrappers, such as FCAresDomainNameResolver. These classes are designed to work with Unreal’s memory management and “eliminate” the risk of memory leaks associated with raw C-style pointer handling.

Handle Timeouts Gracefully

DNS resolution is prone to failure on unstable connections. When initiating a request through the cares system, always define a reasonable timeout period. This ensures that a stalled DNS query doesn’t “eliminate” the app’s ability to eventually report a “Network Connection Failed” message to the user.

Validate IP Versions (IPv4 vs. IPv6)

The cares module supports both IPv4 and IPv6. If your backend infrastructure is strictly one or the other, configure your request flags to only return the desired record types (A or AAAA). This “eliminates” ambiguity and potential connection errors on modern mobile networks that prioritize IPv6.

Use for Backend Telemetry

If your game sends frequent telemetry data to a custom URL, use cares to resolve the address once at startup and cache it. Re-resolving the DNS for every telemetry packet is inefficient; however, refresh the cache periodically to “eliminate” issues if your backend uses a Load Balancer with dynamic IP rotation.

Cross-Platform Reliability

The cares module is highly portable. By using it through the Unreal abstraction, you ensure that your DNS resolution logic behaves identically on Windows, Linux, and Android. This “eliminates” platform-specific networking bugs where one OS might use a different DNS caching policy than another.

Monitor via LogNet

When debugging connection issues, filter your Output Log for LogNet. If the cares module fails to resolve a host, it will log specific error codes (like ARES_ENOTFOUND). Understanding these codes is the fastest way to “eliminate” configuration errors in your DefaultEngine.ini or server firewall settings.

Parallel Resolution for Multiple Services

If your game connects to several microservices at once (e.g., Auth, Chat, and Store), the cares module can handle these requests in parallel. This significantly reduces the total “Time to Menu” for players by “eliminating” the need to wait for each service’s DNS to resolve sequentially.