---
layout: default
title: FBX
---

<!-- ai-generation-failed -->

<h1>FBX</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/FBX/FBX.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the FBX SDK) is the core interchange pipeline for Unreal Engine. It is the primary system responsible for importing and exporting 3D data, including Static Meshes, Skeletal Meshes, Animations, and Morph Targets, from Digital Content Creation (DCC) tools like Maya, 3ds Max, and Blender.

The module handles the translation of complex scene data into Unreal-native formats, facilitating the elimination of manual data entry for vertex positions, bone hierarchies, and animation keyframes.

Practical Usage Tips and Best Practices
1. Standardize on FBX 2020.2

Unreal Engine currently utilizes the FBX 2020.2 version. When exporting from your DCC tool, ensure your exporter settings match this version. Using older or newer versions can lead to data corruption, and standardizing your pipeline assists in the elimination of “Incompatible Version” warnings during import.

2. Centralize Pivot Points at the Origin (0,0,0)

The FBX module treats the DCC world origin as the mesh’s pivot point in Unreal. Before exporting, move your geometry so that the desired pivot point sits at 0,0,0 in your 3D software. This practice ensures the elimination of offset issues when rotating or snapping actors in the level editor.

3. Triangulate Before Export

While Unreal can triangulate meshes during import, it is a best practice to triangulate them within your DCC tool first. This gives you full control over the edge flow and prevents the engine from creating long, thin triangles, leading to the elimination of shading artifacts and lighting seams.

4. Use “Export Selected” to Reduce Bloat

DCC files often contain hidden cameras, lights, and construction history. Always use the “Export Selected” function rather than saving the whole scene to FBX. This minimizes the file size and facilitates the elimination of “Unexpected Object Type” errors during the Unreal import process.

5. Bake Animations and Remove Constraints

The FBX module cannot interpret live constraints (like IK handles or parent constraints) from 3D software. You must Bake Animation in your DCC tool to convert these into keyframes on the joints. This is essential for the elimination of broken or static character movements once the file reaches the engine.

6. Name Materials to Match Textures

The FBX importer can automatically create materials and assign textures if they follow a consistent naming convention. Naming your material slots in the FBX file to match your intended Unreal Material Instances leads to the elimination of time-consuming manual assignment after every re-import.

7. Enable Smoothing Groups

Ensure that Smoothing Groups (or “Treated Normals”) are enabled in your FBX export settings. Without this, the FBX module may interpret the mesh as entirely flat-shaded or faceted. Correct normal data is vital for the elimination of hard edges on organic or curved surfaces.

8. Utilize the “Combine Meshes” Option

If your FBX contains multiple separate objects that should be a single asset, check the Combine Meshes box in the Unreal Import Options. This reduces draw calls and assists in the elimination of a cluttered Content Browser filled with hundreds of tiny individual sub-meshes.