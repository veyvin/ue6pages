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

standard Academy Software Foundation library used for volumetric data. It is primarily responsible for importing and processing .vdb files, which store sparse volumetric data like smoke, fire, clouds, and explosions.

In Unreal Engine 5.3+, this module powers the Sparse Volume Texture (SVT) system and Heterogeneous Volumes. It allows the engine to convert massive, sparse voxel grids into a format that can be efficiently streamed and rendered on the GPU. By leveraging this module, you can eliminate the need for traditional “Flipbook” textures or dense 3D textures, enabling high-fidelity, cinematic volumetric effects that can be scrubbed in Sequencer.

Practical Usage Tips and Best Practices
Optimize Bit Depth on Import
When importing VDBs, the module allows you to choose between 8-bit, 16-bit, and 32-bit formats. For most smoke and fire effects, 8-bit unorm is sufficient for density. Using the lowest acceptable bit depth helps you eliminate unnecessary VRAM consumption and improves streaming performance.
Filter Unused VDB Grids
VDB files often contain multiple “grids” (e.g., density, temperature, velocity, flame). Use the import settings to only map the grids you actually need for your material. This practice helps you eliminate data bloat in your project and keeps the SVT asset size manageable.
Use the SVT Parameter Node in Materials
To sample the data provided by this module, use the Sparse Volume Texture Sample Parameter node in your material graph. This node is specifically designed to handle the page-table mapping of sparse data, helping you eliminate the visual artifacts or “black boxes” associated with sampling empty voxel space.
Enable Path Tracing for High-End Renders
For final cinematic output, use the Path Tracer. Ensure you set the console variable r.PathTracing.HeterogeneousVolumes 1. This module’s data is fully compatible with path-traced scattering and absorption, which helps you eliminate the approximations found in real-time volumetric fog.
Leverage SVT Streaming for Long Sequences
Animated VDB sequences can be massive. This module uses a streaming system similar to Virtual Texturing. In the Heterogeneous Volume Actor, ensure your playback settings are optimized to pre-fetch upcoming frames, which helps you eliminate “popping” or low-resolution frames during fast-moving sequences.
Combine with Niagara Fluids
You can cache Niagara Fluid simulations directly as SVTs via this module’s logic. This allows you to “bake” a complex real-time simulation and play it back as a static or animated asset, helping you eliminate the heavy CPU/GPU cost of re-simulating fluids every time the level loads.
Match VDB Grids to Material Attributes
During import, note which VDB grid (like density) is assigned to which RGBA channel in Attribute A or Attribute B. Correctly masking these channels in your material helps you eliminate logic errors where temperature data is accidentally used to drive opacity.
Properly Release Resources on Elimination
When an animated volume is no longer needed (the “elimination” of the actor from the scene), ensure the SVT asset is not being held in memory by a persistent material instance. This module relies on the streaming pool; freeing up these pages helps you eliminate “Out of Video Memory” errors in asset-heavy levels.