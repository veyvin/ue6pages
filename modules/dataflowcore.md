---
layout: default
title: DataflowCore
---

<!-- ai-generation-failed -->

<h1>DataflowCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Dataflow/Core/DataflowCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AssetRegistry, Chaos, Core, CoreUObject, DeveloperSettings, ImageCore, InputCore, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ne’s node-based procedural content generation framework. It provides the core logic and evaluation graph used to manipulate complex data structures like Geometry Collections, Cloth, and Flesh.

Description

DataflowCore implements a dependency-based evaluation graph where each node processes inputs and produces outputs that flow into downstream dependencies. Unlike Blueprints, which are designed for imperative logic and gameplay events, Dataflow is designed for procedural asset authoring. It allows for a non-destructive workflow where developers can define a recipe—such as fracturing a mesh, clustering pieces, and generating collision—that can be re-evaluated instantly if the source asset or parameters change. It is the architectural backbone that enables the “Dataflow Graph” editor seen in Chaos Destruction and Cloth tools.

Practical Usage Tips and Best Practices
1. Adopt a Non-Destructive Mindset

The primary advantage of DataflowCore is that it is non-destructive. Instead of permanently applying a fracture to a mesh, use Dataflow nodes to define the fracture pattern. If the art team changes the base mesh, the Dataflow graph will automatically re-run the fracture logic on the new geometry, eliminating the need to manually recreate the asset from scratch.

2. Organize with Comments and Named Nodes

As graphs grow in complexity—especially for intricate destruction—they can become difficult to read. Use the built-in comment boxes to group logical sections (e.g., “Primary Fracturing,” “Secondary Detailing,” and “Collision Setup”). This is a best practice for team collaboration, ensuring that other technical artists can follow the procedural logic without tracing every individual wire.

3. Leverage “Overrides” for Batch Processing

You can use Dataflow graphs to process thousands of assets automatically. By setting up “Overrides” within the graph, you can drive node parameters (like Voronoi site counts) using external data or Blueprint utilities. This allows you to apply a consistent “material-based” destruction style across an entire library of props while varying the intensity based on each asset’s volume.

4. Monitor Evaluation Performance

Since Dataflow graphs can be computationally expensive (especially when performing 3D boolean operations or complex simulations), monitor the evaluation time of your nodes. If a graph takes too long to update, consider breaking it down or simplifying the geometry at the start of the chain to ensure the editor remains responsive during iteration.

5. Use Selection Nodes to Target Specific Areas

Don’t apply operations to the whole mesh if you only need to modify a part of it. Use Selection Nodes to isolate specific vertices or faces based on vertex colors, proximity to an actor, or bounding boxes. This allows for localized detail—such as extra fracturing around a door lock—without the performance cost of high-density fracturing across the entire object.

6. Extend via C++ Custom Nodes

While the engine provides many default nodes, DataflowCore is designed to be extensible. If you have a specialized procedural need (such as a custom wood-grain splintering algorithm), create a new node by inheriting from FDataflowNode in C++. This allows you to integrate proprietary logic directly into the visual authoring pipeline.

7. Optimize via Chunk Elimination

In destruction workflows, use Dataflow nodes to manage the density of your Geometry Collections. You can implement logic to filter and remove tiny slivers or “dust” particles that are too small to contribute to the visual experience but still cost physics performance. By automating the elimination of these redundant chunks within the graph, you ensure the resulting asset is optimized for real-time simulation.

8. Verify with the Dataflow Terminal

Always check the Dataflow Terminal (the final output node) to ensure your data is being formatted correctly for the target system (e.g., Chaos Cloth or Geometry Collection). The terminal acts as the bridge between the procedural graph and the actual engine asset; if the terminal is not correctly configured, your procedural changes will not be saved into the final asset.