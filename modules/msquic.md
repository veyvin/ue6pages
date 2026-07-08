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

n of the QUIC (Quick UDP Internet Connections) protocol. It serves as a modern, high-performance transport layer that sits between the low-level UDP sockets and the engine’s networking systems.

QUIC is designed to provide the reliability and security of TCP but with the performance benefits of UDP. In Unreal Engine, this module is primarily used to power the Iris Replication System and advanced networking scenarios. It features built-in TLS 1.3 encryption and multi-streaming capabilities, which helps you eliminate “Head-of-Line Blocking”—a common issue where one lost packet halts the processing of all other data in a standard TCP-like stream.

Practical Usage Tips and Best Practices
Enable via Iris NetDriver
To use MSQUIC, you typically need to configure your DefaultEngine.ini to use a NetDriver that supports it (such as the Iris NetDriver). Setting the transport to QUIC allows the engine to handle thousands of small, independent streams, which helps you eliminate the bottleneck of processing a single monolithic data stream.
Leverage Connection Migration
One of the primary advantages of MSQUIC is its support for connection migration. If a player’s IP address changes (e.g., switching from Wi-Fi to 5G), QUIC can maintain the session without a full disconnect. Implementing this helps you eliminate frustrated players being kicked during minor network transitions.
Configure MTU Discovery
QUIC performs its own Maximum Transmission Unit (MTU) discovery. Ensure your server firewall allows ICMP traffic or relevant UDP packets so that MSQUIC can find the optimal packet size. This helps you eliminate packet fragmentation, which is a major source of latency and packet loss in multiplayer games.
Use for Encrypted Game Traffic
MSQUIC has TLS 1.3 built directly into the protocol. By using this module, your game data is encrypted at the transport level with lower overhead than traditional SSL/TLS wrappers. This allows you to eliminate the need for custom encryption layers while maintaining a high security standard.
Monitor via ‘net.Iris’ Console Variables
Since MSQUIC is often used alongside Iris, use console commands like net.Iris.LogTransportStats 1 to monitor the performance of your QUIC streams. This visibility allows you to eliminate hidden packet-loss issues that might not appear in standard UDP “stat net” views.
Optimize for High Packet Loss
QUIC’s congestion control and loss recovery are more sophisticated than basic UDP. If your game is targeting regions with unstable internet, switching to an MSQUIC-based driver can help you eliminate the “rubber-banding” effect commonly seen when a standard UDP driver fails to recover quickly from dropped packets.
Verify Platform Support
While MSQUIC is cross-platform (Windows, Linux, etc.), always check the BaseEngine.ini or platform-specific documentation for compatibility. Ensuring that the target platform has the necessary library support helps you eliminate “Socket Failed to Initialize” errors during the deployment phase.
Properly Close Connections on Elimination
When a player leaves or a server shuts down (an “elimination” of the session), ensure the NetDriver calls the proper MSQUIC shutdown sequence. QUIC connections are stateful; clean shutdowns help the server eliminate “Zombies”—dangling connections that continue to consume memory and ports because the “Close” handshake was never completed.