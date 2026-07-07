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

for derived data (such as compiled shaders, compressed textures, and physics data). Unlike the legacy “Filesystem” DDC which stores thousands of individual files on disk, IndexedCacheStorage organizes data into a more efficient database-like format, typically managed by Unreal Zen Storage (ZenServer). Its primary purpose is to drastically reduce “Wait for DDC” times and disk I/O overhead by using an index-mapped architecture that allows the engine to query, read, and write multiple cache records in a single, streamlined operation.

Practical Usage Tips and Best Practices
Enable Zen Storage for Maximum Throughput
The IndexedCacheStorage module performs best when Unreal Zen Storage is enabled. In your project’s DefaultEngine.ini, ensure the DDC graph is configured to use Zen. This allows you to eliminate the massive file-count overhead of traditional DDC, leading to faster editor startup times.
Monitor via Zen Dashboard
Use the ZenDashboard.exe tool (found in the engine’s Binaries/Win64 folder) to monitor the health of your indexed cache. Tracking hit/miss ratios helps you eliminate mystery performance drops caused by a cold or corrupted cache.
Prioritize Indexed Backends in DDC Graphs
When defining a custom DerivedDataBackendGraph, ensure your Zen or Indexed entries are positioned before local filesystem entries. This forces the engine to check the faster indexed store first, helping you eliminate redundant and slow disk seeks.
Leverage for Shared Network Caches
This module supports the “Unreal Cloud DDC” and shared Zen instances. Using an indexed storage backend for your team’s shared DDC helps you eliminate the “chattiness” of standard network file shares, significantly speeding up work for remote developers.
Regularly Clean Stale Records
While the indexed system is efficient, it can grow quite large. Use the command-line argument -DDCClean to prune old records. This helps you eliminate “ghost” bugs—where the engine incorrectly loads a stale version of a shader—and frees up significant disk space.
Tune Cache Sizes in ZenStore.ini
You can customize how much disk space the indexed cache is allowed to occupy by editing BaseZenStore.ini. Setting appropriate limits helps you eliminate out-of-disk-space crashes during massive asset cooking or project-wide shader recompiles.
Use for Accelerated Build Machine Priming
On build servers, use the Unreal Virtualization Tool to push data into the indexed cache. By pre-populating the cache during the build process, you can eliminate the initial performance dip that occurs when developers first sync a new version of the project.
Validate with LogDerivedDataCache
If you suspect the cache is not being utilized, set the LogDerivedDataCache category to Verbose. Searching for “Indexed” or “Zen” hits in the log helps you eliminate configuration errors that might be causing the engine to fall back to slower legacy storage methods.