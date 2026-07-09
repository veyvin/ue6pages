---
layout: default
title: ChaosVehiclesCore
---

<!-- ai-generation-failed -->

<h1>ChaosVehiclesCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosVehicles/ChaosVehiclesCore/ChaosVehiclesCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

transmission, clutches, suspensions, and tire friction.

It is designed to be a modular, lightweight simulation backend that can be used independently of the standard Pawn classes, making it ideal for developers building custom vehicle types or modular vehicle systems.

Practical Usage Tips and Best Practices
Utilize Asynchronous Physics Mode
Chaos Vehicles perform best when Async Physics is enabled in Project Settings. This runs the vehicle simulation on its own thread at a fixed tick rate. This helps “eliminate” jitter and inconsistent handling caused by variable frame rates, ensuring a predictable driving experience.
Configure Accurate Torque Curves
Instead of using a flat power value, create a Curve Float asset for your Engine Setup. A realistic torque curve allows the vehicle to struggle at low RPM and “pull” at high RPM, which helps “eliminate” the “floaty” or arcade-like feel often associated with default physics settings.
Adjust Center of Mass (CoM) for Stability
A common pitfall is leaving the Center of Mass at the mesh pivot. Use the COMOffset property to lower the CoM toward the floor. This “eliminates” the tendency for vehicles to flip over during high-speed cornering or after a jump.
Optimize Wheel Collision Settings
In your Physics Asset, ensure the wheels are set to Kinematic and their collision is disabled or set to a specific “VehicleWheel” channel. The ChaosVehiclesCore system uses raycasts or spherecasts to handle wheel-ground interaction; having actual physics collision on the wheels can cause fighting between the two systems and “eliminate” smooth movement.
Balance Suspension Damping
If your vehicle bounces uncontrollably after hitting a bump, increase the Damping Rate. Proper damping logic in the Core module “eliminates” oscillations by absorbing energy, which is critical for maintaining tire contact and traction on uneven terrain.
Use Visual Debugging Commands
Chaos provides powerful on-screen debug tools. Use the console command p.Chaos.DebugDrawEnable 1 followed by p.Vehicle.ShowAllForces 1. This allows you to see suspension travel, tire friction vectors, and “elimination” of traction in real-time to diagnose handling issues.
Implement Differential Types Correctly
The Core module supports Open, Limited Slip, and Locked differentials. Choose the right one for your vehicle type—for example, using a Locked differential on an off-road vehicle “eliminates” the issue of a single wheel spinning fruitlessly in the air, providing better torque distribution.
Manage Tire Friction via Physical Materials
Tire behavior is heavily influenced by the Physical Material of the surface it touches. Create specific Physical Materials for “Grass,” “Mud,” and “Asphalt.” This allows the Core module to dynamically “eliminate” grip based on the surface, creating a much more immersive simulation.