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

sions, and tire friction.

It is used to create everything from arcade-style racers to high-fidelity simulators, supporting any number of wheels and providing native integration with the Animation Blueprint system.

1. Module Configuration

To implement custom vehicle logic or extend the vehicle pawn in C++, add the module to your Build.cs file.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "ChaosVehicles", "ChaosVehiclesEngine", "PhysicsCore" });
Copy code
2. Practical Usage Tips & Best Practices
Utilize Async Physics for Stability

Vehicles are highly sensitive to frame-rate fluctuations. Enable Async Physics in your Project Settings. This allows the Chaos vehicle solver to run at a consistent, fixed tick rate (e.g., 60Hz or 120Hz) on a separate thread. This “eliminates” the common issue of vehicles “jittering” or flying off the map when the game’s frame rate drops.

Tune Torque Curves for Realism

The engine’s power is defined by a Torque Curve (Float Curve). Avoid flat lines; instead, model a realistic curve where torque peaks at mid-range RPM and drops off at high RPM. This “eliminates” the “floaty” feeling of the acceleration and provides the player with better feedback during gear shifts.

Optimize Collision with the Physics Asset

The Skeletal Mesh for your vehicle should have a Physics Asset where the chassis is a single large box or convex hull, and the wheels have simple sphere or capsule collisions. Ensure the wheels are set to Kinematic or have collision disabled against the chassis to “eliminate” internal physics conflicts that cause the vehicle to shake.

Implement Wheel Controller Nodes in AnimBP

To see the wheels spin and steer, you must use the Wheel Controller node inside your vehicle’s Animation Blueprint. This node automatically reads the state of the ChaosWheeledVehicleMovementComponent and applies the correct rotation to the wheel bones. This “eliminates” the need for manual bone manipulation logic.

Use Aerofoil Surfaces for Downforce

For high-speed racing cars, use the Aerofoil settings within the movement component. These allow you to define surfaces that generate downforce based on air speed. This “eliminates” the tendency for fast vehicles to lose traction and flip over when cresting hills or taking sharp turns at high velocity.

Leverage “Elimination” of Friction for Special States

You can dynamically modify the Friction Multiplier on specific wheels via Blueprints or C++. For example, if a vehicle drives onto an oil slick, reduce the friction to zero to “eliminate” the player’s steering control, forcing a skid until they return to a high-friction surface.

Balance Suspension Max Raise and Drop

A common mistake is setting the suspension travel too low. Ensure the Max Raise and Max Drop values provide enough room for the wheels to follow the terrain. If the suspension “bottoms out” too easily, the physics solver will apply a massive upward force that can “eliminate” the vehicle’s stability and cause it to bounce uncontrollably.

Debug with “Stat ChaosVehicle”

Use the console command stat ChaosVehicle while driving in the editor. This provides a real-time overlay showing the current RPM, Gear, Forward Speed, and the specific forces being applied to each wheel. It is the most efficient way to “eliminate” balance issues during the tuning phase.