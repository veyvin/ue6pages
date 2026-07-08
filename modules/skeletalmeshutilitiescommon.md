---
layout: default
title: SkeletalMeshUtilitiesCommon
---

<!-- ai-generation-failed -->

<h1>SkeletalMeshUtilitiesCommon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SkeletalMeshUtilitiesCommon/SkeletalMeshUtilitiesCommon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeCommon, Core, CoreUObject, Engine, ImageCore, InterchangeCore, MeshDescription, MeshUtilitiesCommon, RenderCore, SkeletalMeshDescription, Slate, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

that provides the core backend logic for manipulating skeletal mesh data outside of the standard animation runtime. It acts as a bridge between high-level editor tools (like the Skeletal Mesh Editor) and low-level mesh data, offering functions for skeleton remapping, LOD (Level of Detail) management, and skin weight processing.

This module is essential for building custom editor tools or automation scripts that need to modify the structure of a character. It allows you to eliminate manual, repetitive tasks by programmatically adjusting bone hierarchies, merging meshes, or transferring skin weights between different geometries.

Practical Usage Tips and Best Practices
Automate Skin Weight Transfers
Use the utilities in this module to programmatically transfer skin weights from a high-poly source to a low-poly target. This is particularly useful for garment systems or modular armor, helping you eliminate the need for artists to manually re-paint weights for every mesh variation.
Manage Skeleton Remapping
When importing animations intended for a different bone hierarchy, use this module’s remapping logic to align the source bones with the target skeleton. This helps you eliminate “broken” animations and ensures that retargeting logic has a valid base to work from.
Implement Bone Weight Locking
If you are building a custom skinning tool, leverage the module’s ability to “lock” specific bone influences. By preventing certain vertices from being modified during a smoothing or normalization pass, you can eliminate unwanted deformations in critical areas like the face or mechanical joints.
Optimize LOD Generation
This module provides the underlying logic for the “Skeletal Mesh Reduction” interfaces. You can use it to define which bones should be removed at lower LODs, helping you eliminate unnecessary CPU overhead for characters that are far away from the camera.
Perform Safe Bone Elimination
When simplifying a skeleton for mobile or performance-constrained platforms, use the FSkeletalMeshUtilities to “bake” the influences of a child bone into its parent. This allows for the elimination of unnecessary bones while maintaining the overall skinning silhouette of the character.
Validate Mesh Connectivity
Use the module’s validation functions to check for “zero-weight” vertices or isolated mesh islands that aren’t bound to any bones. Identifying these issues early helps you eliminate visual glitches like “stretching” vertices that stay at the world origin during animation.
Utilize for Dataflow Integration
In UE 5.5+, this module is increasingly used as a backend for Dataflow nodes. If you are creating custom Dataflow graphs for skeletal meshes, wrap this module’s functions into your nodes to eliminate the complexity of manual buffer management.
Refresh Buffers on Asset Modification
Whenever you use this module to modify a mesh (such as during the “elimination” of a specific LOD or Morph Target), always call the appropriate update functions to refresh the render buffers. This ensures that the editor viewport immediately reflects your changes and helps you eliminate stale preview data.