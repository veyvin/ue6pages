---
layout: default
title: HierarchicalLODUtilities
---

<!-- ai-generation-failed -->

<h1>HierarchicalLODUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/HierarchicalLODUtilities/HierarchicalLODUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BSPUtils, Core, CoreUObject, EditorFramework, Engine, MaterialUtilities, MeshDescription, Projects, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

urce/Developer/HierarchicalLODUtilities, this module is an editor-only utility that bridges the gap between high-level world building and low-level mesh merging/simplification. It contains the core logic for clustering actors together based on spatial proximity and invoking the mesh reduction and material baking pipelines.

Primary uses include:

Actor Clustering: Automatically grouping actors into clusters based on their bounding boxes and a target “Fill Percentage.”
Proxy Mesh Generation: Automating the workflow of merging multiple static meshes into a single mesh and baking their materials into a single texture atlas.
HLOD Outliner Support: Powering the “Generate Clusters” and “Generate Proxy Meshes” buttons found in the HLOD Outliner window.
Integration with World Partition: Providing the utilities that World Partition uses to generate HLOD cells for massive open-world environments.
Practical Usage Tips and Best Practices
1. Define HLOD Layers Strategically

Instead of using a single global setting, define multiple HLOD Layers for different asset types (e.g., one for buildings, one for vegetation). This allows the HierarchicalLODUtilities module to apply different mesh reduction strengths to each category, leading to the elimination of visual artifacts in complex assets.

2. Utilize HLOD Volumes for Manual Control

While the module’s clustering algorithm is robust, it can sometimes group actors illogically. Use HLOD Volumes to force specific actors into the same cluster. The utilities module prioritizes these volumes, ensuring that critical landmarks are merged exactly how you intend.

3. Monitor Mesh/Vertex Count via DumpStats

Use the console command wp.Editor.HLOD.DumpStats to generate a CSV file of your HLOD data. This allows you to see the exact triangle reduction achieved by the module. Analyze this data to find “heavy” HLODs that require more aggressive simplification or the elimination of specific high-poly sub-assets from the cluster.

4. Exclude Non-Significant Actors

Small actors like pebbles, grass blades, or interior furniture should rarely be included in HLODs. In the Actor’s details panel, set Include in HLOD to false. This streamlines the work for the HierarchicalLODUtilities module, reducing the time required to bake proxy meshes and saving significant VRAM.

5. Verify Distance Field Generation

By default, merged HLOD meshes may not have distance fields. If your distant vistas rely on Distance Field Ambient Occlusion (DFAO), ensure the “Generate Distance Field” option is enabled in the Mesh Generation settings. This ensures the elimination of “flat” lighting on your distant proxy geometry.

6. Optimize Material Baking for VRAM

When the module bakes proxy materials, it creates a texture atlas. Set a strict Max Texture Size (e.g., 1024x1024) for your HLOD layers. Since these assets are only seen from a distance, high-resolution textures are unnecessary and their elimination significantly improves streaming performance.

7. Use HLOD Relevant Color for Debugging

In the viewport, use the HLOD Relevant Color mode (new in 5.4+) to visualize which actors are currently being considered for HLOD generation. This visual feedback helps you quickly identify and remove actors that are too small or located underground, keeping your HLOD clusters lean.

8. Strategic Elimination of Outdated HLODs

HLODs can become “stale” as you move actors during level design. Periodically use the Delete Clusters action in the HLOD Outliner to clear old data before running a final production build. This ensures that the utilities module is working with a fresh, accurate representation of your level’s current state.