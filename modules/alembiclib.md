---
layout: default
title: AlembicLib
---

<!-- ai-generation-failed -->

<h1>AlembicLib</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Alembic/AlembicLib.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">Imath</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

terchange format in Unreal Engine. It serves as the bridge between the open-source Alembic framework and the engine’s internal data structures, allowing high-fidelity, baked vertex animations and complex simulations to be brought into the real-time environment.

What it is and What it’s used for

AlembicLib provides the underlying libraries and parsers required to read baked geometric results from Digital Content Creation (DCC) tools like Houdini, Maya, or Blender. Unlike FBX, which typically uses bones and skinning, AlembicLib processes vertex-level transformations. It is used for:

Complex Simulations: Bringing in fluid, cloth, or destruction sims that are too heavy to calculate in real-time.
Geometry Caches: Playing back meshes with changing topology or high-density vertex movement.
Cinematics: Importing high-fidelity character performances where traditional skeletal animation may lack the required precision.
Practical Usage Tips and Best Practices
1. Choose the Correct Import Type

AlembicLib supports three distinct import paths. Select based on your performance budget:

Static Mesh: Imports a single frame as a standard mesh.
Geometry Cache: Best for complex sims; plays back via the CPU.
Skeletal Mesh: Converts vertex animation into Morph Targets (processed on the GPU). Use this for better performance if the mesh topology is constant.
2. Triangulate and Clean Geometry

Unreal Engine only supports three- and four-sided polygons. Before exporting your cache, ensure you triangulate your mesh or ensure it consists strictly of quads. Geometry containing N-gons (polygons with more than 4 sides) will cause the AlembicLib parser to fail or produce visual artifacts.

3. Use “Write Face Sets” for Material IDs

If you need multiple materials on a single Alembic cache, ensure “Write Face Sets” (in Maya) or equivalent attributes are enabled during export. AlembicLib uses these sets to generate Material Slots in Unreal Engine; otherwise, the entire cache will be treated as a single material element.

4. Account for Scale Differences

DCC tools often use different unit scales (e.g., Houdini uses meters, while Unreal uses centimeters). A common best practice is to apply a scale factor of 100.0 during the export or within the Alembic Import Options to ensure your simulation isn’t microscopic upon arrival.

5. Optimize Vertex Counts for Real-Time

While AlembicLib can handle massive files, Geometry Caches are memory-intensive. For real-time applications, aim to keep your vertex count under 1 million per frame. If a simulation is too heavy, use an “Adaptive Remesh” or “Decimation” pass in your DCC tool before exporting to eliminate unnecessary geometric density.

6. Enable the Experimental Streaming Plugin

For exceptionally large caches that do not fit in RAM, enable the Geometry Cache from Alembic plugin. This allows the engine to stream the data from the disk rather than loading the entire .uasset into memory, which is essential for long-duration cinematic backgrounds.

7. Bake Vertex Attributes Carefully

To keep file sizes manageable, only export the attributes you absolutely need (typically Position, UVs, and Normals). Avoid exporting velocity or custom color attributes unless your materials specifically use them for effects like motion blur or vertex-driven masking, as these significantly bloat the cache size.

8. Utilize the Geometry Cache Track in Sequencer

To synchronize your Alembic animation with your scene, add the Geometry Cache Actor to a Level Sequence. Add a Geometry Cache Track to the actor to gain frame-accurate control over playback, start offsets, and play rates, ensuring the simulation aligns perfectly with your cinematic timing.