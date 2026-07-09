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

utility that converts complex, multi-node Material graphs into flat, performant 2D textures. It “flattens” logic—such as math expressions, procedural noise, and layered textures—into standard image maps (BaseColor, Normal, Roughness, etc.).

This module is primarily used for optimization (reducing instruction counts), HLOD (Hierarchical Level of Detail) generation, and preparing assets for export to platforms or formats that do not support Unreal’s proprietary shading language (such as glTF, USD, or mobile devices).

Practical Usage Tips & Best Practices
1. Use “Use Mesh Data” for World-Space Logic

If your material uses nodes like WorldPosition, VertexColor, or ObjectOrientation, a simple plane bake will result in incorrect textures.

Best Practice: In the Material Baking Options, enable Use Mesh Data. This ensures the baker samples the material specifically as it appears on the target geometry, leading to the elimination of “flat” or “broken” procedural effects that rely on the mesh’s 3D volume.
2. Handle UDIMs via UV Offsets

By default, the Material Baker typically only processes the 0-1 UV space (UDIM 1001).

Tip: To bake UDIMs, you must manually offset your material’s UV coordinates by 1.0 unit for each tile and perform separate bakes. This workaround facilitates the elimination of data loss for high-fidelity assets that utilize multi-tile UV layouts.
3. Proactive “Elimination” of View-Dependent Nodes

The baker captures a static snapshot of the material. Nodes like Fresnel, CameraVector, or SceneColor cannot be accurately baked because they change based on player movement.

Best Practice: Before baking, simplify your graph to remove or constant-bias any view-dependent logic. This ensures the elimination of black spots or “hallucinated” reflections in your final baked texture.
4. Optimize Resolution per Channel

Not every texture channel requires a 4K resolution. Baking everything at maximum size creates massive memory overhead.

Tip: Use the per-channel resolution overrides in the Baking Options. For example, bake BaseColor at 2048x2048 but bake Roughness or Ambient Occlusion at 1024x1024. This leads to the elimination of wasted VRAM while maintaining visual quality where it matters most.
5. Verify the “Blend Mode” for Opacity

Baking a masked or translucent material into an Opaque material will cause your transparency to turn black or white.

Best Practice: Set the Output Blend Mode in the baker settings to match your source material. If you need an alpha channel, ensure you are baking the Opacity or OpacityMask channel into the texture’s alpha, resulting in the elimination of “hard-edged” black boxes around your transparent assets.
6. Leverage for Mobile Instruction Reduction

Complex materials with dozens of texture samples and heavy math can cause performance drops on mobile GPUs.

Tip: Use the Material Baker to consolidate 5-10 texture samples into a single “Packed” texture (e.g., RGB = Mask1, Mask2, Mask3). This results in the elimination of high sampler counts, which is a common bottleneck on mobile hardware.
7. Fixup Redirectors After Saving Baked Assets

When you “Bake Out Materials,” the engine creates transient assets that must be saved to your Content folder.

Best Practice: After saving the new textures and materials, right-click your folder and select Fixup Redirectors. This ensures the elimination of broken file paths when moving the newly baked assets into your final production folders.
8. Use for glTF and USD Export Prep

External 3D software cannot interpret Unreal’s .uasset material graphs.

Tip: If you are exporting a character or environment to another DCC tool, run the Material Baker first. Converting the graph to standard textures ensures the elimination of “missing material” errors when the asset is opened in Maya, Blender, or Omniverse.