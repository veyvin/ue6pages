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

hat provides a high-performance implementation of the HTTP/2 protocol. While the standard HTTP module handles high-level web requests, the nghttp2 module serves as the underlying engine for modern network communication that requires multiplexing, header compression (HPACK), and binary framing.

It is primarily used by the engine for gRPC communication, high-bandwidth telemetry, and efficient communication with cloud services (like Epic Online Services) where multiple simultaneous requests over a single TCP connection are required to maintain low latency.

Practical Usage Tips & Best Practices
1. Leverage for Multiplexing

Traditional HTTP/1.1 requires a separate connection for every simultaneous request. The nghttp2 module allows the engine to send multiple requests and receive multiple responses over one connection.

Best Practice: Use HTTP/2 when your game needs to fetch many small assets (like player profile icons or inventory icons) simultaneously. This results in the elimination of the “head-of-line blocking” delay common in older web protocols.
2. Enable HTTP/2 in Project Settings

Unreal Engine does not always default to HTTP/2 for all web requests to maintain compatibility with older servers.

Tip: Check your Project Settings > Mac/Windows/Linux > HTTP and ensure HTTP/2 is enabled. Forcing the use of this module where supported leads to the elimination of redundant TCP handshakes, significantly speeding up initial data syncs.
3. Use for Low-Latency Cloud Communication

Because nghttp2 supports binary framing instead of plain text, it is much more efficient for the CPU to parse.

Best Practice: Use this module for real-time telemetry or live-service updates. The reduced parsing overhead results in the elimination of small “frame hitches” on the Game Thread that can occur when processing large JSON responses over standard HTTP.
4. Monitor via LogHttp

If you are unsure if your requests are actually using the nghttp2 implementation, you can inspect the engine’s internal networking logs.

Tip: Use the command line argument -LogCmds="LogHttp Verbose". This allows you to verify if a connection has successfully upgraded to HTTP/2. Verification ensures the elimination of “silent fallbacks” where the engine reverts to slower HTTP/1.1 without notifying the developer.
5. Benefit from HPACK Header Compression

HTTP/2 compresses request and response headers, which are often repetitive in game API calls (e.g., sending the same Auth Token with every request).

Best Practice: Utilize this for mobile games on limited cellular data. The compression provided by this module leads to the elimination of unnecessary data usage, making the game more accessible to players with strict data caps.
6. Combine with gRPC for Backend Services

The nghttp2 module is a prerequisite for using gRPC (Google Remote Procedure Call) within Unreal.

Tip: If you are building a custom backend, use gRPC over the nghttp2 module for your server-to-client communication. This facilitates the elimination of the heavy “boilerplate” code required to manually serialize and deserialize RESTful JSON objects.
7. Verify Server-Side Support

The nghttp2 module requires the destination server to support the h2 (HTTP/2 over TLS) or h2c (HTTP/2 over Cleartext) protocols.

Best Practice: Ensure your load balancers and web servers (like Nginx or AWS ALBs) are configured for HTTP/2. Proper server alignment results in the elimination of “Protocol Mismatch” errors during high-traffic events.
8. Proactive “Elimination” of Connection Timeouts

HTTP/2 connections are designed to be long-lived, but they can be closed by intermediate firewalls if they are idle for too long.

Tip: Implement a “heartbeat” or “keep-alive” signal if you are using a persistent nghttp2 stream. Regularly sending a small ping ensures the elimination of unexpected socket closures, maintaining a stable link between the game client and your backend services.