---
layout: default
title: MeshBoneReduction
---


<h1>MeshBoneReduction</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshBoneReduction/MeshBoneReduction.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationBlueprintLibrary, Core, CoreUObject, Engine, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ing Skeletal Meshes by simplifying their underlying bone structures at lower Levels of Detail (LODs). This module provides the logic for the Skeletal Mesh Reduction Tool, allowing the engine to automatically remove bones that contribute minimally to the mesh’s silhouette at a distance and remap their skin weights to the remaining parent bones.

This module is essential for character-heavy games, as it helps eliminate the performance cost of processing complex skeletons for background characters. By reducing the bone count in the bone buffer, it significantly lowers the CPU cost of skinning and animation updates.

Practical Usage Tips and Best Practices
Prioritize Critical Bones for Silhouette
In the Asset Details panel under LOD Info, use the Bones to Prioritize array. Add essential joints like the head, hands, or feet to this list. This module will ensure these joints remain intact during reduction, helping you eliminate visual collapses or “flattening” of the character’s key features at low LODs.
Set High Weight of Prioritization
When prioritizing bones, use a high Weight of Prioritization value (e.g., 5,000). This tells the reduction algorithm to focus heavily on preserving the geometry around these specific bones. This practice helps you eliminate pointiness or jagged edges in sensitive areas like the face or fingers.
Use ‘Lock Mesh Edges’ for Connectivity
If your character has disconnected mesh parts (like a separate head or armor pieces), enable Lock Mesh Edges in the Reduction Settings. This module will lock the boundary vertices, helping you eliminate visible gaps or “holes” that can appear when adjacent bones are reduced differently.
Leverage Termination Criterion
Use the Termination Criterion setting to choose between Max Triangles or Max Vertices. If your performance bottleneck is memory-related, focus on vertex reduction; if it is GPU-bound, focus on triangle reduction. Choosing the right criterion helps you eliminate the specific bottleneck affecting your target hardware.
Remove Decorative Bones Automatically
For distant LODs, use the module to remove “leaf” bones like individual finger joints, hair strands, or scarf bones. Remapping these weights to the hand or head helps you eliminate the overhead of the Animation Blueprint calculating transforms for parts the player can no longer see.
Remap Skin Weights Correctly
Ensure that when a bone is removed, its skin weights are remapped to its nearest parent. The module handles this by default, but you should verify the results in the Mesh Editor using the “Character > Mesh > Bone Colors” view to eliminate “stretching” artifacts where vertices are stuck to the world origin.
Combine with ‘Remove Morph Targets’
When reducing bones for low LODs, also enable Remove Morph Targets in the LOD settings. Since morph targets rely on vertex offsets, keeping them on a heavily reduced mesh is often redundant. This helps you eliminate unnecessary memory bloat in your packaged build.
Test with the LOD Picker
Use the LOD Picker in the viewport to force the mesh into its lowest LOD state. Walk around the character to ensure the “elimination” of certain bones hasn’t caused catastrophic skinning errors. This visual check allows you to eliminate logic errors in your prioritization list before finalizing the asset.