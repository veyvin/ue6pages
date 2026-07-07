---
layout: default
title: NaniteUtilities
---

<!-- ai-generation-failed -->

<h1>NaniteUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/NaniteUtilities/NaniteUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopWidgets, Engine, GeometryCore, ImageCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

vel geometric processing and math functions required to build, optimize, and debug Nanite meshes.

Description and Purpose

While the NaniteBuilder module handles the high-level orchestration of creating Nanite assets, NaniteUtilities contains the “heavy lifting” logic. Its primary purpose is to provide algorithms for triangle clustering, edge collapsing, and error metric calculations. It is responsible for taking a high-density mesh and partitioning it into the hierarchical “clusters” that Nanite streams at runtime. By utilizing this module, the engine can eliminate massive amounts of redundant geometric data while ensuring that the visual transitions between different levels of detail are seamless and crack-free.

Practical Usage Tips and Best Practices
Analyze Cluster Density via Nanite Stats
Use the module’s integration with the NaniteStats command to monitor cluster counts. If a mesh has an unusually high number of clusters for its size, it may indicate “dirty” geometry (like disconnected faces). Cleaning the source mesh helps you eliminate unnecessary streaming overhead and memory bloat.
Adjust Trim Relative Error for Quality
In the Nanite settings, the “Trim Relative Error” uses utilities from this module to determine how much detail to strip away. Keeping this value between 0.02 and 0.04 is a best practice to eliminate visible “faceting” on curved surfaces while still maintaining a high level of optimization.
Leverage for Custom Import Pipelines
If you are building an automated pipeline to import photogrammetry data, use the helpers in this module to pre-validate your meshes. Ensuring vertices are welded and normals are consistent before the Nanite build process is the best way to eliminate “holes” or lighting artifacts in the final Nanite representation.
Monitor “Cluster SW” vs. “Cluster HW”
This module defines the logic for how clusters are rasterized (either via Hardware or Software paths). Use the Nanite visualization modes to identify meshes that are falling back to the slower Software (SW) path. Simplifying the material complexity on these meshes is the best way to eliminate performance bottlenecks on older GPUs.
Optimize Voxel Resolution for Displacement
When using Nanite Displacement (Experimental), the module’s utilities calculate how many extra triangles to generate. Setting a sensible Magnitude and Center value helps the builder eliminate “oversampling,” where the engine generates more detail than the displacement map can actually provide.
Verify Material Slot Boundaries
Nanite clusters are split based on material IDs. If you have a mesh with dozens of tiny material slots scattered across the surface, the utilities will be forced to create more clusters. Consolidating materials is a best practice to eliminate fragmented clusters, which improves GPU culling efficiency.
Check for Non-Manifold Geometry
Nanite’s clustering algorithm works best on “water-tight” meshes. Use the visualization tools provided by this module to look for “Red” areas in the Cluster view, which often indicate non-manifold edges. Fixing these in your source DCC helps you eliminate flickering or disappearing triangles during camera movement.
Understand the “Proxy” Mesh Fallback
For platforms that do not support Nanite, this module generates a “Proxy” mesh. You can adjust the Proxy Triangle Percent to control the quality of this fallback. Fine-tuning this setting ensures you eliminate the risk of your game looking poor on mobile or legacy consoles while still using Nanite on high-end hardware.