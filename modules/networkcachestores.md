---
layout: default
title: NetworkCacheStores
---

<!-- ai-generation-failed -->

<h1>NetworkCacheStores</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/NetworkCacheStores/NetworkCacheStores.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DerivedDataCache, DesktopPlatform, DevHttp, Json, SSL, Zen</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine Derived Data Cache (DDC) system. It provides the implementation for remote and networked storage backends, allowing multiple developers and build machines to share compiled assets (like shaders, textures, and audio) over a network rather than each machine regenerating them locally.

In modern workflows (UE 5.4+), this module is primarily associated with the Zen Store and Unreal Cloud DDC architectures. It handles the communication between the engine and the cache server (via HTTP/REST), helping you eliminate redundant processing time and local disk bloat by fetching already-processed data from a shared “Source of Truth.”

Practical Usage Tips and Best Practices
Implement a Tiered DDC Graph
Configure your DDC graph to check a Local Zen Store first, then a Shared Regional Zen Server, and finally a Cloud DDC. This hierarchy ensures that you fetch data from the fastest possible source, helping you eliminate network latency bottlenecks for assets already available on your local network.
Use Zen Server for Office LANs
For teams working in the same physical location, use a dedicated machine to run a Zen Server as a shared DDC. This module allows all workstations to contribute to and pull from this server, which helps you eliminate the massive “morning sync” shader compilation wait times for your team.
Deploy Unreal Cloud DDC for Remote Work
If your team is distributed globally, utilize the Cloud DDC functionality supported by this module. It allows for authenticated, high-latency-tolerant storage over the internet, helping you eliminate the need for remote developers to leave their PCs running overnight just to “cook” a project.
Configure S3/Blob Storage for Build Farms
When setting up a Continuous Integration (CI) pipeline, point the NetworkCacheStores configuration to a cloud storage bucket (like AWS S3 or Azure Blob). This ensures that once the build farm processes an asset, every developer in the organization gets the benefit, helping you eliminate duplicate work across the company.
Monitor Cache Hit Rates via ‘stat DDC’
Use the console command stat DDC to see how much data is being pulled from the network versus generated locally. If your “Hit Rate” is low, it may indicate a configuration error or a network issue. Identifying these gaps allows you to eliminate hidden performance drains during the development cycle.
Set Up Data Retention Policies
Shared network caches can grow to several terabytes. Use the storage server’s internal tools to set “Time to Live” (TTL) or “Least Recently Used” (LRU) deletion policies. Regular cleanup of old, unused cached data helps you eliminate wasted storage costs on your servers.
Use ‘Projected’ and ‘Virtual’ Assets
When combined with Virtual Assets, this module allows you to download only the “Structured Data” (small files) from Perforce while pulling the “Bulk Data” from the network cache only when needed. This helps you eliminate massive initial project download times, reducing a 500GB project to a few gigabytes of metadata.
Properly Handle Cache Invalidation
If you change a core engine shader or a global compression setting, the “Key” for the cached data will change. When performing a major engine upgrade (the “elimination” of the old version’s cache compatibility), ensure you clear the shared network cache to eliminate “Corrupt Texture” or “Invalid Shader” errors caused by old data remnants.