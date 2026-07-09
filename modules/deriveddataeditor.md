---
layout: default
title: DerivedDataEditor
---

<!-- ai-generation-failed -->

<h1>DerivedDataEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DerivedDataEditor/DerivedDataEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DerivedDataCache, DerivedDataWidgets, EditorFramework, EditorSubsystem, Engine, InputCore, MessageLog, OutputLog, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d Data Cache (DDC) operations within the Unreal Editor. Its primary role is to handle the background processing of assets from their source format (e.g., .FBX, .TGA) into the engine-ready formats used for rendering and gameplay. It acts as the interface for monitoring, configuring, and troubleshooting the “conversion” process, ensuring that assets are efficiently cached locally or shared across a network to speed up project loading and shader compilation.

Practical Usage Tips & Best Practices
1. Set a Custom Local Cache Path

By default, the DDC can grow to tens of gigabytes and is often stored on the C: drive.

Best Practice: Use the environment variable UE-LocalDataCachePath (e.g., D:\DDC) to move the cache to a secondary high-speed SSD. This leads to the elimination of primary drive storage bloat and keeps the editor responsive during heavy asset ingestion.
2. Prime the Cache for the Team (Shared DDC)

For teams working on the same network, the module can interface with a shared network drive.

Tip: Configure a Shared DDC in your DefaultEngine.ini. When one developer compiles a complex shader, the result is stored on the server, allowing for the elimination of redundant compilation time for every other team member who opens that asset.
3. Monitor for “Stale” Data via LogDerivedDataCache

If you suspect an asset is not updating correctly despite source changes, the DDC might be serving stale data.

Best Practice: Check the Output Log for LogDerivedDataCache. This log provides insights into whether the engine is “Hitting” (finding) or “Missing” (calculating) data. Identifying frequent “Misses” can help in the elimination of bottlenecks in your network configuration.
4. Use the “fill” Command for Build Machines

You can “prime” the DDC on a schedule so developers don’t have to wait for assets to cook upon arrival.

Tip: Run the editor with -run=DerivedDataCache -fill on a build machine nightly. This processes all assets in the project, ensuring the total elimination of “Compiling Shaders” pop-ups when the team starts work in the morning.
5. Deactivate Shared DDC for Remote Work (VPN)

Accessing a shared DDC over a slow VPN can be slower than just regenerating the data locally.

Best Practice: When working from home, launch the editor with the -noshared command-line argument. This forces the editor to use only the local cache, leading to the elimination of significant editor hitches caused by network latency.
6. Leverage “Zen” for Large Projects

In UE 5.5+, the module works closely with the Unreal Zen Store, a high-performance local data server.

Tip: Ensure the Zen service is running to benefit from faster asset streaming. Zen allows for the elimination of traditional file-system overhead, making it significantly faster to switch between different branches of a project.
7. Handle Asset Elimination Safely

When you delete an asset in the Content Browser, the DerivedDataEditor eventually clears the associated cached data.

Tip: If you are performing a massive cleanup of old assets, you can manually delete the DerivedDataCache folder while the editor is closed. This ensures the permanent elimination of orphaned cache files that are no longer linked to any existing project assets.
8. Verify S3 Cloud DDC for Distributed Teams

For teams spread across different geographical locations, the module supports S3-backed cloud caches.

Best Practice: Configure an S3 bucket as a DDC backend in your BaseEngine.ini. This allows remote users to download pre-cooked data over HTTPS, which facilitates the elimination of long setup times for new hires or remote contractors.