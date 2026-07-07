---
layout: default
title: DerivedDataWidgets
---

<!-- ai-generation-failed -->

<h1>DerivedDataWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DerivedDataWidgets/DerivedDataWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DerivedDataCache, EditorFramework, EditorSubsystem, Engine, InputCore, MessageLog, OutputLog, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

s the user interface components for monitoring the Derived Data Cache (DDC). It is responsible for the “Derived Data” status bar widget located in the bottom-right corner of the Unreal Editor.

This module allows developers to visualize how the engine is handling asset compilation (shaders, textures, meshes) in real-time. It provides critical insights into cache hits, misses, and the latency of remote storage solutions like ZenServer or Unreal Cloud DDC.

1. Monitor Remote Cache Latency

In a studio environment using a Shared DDC, network latency is a primary bottleneck.

Best Practice: Click the Derived Data widget and select View Cache Statistics. Ensure your “Remote” Zen latency is ideally below 20ms. If latency exceeds 60ms, the engine may bypass the shared cache and recompile assets locally, eliminating the benefits of the shared system.
2. Identify “Cache Miss” Culprits

If the editor feels sluggish during asset loading, use the statistics provided by this module to check for high “Miss” rates.

Tip: If you see a high number of misses for a specific asset type (like Shader), it indicates that your build machine or other team members have not yet pushed those assets to the shared cache. This is a signal that you might need to run a “Warmup” commandlet on your DDC.
3. Verify ZenServer Connectivity

Since UE 5.4, the engine uses Unreal Zen Server as the default local DDC.

Best Practice: Use the widget to confirm that your “Local” store is listed as Cache Type = Zen. If it shows a “Filesystem” fallback, your local Zen service may be crashed or blocked by a firewall, leading to slower I/O performance.
4. Troubleshoot “Stuck” Asset Processing

Sometimes the editor appears to be stuck “Processing Assets” indefinitely.

Tip: Hover over the Derived Data widget to see exactly which background tasks are running. If the widget shows it is waiting on a remote resource, you can identify if the issue is your local CPU being pinned or a slow response from the Cloud DDC.
5. Check Cloud DDC Health

For distributed teams, the Unreal Cloud DDC is the primary source of truth.

Best Practice: Use the status widget to ensure you are authenticated and connected. The widget will display a warning icon if your authentication token has expired, preventing you from downloading assets and forcing your machine to waste time compiling them locally.
6. Analyze Cache Hit Ratios

The “Cache Statistics” panel provided by this module shows a ratio of Hits vs. Misses.

Tip: Aim for a Hit ratio of 90% or higher in a mature project. If your ratio is low, it means your team is frequently duplicating work. Use this data to justify a “Nightly Cook” or “DDC Warmup” script that populates the cache for everyone before the workday starts.
7. Debug Virtual Asset (VA) Pulls

When using Virtual Assets, the editor only downloads bulk data when needed.

Best Practice: Use the Derived Data stats to monitor “Virtual Asset” traffic. If you see high “Remote” traffic when simply opening a map, it means the VA system is successfully pulling data from the DDC instead of requiring you to download 100GB+ of raw data from Perforce.
8. Use for Performance Profiling

The Derived Data status is a key metric during “First Run” or “Sync” scenarios.

Tip: When onboarding a new developer or switching branches, keep the statistics window open. This allows you to differentiate between a “Hardware Bottleneck” (CPU compiling shaders) and a “Network Bottleneck” (downloading derived data), helping you eliminate guesswork when diagnosing slow editor performance.