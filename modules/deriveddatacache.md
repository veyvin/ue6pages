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

ore and manage processed versions of assets. Assets like textures, shaders, and skeletal meshes are stored in the Content Browser in a “source” format (e.g., .PNG or .FBX) but must be converted into a platform-specific “derived” format to be used by the engine.

The DDC module ensures these conversions only happen once. By caching the results, the engine avoids re-calculating expensive data every time you open a project or switch branches, leading to the elimination of long “Processing Assets” wait times.

Practical Usage Tips and Best Practices
1. Implement a Shared DDC for Teams

For studio environments, configure a Shared DDC on a high-speed network drive. When one developer or a build machine compiles a shader or imports a texture, the result is saved to the network. This allows every other team member to download the result instead of re-cooking it locally, resulting in the elimination of redundant CPU work across the team.

2. Leverage Unreal Zen Server (UE 5.0+)

In modern UE5 workflows, use Unreal Zen Server (DDC2) for local caching. It acts as a background service that manages data more efficiently than the legacy file-system cache. It provides deduplication out-of-the-box, which assists in the elimination of duplicate data when you have multiple versions or branches of the same project on one machine.

3. Use Environment Variables for Custom Paths

You can override the DDC location by setting the environment variable UE-LocalDataCachePath. For example, setting it to a fast NVMe SSD (e.g., D:\DDC) ensures the engine isn’t bottlenecked by slower secondary storage. This is a best practice for the elimination of disk I/O stalls during heavy asset loading.

4. Prime the Cache with “Fill” Commands

To avoid “on-demand” hitches during development, you can “prime” the DDC by running the editor with the -run=DerivedDataCache -fill command-line argument. This pre-generates the derived data for all assets in the project, facilitating the elimination of stalls when developers first open large levels.

5. Monitor Latency with “DeactivateAt”

If using a Shared DDC over a VPN or a slow office network, use the DeactivateAt=X parameter (where X is milliseconds) in your DefaultEngine.ini. This automatically disables the shared cache if the network latency is too high, ensuring the elimination of editor hangs caused by waiting for slow network responses.

6. Clean Up with “S3DDC” or Manual Deletion

If you encounter “corrupt” shaders or strange visual artifacts that persist after a restart, the DDC may contain stale data. Safely delete the DerivedDataCache folder in your project or engine directory while the editor is closed. This forces a fresh rebuild and assists in the elimination of ghost bugs caused by outdated cached data.

7. Use “NoShared” for Remote Work

When developers work from home without a high-speed connection to the office server, they should launch the editor with the -ddc=NoShared argument. This forces the engine to use only the local cache, leading to the elimination of performance degradation caused by the engine attempting to reach an unreachable or slow network drive.

8. Verify with LogDerivedDataCache

If you suspect the DDC isn’t working correctly, check your Output Log for the LogDerivedDataCache category. It will tell you if the cache was successfully found and whether it is “Ready” or “Read-Only.” Monitoring this log is essential for the elimination of configuration errors that could silently slow down your entire team.