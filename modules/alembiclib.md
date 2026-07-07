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

for the Alembic SDK integration within Unreal Engine. It is responsible for parsing and processing .abc files, which are used to bring complex, baked vertex animations and simulations from DCC tools (like Houdini, Maya, or Blender) into the engine.

While the AlembicImporter module handles the high-level Editor UI and asset creation, AlembicLib manages the low-level data extraction required to generate GeometryCache, SkeletalMesh, or StaticMesh assets.

Practical Usage Tips & Best Practices
1. Module Dependency Setup

If you are developing custom C++ tools to automate the processing of cache data or building a procedural importer, you must include AlembicLib in your Build.cs. Because this is almost always an editor-side operation, wrap it in a target check:

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "AlembicLib", "AlembicLibrary" });

	}

	```

	 

	#### 2. Respect the Polygon Constraint

	Alembic assets in Unreal Engine strictly support **three and four-sided polygons**. If your source geometry contains N-gons (polygons with >4 sides), the `alembiclib` parser will fail to load the data correctly. Always triangulate or quadrangulate your mesh in your DCC (Maya/Houdini/Blender) before export.

	 

	#### 3. Use Face Sets for Material ID Mapping

	`alembiclib` uses **Face Sets** to determine Material Slots. In Maya, ensure you assign materials at the **component (face) level** rather than the object level. If materials are assigned at the object level, the importer treats the entire mesh as a single material slot. Enable "Write Face Sets" in your Alembic export settings to ensure this data is preserved.

	 

	#### 4. Choose the Right Import Type (CPU vs GPU)

	The way `alembiclib` data is processed depends on the import method:

	*   **Geometry Cache:** Read via the **CPU**. Best for complex, non-topologically stable simulations, but expensive for large crowds.

	*   **Skeletal Mesh (Morph Targets):** Processed via the **GPU**. This is significantly more performant for high-instance counts (like a field of grass or a crowd) but requires the animation to be compressed into morph targets.

	 

	#### 5. Coordinate Space Correction

	Alembic files often use different coordinate systems (e.g., Y-Up vs. Unreal's Z-Up). When using the `alembiclib` API or the importer, ensure you set the correct **Conversion Preset** (e.g., Maya, Max) to avoid having your mesh imported sideways or mirrored.

	 

	#### 6. Enable UV Write and Write Color Sets

	By default, some DCC exporters do not include UV or Vertex Color data in the Alembic stream to save space. To ensure `alembiclib` can reconstruct your materials correctly, you must explicitly enable **UV Write** and **Write Color Sets** during the export process.

	 

	#### 7. Leverage the Experimental Streaming Plugin

	For massive caches that exceed memory limits, use the **Geometry Cache from Alembic** plugin (which utilizes `alembiclib` internally). This allows the engine to stream portions of the cache from disk instead of loading the entire asset into memory, which is essential for long-form cinematic sequences.

	 

	#### 8. Vertex Animation Textures (VAT) Fallback

	If `alembiclib` processing becomes a bottleneck in your project, consider using the **AnimToTexture** plugin. This bakes the Alembic vertex data into textures, allowing the GPU to handle the animation entirely via a Material's World Position Offset (WPO), bypassing the need for complex cache playback at runtime.
Copy code
2. Strict Polygon Constraints

The AlembicLib parser strictly supports three and four-sided polygons. If your source file contains N-gons (polygons with more than 4 sides), the import will fail or produce corrupted geometry. Always triangulate your mesh in your DCC before exporting to ensure the engine can read the indices correctly.

3. Material Assignment via Face Sets

The module uses Face Sets to define material IDs. In your DCC, you must assign materials at the component (face) level rather than the object level. Ensure “Write Face Sets” is enabled in your exporter settings; otherwise, the engine will combine the entire cache into a single material slot, making it difficult to eliminate visual artifacts on complex models.

4. Choose Performance: CPU vs. GPU

The way the library data is used at runtime depends on the asset type:

Geometry Cache: Data is processed by the CPU. This is flexible for changing topology but can be heavy for performance.
Skeletal Mesh: Data is converted into Morph Targets and processed by the GPU. This is significantly more efficient for playback, especially when many instances of the same animation are on screen.
5. Coordinate System Alignment

Alembic files often use different orientations (e.g., Y-Up vs. Unreal’s Z-Up). Use the Conversion Preset settings during import to ensure AlembicLib applies the correct rotation and scale. Incorrect settings often result in models being mirrored or imported sideways.

6. Leverage Streaming for Large Files

For massive files that cannot fit into memory, enable the Geometry Cache from Alembic plugin. This utilizes AlembicLib to stream the cache data directly from the disk rather than loading it as a standard .uasset. This is a best practice for long-form cinematic content where memory budgets are tight.

7. Verify UV and Color Set Export

By default, some exporters omit UVs or Vertex Colors to reduce file size. To ensure the library can properly reconstruct the look of your mesh, verify that UV Write and Write Color Sets are enabled in the export dialog of your DCC. Without these, the resulting engine asset will lack texture coordinates.

8. Vertex Animation Texture (VAT) Alternative

If the overhead of a full Alembic cache is too high for your gameplay needs, use the AnimToTexture plugin. This bakes the data parsed by AlembicLib into textures, allowing the GPU to drive the animation via a material’s World Position Offset. This is the most performant way to handle hundreds of animated objects, such as a field of flowers or a crowd.