---
layout: default
title: DataflowEngine
---

<!-- ai-generation-failed -->

<h1>DataflowEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Dataflow/Engine/DataflowEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, Core, CoreUObject, DataflowCore, Engine, GeometryCore, ImageCore, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

aflow Graph system. It provides the evaluation logic and execution framework for node-based procedural asset generation.

What it is and What it’s used for

The Dataflow system is a dependency-based graph environment that allows for non-destructive asset creation. While the DataflowEditor handles the UI, the DataflowEngine is responsible for the actual processing of data—taking inputs, running them through a series of nodes, and outputing a finalized asset or simulation state.

Primary uses include:

Chaos Flesh & Cloth: Powering the procedural generation of tetrahedral meshes for soft-body simulations.
Geometry Collections: Handling complex fracturing and clustering logic for the Chaos physics system.
Procedural Authoring: Enabling a “non-destructive” workflow where you can revert or modify any step in an asset’s creation without starting over.
Asset Automation: Processing thousands of assets automatically by applying the same Dataflow graph logic across multiple source meshes.
Practical Usage Tips and Best Practices
1. Prefer Dataflow for Non-Destructive Iteration

Traditional workflows (like manual fracturing) are destructive. If you need to change a fracture pattern, you usually have to start from the beginning. By using the DataflowEngine, you can simply change a seed value or a noise parameter in the graph, and the engine will re-evaluate only the affected nodes, significantly reducing iteration time.

2. Master the Evaluation Context

The DataflowEngine uses an evaluation context to manage memory. When writing custom C++ nodes, always ensure you are reading from the FContext. This prevents the engine from re-calculating the entire graph if only a small branch has changed, leading to the elimination of unnecessary CPU overhead.

3. Use for Chaos Flesh Tetrahedralization

If you are working with Chaos Flesh, use the DataflowEngine to generate your tetrahedral volumes. It supports multiple algorithms, such as “Iso-surface Stuffing” and “TetWild.” Using the graph system allows you to preview the internal simulation structure of a character’s muscles before committing to a solver.

4. Leverage “Caching” for Performance

Simulation-heavy Dataflow graphs (like high-resolution cloth or flesh) can be computationally expensive. Use the DataflowEngine’s Caching system to record the results of a simulation. You can then play back these results in Sequencer, allowing for high-quality cinematic results without the real-time simulation cost.

5. Implement Custom Nodes in C++

The DataflowEngine is designed to be extensible. If you have a specific procedural requirement not met by standard nodes, inherit from FDataflowNode. By registering your custom node with the engine, you can expose complex math or proprietary algorithms to your technical artists through the visual graph.

6. Utilize the Terminal Node

Every Dataflow graph requires a Terminal Node to output a result (e.g., a Geometry Collection or a Flesh Asset). Ensure your graph logic is streamlined toward this output. A best practice is to have multiple Terminal nodes for different LODs, allowing the engine to evaluate lower-complexity versions of the asset for distant views.

7. Debug with “Dataflow Insights”

When a graph isn’t producing the expected result, use the built-in visualization tools provided by the engine. You can inspect the data flowing through any connection in the graph to see exactly where a mesh’s topology might be breaking or where a simulation attribute is being lost.

8. Strategic Elimination of Complexity

For real-time performance, use the DataflowEngine to generate low-resolution “proxy” geometry for the physics solver while maintaining a high-resolution mesh for rendering. This “sim-to-render” mapping ensures that the physics engine stays fast while the visual quality remains at a cinematic level.