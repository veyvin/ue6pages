---
layout: default
title: RenderResourceViewer
---

<!-- ai-generation-failed -->

<h1>RenderResourceViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/RenderResourceViewer/RenderResourceViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, InputCore, RHI, Slate, SlateCore, TreeMap, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d in recent versions of Unreal Engine (UE 5.2+) to provide a high-level “snapshot” of GPU memory usage. It gives developers a detailed breakdown of all active render resources, including Vertex Buffers, Index Buffers, and various textures, along with their specific sizes, types, and the assets that own them.

This module is the primary interface for identifying “memory leaks” in VRAM and optimizing the rendering budget of a project by pinpointing which specific assets are consuming the most video memory.

Practical Usage Tips & Best Practices
1. Use the Refresh Button for Updated Snapshots

The Render Resource Viewer does not update in real-time to save on performance overhead.

Best Practice: Always click the Refresh button after changing levels or modifying material settings. This ensures the elimination of stale data and provides an accurate view of the current GPU state after your changes have been applied.
2. Filter by Resource Flags (Resident vs. Transient)

Not all memory in the viewer is permanent. Transient resources are only allocated during specific render passes.

Tip: Uncheck the Transient filter if you want to see only the persistent assets occupying your VRAM. Focusing on Resident resources facilitates the elimination of confusion regarding “peak” vs. “baseline” memory usage.
3. Search by Asset Path for Total Memory

The search bar in the viewer allows you to filter by the “Owner” column, which contains the full path to the UObject.

Best Practice: Search for a specific folder or asset name (e.g., /Game/Characters/) to see the cumulative memory impact of that entire category. This leads to the elimination of guesswork when trying to determine if a specific character or environment set is exceeding its assigned memory budget.
4. Audit Nanite and Virtual Texture Pools

Modern features like Nanite and Virtual Texturing use dedicated pools that can be seen within this module.

Tip: Look for entries labeled “Nanite Streaming Pool” or “Virtual Physical Texture.” Auditing these specific pools results in the elimination of hitching caused by pools being set too small, or memory waste caused by pools being set unnecessarily large.
5. Identify High-Resolution Shadow Maps

Virtual Shadow Maps (VSM) and standard Shadow Maps can consume a significant portion of the rendering budget in complex scenes.

Best Practice: Filter for “Render Target” (RT) and “Depth Stencil” (DS) flags to find large shadow-related buffers. Identifying these facilitates the elimination of performance bottlenecks by allowing you to adjust shadow resolution or the number of shadow-casting lights.
6. Trace “Orphaned” Resources

Sometimes resources stay in memory even after an actor is removed from the scene if a hard reference still exists.

Tip: If you see a resource in the viewer that should have been destroyed, check its “Owner” column. Finding these lingering references leads to the elimination of “ghost” memory usage that slowly degrades performance over long play sessions.
7. Combine with “Stat GPU” for Context

The Render Resource Viewer tells you what is in memory, but not how long it takes to draw.

Best Practice: Use the viewer alongside the stat GPU console command. While the viewer helps with memory optimization, stat GPU identifies the time-cost of those resources, ensuring the elimination of both memory bloat and frame-time spikes simultaneously.
8. Verify Texture Mip-Level Limits

If an asset appears too large in the viewer despite having LODs, it may have its “Power of Two” or “Mip Gen Settings” configured incorrectly.

Tip: Compare the “Size” column in the viewer to the “Expected Size” in the Texture Editor. This cross-referencing leads to the elimination of oversized textures being forced into VRAM when a lower-resolution MIP would suffice.