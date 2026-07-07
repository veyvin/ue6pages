---
layout: default
title: DerivedDataCache
---

<!-- ai-generation-failed -->

<h1>DerivedDataCache</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DerivedDataCache/DerivedDataCache.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed network drives, and cloud-based caching.

Practical Usage Tips and Best Practices
1. Set Up a Shared DDC for Teams

In a studio environment, utilize a Shared DDC located on a high-speed network drive (or via Zen Server). When one developer compiles a shader or compresses a texture, the result is uploaded to the shared cache. Other team members then download the pre-compiled data, resulting in the elimination of redundant compilation time across the entire team.

2. Use Environment Variables for Multi-Branch Work

If you work across multiple branches of the same project, your DDC can grow massive and cause conflicts. Set the UE-LocalDataCachePath environment variable to a central location on your fastest drive (SSD). This ensures all engine versions share the same cache and facilitates the elimination of “splash screen hangs” when switching branches.

3. Toggle Shared DDC for Remote Work

For developers working from home over a VPN, a Shared DDC on an office server can actually slow the engine down due to network latency. In these cases, it is a best practice to set UE-SharedDataCachePath=None. This forces the engine to rely on the local SSD, leading to the elimination of long stalls caused by slow network file access.

4. Distribute a “Bootstrap” DDC

When onboarding new developers to a large project, you can zip and share a local DDC folder. The new user can place this in their local DDC directory before opening the project for the first time. This simple step ensures the elimination of the several-hour “Initial Shader Compile” phase.

5. Monitor Cache Hits with “stat DDC”

Use the console command stat DDC to see real-time statistics on cache hits and misses. If you see a high number of “Misses” for assets that should be cached, it indicates a configuration error in your BaseEngine.ini. Fixing these settings results in the elimination of unnecessary CPU cycles spent regenerating data.

6. Leverage Zen Server in UE 5.3+

Starting with recent versions, Unreal Engine defaults to Zen Storage Server for local DDC. It is more efficient at handling thousands of small files than the traditional filesystem backend. Ensure your firewall allows local loopback traffic for the Zen process to ensure the elimination of connection errors during asset loading.

7. Periodically Clear Local DDC

The DDC does not automatically delete old, unused data, which can lead to it consuming hundreds of gigabytes over time. If your drive is full, you can safely delete the DerivedDataCache folder while the editor is closed. The engine will regenerate only what it needs, leading to the elimination of “stale” data taking up valuable disk space.

8. Use S3 or Unreal Cloud DDC for Global Teams

For teams distributed across different geographical regions, a standard network share is too slow. Use the Unreal Cloud DDC (available on GitHub) or an S3-backed cache. This allows for regional endpoints with background replication, ensuring the elimination of high-latency bottlenecks for international collaborators.