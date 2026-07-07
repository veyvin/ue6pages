---
layout: default
title: StreamingFile
---

<!-- ai-generation-failed -->

<h1>StreamingFile</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/StreamingFile/StreamingFile.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, NetworkFile, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

(UFS) that enables efficient, asynchronous reading of files from the disk, particularly from Pak files.

Description and Purpose

The StreamingFile module provides the implementation for FStreamingFile, which is a specialized wrapper around the platform’s native file system. Its primary purpose is to handle high-performance, non-blocking I/O operations for large assets. Unlike standard file reads that might stall the Game Thread, this module works with the Async Loading Framework to stream data chunks into memory as needed. It manages the complexities of finding files within multiple mounted Pak files, prioritizing “patches” over base game data, and handling the decompression of assets on the fly. By using this module, the engine can eliminate significant hitches during level transitions or dynamic asset loading.

Practical Usage Tips and Best Practices
Avoid Synchronous Flushes
The most common mistake is calling a function that forces a “Flush” on the streaming file system (like a synchronous LoadObject during gameplay). This forces the engine to stop and wait for the I/O, which you should avoid to eliminate frame-rate spikes or “hitches” during streaming.
Understand Pak File Priority
The module searches Pak files based on a priority system (often using the _P suffix for patches). Ensure your patch files are named correctly so the FStreamingFile logic can eliminate the use of outdated assets by prioritizing the newer Pak entries.
Leverage I/O Scheduling via IoStore
In modern Unreal Engine versions, the Streaming File system works alongside the IoStore. This system groups small file requests into larger, more efficient batches. Utilizing the Zen Loader/IoStore format is a best practice to eliminate excessive disk seek times, especially on consoles and NVMe drives.
Monitor via “stat Streaming”
Use the console command stat Streaming to get a real-time breakdown of how many files are currently being read and the bandwidth being consumed. This allows you to eliminate I/O bottlenecks by identifying assets that are too large or being requested too frequently.
Use Async Loading Time Limits
You can tune the performance of the streaming system using cvars like s.AsyncLoadingTimeLimit. Setting a strict budget (e.g., 5ms) ensures the streaming logic doesn’t consume too much of the frame, helping you eliminate Game Thread interference.
Minimize “File Not Found” Errors
Every failed file request through the streaming system incurs a performance penalty as it searches through all mounted Paks. Use the Asset Registry to verify an asset exists before attempting to stream it, which helps you eliminate wasted CPU cycles on invalid paths.
Batch Small Files into Paks
The Streaming File system is optimized for reading large chunks from a few Paks rather than thousands of tiny individual files on the disk. Batching your content helps the system eliminate the overhead associated with opening and closing hundreds of file handles.
Check for Thread Safety
When writing custom C++ that interacts with IPlatformFile, ensure you are using the streaming-aware interfaces if you are on a background thread. This ensures you eliminate race conditions where two threads might attempt to access the same file offset simultaneously.