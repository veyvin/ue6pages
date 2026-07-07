---
layout: default
title: Blosc
---

<!-- ai-generation-failed -->

<h1>Blosc</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Blosc/Blosc.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ompressor library. It is a high-performance, multi-threaded compressor specifically designed for binary data. Unlike general-purpose compressors (like Zlib), Blosc is optimized to transmit data to the CPU at speeds faster than a traditional non-compressed memory fetch by leveraging the L1/L2 caches.

In Unreal Engine, this module is primarily used by systems that handle massive buffers of structured data, such as the Derived Data Cache (DDC), Electra Media Player, and internal caching for Niagara or Nanite build data.

1. Use for Memory-to-Memory Compression

Blosc is not intended for compressing files on disk to save space (use Oodle or LZ4 for that). Use the Blosc module when you need to compress large blocks of data in RAM to save memory bandwidth or to store temporary transient data that needs to be accessed extremely quickly.

2. Choose the Right Inner Codec

Blosc is a “meta-compressor,” meaning it can use different libraries internally.

BloscLZ: The default; best for extreme speed.
LZ4: Excellent for high-speed decompression.
Zstd: Better compression ratios at the cost of some speed.
Zlib: Provided for compatibility but generally slower in this context.
3. Leverage the Shuffle Filter

One of Blosc’s most powerful features is the Shuffle filter. It rearranges the bytes of your data (e.g., grouping the first bytes of all integers, then the second bytes).

Best Practice: Always use Shuffle when your data consists of structured arrays (like float arrays for vertex positions or int32 IDs). This drastically improves the compression ratio for binary patterns without a significant performance hit.
4. Direct Thread Management

The Blosc module supports internal multi-threading. You can specify the number of threads to use for a compression task.

Tip: In UE5, it is usually best to set the thread count to 1 if you are already inside a Task Graph or ParallelFor loop to avoid “over-subscription,” where too many threads compete for CPU time and eliminate the speed benefits of the compressor.
5. Target the Cache Size

Blosc performs best when its “block size” fits within your CPU’s L1 or L2 cache.

Best Practice: Unless you have a specific technical reason, leave the block size to 0 (automatic). The Blosc module will automatically detect the host CPU’s cache topology and tune itself for maximum throughput.
6. Memory Alignment

Blosc is highly sensitive to memory alignment.

Tip: Ensure that the input buffers you pass to the Blosc module are aligned to 16-byte or 32-byte boundaries (using FMemory::Malloc with alignment). This allows the compressor to use SIMD instructions (SSE2/AVX2), which can double the processing speed.
7. Avoid Small Buffers

Blosc is optimized for large blocks of data (kilobytes to megabytes).

Constraint: Do not use the Blosc module to compress small structs or individual strings. The overhead of setting up the compression context will eliminate any performance gains. For small data, use FArchive with standard compression or no compression at all.
8. Use for DDC Custom Versions

If you are developing a custom plugin that generates a lot of “Derived Data” (like a custom mesh format), consider using Blosc to compress the data before sending it to the DDC. This reduces the time spent on network/disk I/O when the engine needs to fetch that data on another machine, speeding up team-wide build times.