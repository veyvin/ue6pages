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

le acts as the bridge between the low-level Chaos physics solver and the Unreal Actor system. It manages the simulation of engines, transmissions, torque curves, steering, and suspension. It is the modern replacement for the legacy PhysX-based WheeledVehicle module, offering more robust stability and support for any number of wheels.

Practical Usage Tips and Best Practices
1. Use the Correct Pawn and Component

To build a vehicle, your Blueprint class must derive from WheeledVehiclePawn. This base class automatically includes the ChaosVehicleMovementComponent, which is where you configure the specific physics properties like mass, drag, and engine torque.

2. Implement a Smooth Torque Curve

A vehicle’s performance is driven by its Torque Curve (a Float Curve asset). Ensure your curve starts at a realistic RPM (e.g., 800–1000) and peaks appropriately. A poorly defined curve can lead to the elimination of driveability, causing the vehicle to stall or have unrealistic acceleration.

3. Enable Asynchronous Physics

For the most stable vehicle simulation, especially at high speeds, enable Tick Async Physics in your Project Settings. This allows the vehicle solver to run on its own thread at a fixed interval, ensuring the elimination of jitter and “vibrating” wheels caused by variable frame rates.

4. Setup the Animation Blueprint with WheelController

Vehicles require a specific Animation Blueprint. You must use the Wheel Controller node in the AnimGraph. This node automatically handles the rotation and suspension offset of the wheels based on the data provided by the ChaosVehicleMovementComponent, ensuring the elimination of manual bone rotation logic.

5. Tune Suspension Forces Carefully

Suspension is often the cause of “flipping” vehicles. Adjust the Suspension Max Raise/Drop and Spring Rate to match the vehicle’s mass. If the springs are too stiff, hitting a small bump can lead to the total elimination of traction as the vehicle is launched into the air.

6. Optimize Collision in the Physics Asset

The Physics Asset (PhAT) for your vehicle should have a simple box or convex hull for the chassis. Never enable collision for the wheel bones in the Physics Asset; instead, let the ChaosVehicleMovementComponent handle wheel collisions via its raycast/shapecast system to avoid the elimination of stable movement through internal collision conflicts.

7. Use Enhanced Input for Controls

Map your throttle, brake, and steering inputs using the Enhanced Input system. This allows for better deadzone management and sensitivity curves. For example, applying a “Complex” trigger to the brake input can assist in the elimination of instant lock-ups on controllers.

8. Debug with “stat physics” and “show debug vehicle”

If the vehicle is behaving unexpectedly, use the console command showdebug vehicle. This displays real-time telemetry, including RPM, current gear, wheel friction, and suspension compression. This is the most effective way to identify and trigger the elimination of bugs in your vehicle’s handling setup.