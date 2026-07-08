---
layout: default
title: ClothingSystemRuntimeInterface
---

<!-- ai-generation-failed -->

<h1>ClothingSystemRuntimeInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ClothingSystemRuntimeInterface/ClothingSystemRuntimeInterface.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Slate</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

solver being used (such as Chaos Cloth or the legacy NvCloth).

By using this interface, the engine can manage clothing assets, handle LOD transitions, and process skinning data without needing to know the low-level mathematical implementation of the cloth solver.

Practical Usage Tips and Best Practices
1. Module Dependency Management

When writing C++ code that needs to interact with clothing—such as checking if a character has cloth assets assigned or manually triggering a simulation reset—you must include ClothingSystemRuntimeInterface in your project’s .Build.cs file. This ensures you have access to the base UClothingAssetBase and IClothingSimulation classes.

2. Efficient Simulation Resetting

To prevent “stretched” cloth artifacts after a character teleports, do not simply wait for the physics to catch up. Use the interface to call a simulation reset. In C++, you can access the UClothingSimulationInteractor through the Skeletal Mesh Component to trigger a teleport/reset, ensuring the elimination of visual “streaking” across the map.

3. Optimize with Clothing LODs

The interface manages the transition between simulation and static skinning. In the Skeletal Mesh Editor, ensure you configure Clothing LODs. You can set the cloth to stop simulating at far distances, switching back to standard bone skinning. This is critical for the elimination of unnecessary CPU overhead in scenes with many background characters.

4. Shared Physics Assets for Collisions

The interface relies on the Physics Asset assigned to the clothing data for collision detection. For the best performance, create a specialized, simplified Physics Asset containing only essential capsules for the limbs. This ensures the elimination of complex collision checks that could degrade the frame rate.

5. Utilize Backstop to Prevent Clipping

When painting cloth weights, use the Backstop properties defined in the clothing asset. Backstop provides a spherical “safety zone” behind each vertex based on its animated position, effectively pushing the cloth away from the body. This is the most effective way to ensure the elimination of character mesh clipping during extreme animations.

6. Debugging via Console Commands

Because this is an interface module, you can use universal console commands to debug any solver implementing it. Use p.ClothPhysics 0 to globally disable all clothing simulations. This is useful for identifying if a performance drop is specifically caused by the cloth system, aiding in the elimination of performance bottlenecks.

7. Handle Clothing Data via Data Assets

The interface allows for the dynamic swapping of clothing data. If your game features a character customizer, treat clothing pieces as UClothingAssetBase pointers. This allows you to apply or remove clothing logic at runtime via the ApplyClothingAsset function on the Skeletal Mesh Component, leading to the elimination of rigid, non-customizable character setups.

8. Monitor Parallel Task Execution

Clothing simulations are typically offloaded to worker threads. Use Unreal Insights to verify that the ParallelClothTask is not bottlenecking your frame. If the task is taking too long, consider reducing the “Substeps” or “Iterations” in the specific cloth solver configuration to ensure the elimination of Game Thread stalls.