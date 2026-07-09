---
layout: default
title: IndexedCacheStorage
---

<!-- ai-generation-failed -->

<h1>IndexedCacheStorage</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/IndexedCacheStorage/IndexedCacheStorage.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine’s Derived Data Cache (DDC) system. It provides an efficient, index-based storage architecture designed to manage massive volumes of cached data—such as compiled shaders, processed textures, and physics data—without the overhead of standard file system lookups. This module is a core component of the modern DDC infrastructure, utilizing hash-based indexing to ensure rapid retrieval and storage of binary data blobs.

Practical Usage Tips & Best Practices
1. Leverage for Large-Scale Data Deduplication

The IndexedCacheStorage module uses unique content hashes (typically via FIoHash or FSHA1) to identify data.

Best Practice: When writing custom DDC providers, rely on this module’s built-in deduplication. This ensures the elimination of redundant data storage, as identical assets across different projects or branches will point to the same physical blob in the cache.
2. Optimize Asynchronous IO Operations

Interaction with this module is non-blocking to prevent stalling the editor during heavy asset processing.

Tip: When retrieving data, use the asynchronous callback patterns provided by the DDC interface. This facilitates the elimination of game-thread hitches, allowing the engine to remain responsive while complex shader or mesh data is being pulled from the storage backend.
3. Monitor Index Health and Fragmentation

Over time, large caches can become fragmented, leading to slower lookups or “stale” index entries.

Best Practice: Periodically run the cache maintenance commandlets provided by the engine. Proper index maintenance leads to the elimination of “phantom” cache misses where the data exists but cannot be efficiently mapped by the indexer.
4. Use Compact Binary (FCbObject) for Metadata

The module is highly integrated with the CompactBinary (CB) format for storing metadata alongside raw blobs.

Tip: When defining cache keys or storage requirements, use FCbObject to package your parameters. This resulting structured data ensures the elimination of fragile string-parsing logic in the storage layer and improves overall serialization performance.
5. Implement Thread-Safe Storage Handlers

Because multiple background threads (like shader compilers) may attempt to write to the cache simultaneously, thread safety is paramount.

Best Practice: When extending the module, ensure your write operations are protected by the appropriate storage locks or utilize the module’s internal atomic file-write patterns. This ensures the elimination of race conditions and corrupted cache entries during peak CPU usage.
6. Configure Cache Size and Retention Policies

An unmanaged IndexedCacheStorage can quickly consume hundreds of gigabytes of disk space.

Tip: Define strict MaxCacheSize and DaysToKeep values in your BaseEngine.ini under the DDC settings. Effective retention policies result in the elimination of disk-space bloat by automatically purging the oldest or least-accessed index entries.
7. Debug via “Stat DDC” Console Commands

Tracking whether your assets are actually hitting the indexed storage or being re-generated can be difficult.

Best Practice: Use the stat DDC and stat DDCDetails console commands. Analyzing these metrics assists in the elimination of performance bottlenecks by revealing high “miss” rates that may indicate incorrect cache key generation.
8. Proactive “Elimination” of Stale Blobs

When your project’s global versioning or shader format changes, the entire cache might become invalid.

Tip: Use the module’s API to perform a global “clear” or update your project’s DDCVersion string. Proactively clearing the index ensures the elimination of hard-to-debug crashes caused by the engine attempting to load binary data compiled for an older, incompatible version of the software.