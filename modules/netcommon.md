---
layout: default
title: NetCommon
---

<!-- ai-generation-failed -->

<h1>NetCommon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Net/Common/NetCommon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

provides platform-independent primitives for networking. It sits beneath the high-level replication systems (like the NetDriver and the new Iris system) and provides the essential tools for bit-level serialization and packet processing.

What it is and What it’s used for

Located in Engine/Source/Runtime/NetCommon, this module is the engine’s “utility belt” for raw data transmission. Its primary responsibility is to ensure that data can be packed tightly into bits (rather than bytes) to minimize bandwidth and passed through a chain of processors (PacketHandlers) for security or compression before hitting the network hardware.

Primary uses include:

Bit-Level Serialization: Providing FBitWriter and FBitReader for packing booleans, integers with custom bit-counts, and quantized vectors into the smallest possible footprint.
Packet Handling Pipeline: Defining the PacketHandler and HandlerComponent architecture, which manages features like Oodle Compression and AES Encryption.
Reliability Logic: Containing the base classes for handling sequence numbers, packet acknowledgments (ACKs), and connection handshaking.
Iris Integration: Providing the low-level bit-stream logic required by the Iris replication system for high-performance state synchronization.
Practical Usage Tips and Best Practices
1. Always Check for Reader Overflow

When reading data from an FBitReader (commonly inside a NetSerialize override), always call Reader.IsError() or check Reader.GetBitsLeft(). If a packet is malformed or truncated, continuing to read will return garbage data. Checking for errors is the best practice for the elimination of “Heisenbugs” caused by reading out-of-bounds memory during a network hitch.

2. Use Precise Bit Counts for Integers

Don’t use the standard << operator for small integers or enums. Use Writer.WriteInt(Value, MaxValue) or Writer.SerializeInt(Value, BitCount). If an enum only has 4 values, you only need 2 bits. Using precise bit counts is the primary strategy for the elimination of wasted bandwidth in high-frequency RPCs.

3. Leverage FNetBitReader/Writer for UObjects

When serializing UObject pointers or FSoftObjectPath, prefer FNetBitReader and FNetBitWriter over their base versions. These subclasses include specialized operators that interface with the PackageMap, ensuring the elimination of “NULL” references on the client by correctly mapping Global IDs (GUIDs) during transmission.

4. Optimize Booleans via Bit Packing

In standard C++, a bool often occupies 1 byte (8 bits). Within the NetCommon bitstreams, a bool occupies exactly 1 bit. If your character has 16 boolean flags, they will collectively take only 2 bytes of network traffic. This native bit-packing results in the elimination of the need for manual bitmasking logic in your gameplay code.

5. Extend the PacketHandler for Custom Security

If you need to implement a proprietary security protocol or custom analytics, create a class inheriting from HandlerComponent. By inserting your component into the PacketHandlerProfileConfig in BaseEngine.ini, you ensure the elimination of “clear-text” data before it ever leaves the machine.

6. Mind the “LWC” Precision vs. Bandwidth

With UE5’s Large World Coordinates, FVector components are now doubles (64-bit). In NetSerialize, use FVector_NetQuantize or explicitly serialize as floats if millimeter precision isn’t required at long distances. This ensures the elimination of doubled bandwidth costs for simple movement data.

7. Avoid Overflowing the MTU

The Maximum Transmission Unit (MTU) for most game packets is around 1400 bytes. When using FBitWriter for custom data, monitor the GetNumBytes() result. Sending bunches that exceed the MTU causes the engine to split them into “Partial Bunches,” which can lead to the elimination of network performance due to increased CPU overhead.

8. Strategic Elimination of Unused Reliability

For data that changes every frame (like a character’s simulated velocity), use Unreliable delivery. This prevents the NetCommon logic from attempting to re-send old, irrelevant data if a packet is lost. Proper use of unreliable streams results in the elimination of “buffer bloat” and latency spikes on unstable connections.