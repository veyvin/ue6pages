---
layout: default
title: Itoo
---

<!-- ai-generation-failed -->

<h1>Itoo</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/ThirdParty/Itoo/Itoo.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine’s Datasmith ecosystem, specifically designed to handle assets exported from iToo Software’s popular 3ds Max plugins: Forest Pack and RailClone.

Description and Purpose

The itoo module provides the translation logic required to convert complex, procedurally scattered data from 3ds Max into highly optimized Unreal Engine Actors. When a scene containing Forest Pack or RailClone objects is imported via Datasmith, this module interprets the scattering metadata and reconstructs the scene using Hierarchical Instanced Static Mesh (HISM) components. This ensures that even scenes with millions of scattered trees, rocks, or architectural elements remain performant by leveraging the engine’s built-in foliage technology and instanced rendering, rather than importing each instance as a unique, memory-heavy actor.

Practical Usage Tips and Best Practices
Leverage HISM for Performance
The module automatically converts scattered objects into HISM components. This is critical for performance because it allows the engine to batch all instances into a single draw call per material. Using this module helps you eliminate the massive CPU overhead associated with managing thousands of individual Static Mesh Actors.
Replace Geometry with the “Bounding Box Only” Setting
In 3ds Max, you can apply a Datasmith Attributes Modifier to an iToo object and set it to “Export Bounding Box Only.” Upon import, the itoo module will create the instances using simple boxes. You can then swap the Static Mesh in the HISM component for a high-quality Unreal asset (like a Megascans tree) to eliminate the need for importing heavy geometry from 3ds Max.
Synchronize via Datasmith Direct Link
The itoo module supports the Datasmith Direct Link workflow. If you adjust the scattering density or distribution in 3ds Max, you can sync the changes to Unreal without a full re-import. This allows you to eliminate the time-consuming process of manually re-placing assets whenever the scene design changes.
Manage Large-Scale Culling via Per-Instance Fade
Because the module utilizes HISMs, you can take advantage of the “Start/End Cull Distance” settings in the component’s details panel. Setting these distances properly helps you eliminate unnecessary GPU rendering of distant scattered objects that are not visible to the player.
Convert to Foliage Mode for Manual Editing
If you need to manually tweak the placement of imported iToo objects, you can use the Actor to Foliage tool. Converting the HISM instances into the Foliage system allows you to use the Foliage brush to add or eliminate specific instances with more artistic control than the procedural importer provides.
Check Material Assignments Post-Import
Forest Pack objects often use “Multi/Sub-Object” materials in 3ds Max. The itoo module attempts to translate these into multiple material slots on the HISM. Always verify that your Unreal materials are correctly assigned to these slots to eliminate visual glitches where the wrong texture is applied to your scattered instances.
Use Data Layers for Complex Biomes
When importing massive amounts of iToo data, use Data Layers to organize the resulting Actors. You can place different biomes (e.g., “Forest_Floor” and “River_Rocks”) on separate layers. This allows you to toggle visibility in the editor, helping you eliminate viewport lag while working on unrelated parts of the level.
Verify Pivot Points in 3ds Max
The itoo module relies on the pivot point of the “source” object in 3ds Max. If your pivot is offset, all instances in Unreal will be misaligned. Ensuring your pivots are centered at the base of your objects before export is the best way to eliminate “floating” or “sunk” assets in your Unreal level.