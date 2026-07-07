---
layout: default
title: SpeedTree
---

<!-- ai-generation-failed -->

<h1>SpeedTree</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/SpeedTree/SpeedTree.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

designed to handle the import, rendering, and animation of procedural foliage assets created in the SpeedTree modeler.

Description and Purpose

This module provides the necessary logic to interpret .st9 and legacy .st file formats, converting them into high-performance Static Meshes with specialized vertex data. Its primary purpose is to bridge the gap between SpeedTree’s procedural generation and Unreal’s rendering pipeline, specifically handling complex features like seamless LOD (Level of Detail) transitions and wind simulations. By using the SpeedTree module, the engine can eliminate the manual effort of setting up complex foliage shaders, as it automatically generates the required Material Instances and applies the SpeedTreeWind node for realistic movement.

Practical Usage Tips and Best Practices
Utilize the SpeedTreeWind Node
Inside the Material Editor, always use the SpeedTreeWind node to drive your foliage animation. This node is specifically optimized to read the vertex color data and wind weights exported from the SpeedTree modeler, helping you eliminate the jittery or “rubbery” look of generic sine-wave wind.
Implement World Position Offset (WPO) Culling
For large forests, set a WPO Disable Distance in your foliage settings or material. This allows the engine to stop calculating complex wind math for distant trees, which is essential to eliminate unnecessary GPU overhead while maintaining visual fidelity for close-up assets.
Choose Between “Simple” and “Pivot Painter” Wind
SpeedTree imports often offer multiple wind complexity levels. Use “Simple Wind” for background forests and reserve the high-fidelity “Pivot Painter” style for hero trees near the camera. This strategy helps you eliminate performance bottlenecks in densely vegetated scenes.
Leverage Seamless LOD Transitions
The module supports a unique “Smooth LOD” feature that morphs the geometry between detail levels. Ensure this is enabled in your SpeedTree asset settings to eliminate “popping” artifacts as the player moves through the environment.
Apply Color Variation via the Material
To make a forest look natural, use the PerInstanceRandom or ObjectRadius nodes within the generated SpeedTree material to slightly shift the hue of the leaves. This helps you eliminate the repetitive “stamped” look of using the exact same texture across hundreds of instances.
Optimize with Nanite (UE 5.1+)
With the introduction of Nanite Programmable Rasterizer, you can now use Nanite on SpeedTree assets with masked leaf materials. This allows you to eliminate traditional LOD management entirely, though you must still monitor the complexity of the World Position Offset math.
Audit Subsurface Scattering (SSS) Masks
SpeedTree assets usually import with a Subsurface mask to simulate light passing through leaves. Check these masks in the Material Instance; if the subsurface effect is too strong, it can cause the trees to glow unnaturally in shadows. Adjusting this helps you eliminate “radioactive” looking foliage.
Use the SpeedTree Importer for Billboards
When importing, the module can generate a “Billboard” mesh for the final LOD. Ensure your billboard textures are high-quality and match the lighting of the 3D mesh. This ensures you eliminate a harsh visual break when the tree transitions to a 2D sprite at long distances.