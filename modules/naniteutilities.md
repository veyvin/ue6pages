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

module that provides the underlying logic for the Nanite Tools window and the optimization workflows for virtualized geometry. While the Nanite renderer handles the drawing of high-poly meshes at runtime, this module is focused on the auditing, conversion, and optimization of assets in the Content Browser.

It is primarily used to identify meshes that are good candidates for Nanite, detect errors in Nanite-enabled assets (such as unsupported blend modes), and batch-convert legacy geometry into the Nanite format.

Practical Usage Tips & Best Practices
1. Perform a “Nanite Audit” for Scene Optimization

The module provides the logic behind the Nanite Tools > Optimize tab, which scans your project for non-Nanite meshes with high triangle counts.

Best Practice: Regularly run a “Perform Audit” with a set triangle threshold (e.g., 2000+ triangles). This ensures the elimination of performance bottlenecks caused by complex standard static meshes that should be leveraging Nanite’s GPU-driven pipeline.
2. Fine-Tune the Triangle Threshold

Not every tiny prop should be Nanite. Very low-poly objects (under 500-1000 triangles) can actually be faster as standard static meshes due to Nanite’s fixed overhead.

Tip: Use the utility settings to adjust the audit threshold. Filtering out simple shapes leads to the elimination of unnecessary disk space usage and keeps your Nanite cluster data focused on high-detail geometry.
3. Identify Unsupported Material Features

Nanite has specific limitations regarding certain material features like World Position Offset (WPO) or specific blend modes.

Best Practice: Use the Errors tab in the Nanite Tools to find meshes using incompatible materials. Identifying these early results in the elimination of visual artifacts or rendering “black-box” errors in your scene.
4. Automated Conversion of High-Poly Assets

The module facilitates the bulk conversion of assets through the “Enable Nanite” button in the audit tool.

Tip: Rather than enabling Nanite manually for every mesh, use the audit window to select all high-detail candidates and convert them in one pass. This facilitates the elimination of tedious manual labor and ensures a consistent optimization pass across the entire project.
5. Monitor the “Fallback Mesh” Quality

For platforms or hardware that do not support Nanite, the engine generates a “Fallback” mesh.

Best Practice: Check the “Fallback Relative Error” settings via the mesh utility logic. Adjusting this value ensures the elimination of extreme visual “popping” when the engine transitions from a Nanite mesh to its standard proxy version.
6. Optimize Overlapping Geometry (Overdraw)

The utilities module supports the visualization modes used to detect high density and overdraw.

Tip: Use the Nanite Overdraw view mode to find areas where too many Nanite meshes are stacked closely together. Reducing this density leads to the elimination of performance degradation in the virtualized geometry pass, which can occur when thousands of small clusters overlap.
7. Handle WPO and Shadow Map Performance

While Nanite supports World Position Offset (WPO), it can be expensive when applied to millions of triangles.

Best Practice: Use the “Evaluate WPO” visualizer provided by the utility framework to see which Nanite meshes are actively using displacement logic. Disabling WPO on distant or unimportant Nanite assets results in the elimination of excessive GPU cycles in the Virtual Shadow Map (VSM) pass.
8. Verify Data Size on Disk

Nanite assets are often smaller in VRAM but can be larger on disk compared to heavily compressed low-poly meshes.

Tip: Use the Nanite Audit tool to monitor the disk footprint of your converted assets. Auditing your data sizes leads to the elimination of bloated project builds by only enabling Nanite on meshes where the detail-to-size ratio is beneficial.