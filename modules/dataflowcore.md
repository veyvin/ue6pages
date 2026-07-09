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

ne’s Dataflow Graph system. It provides the core C++ logic for building, evaluating, and managing dependency-based procedural graphs. Unlike traditional destructive workflows, Dataflow uses this module to handle “Managed Array Collections,” which allow for non-destructive data transformation. It is the underlying technology powering modern engine features like Chaos Cloth, Chaos Flesh, and Geometry Collection fracturing.

Practical Usage Tips & Best Practices
1. Understand Managed Array Collections

The primary data structure handled by DataflowCore is the FManagedArrayCollection.

Best Practice: When creating custom nodes, treat the collection as a flexible container of named attributes (like Position, Normal, or Weight). This allows you to pass complex geometry and simulation data between nodes without the overhead of heavy UObject casting, leading to the elimination of memory bottlenecks.
2. Leverage Dependency-Based Evaluation

DataflowCore uses a “push-pull” evaluation model where a node only re-evaluates if its upstream inputs have changed.

Tip: Avoid putting heavy logic in every node. Design your graph so that expensive calculations are isolated in specific nodes. This ensures that minor tweaks to a “Color” node don’t trigger a total elimination of the cached geometry data from an expensive “Fracture” node.
3. Use Dataflow Variables for Iteration

The module supports a variable system that allows graph parameters to be exposed to the outside world.

Best Practice: Instead of hard-coding values like “Fracture Level” or “Cloth Stiffness,” use “Get Variable” nodes. This allows a single Dataflow asset to be reused across multiple game assets with different settings, facilitating the elimination of redundant graph assets.
4. Optimize with Node Caching

DataflowCore provides caching mechanisms to store the results of node evaluations.

Tip: During development, if you notice the graph is sluggish, check the caching settings on high-poly processing nodes. Proper caching prevents the engine from re-calculating the entire procedural chain on every mouse click, which helps in the elimination of editor lag.
5. Extend via C++ Nodes

While many nodes exist for Chaos and Geometry, the system is designed to be extended.

Best Practice: To create a custom node, inherit from FDataflowNode. Use the DATAFLOW_NODE_DEFINE_PROPERTIES macro to expose pins. This is the most efficient way to integrate custom procedural algorithms into the Unreal pipeline, ensuring the elimination of “black box” logic that designers cannot tweak.
6. Coordinate with Asset Elimination and Lifecycle

When an asset using a Dataflow graph (like a Geometry Collection) is destroyed or removed, the DataflowCore handles the cleanup of the temporary evaluation contexts.

Tip: If you are managing Dataflow components dynamically in C++, ensure you properly register the component with the Dataflow editor’s context to avoid memory leaks. The correct handling of the component’s elimination ensures that the underlying simulation data is freed correctly.
7. Debug with the Dataflow Terminal

The “Terminal” node is the final output of any Dataflow graph.

Best Practice: Use multiple Terminal nodes for different output types (e.g., one for the simulation mesh and one for the collision body). In the Dataflow Editor, you can switch which terminal is being viewed to inspect different stages of the procedural pipeline, aiding in the elimination of visual artifacts.
8. Use Dataflow for Non-Destructive Ingestion

DataflowCore is increasingly used to replace static “Import” steps.

Tip: Use the module to create ingestion pipelines where you import a raw mesh and use Dataflow nodes to automatically generate skin weights, LODs, and collision shapes. This allows you to update the source mesh without losing your setup, leading to the elimination of repetitive manual setup tasks.