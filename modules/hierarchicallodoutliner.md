---
layout: default
title: HierarchicalLODOutliner
---

<!-- ai-generation-failed -->

<h1>HierarchicalLODOutliner</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/HierarchicalLODOutliner/HierarchicalLODOutliner.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, HierarchicalLODUtilities, InputCore, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

management logic for the Hierarchical Level of Detail (HLOD) system. Unlike standard LODs that swap a single mesh for a lower-resolution version, HLODs group multiple Static Mesh Actors together into a single “Proxy Mesh.” This module allows developers to visualize, generate, and organize these clusters, which are critical for maintaining high performance in large-scale environments by reducing draw calls and triangle counts at long distances.

Practical Usage Tips & Best Practices
1. Use the “Forced LOD Level” for Visual Validation

It can be difficult to see if an HLOD looks correct when it only appears at great distances.

Tip: In the HLOD Outliner, use the Forced LOD Level dropdown (or the r.HLOD.ForceLOD console command). This allows you to view the proxy meshes up close, facilitating the elimination of visual artifacts, gaps, or texture popping before you finalize the build.
2. Manually Define Clusters with HLOD Volumes

The automatic clustering algorithm sometimes groups objects logically unrelated or physically separated by walls.

Best Practice: Drag Hierarchical LOD Volumes into your level to manually encompass specific groups of actors (like a cluster of houses). This ensures the elimination of inefficient, overlapping clusters that the automated system might generate.
3. Enable “Generate Single Cluster for Level” in Sublevels

For massive worlds utilizing many sublevels (e.g., a specific building or a small camp), the default clustering can be overkill.

Tip: In the World Settings of a sublevel, enable Generate Single Cluster for Level. This forces the system to treat the entire sublevel as one unit, leading to the elimination of complex cluster-calculation times during the build process.
4. Optimize via “Simplify Mesh” and Proxy Geometry

The HLOD system can either merge meshes or use the Proxy Geometry tool to create a completely new, simplified shell.

Best Practice: For distant background mountains or cityscapes, enable Simplify Mesh. This creates a “shrink-wrapped” version of the geometry, which assists in the elimination of internal polygons that would never be seen by the player, saving significant GPU memory.
5. Exclude Small or Invisible Actors

Small props like pebbles or interior furniture should not be part of a distant HLOD proxy as they contribute little to the silhouette but increase texture size.

Tip: Select an actor and uncheck Can be in Cluster in its details panel. This results in the elimination of “noise” in your HLOD textures and keeps the proxy mesh focused on the most important structural shapes.
6. Transition to PCG for Modern HLOD Management

In Unreal Engine 5.6 and 5.7, the Procedural Content Generation (PCG) framework can handle some aspects of actor grouping.

Best Practice: For procedural forests or rock fields, use PCG to manage instances. This allows for the elimination of the need to manually rebuild HLOD clusters every time you move a procedural asset, as the PCG graph can handle the density and representation.
7. Rebuild Individual Clusters to Save Time

Rebuilding HLODs for an entire persistent level can take hours in complex projects.

Tip: Right-click a specific cluster in the HLOD Outliner and select Rebuild Proxy Mesh. This localized update ensures the elimination of massive wait times when you only made changes to a small area of the map.
8. Monitor Quad Overdraw in Distant Views

Even simplified HLODs can cause performance issues if they result in sub-pixel triangles at extreme distances.

Best Practice: Use the Quad Overdraw view mode while looking at your HLODs. If they appear bright red, increase the simplification settings or the distance at which they appear. This leads to the elimination of GPU bottlenecks caused by the hardware rendering triangles smaller than a single pixel.