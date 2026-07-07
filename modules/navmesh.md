---
layout: default
title: Navmesh
---

<!-- ai-generation-failed -->

<h1>Navmesh</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Navmesh/Navmesh.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the core pathfinding system in Unreal Engine that translates physical level geometry into a walkable surface for AI agents.

Description and Purpose

The NavMesh module is responsible for the generation and maintenance of the Navigation Mesh, a simplified polygonal representation of a level’s walkable areas. Its primary purpose is to provide the data structure needed for A* pathfinding and agent steering. It handles voxelization of geometry, region partitioning, and polygon generation. By using this system, developers can eliminate the need for manual waypoint placement, allowing AI agents to dynamically calculate the most efficient paths while avoiding obstacles and respecting architectural constraints.

Practical Usage Tips and Best Practices
Use Navigation Invokers for Open Worlds
In massive levels, generating a NavMesh for the entire world is memory-intensive. Enable Navigation Invokers on your AI agents and set the Navigation System to “Generate Navigation Only Around Navigation Invokers.” This helps you eliminate the massive memory footprint of world-wide NavMesh tiles by only generating them where AI is actually present.
Optimize Cell Size and Cell Height
The CellSize and CellHeight settings in the RecastNavMesh actor determine the resolution of the voxelization. A smaller cell size increases precision but dramatically slows down build times. Finding a balance (typically between 15 and 20 for standard characters) is a best practice to eliminate long bake times while maintaining path accuracy.
Leverage Nav Modifier Volumes
Use Nav Modifier Volumes to assign different “Area Classes” to parts of your level (e.g., Water, Mud, or Fire). By increasing the “Cost” of these areas, you can influence AI behavior to eliminate illogical paths, such as an agent walking through a dangerous lava pit instead of taking a nearby bridge.
Enable Dynamic Runtime Generation
If your level features destructible environments or moving platforms, set the Runtime Generation to “Dynamic.” This ensures the NavMesh updates in real-time as the environment changes, which is the best way to eliminate “ghost paths” where AI tries to walk through a wall that was recently built or moves toward an object that has been removed.
Adjust Agent Step Height and Slope
Ensure your NavMesh settings match your character’s physical capabilities. Correctly setting the Agent Max Step Height and Agent Max Slope helps you eliminate situations where AI agents get stuck on small curbs or try to climb vertical surfaces they weren’t designed to scale.
Utilize Nav Link Proxies for Gaps
For navigation between disconnected areas, such as jumping across a gap or climbing a ladder, use Nav Link Proxies. These act as “bridges” in the NavMesh graph, allowing you to eliminate navigation breaks that would otherwise prevent an agent from reaching its destination.
Minimize “Can Ever Affect Navigation” on Small Props
By default, every static mesh affects the NavMesh. For small debris, pebbles, or non-colliding grass, disable the Can Ever Affect Navigation checkbox in the actor’s details. This helps you eliminate “noisy” NavMesh generation, which reduces the polygon count of the mesh and improves pathfinding performance.
Use NavMesh Resolutions for Variable Detail
If your level has areas that require high precision (like narrow corridors) and others that don’t (like flat plains), use Nav Mesh Resolution volumes. Setting different resolutions for these areas allows the engine to eliminate unnecessary detail in open spaces while maintaining the precision needed for tight interior navigation.