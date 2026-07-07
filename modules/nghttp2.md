---
layout: default
title: nghttp2
---

<!-- ai-generation-failed -->

<h1>nghttp2</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/nghttp2/nghttp2.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ry, which serves as the engine’s primary implementation of the HTTP/2 protocol.

Description and Purpose

While standard web requests often use HTTP/1.1, the nghttp2 module allows Unreal Engine to leverage the more modern HTTP/2 standard for its networking needs. Its primary purpose is to provide features like header compression (HPACK) and multiplexing, which allows multiple data requests to be sent over a single TCP connection simultaneously. This is especially critical for engine systems that handle high volumes of small data packets—such as Zen Server, Virtual Assets, and cloud-based asset streaming—as it helps eliminate the “head-of-line blocking” delay common in older protocols.

Practical Usage Tips and Best Practices
Enable HTTP/2 in Project Settings
To ensure the engine utilizes this module, check your Project Settings under the HTTP section and ensure that “Use HTTP/2” is enabled. This allows the engine to eliminate the overhead of opening multiple connections when downloading many small assets from a remote server or DDC (Derived Data Cache).
Leverage for Zen Server Streaming
The Zen Storage Server uses nghttp2 to stream cooked data to target devices. When testing on consoles or mobile via a network, ensure your host PC and client are on a high-bandwidth connection. This allows the multiplexing features of nghttp2 to eliminate latency spikes during level transitions.
Debug via Network Console Variables
Use the console command HTTP.LogHttp2Transport 1 to see detailed logs of how the engine is framing and multiplexing requests. Monitoring these logs is the best way to eliminate connectivity issues where a proxy or firewall might be stripping the HTTP/2 headers.
Utilize for Virtual Asset Handshakes
If your team uses Virtual Assets (storing bulk data outside the .uasset file), the engine uses nghttp2 to pull that data from a central server. Ensuring your server supports HTTP/2 is a best practice to eliminate “Asset Not Found” hitches that occur when the engine is waiting for a legacy HTTP/1.1 queue to clear.
Monitor Concurrent Stream Limits
HTTP/2 allows many streams per connection, but servers often have a limit (e.g., 100 streams). If you are writing custom C++ to pull data from a web API, respect these limits to eliminate “Stream Refused” errors. Use the IHttpRequest interface, which handles the underlying nghttp2 logic for you safely.
Optimize Header Size
While nghttp2 uses HPACK to compress headers, sending excessively large custom headers can still impact performance. Keep your authentication tokens and metadata concise to eliminate unnecessary bandwidth consumption, especially for mobile users on cellular data.
Ensure SSL/TLS Compatibility
Almost all implementations of HTTP/2 (including nghttp2 in UE) require a secure connection (HTTPS). Always ensure your remote endpoints have valid SSL certificates. This requirement helps you eliminate “Insecure Connection” failures when the engine attempts to upgrade a connection from HTTP/1.1 to HTTP/2.
Prefer for REST API Heavy Games
If your game relies heavily on backend services (for inventory, leaderboards, or matchmaking), the nghttp2 module’s ability to keep a single connection open is far more efficient than the “connect-request-close” cycle of HTTP/1.1. This architecture is the best way to eliminate the battery drain and CPU overhead associated with constant handshake negotiations.