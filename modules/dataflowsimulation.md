---
layout: default
title: DataflowSimulation
---

<!-- ai-generation-failed -->

<h1>DataflowSimulation</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Dataflow/Simulation/DataflowSimulation.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, Core, CoreUObject, DataflowCore, DataflowEngine, Engine, RHI, RenderCore, RigidPhysics</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

framework in Unreal Engine. While the core Dataflow module handles the graph-based authoring of procedural assets (like fracturing geometry or generating cloth masks), the DataflowSimulation module is responsible for the runtime evaluation and execution of these graphs when they are used for real-time physics and simulation.

It acts as the execution engine that allows Chaos physics solvers (Cloth, Flesh, and Destruction) to pull data from a Dataflow graph during gameplay or in-editor simulation.

1. Differentiate Between Authoring and Simulation

Dataflow is split into an Editor component (for building graphs) and a Simulation component (for running them).

Best Practice: Use the DataflowSimulation module when you need to drive simulation parameters dynamically at runtime. For example, if you want a character’s cloth properties to change based on an “internal wetness” variable, this module handles the re-evaluation of the graph logic to update the physics state.
2. Optimize Evaluation Frequency

Evaluating a complex Dataflow graph can be computationally expensive.

Tip: Avoid re-evaluating the simulation graph every tick unless absolutely necessary. Use the module’s caching capabilities to store the results of expensive procedural operations, and only trigger a re-evaluation when a significant input parameter changes.
3. Leverage for Chaos Flesh (Deformable Bodies)

This module is a primary driver for the Chaos Flesh system used for muscle and soft-body simulation.

Best Practice: When setting up Flesh assets, use DataflowSimulation to handle the vertex-level constraints. It allows the simulation to procedurally determine which parts of a mesh should be rigid versus elastic based on the bone influences passed through the graph.
4. Use for Procedural Destruction Logic

While standard Geometry Collections are often static, DataflowSimulation allows for “living” destruction assets.

Tip: Use the module to procedurally adjust the “Damage Threshold” or “Connection Strength” of a Geometry Collection based on gameplay events. This allows you to eliminate fixed destruction patterns in favor of dynamic, graph-driven structural integrity.
5. Monitor Performance with Unreal Insights

Because simulation evaluation happens on the physics or worker threads, it can be hard to track with standard stat commands.

Best Practice: Use Unreal Insights and look for Dataflow and Simulation trace events. If you see long “bubbles” in the frame, it usually means your simulation graph is too complex for real-time evaluation and needs to be simplified or baked.
6. Correct Module Dependencies

If you are writing custom C++ nodes that need to interact with the runtime simulation state, you must include the module in your Build.cs:

C#
PublicDependencyModuleNames.AddRange(new string[] { "DataflowCore", "DataflowSimulation", "Chaos" });
Copy code

Note: Ensure you are separating your DataflowEditor code from your DataflowSimulation code to prevent linker errors in cooked builds.

7. Global Simulation Control

The module provides buttons in the Dataflow Editor toolbar to Start, Pause, and Step through the simulation.

Tip: When debugging a procedural asset, use the “Step” feature. This allows you to see exactly how the DataflowSimulation module is passing data from one node to the next, helping you identify which node is causing a simulation to “explode” or fail.
8. Use Simulation Caching to Save CPU

For complex procedural animations or cloth behaviors that don’t need to be interactive, use the caching features provided by the simulation interface.

Best Practice: Record a simulation session into a Chaos Cache Collection. This allows the engine to skip the Dataflow graph evaluation entirely during gameplay, playing back the recorded vertex data instead. This is the best way to eliminate high CPU costs for cinematic-quality physics.