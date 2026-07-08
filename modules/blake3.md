---
layout: default
title: BLAKE3
---

<!-- ai-generation-failed -->

<h1>BLAKE3</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/BLAKE3/BLAKE3.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ographic-strength hashing implementation based on the BLAKE3 algorithm. It is integrated into the engine’s core utilities to provide a significantly faster alternative to MD5 and SHA-256 while remaining highly secure.

In Unreal Engine, BLAKE3 is primarily used for data deduplication, Derived Data Cache (DDC) key generation, and verifying the integrity of large binary blobs. Its design allows it to be multithreaded and vectorized, making it ideal for the high-throughput requirements of modern game development pipelines.

Practical Usage Tips and Best Practices
1. Use for DDC and Zen Store Keys

When building custom systems that interact with the Derived Data Cache (DDC) or Unreal Zen Store, prefer BLAKE3 for generating cache keys. Its speed ensures that the hashing process itself doesn’t become a bottleneck during the high-speed retrieval or storage of assets.

2. Leverage SIMD Parallelism

BLAKE3 is designed to take advantage of SIMD (Single Instruction, Multiple Data) on modern CPUs. When hashing very large files or buffers in C++, ensure you are using the engine’s provided FBlake3 wrapper, which internally utilizes SSE4.1, AVX2, or NEON instructions for the elimination of wasted CPU cycles.

3. Implement Incremental Hashing

For large data streams (like multi-gigabyte PAK files), do not load the entire file into memory. Use the Update method in the FBlake3 class to process the data in chunks. This maintains a low memory footprint while still producing a single, definitive hash of the entire file.

C++
	FBlake3 Hasher;

	Hasher.Update(BufferPtr, BufferSize);

	FBlake3Hash Hash = Hasher.Finalize();
Copy code
4. Prefer BLAKE3 over MD5 for New Systems

While MD5 was historically the engine default for asset hashing, it is susceptible to collision attacks and is slower on modern hardware than BLAKE3. For any new internal tools or data validation systems, use BLAKE3 to ensure the total elimination of legacy security vulnerabilities and performance drags.

5. Thread-Safe Hashing Operations

The FBlake3 state object is not thread-safe; however, because the algorithm is so fast, you can simply create a local FBlake3 instance on the stack within a worker thread. This allows you to hash multiple files in parallel across all CPU cores without needing complex synchronization or mutexes.

6. Use for Rapid Data Deduplication

In build pipelines or procedural generation systems where you need to check if a piece of data has already been processed, use a BLAKE3 hash as a unique identifier. The extremely low collision probability allows for the elimination of redundant processing by simply comparing 256-bit hashes.

7. Verify Integrity of Downloaded Content

If your game downloads DLC or modular content at runtime, use BLAKE3 to verify the integrity of the downloaded chunks. By comparing the local hash against a manifest, you can ensure the elimination of corrupted data before it is passed to the engine’s serialization system.

8. Monitor Performance via Unreal Insights

If you are performing heavy batch hashing, use Unreal Insights to monitor the time spent in hashing functions. If hashing appears as a significant cost, check that you aren’t re-hashing static data and that your buffers are properly aligned for the underlying SIMD instructions.