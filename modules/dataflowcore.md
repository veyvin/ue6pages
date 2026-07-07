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

n Unreal Engine, used for procedural asset generation and non-destructive data transformation.

Description and Purpose

This module provides the core framework for Dataflow Graphs, which are dependency-based node graphs that produce assets (such as Chaos Cloth, Chaos Flesh, and Geometry Collections) after evaluation. Unlike traditional destructive workflows where changes are permanent, Dataflow allows for a procedural approach where you can modify nodes and see results instantly. It is designed to be highly extensible via C++, allowing developers to create custom nodes that manipulate raw data collections. Its primary purpose is to improve iteration times and automate the ingestion pipeline for complex physics assets.

Practical Usage Tips and Best Practices
Embrace the Non-Destructive Workflow
The primary benefit of Dataflow is the ability to revert or skip steps without losing work. Use this to experiment with different fracturing patterns or cloth configurations. If a specific node setup isn’t working, you can simply disconnect it or bypass it to eliminate its effect on the final asset.
Automate Asset Ingestion Pipelines
Use Dataflow to create standard “recipes” for common tasks like generating skin weights or LODs for clothing. By applying a standard Dataflow graph to multiple assets, you can eliminate the manual labor of setting up physics for every new character or destructible prop in your project.
Integrate Geometry Scripting for Dynamic Results
In UE 5.6, you can use the ApplyGeometryScriptToMesh node within a Dataflow graph. This allows you to use Geometry Scripting logic to procedurally modify meshes before they are converted into physics assets, helping you eliminate the need for external modeling software for minor geometry tweaks.
Optimize Graphs by Reducing Re-evaluations
Dataflow graphs are dependency-based. To maintain high performance, avoid creating overly complex “spaghetti” graphs where a single change at the start triggers a massive re-calculation. Group related logic into sections to help eliminate unnecessary processing overhead during iteration.
Use for Destruction State Management
When setting up a Geometry Collection, use Dataflow to define the anchor points and strain thresholds. This ensures that when a player triggers an elimination of a structure, the destruction follows a predictable, artist-authored pattern rather than a purely random one.
Export Geometry for External Review
If you need to verify the procedural geometry generated within the graph, use the ClothCollectionToDynamicMesh and Write String to File nodes to export an .obj file. This is a great way to eliminate uncertainty regarding the quality of the generated sim-meshes or collision geometry.
Leverage Dataflow for Character Elimination Effects
For complex elimination sequences involving “Chaos Flesh” (flesh simulation) or intricate clothing, use a Dataflow graph to manage how the simulated components react to terminal forces. This ensures the simulation remains stable even under the extreme physics impulses often seen during an elimination.
Monitor Memory with Data Collections
Since Dataflow works on “Collections” (a generic container for attributes), keep an eye on the number of attributes you are adding. Every attribute adds to the memory footprint of the asset. Periodically audit your graphs to eliminate unused attribute nodes that are no longer contributing to the final simulation.