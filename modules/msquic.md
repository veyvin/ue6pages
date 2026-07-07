---
layout: default
title: MsQuic
---

<!-- ai-generation-failed -->

<h1>MsQuic</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/MsQuic/MsQuic.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

UIC transport protocol, based on Microsoft’s open-source library. QUIC is a modern UDP-based protocol that provides the reliability of TCP but with significantly lower latency and improved security (built-in TLS 1.3).

In Unreal Engine, this module is primarily used as the high-performance transport layer for HTTP/3 requests and as an alternative backend for the Iris Replication System. It is designed to solve the “head-of-line blocking” issues common in older protocols, making it ideal for high-concurrency connections and unstable network environments.

Practical Usage Tips and Best Practices
1. Enable for HTTP/3 Support

To utilize the speed of HTTP/3 for your backend communications (like downloading patches or fetching player profiles), you must ensure the MsQuic module is available.

Action: Add "MsQuic" to your PrivateDependencyModuleNames in your *.Build.cs file. This allows your project to use the QUIC-based HTTP implementation, helping you eliminate the slow “handshake” overhead associated with traditional HTTPS/TCP.
2. Use for High-Latency Network Environments

Traditional TCP connections can stall if a single packet is lost. MsQuic handles multiple streams independently.

Tip: If your game targets mobile players or regions with unstable internet, use MsQuic-backed data streams. Because it treats different data streams as independent, a lost packet in one stream won’t block others, which helps you eliminate “jitter” and hitching in your network traffic.
3. Transition to Iris with MsQuic

The Iris Replication System can utilize MsQuic as a net driver backend to handle massive object counts more efficiently.

Best Practice: In your DefaultEngine.ini, configure Iris to use the QUIC transport for dedicated server connections. This utilizes the protocol’s native multiplexing to eliminate the CPU overhead often found in custom UDP reliability layers.
4. Leverage Zero-RTT (0-RTT) Reconnection

One of MsQuic’s greatest advantages is the ability to resume a connection without a full handshake.

Action: Enable 0-RTT in your connection settings. If a player momentarily loses their Wi-Fi signal and reconnects, they can resume sending data immediately. This helps you eliminate the “Reconnecting…” screen delay for short-duration signal drops.
5. Verify Platform Support

While MsQuic is cross-platform, its performance and availability can vary by OS.

Best Practice: MsQuic is most robust on Windows (using Schannel) and Linux (using OpenSSL). When targeting mobile or consoles, always implement a standard UDP/TCP fallback. Testing your network stack early on target hardware helps you eliminate unexpected connection failures during deployment.
6. Coordinate with AESGCM Encryption

MsQuic requires TLS 1.3, which works best with modern encryption handlers.

Tip: Combine MsQuic with the AESGCM packet handler for the most secure and performant encryption path. Using hardware-accelerated encryption alongside the QUIC protocol helps you eliminate the performance penalty usually associated with secure game traffic.
7. Monitor via Net Stats

Unreal Engine provides specific console variables to monitor QUIC performance.

Action: Use net.Iris.UseMsQuic 1 to toggle the backend and monitor the results with stat net. Observing the round-trip time (RTT) and packet loss metrics helps you eliminate bottlenecks in your server’s bandwidth allocation.
8. Optimize Buffer Sizes

Because QUIC handles flow control internally, standard socket buffer settings may not be optimal.

Best Practice: Adjust the SendBuffer and RecvBuffer sizes in your BaseEngine.ini specifically for the MsQuic net driver. Tuning these based on your game’s maximum expected throughput helps you eliminate packet drops during bursts of high-intensity replication.