---
layout: default
title: OpenVDB
---

<!-- ai-generation-failed -->

<h1>OpenVDB</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/OpenVDB/OpenVDB.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">Boost, IntelTBB</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

y Award-winning OpenVDB library, a hierarchical data structure designed to manage sparse volumetric data. It is the industry standard for storing and manipulating voxels that do not fill a uniform grid (like smoke, clouds, fire, or liquid).

In Unreal Engine 5, this module is the backbone of the Sparse Volume Texture (SVT) system and Heterogeneous Volumes. It allows the engine to import .vdb files from external DCC tools (like Houdini or EmberGen) and convert them into a format that can be rendered efficiently in real-time or via the Path Tracer.

Practical Usage Tips and Best Practices
1. Optimize Attributes on Import

VDB files often contain many “grids” or attributes (density, temperature, velocity, etc.) that may not all be needed for your scene.

Best Practice: Only import the specific channels required for your material. For example, if you only need smoke, import “density.” Eliminating unused channels like “temperature” or “internal_data” during the import process significantly reduces the memory footprint on the GPU.
2. Choose the Correct Bit-Depth (8-bit vs. 16-bit)

The OpenVDB importer allows you to map attributes to different bit-depths.

Tip: Map high-frequency data like “Density” to 8-bit unorm if the range is 0 to 1, and use 16-bit float for data requiring higher precision like “Velocity” or “Temperature.” This helps you eliminate visual banding while maintaining a low memory profile.
3. Utilize “Pivot at Centroid”

VDB files are often authored with a pivot point at the corner of the bounding box (the origin).

Action: When importing a VDB into a Sparse Volume Texture, check the Pivot at Centroid box. This centers the pivot within the volume, making it much easier to rotate and scale the volume inside the level, eliminating the frustration of offset transforms.
4. Use for Animated VDB Sequences

The OpenVDB module supports importing a series of files (e.g., fire_001.vdb, fire_002.vdb) as a single Animated Sparse Volume Texture.

Best Practice: Ensure your file sequence is numbered sequentially. The importer will automatically detect the sequence. Using an animated SVT instead of a standard flipbook helps you eliminate the “flat” look of 2D sprites and provides true 3D depth to your simulations.
5. Sample with SVT Parameter Nodes

To use the data processed by the OpenVDB module in a material, you must use a specific sampling node.

Action: Use the Sparse Volume Texture Sample node (or SVT Parameter for animated versions) in a Volume Domain material. Mapping the local position to the volume’s UVs helps you eliminate coordinate-space errors, ensuring the voxels appear correctly aligned with the Actor’s bounds.
6. Leverage Mip-Levels for Performance

Sparse Volume Textures generated from OpenVDB data support mip-mapping just like 2D textures.

Tip: The SVT system automatically streams lower-resolution mips when the camera is far away. In your material, you can explicitly sample coarser mips for background elements. This helps you eliminate GPU performance bottlenecks in scenes with many volumetric effects.
7. Combine with Heterogeneous Volume Actors

Once your VDB is imported as an SVT, it is best displayed using the Heterogeneous Volume component.

Action: Assign your volume material to a Heterogeneous Volume Actor. This actor is optimized for sampling sparse data, helping you eliminate the light-leaking and artifacts often found when using standard volumetric fog for dense simulations.
8. Verify Data with the “Source File Grid Info”

Sometimes a VDB file appears empty after import because the grid names don’t match what the engine expects.

Tip: Look at the Source File Grid Info in the import window. It lists the exact names of the grids found in the .vdb file. Matching your “Attribute” mapping to these specific names helps you eliminate the issue of “invisible” volumes caused by naming mismatches.