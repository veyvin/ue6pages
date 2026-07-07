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

t runtime, ensuring that the engine can interact with different simulation backends without being hard-coded to a specific implementation.

This module is primarily used by developers to access cloth simulation data, manage clothing assets on actors, and provide a foundation for custom cloth solver integrations.

Practical Usage Tips and Best Practices
1. Include Module Dependencies

To interact with clothing assets or simulation states in C++, you must include this module in your Build.cs. Because it is an interface module, it is lightweight and safe to include in both runtime and editor modules:

C#
PublicDependencyModuleNames.AddRange(new string[] { "ClothingSystemRuntimeInterface" });
Copy code
2. Accessing the Simulation via IClothingSimulation

When you need to interact with a running cloth sim, use the IClothingSimulation interface. This allows you to perform tasks such as updating simulation wind, gravity, or custom forces. Accessing the simulation through this interface ensures the elimination of hard dependencies on a specific solver like Chaos.

3. Manage Cloth Assets via UClothingAssetBase

All clothing data—including physical properties, masks, and weight maps—derives from UClothingAssetBase. If you are building a system to dynamically swap character outfits, you should store and pass references using this base class to maintain compatibility across different types of clothing assets.

4. Optimize via Simulation Frequency

Use the interface settings to control the simulation step. High-frequency updates provide better collision but are expensive. For background characters, use the interface to lower the simulation rate, leading to the elimination of wasted CPU cycles on cloth that isn’t central to the player’s view.

5. Handle Clothing Teleports

When a character is instantly moved across a level, the cloth simulation may “stretch” or glitch. Use the ForceNextUpdateTeleportAndReset() method provided by the clothing systems. This results in the elimination of unsightly physics artifacts by resetting the cloth particles to their skinned positions instantly.

6. Use Clothing Interactors for Runtime Changes

For UE 5.5 and later, use the Clothing Interactors (derived from UClothingInteractor) to modify simulation parameters like “Lift” or “Drag” at runtime. This allows gameplay events (like a character entering a high-wind area) to procedurally adjust the cloth behavior without recreating the entire simulation state.

7. Debugging with “SkeletalMesh.DisplayCloth”

The interface supports engine-wide debug commands. Use SkeletalMesh.DisplayCloth 1 to visualize the simulation mesh, particles, and constraints. This is the most effective way to identify if a simulation failure is due to bad skinning or incorrect physical constraints, allowing for the quick elimination of authoring errors.

8. Verify Physics Asset (PhAT) Collisions

Cloth simulation relies on the Physics Asset assigned to the Skeletal Mesh. Ensure that the collision capsules in the PhAT are properly sized. Overlapping or inverted capsules can cause the solver to “explode,” so use the runtime interface’s visualization tools to ensure the elimination of collision volumes that interfere with the cloth’s rest state.