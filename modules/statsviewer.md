---
layout: default
title: StatsViewer
---

<!-- ai-generation-failed -->

<h1>StatsViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/StatsViewer/StatsViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, Core, CoreUObject, EditorFramework, Engine, InputCore, Landscape, RHI, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ndow in the Unreal Editor (Window > Statistics). It acts as a centralized data aggregator that pulls information from various parts of the engine—such as lighting, textures, primitives, and the cooker—to provide developers with an audit of their current level.

This module is a primary tool for performance profiling, allowing you to identify which assets are consuming the most memory or rendering time. It helps you eliminate bottlenecks by pinpointing exactly which actors or textures are exceeding your project’s performance budgets.

Practical Usage Tips and Best Practices
Audit Primitive Triangle Counts
In the “Primitive Stats” mode, you can see a list of every mesh in the level along with its triangle count and memory footprint. Sort by triangle count to identify high-poly assets that need Nanite enabled or LOD adjustments to eliminate unnecessary GPU draw time.
Identify Uncompressed Textures
Use the “Texture Stats” mode to check the “Max Dimension” and “Format” of loaded textures. If you find large textures using uncompressed formats (like RGBA8), you can quickly navigate to them and apply proper compression settings to eliminate excessive VRAM usage.
Review Lighting Build Info
If your lightmap bakes are taking too long, use the “Lighting Build Info” mode to see exactly how many seconds were spent on each actor. This helps you identify meshes with excessively high lightmap resolutions, allowing you to lower them and eliminate long wait times during the build process.
Check for Unmapped Texels
The statistics window can report the percentage of unmapped texels on a mesh. High values usually indicate poor UV layouts or overlapping lightmaps. Identifying these early allows you to fix the assets and eliminate visual artifacts like black spots or lighting seams.
Leverage Cooker Stats for Packaging
The “Cooker Stats” view provides information on assets processed during the last cook. Use this to find large assets that are being included in your build accidentally, helping you eliminate “bloat” from your final packaged game size.
Quick Asset Navigation
Double-clicking any entry in the Stats Viewer will automatically select that actor in the Level Viewport or find the asset in the Content Browser (now Fab). This workflow helps you eliminate the time spent searching through the World Outliner for problematic objects.
Monitor Static Mesh Lighting Memory
The “Static Mesh Lighting Info” mode shows the total memory used by lightmap textures per actor. In memory-constrained environments like mobile, use this data to eliminate non-essential static lighting on small props that could use cheaper dynamic or vertex lighting instead.
Handle Data Refresh on Actor Elimination
The Stats Viewer does not always update in real-time to avoid performance hitches. If you delete actors from your scene (the “elimination” of an object), ensure you click the Refresh button in the Statistics window to eliminate stale data from your current performance report.