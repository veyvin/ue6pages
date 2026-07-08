---
layout: default
title: DerivedDataTool
---

<!-- ai-generation-failed -->

<h1>DerivedDataTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/DerivedDataTool/DerivedDataTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, DerivedDataCache, DesktopPlatform, NetworkCacheStores, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e, audit, and maintain the Derived Data Cache (DDC). It serves as the primary interface for developers to interact with the engine’s cached data outside of the standard Editor environment.

What it is and What it’s used for

In Unreal Engine, “Derived Data” refers to platform-specific versions of assets (like compressed textures or compiled shaders) that are generated from source files. The DerivedDataTool module provides a commandlet—UDerivedDataToolCommandlet—that allows teams to analyze and manipulate this data at scale.

Primary uses include:

DDC Auditing: Identifying which assets are missing from the cache or which ones are taking up excessive space.
Cache Warming: Pre-generating derived data on a build server so that artists and designers don’t have to wait for “Compiling Shaders” when they sync the project.
Migration Support: Assisting in the transition from legacy DDC systems to the modern Zen Store (DDC2) architecture.
Storage Maintenance: Cleaning up stale or corrupted entries from local or shared cache locations to free up disk space.
Practical Usage Tips and Best Practices
1. Warm the Cache in CI/CD

To ensure the elimination of “startup stalls” for your team, run the tool as part of your nightly build pipeline. Use the -fill flag to pre-process all assets for your target platforms. When team members sync in the morning, their local engine will pull the ready-made data from the shared DDC instead of compiling it locally.

bash
UnrealEditor-Cmd.exe ProjectName -run=DerivedDataCache -fill
Copy code
2. Audit for Cache Misses

If your team complains about slow load times despite having a shared DDC, use the -audit flag. This will generate a report showing “Cache Misses”—assets that were requested but not found in the shared store. High miss rates usually indicate that your build machine is not covering all necessary platforms or engine configurations.

3. Transition to Zen Store (DDC2)

With the release of UE 5.4 and 5.5, the engine is moving toward the Zen Store (a high-performance DDC service). Use the DerivedDataTool to verify your Zen connection. If you are setting up a shared Zen DDC for an office, use the tool to “push” existing legacy cache data into the Zen service to prevent having to rebuild everything from scratch.

4. Manage Multi-Branch DDCs

If you work across multiple branches (e.g., Main, Release, Dev), set the UE-LocalDataCachePath environment variable. You can use the DerivedDataTool to point all branches to a single local directory. This allows the engine to share compiled shaders and textures across branches, saving massive amounts of disk space.

5. Clean Stale Data with -clean

The DDC can grow to hundreds of gigabytes over time. Periodically run the tool with cleaning parameters to remove entries that haven’t been accessed in a specific number of days. This prevents the “Cache Churn” that occurs when a drive becomes too full for the operating system to manage efficiently.

6. Troubleshoot with LogDerivedDataCache

If the tool is failing to fill or find data, check the logs for LogDerivedDataCache. This log category provides detailed info on whether the tool is hitting the Local, Shared, or Cloud layer of your DDC graph. It will specifically flag if a network share is unreachable or if a “latency cap” is deactivating your shared DDC.

7. Build DDC Paks for Remote Workers

For team members working with limited bandwidth (where a Shared DDC over VPN is too slow), use the tool to create a DDC Pak (.ddp). You can distribute this file alongside your project. The tool will bundle all essential derived data into one file that the engine reads locally, providing the benefits of a shared DDC without the network overhead.

8. Verify Data Integrity

Use the -Verify flag if you suspect cache corruption (e.g., textures appearing with strange artifacts). This command forces the tool to re-hash and check the integrity of cached items against the source assets. It will flag and can be configured to eliminate corrupted entries, forcing the engine to regenerate them correctly.