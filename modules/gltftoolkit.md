---
layout: default
title: gltfToolkit
---

<!-- ai-generation-failed -->

<h1>gltfToolkit</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/glTF-Toolkit/gltfToolkit.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

igned to handle the high-fidelity interchange of 3D assets using the glTF 2.0 (GL Transmission Format) standard. It provides the underlying logic for exporting Unreal Engine content—such as Static Meshes, Materials, and Level Sequences—into a format compatible with external web viewers, DCC tools (like Blender), and Fab. It is specifically optimized for Material baking and the translation of Unreal’s PBR (Physically Based Rendering) properties into the glTF schema.

Practical Usage Tips & Best Practices
1. Utilize glTF Proxy Materials for Runtime Exports

At runtime, Unreal Engine cannot perform full Material baking. If your project requires users to export assets during a live session, you must prepare “Proxy Materials.”

Best Practice: Create a simplified version of your Material and assign it as a GLTF Proxy Material in the Asset User Data. This ensures the elimination of “gray-box” exports, as the system will use these pre-baked proxies instead of trying to compile shaders on the fly.
2. Choose “Simple” vs. “Mesh Data” Baking Modes

The toolkit offers two primary ways to bake Materials into textures: “Simple” and “Use Mesh Data.”

Tip: Use Simple mode for tiled textures to preserve UV tiling. Use Mesh Data mode if your Material relies on vertex colors or world position. Choosing the correct mode leads to the elimination of visual discrepancies where baked textures appear stretched or incorrectly aligned on the model.
3. Override Default Input Bake Settings

By default, the glTF exporter might bake every texture at a generic resolution (e.g., 1024x1024), which is often overkill for Roughness maps but too low for Base Color.

Best Practice: Use the Default Input Bake Settings in the GLTF Export Options to set per-input resolutions and filter types. This results in the elimination of wasted memory and disk space by optimizing the size of each individual texture map.
4. Leverage the GLTFBuilder API in C++

For advanced developers, the GLTFBuilder class allows you to manually construct a glTF scene programmatically before saving it to disk.

Tip: Use the builder to inject custom metadata or glTF extensions into the file. This allows for the elimination of external post-processing steps, as you can tailor the exported file structure directly within your Unreal C++ pipeline.
5. Verify Exports with the “Preview” Feature

Before batch-exporting hundreds of assets for a platform like Fab, you can see how the toolkit will interpret your Unreal assets.

Best Practice: Use the Create GLTF Proxy Material right-click action in the Content Browser to generate a preview. This facilitates the elimination of trial-and-error by showing you exactly how the Material inputs will be compressed and packed before you finalize the export.
6. Optimize via Texture Channel Packing

The glTF standard expects specific maps, such as the Metallic-Roughness-Occlusion (ORM) map, to be packed into the R, G, and B channels of a single texture.

Tip: Ensure your Unreal Materials are set up to provide these inputs clearly to the exporter. The toolkit’s ability to auto-pack these channels ensures the elimination of redundant texture samplers in the target application, improving web and mobile performance.
7. Control Animation Sampling Rates

When exporting ALevelSequence or UAnimSequence assets, the toolkit must “bake” the curves into discrete keyframes.

Best Practice: Adjust the Frame Rate setting in the export options to match your target platform’s needs. This assists in the elimination of “choppy” animations (if the rate is too low) or excessive file sizes (if the rate is unnecessarily high).
8. Implement Safe “Elimination” of Temporary Export Data

The toolkit often generates transient textures and temporary files during the baking process which can clutter your project’s intermediate folders.

Tip: When using the C++ API, ensure you are calling the appropriate cleanup functions on the FGLTFExporter object. Proper cleanup ensures the elimination of “phantom” assets and build-cache bloat in your local development environment.