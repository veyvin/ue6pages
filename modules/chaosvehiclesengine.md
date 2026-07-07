---
layout: default
title: ChaosVehiclesEngine
---

<!-- ai-generation-failed -->

<h1>ChaosVehiclesEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosVehicles/ChaosVehiclesEngine/ChaosVehiclesEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, ChaosVehiclesCore, Core, CoreUObject, Engine, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

core Chaos physics solver and the Unreal Engine Actor system. It provides the base C++ classes and components, such as UChaosWheeledVehicleMovementComponent, required to create driveable vehicles with complex suspension, engine, and transmission simulations.

This module replaces the legacy PhysX vehicle system and is used to handle everything from standard four-wheel cars to multi-axle tanks and experimental n-wheeled vehicles.

Practical Usage Tips and Best Practices
1. Configure the ChaosVehiclesPlugin

Before you can use this module in C++, you must ensure the ChaosVehiclesPlugin is enabled in your .uplugin or .project file. In your Build.cs, add the module dependency to access the movement component:

C#
PublicDependencyModuleNames.AddRange(new string[] { "ChaosVehicles", "ChaosVehiclesEngine" });
Copy code
2. Bone Orientation is Critical

For the vehicle physics to calculate correctly, your Skeletal Mesh joints must follow a specific convention: X-Forward and Z-Up. If your wheels are oriented differently, the suspension forces will apply in the wrong direction, leading to the elimination of your vehicle’s stability as it may flip or fly away upon spawning.

3. Disable Wheel Collision in Physics Assets

The ChaosWheeledVehicleMovementComponent handles wheel collision internally using raycasts or sphere traces. You must ensure that the collision bodies for the wheels in your Physics Asset are set to “No Collision” or “Query Only.” Failure to do this will cause the chassis to collide with its own wheels, preventing movement.

4. Use “WheelController” in AnimBlueprints

To visualize the physics simulation (steering, rotation, and suspension travel), you must use the WheelController node inside your vehicle’s Animation Blueprint. This node automatically reads the state from the movement component and applies it to the corresponding bones, ensuring the elimination of manual “per-wheel” animation logic.

5. Define an Accurate Torque Curve

The engine’s power is determined by a Runtime Float Curve. Ensure your curve starts at 0 RPM and covers the full range of your engine’s power band. Without a properly defined torque curve, the vehicle may lack the force to overcome friction, effectively resulting in the elimination of its ability to move from a standstill.

6. Leverage Async Physics for Determinism

In Project Settings, enable Async Physics for the most consistent vehicle handling. This allows the vehicle simulation to run at a fixed frequency (e.g., 60Hz or 100Hz) independent of the frame rate. This is essential for the elimination of “physics jitter” where vehicle behavior changes based on the player’s FPS.

7. Tune Suspension Dampening

A common mistake is setting high spring rates without enough dampening. Use the DampingRatio setting in your Wheel Blueprint to prevent the vehicle from bouncing uncontrollably. A well-tuned ratio (usually between 0.3 and 0.8) ensures the elimination of oscillating forces that make cars feel “floaty.”

8. Set Up “Sleep” Thresholds for Performance

To save CPU resources, configure the Sleep Thresholds in the vehicle component. When a vehicle is stationary and not being controlled, the physics solver should put it to “sleep.” This leads to the elimination of unnecessary computations for parked cars in a large open-world environment.