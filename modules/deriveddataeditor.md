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

agement logic for the Derived Data Cache (DDC), which handles all asynchronously generated asset data.

Description and Purpose

This module acts as the “frontend” for the DDC system within the Unreal Editor. Many assets (Textures, Shaders, Audio) require platform-specific processing before they can be used. The DerivedDataEditor coordinates how this data is fetched, stored, and displayed to the user. In recent versions like UE 5.4 and 5.6, this module heavily integrates with the Zen Server and Unreal Cloud DDC to manage local and shared caches. Its primary purpose is to eliminate the need for every developer to locally re-compile the same assets, drastically reducing project load times and shader compilation waits across a team.

Practical Usage Tips and Best Practices
Utilize the Zen Dashboard
In UE 5.6, you can access the Zen Dashboard through this module (found under the “Derived Data” button in the status bar). Use it to monitor the health and throughput of your local Zen Server. Monitoring this allows you to eliminate “invisible” performance bottlenecks caused by a struggling local cache service.
Configure a Shared DDC for Teams
One of the most effective ways to eliminate idle time is to set up a Shared DDC on a fast local network drive. By adding a [DerivedDataBackendGraph] entry to your DefaultEngine.ini, the module can pull already-cooked assets from your teammates’ machines or a build server.
Shift to Zen Storage Server
Traditional filesystem-based DDC is prone to “loose file” overhead. Transitioning your project to use Zen Storage Server (now the default) allows the module to handle data via a streamlined database. This helps eliminate the high I/O latency associated with reading thousands of small files during a cold boot.
Enable S3 or Cloud DDC for Remote Work
If your team works remotely, configure the Unreal Cloud DDC. This module will then fetch assets over HTTPS rather than a slow VPN file share. This is the best way to eliminate the “stuck at 45%” splash screen issues frequently encountered by remote developers.
Monitor Cache “Misses” during Iteration
If you notice frequent shader recompiles, check the logs for “DDC Miss.” A high miss rate usually indicates that your cache is too small or your DDC keys are being invalidated by frequent engine version changes. Identifying this helps you eliminate redundant computation time.
Clear Cache Safely to Resolve Corruption
If an asset like a player elimination VFX is rendering incorrectly despite no changes to the source, the cached derived data might be corrupt. Rather than deleting your entire project, use the module’s ability to “invalidate” specific entries or clear the local folder to eliminate the corrupted binary data.
Use Global Local DDC Paths
For developers with multiple engine versions, set a global DDC path in your Editor Preferences. This allows the DerivedDataEditor to share cached assets across different projects on the same machine, helping you eliminate the disk space waste of duplicate caches.
Optimize for Fast Local SSDs
The DDC is extremely I/O intensive. Always point your local DDC to your fastest NVMe drive. This ensures that the DerivedDataEditor can stream processed textures into memory as quickly as possible, which helps eliminate texture popping and hitching while navigating the viewport.