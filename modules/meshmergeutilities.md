---
layout: default
title: MeshMergeUtilities
---

<!-- ai-generation-failed -->

<h1>MeshMergeUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshMergeUtilities/MeshMergeUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the underlying logic for combining multiple Static Meshes into a single asset. It is the engine behind the Merge Actors tool and the HLOD (Hierarchical Level of Detail) system.

Beyond simple geometry merging, this module handles complex tasks such as material baking, UV re-parameterization, and mesh simplification. It is primarily used to optimize environments by reducing the total number of actors in a scene and consolidating multiple draw calls into a single one.

Practical Usage Tips & Best Practices
1. Use “Merge” to Reduce Draw Calls

The most common use of this module is to combine several small meshes that share the same materials into one large mesh.

Best Practice: Select actors that are physically close to each other and share the same Material Instance. This results in the elimination of redundant draw calls, as the GPU can process the combined geometry in a single pass rather than multiple individual calls.
2. Leverage Proxy Meshes (Simplify) for Distance Geometry

The module provides a “Proxy” or “Simplify” method which creates a new, low-poly mesh and bakes all original textures into a single texture atlas.

Tip: Use this for background buildings or “vista” objects. This allows for the elimination of heavy polygon counts in the distance while maintaining the visual silhouette and color of the original complex objects.
3. Control Texture Resolution via Bake Settings

When merging materials, the module must decide how large the new baked texture will be.

Best Practice: Don’t use 4K bakes for everything. Match the bake resolution to the object’s importance and distance from the player. Optimizing these dimensions leads to the elimination of wasted VRAM and reduces the total disk size of your project.
4. Manage UV Channel Conflicts

When merging meshes, their UV layouts will overlap if not handled correctly.

Tip: Ensure you check the “Generate Lightmap UVs” option during the merge. This facilitates the elimination of lighting artifacts by creating a new, non-overlapping UV channel specifically for lightmaps in the newly combined mesh.
5. Be Mindful of Pivot Point Alignment

By default, the merged mesh will set its pivot to the world origin (0,0,0) or the center of the selection.

Best Practice: Use the “Pivot Selection at Zero” or “Pivot at First Selected” options to keep your new actor manageable. Proper pivot placement ensures the elimination of “offset” issues when trying to rotate or move the combined mesh later in the level design process.
6. Optimize Collision Complexity

Merging 100 small rocks into one large mesh can result in a very complex and expensive collision shape.

Tip: In the merge settings, select “Calculate Correct LOD Model” and consider using a simplified primitive (like a Box or Sphere) for the collision of the new actor. This results in the elimination of CPU physics bottlenecks caused by overly complex triangular collision meshes.
7. Balance Memory vs. Draw Calls

Merging objects creates a brand-new .uasset file on your disk, which increases the memory footprint.

Best Practice: Only merge objects that are used frequently together. If you merge unique sets of objects everywhere, you may experience the elimination of your memory budget. Use Instanced Static Meshes instead if you are repeating the exact same object many times.
8. Clean Up “Fixup Redirectors” Post-Merge

When you merge actors, the engine creates new assets and sometimes moves references around.

Tip: After performing a large merge and saving the new assets, right-click your content folders and select Fixup Redirectors. This ensures the elimination of broken internal links and keeps the project structure healthy for source control.