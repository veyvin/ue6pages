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

ge Tips and Best Practices
1. Add to Build Dependencies for Custom Solvers

If you are writing custom vehicle simulation logic or extending the vehicle simulation beyond the default 4-wheeled car (e.g., custom tanks or mechs), you must include this module in your Build.cs.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "ChaosVehicleCore", "ChaosVehicles" });

	```

	 

	#### 2. Leverage Async Physics for Determinism

	ChaosVehicleCore is designed to run on the **Physics Thread** rather than the Game Thread.

	*   **Best Practice:** In your Project Settings, enable **Tick Physics Async**. This allows the vehicle solver to run at a fixed frequency (e.g., 60Hz or 100Hz) regardless of the rendering frame rate. This helps **eliminate** "jittery" vehicle behavior caused by variable frame times and is a requirement for competitive racing games.

	 

	#### 3. Understand the Simulation State (FVehicleSimulationState)

	The core simulation logic uses `FVehicleSimulationState` to store the physics data for a single frame (velocity, torque, wheel RPM).

	*   **Tip:** When implementing custom networking, this struct is what you should serialize. By passing the `FVehicleSimulationState` between the server and client, you can **eliminate** desyncs because the client's local Chaos solver will have the exact starting parameters used by the server.

	 

	#### 4. Optimize Solver Substepping

	For high-speed vehicles, the default physics step might not be enough to prevent wheels from "clipping" through the ground or losing traction.

	*   **Action:** Increase the **Substepping Count** in the vehicle's physics settings. This tells the `ChaosVehicleCore` to run multiple smaller solver iterations per frame. While more expensive, it helps **eliminate** physics instabilities during high-velocity collisions or sharp turns.

	 

	#### 5. Use Modular Sim Components (UE 5.5+)

	The "Core" logic now supports a tree-based modular approach. Instead of a monolithic vehicle, you can attach individual simulation modules (Engine, Clutch, Transmission, Aerofoil).

	*   **Best Practice:** For complex vehicles (like 8x8 trucks or planes), use the modular simulation components found in this module. This allows you to **eliminate** the limitations of the standard 4-wheel `WheeledVehiclePawn` by building a custom simulation tree.

	 

	#### 6. Implement Network Resimulation

	This module provides the necessary callbacks for the **Network Physics Component** to perform "Rewind and Resimulate" logic.

	*   **Tip:** If a client deviates from the server's path, the engine uses `ChaosVehicleCore` to "rewind" the vehicle state and "replay" the inputs. To ensure this works, keep your custom vehicle logic inside the `SimulationTick` callback rather than the standard `Tick`, **eliminating** non-deterministic gameplay bugs.

	 

	#### 7. Profile with Chaos Visual Debugger (CVD)

	Because this module runs on the physics thread, standard `DrawDebug` calls from the Game Thread can be inaccurate or latent.

	*   **Action:** Use the **Chaos Visual Debugger** (Tools > Chaos Visual Debugger). It can record the "Core" state of the vehicle solver, allowing you to scrub through frames to see exactly where a wheel lost contact or a suspension spring bottomed out, **eliminating** guesswork in physics tuning.

	 

	#### 8. Tune Aerofoils for Ground Effect

	The core solver includes sophisticated `FAerofoil` logic that can be used for more than just planes.

	*   **Tip:** Add Aerofoil surfaces to your racing cars to simulate downforce. By adjusting the "Lift" and "Drag" coefficients in the core simulation, you can **eliminate** the "floaty" feeling of high-speed vehicles and make them feel "planted" to the track as they accelerate.
Copy code
2. Leverage Async Physics for Determinism

ChaosVehicleCore is designed to run on the Physics Thread rather than the Game Thread.

Best Practice: In your Project Settings, enable Tick Physics Async. This allows the vehicle solver to run at a fixed frequency (e.g., 60Hz or 100Hz) regardless of the rendering frame rate. This helps eliminate “jittery” vehicle behavior caused by variable frame times and is a requirement for competitive racing games.
3. Understand the Simulation State (FVehicleSimulationState)

The core simulation logic uses FVehicleSimulationState to store the physics data for a single frame (velocity, torque, wheel RPM).

Tip: When implementing custom networking, this struct is what you should serialize. By passing the FVehicleSimulationState between the server and client, you can eliminate desyncs because the client’s local Chaos solver will have the exact starting parameters used by the server.
4. Optimize Solver Substepping

For high-speed vehicles, the default physics step might not be enough to prevent wheels from “clipping” through the ground or losing traction.

Action: Increase the Substepping Count in the vehicle’s physics settings. This tells the ChaosVehicleCore to run multiple smaller solver iterations per frame. While more expensive, it helps eliminate physics instabilities during high-velocity collisions or sharp turns.
5. Use Modular Sim Components (UE 5.5+)

The “Core” logic now supports a tree-based modular approach. Instead of a monolithic vehicle, you can attach individual simulation modules (Engine, Clutch, Transmission, Aerofoil).

Best Practice: For complex vehicles (like 8x8 trucks or planes), use the modular simulation components found in this module. This allows you to eliminate the limitations of the standard 4-wheel WheeledVehiclePawn by building a custom simulation tree.
6. Implement Network Resimulation

This module provides the necessary callbacks for the Network Physics Component to perform “Rewind and Resimulate” logic.

Tip: If a client deviates from the server’s path, the engine uses ChaosVehicleCore to “rewind” the vehicle state and “replay” the inputs. To ensure this works, keep your custom vehicle logic inside the SimulationTick callback rather than the standard Tick, eliminating non-deterministic gameplay bugs.
7. Profile with Chaos Visual Debugger (CVD)

Because this module runs on the physics thread, standard DrawDebug calls from the Game Thread can be inaccurate or latent.

Action: Use the Chaos Visual Debugger (Tools > Chaos Visual Debugger). It can record the “Core” state of the vehicle solver, allowing you to scrub through frames to see exactly where a wheel lost contact or a suspension spring bottomed out, eliminating guesswork in physics tuning.
8. Tune Aerofoils for Ground Effect

The core solver includes sophisticated FAerofoil logic that can be used for more than just planes.

Tip: Add Aerofoil surfaces to your racing cars to simulate downforce. By adjusting the “Lift” and “Drag” coefficients in the core simulation, you can eliminate the “floaty” feeling of high-speed vehicles and make them feel “planted” to the track as they accelerate.