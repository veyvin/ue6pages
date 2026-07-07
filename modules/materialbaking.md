---
layout: default
title: MaterialBaking
---

<!-- ai-generation-failed -->

<h1>MaterialBaking</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MaterialBaking/MaterialBaking.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, MeshDescription, PropertyEditor, RHI, RenderCore, Renderer, Slate, SlateCore, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

graph-based materials into static 2D textures.

Description and Purpose

This module provides the logic and interfaces (such as IMaterialBakingModule) required to render material properties—like Base Color, Metallic, and Normal—into texture maps. Its primary purpose is to convert expensive, instruction-heavy materials into simple, performant ones. This is essential for optimizing games for mobile or low-end hardware, generating proxy meshes (HLODs), and exporting assets to external formats like glTF. By using this module, developers can eliminate the high GPU cost of procedural shaders by pre-calculating their output into standard image files.

Practical Usage Tips and Best Practices
Use for HLOD and Proxy Mesh Generation
When creating Hierarchical Levels of Detail (HLODs), this module is responsible for merging the materials of multiple distant objects into a single atlas. This is a best practice to eliminate excessive draw calls and reduce the memory overhead of distant background scenery.
Enable “Use Mesh Data” for Accuracy
In the Material Baking Options, checking Use Mesh Data allows the baker to account for mesh-specific information like Vertex Colors and World Position. This helps you eliminate visual inaccuracies when baking materials that rely on the physical shape or orientation of the object.
Implement the UDIM Workaround
In recent engine versions, the default baker may only target the 0-1 UV space (UDIM 1001). To bake higher UDIM tiles, apply a UV offset to your material instance before baking each tile. This manual step allows you to eliminate the limitation and successfully bake high-fidelity, multi-tile assets.
Optimize Resolution per Channel
Don’t bake every channel at the same resolution. For example, you might bake Base Color at 2048x2048 but Roughness at 512x512. Adjusting these settings helps you eliminate texture bloat and keep your final package size manageable.
Leverage glTF Proxy Materials
If you are exporting assets for the web or external viewing, use this module to create glTF Proxy Materials. This ensures the complex Unreal material logic is “baked down” into a format the glTF standard understands, which helps you eliminate missing textures in external viewers.
Avoid View-Dependent Nodes
Material baking is a static process. Nodes like CameraVector, Fresnel, or SceneColor do not bake well because they change based on the player’s perspective. Removing or replacing these nodes before baking is the best way to eliminate unsightly artifacts in your final textures.
Coordinate via IMaterialBakingModule in C++
If you are building custom editor tools, use the IMaterialBakingModule::Get().BakeMaterials() function. This provides a programmatic way to batch-process assets, helping you eliminate the tedious task of manually clicking “Bake” for every mesh in a large project.
Check for Transient Material Cleanup
The baking process often generates transient (temporary) materials in the content browser. Always ensure you “Save As” the resulting textures and re-assign them to a permanent material. This prevents the engine from losing the baked data upon restart, helping you eliminate “Missing Texture” errors later.