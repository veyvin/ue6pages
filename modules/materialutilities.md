---
layout: default
title: MaterialUtilities
---

<!-- ai-generation-failed -->

<h1>MaterialUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MaterialUtilities/MaterialUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ne designed for the high-level manipulation, baking, and flattening of Material graphs. It provides the underlying logic for converting complex, node-based materials into simplified, static textures and proxy materials.

This module is primarily used by the engine’s optimization tools, such as the Proxy Mesh generator and HLOD (Hierarchical Level of Detail) systems. By collapsing expensive shader logic into a few baked textures, it facilitates the elimination of draw call overhead and pixel shader complexity in large-scale environments.

Practical Usage Tips and Best Practices
1. Enable Module in Build.cs

Since MaterialUtilities is a developer-only module, it is not available in Shipping builds. When using its functions in custom editor tools, ensure it is added to your Editor.Build.cs file. This practice leads to the elimination of linker errors during the compilation of your editor-only plugins:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("MaterialUtilities");

	}
Copy code
2. Leverage for HLOD and Proxy Mesh Optimization

When generating HLODs for distant clusters of actors, the MaterialUtilities logic is responsible for merging multiple materials into a single atlas. Utilizing this module effectively facilitates the elimination of excessive state changes on the GPU, allowing the engine to render massive vistas with a single draw call.

3. Handle UDIM Limitations During Baking

As of current versions, standard Material baking may default to the 0-1 UV space. If your assets use UDIMs, you must manually apply a UV offset for each tile before baking. Understanding this limitation assists in the elimination of “Missing Texture” artifacts where only the first UDIM tile (1001) is correctly captured in the bake.

4. Check “Use Mesh Data” for Vertex Color

If your Material uses VertexColor or WorldPosition nodes, ensure the “Use Mesh Data” flag is enabled in the baking options. This allows the module to sample actual geometry data rather than a flat plane, which leads to the elimination of “Flat Gray” or “Black” textures that occur when mesh-specific nodes fail to resolve.

5. Bake Out Logic for “Elimination” of Shader Complexity

For mobile or VR projects where shader instruction counts are strictly limited, use the “Bake Out Materials” tool (powered by this module) to convert procedural noises or heavy math into textures. This facilitates the elimination of performance hitches caused by overdrawn or complex pixel shaders on low-end hardware.

6. Coordinate with the MaterialBaking Module

MaterialUtilities often works in tandem with the MaterialBaking module. While MaterialBaking handles the rendering of the textures, MaterialUtilities provides the utility functions to manage the resulting assets and material instances. Keeping both modules in your dependency list is a best practice for the elimination of “Missing Function” errors.

7. Monitor Output Resolution for Memory Savings

The module allows you to specify the resolution of baked textures (e.g., 512x512, 1024x1024). Always choose the lowest acceptable resolution for distant objects. Carefully managing these settings leads to the elimination of unnecessary VRAM bloat that occurs when many low-priority assets are baked at 4K resolution.

8. Use for Custom Editor Baking Tools

If you are building a custom tool to “flatten” materials for a marketplace asset or a specific pipeline, call FMaterialUtilities::ExportMaterial. This function automates the creation of a simplified material instance and its corresponding textures, which assists in the elimination of repetitive manual workflow steps for technical artists.