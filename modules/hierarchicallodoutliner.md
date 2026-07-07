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

evels. Its primary purpose is to group multiple Static Mesh Actors into “Clusters” and then generate a single, simplified Proxy Mesh to represent that entire cluster at long view distances. By reducing hundreds of individual actors to one draw call, this system helps eliminate CPU and GPU bottlenecks caused by high actor counts in open-world environments. It is essentially the “manager” for the transition between standard LODs and highly optimized distant representations.

Practical Usage Tips and Best Practices
Use HLOD Volumes for Precise Clustering
While the system can generate clusters automatically based on distance, you can place HLOD Volumes in your level to manually define which actors should be grouped together. This allows you to eliminate “leaking” clusters where objects from different buildings are incorrectly merged.
Enable “Generate Single Cluster for Level” for Sublevels
If you use a level-streaming architecture where each house or small landmark is its own sublevel, check the “Generate Single Cluster for Level” option in the HLOD Outliner. This forces the entire sublevel to become one HLOD, which helps you eliminate the time-consuming automated cluster generation process.
Prioritize Material Merging to Reduce Draw Calls
In the HLOD Layer settings, ensure that Mesh Merge Settings are configured to bake textures into an atlas. This allows the proxy mesh to use a single material, helping you eliminate redundant draw calls that occur when a merged mesh still requires multiple material slots.
Override HLOD Settings for World Partition
In modern UE5 projects using World Partition, HLODs are managed via HLOD Layers in the Data Layer outliner. Use the HierarchicalLODOutliner logic to define different layer types (e.g., “Simplified Mesh” for buildings vs. “Approximation” for distant mountains) to eliminate unnecessary geometry detail where it isn’t visible.
Visualize with “Forced LOD Level”
Use the Forced LOD Level menu within the HLOD Outliner to manually trigger the display of HLODs in the viewport. This is a critical debugging step to eliminate visual artifacts, such as “popping” or holes in the geometry, before building the final game package.
Exclude Specific Actors from Clusters
Not every actor should be part of an HLOD. For small props or internal items that are never seen from a distance, uncheck “Can be in Cluster” in the actor’s details panel. This helps the outliner eliminate useless data from the proxy mesh, keeping the file size small.
Rebuild Individual Clusters to Save Time
Building HLODs for a massive level can take hours. If you only modified one small area, right-click that specific cluster in the HLOD Outliner and select “Rebuild Proxy Mesh.” This allows you to eliminate the need for a full level rebuild during iterative development.
Manage Texture Resolution for Proxy Materials
In the Mesh Generation settings, carefully tune the Material Bake Size. Using a \(512 \times 512\) or \(1024 \times 1024\) texture for a distant cluster is usually sufficient. Over-specifying this resolution will eliminate your memory overhead benefits by bloating the project’s disk footprint.

Would you like a summary of the next segment covering HLOD Layer Assets and their specific properties?