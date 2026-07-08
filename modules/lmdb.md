---
layout: default
title: lmdb
---

<!-- ai-generation-failed -->

<h1>lmdb</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/lmdb/lmdb.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Memory-Mapped Database. It is a tiny, fast, and extremely reliable embedded key-value store that Unreal Engine utilizes primarily for its internal data caching and storage architectures, such as the Zen Store and Derived Data Cache (DDC).

What it is and What it’s used for

Located in Engine/Source/ThirdParty/lmdb, this module provides a transactional database that uses memory-mapped files. This allows the engine to handle massive amounts of data—like compiled shaders, cooked textures, and metadata—with near-instantaneous read access by treating the database file as part of the system’s memory.

Primary uses include:

Zen Server Backend: Serving as the underlying storage engine for the Zen Server, managing the local DDC for faster editor startup and asset loading.
Content-Addressable Storage (CAS): Efficiently mapping unique content hashes to their respective data blocks to prevent data duplication.
Asset Metadata Tracking: Storing fast-lookup information for the Unreal Zen Store, allowing the engine to quickly identify if a cooked asset is up to date.
Practical Usage Tips and Best Practices
1. Always Use Fast Local Storage

LMDB performance is directly tied to the speed of the disk it resides on. In your Project Settings, ensure your Global Local DDC Path points to an NVMe SSD. High-speed storage is essential for the elimination of I/O bottlenecks during asset-heavy tasks like opening a large map for the first time.

2. Avoid Network Drives for LMDB Files

Because LMDB uses memory-mapping, it is highly sensitive to file-locking behaviors on network shares (SMB/NFS). Running a local DDC from a network drive can lead to crashes or severe corruption. Using local disks only is a best practice for the elimination of database instability.

3. Monitor Usage via Zen Dashboard

You can inspect the state of the LMDB-backed Zen Store by clicking the Derived Data button at the bottom of the Editor and selecting Launch Zen Dashboard. This tool provides stats on cache hits and misses, helping in the elimination of confusion regarding why certain assets are being recompiled.

4. Configure Shared DDC for Team Environments

While LMDB handles the local cache, teams should pair it with a Shared DDC. This ensures that once one person uses LMDB to store a compiled asset locally, it is pushed to the network share for others. This workflow results in the elimination of redundant processing time across the entire studio.

5. Understand “Copy-on-Write” Reliability

LMDB uses a “copy-on-write” design, meaning it never overwrites existing data—it writes to new pages instead. This makes it virtually immune to corruption during a crash. This reliability ensures the elimination of “Corrupt DDC” errors that used to plague older, file-based caching systems in legacy Unreal versions.

6. Optimize VMA Limits on Linux

On Linux servers or workstations, LMDB’s memory-mapping can occasionally hit “Virtual Memory Area” (VMA) limits. If you experience crashes on Linux, increasing the vm.max_map_count in the OS kernel settings is a recommended step for the elimination of memory allocation failures.

7. Deduplication Benefits

Because the LMDB module supports content-addressable storage, it automatically deduplicates identical data across different projects or branches on your machine. This leads to the elimination of wasted disk space, allowing you to maintain multiple workspaces without multiplying your storage requirements.

8. Strategic Elimination of Stale Cache

If you encounter persistent, inexplicable asset errors, you can safely delete the Zen folder in your local DDC directory. Since LMDB is a cache, the engine will simply rebuild the necessary data. This manual elimination of the database is the “nuclear option” for resolving complex corruption issues without affecting your source .uasset files.