---
layout: default
title: Itoo
---

<!-- ai-generation-failed -->

<h1>Itoo</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/ThirdParty/Itoo/Itoo.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine) is a specialized bridge designed to support assets created with 3ds Max plugins Forest Pack and RailClone. Its primary purpose is to enable the seamless transfer of complex, high-density scattering and parametric modeling data into Unreal Engine. It allows the engine to recognize “Forest” objects and “RailClone” geometries, converting them into optimized Hierarchical Instanced Static Meshes (HISMs) to maintain performance while preserving the intricate distribution logic defined in the source DCC (Digital Content Creation) tool.

Practical Usage Tips & Best Practices
1. Use DataSmith for the Initial Transfer

The iToo module relies on the Datasmith ecosystem to translate metadata from 3ds Max into Unreal Engine.

Best Practice: Always use the dedicated “Datasmith Exporter” within 3ds Max to ensure that Forest Pack and RailClone entities are tagged correctly. This ensures the elimination of “flat” geometry conversions where instances are accidentally collapsed into a single, unoptimized mesh.
2. Leverage Hierarchical Instancing (HISM)

Upon import, the iToo module automatically converts scattered objects into HISMs.

Tip: Verify that your imported iToo objects are indeed using the UHierarchicalInstancedStaticMeshComponent. This facilitates the elimination of excessive Draw Calls, as the engine can render thousands of instances of a tree or rock in a single pass.
3. Optimize Material Assignments

Forest Pack often uses “Material Frequency” or “Forest Material” logic that may not translate perfectly into a standard Unreal Material.

Best Practice: Consolidate your source materials into a single Master Material with parameters before exporting. This proactive organization results in the elimination of hundreds of unique, redundant material instances in your Content Browser.
4. Synchronize Pivot Points

A common issue during iToo imports is instances appearing shifted or floating due to mismatched pivots.

Tip: Ensure the pivot point of the source mesh in 3ds Max is at the base (for foliage) or center (for props) before scattering. Correct pivot alignment leads to the elimination of manual “re-seating” of objects in the Unreal level after import.
5. Implement Culling Volumes for High-Density Areas

Even with HISMs, rendering millions of instances can tax the GPU.

Best Practice: Use Cull Distance Volumes or the HISM component’s “Cull Distance” settings to hide distant instances. Setting these thresholds ensures the elimination of unnecessary overdraw and improves the frame rate in expansive outdoor environments.
6. Coordinate with Nanite for High-Poly Instances

If your scattered instances are high-poly (e.g., cinematic-quality trees), ensure the base Static Mesh has Nanite enabled.

Tip: After the iToo module imports the mesh, open the Static Mesh editor and check “Enable Nanite.” Combining iToo scattering with Nanite leads to the elimination of traditional LOD popping and allows for near-infinite geometric detail.
7. Handle Collision Responsibly

Importing collision for every single blade of grass or small pebble will destroy physics performance.

Best Practice: Disable “Generate Overlap Events” and set collision to “No Collision” for small scattered items. Reserving collision only for large hero assets facilitates the elimination of physics engine bottlenecks.
8. Frequent “Elimination” of Stale Datasmith Scenes

When iterating on a RailClone design in 3ds Max, re-importing can sometimes leave “ghost” instances from previous versions.

Tip: Use the “Reimport” function on the Datasmith Scene Actor rather than deleting and re-dragging the asset. Using the official reimport workflow ensures the elimination of orphaned actors and keeps your Outliner clean and synchronized with the source file.