---
layout: default
title: ClothingSystemRuntimeNv
---

<!-- ai-generation-failed -->

<h1>ClothingSystemRuntimeNv</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ClothingSystemRuntimeNv/ClothingSystemRuntimeNv.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Understand Its Legacy Status
Recognize that ClothingSystemRuntimeNv is no longer the primary focus for Epic’s development. New features, such as Machine Learning Cloth and enhanced wind interactions, are built specifically for Chaos. If you are starting a new project, you should eliminate the use of NvCloth in favor of Chaos Cloth to ensure long-term support.
Use for Legacy Asset Migration
If you are upgrading a UE4 project to UE5, this module allows your existing cloth assets to function without immediate re-authoring. You can verify the simulation in the Skeletal Mesh Editor; however, consider this a “bridge” solution while you plan a migration to the Chaos system.
Monitor Performance with Stat Commands
Use the console command stat cloth to see the performance cost of the NvCloth simulation. Because this module runs on a separate task system, you can see how much time is spent on the “Cloth Task.” If the cost is too high, you must eliminate high-density vertex counts in your simulation meshes.
Configure Max Physics Delta Time
NvCloth can become unstable at low frame rates. If you notice cloth “exploding” or jittering during a frame drop—such as during a complex player elimination effect—adjust the p.Cloth.MaxDeltaTimeTeleportMultiplier console variable to force a teleport instead of an unstable simulation.
Optimize via “Remove from Mesh”
In the Clothing properties of your Skeletal Mesh, ensure you use the “Remove from Mesh” option for your simulation source. This allows the worker to eliminate the rendering overhead of the simulation mesh itself, using it only to drive the visual “render mesh” through skinning.
Avoid Mixing Solvers on One Character
While it is technically possible to have multiple cloth assets, you should eliminate the practice of mixing NvCloth and Chaos Cloth assets on a single character. This can lead to conflicting physics states and unnecessary memory overhead as the engine would have to initialize two different physics runtimes.
Set Gravity and Wind Scales
NvCloth settings for gravity and wind often feel different than Chaos. If you are stuck using this module, ensure you tune the “Wind Adaptation” and “Gravity Scale” within the Clothing Asset to match your world settings. Improper scaling is a leading cause of “floaty” cloth that you should eliminate through testing.
Utilize for Platform-Specific Performance
In some very specific edge cases on older hardware, the NvCloth solver may still show slightly different performance characteristics. If you must use it, use Device Profiles to toggle cloth simulation on or off, ensuring that the simulation is eliminated on low-end mobile devices to maintain a stable frame rate.