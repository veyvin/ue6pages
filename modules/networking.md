---
layout: default
title: Networking
---

<!-- ai-generation-failed -->

<h1>Networking</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Networking/Networking.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

actions for network communication that sit between the raw socket layer and the engine’s high-level Replication system.

What it is and What it’s used for

Located in Engine/Source/Runtime/Networking, this module provides the interfaces and helper classes needed to manage network connections, listen for incoming data, and send packets without dealing with platform-specific socket APIs (like WinSock or BSD sockets).

Primary uses include:

Socket Management: Creating and managing FSocket objects via the ISocketSubsystem.
Data Streaming: Providing the FArrayWriter and FArrayReader for serializing complex data structures into byte arrays.
Networking Utilities: Handling common tasks like IP address parsing (FIPv4Address), DNS lookups, and port management.
Backend Communication: Frequently used for non-gameplay networking, such as connecting to a custom master server, telemetry endpoint, or external database.
Practical Usage Tips and Best Practices
1. Use the SocketSubsystem for Portability

Never use raw platform socket calls. Always use ISocketSubsystem::Get() to create sockets. This ensures the elimination of platform-specific code, allowing your networking logic to work seamlessly across Windows, Linux, and Consoles.

2. Set Sockets to Non-Blocking Mode

By default, some socket operations can “stall” the thread while waiting for data. Always call SetNonBlocking(true) on your FSocket instances. This is a best practice for the elimination of game-thread hitches, ensuring your UI and rendering remain fluid even if a network request is slow.

3. Implement a Receive Timeout

When waiting for a response from a custom server, use Wait with a specified timeout. Failing to set a timeout can cause a thread to hang indefinitely, while a properly configured timeout results in the elimination of “zombie” threads that consume system resources without progressing.

4. Leverage FArrayWriter for Serialization

To send a struct over a socket, use FArrayWriter and the << operator. This automatically handles the conversion of Unreal types (like FString or FVector) into a byte stream. It is the primary method for the elimination of manual byte-buffer management and potential memory leaks.

5. Be Mindful of “Endianness”

While most modern platforms are Little-Endian, always be cautious when communicating with external servers. Use the ByteOrder utilities to ensure your multi-byte integers are consistent. Correct byte-ordering leads to the elimination of corrupted data when passing values between different CPU architectures.

6. Optimize Packet Sizes for MTU

For custom UDP communication, keep your packet size below 1300 bytes. If your data exceeds the MTU (Maximum Transmission Unit), the network hardware will fragment the packet, which leads to the elimination of reliability and a significant increase in packet loss on unstable networks.

7. Close and Cleanup Sockets Properly

Always call Close() and then ISocketSubsystem::Get()->DestroySocket() in your module’s shutdown or Actor’s EndPlay. Neglecting this leads to “Address already in use” errors on the next run; proper cleanup ensures the elimination of port-binding conflicts during rapid iteration.

8. Strategic Elimination of Unreliable Connections

For high-frequency telemetry or heartbeat signals, use UDP rather than TCP. UDP’s “fire and forget” nature results in the elimination of the heavy handshake and retransmission overhead associated with TCP, which is critical for maintaining performance in a high-speed game environment.