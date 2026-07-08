---
layout: default
title: NavigationSystem
---

<!-- ai-generation-failed -->

<h1>NavigationSystem</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NavigationSystem/NavigationSystem.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, Core, CoreUObject, EditorFramework, Engine, GeometryCollectionEngine, Navmesh, RHI, RenderCore, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ding and spatial reasoning for AI agents in Unreal Engine. It manages the generation, storage, and querying of the Navigation Mesh (NavMesh), which acts as a walkable surface representation of the level’s collision geometry.

This module provides the logic for both static and dynamic navigation, allowing AI to find paths around obstacles, use specialized traversal links (NavLinks), and avoid other agents. By abstracting complex geometric calculations into simple path requests, it helps you eliminate the need for manual waypoint systems or custom A* implementations.

Practical Usage Tips and Best Practices
Optimize with the Highest Possible Cell Size
In your RecastNavMesh actor or Project Settings, set the Cell Size and Cell Height as high as your agents’ dimensions allow. Larger cells significantly speed up NavMesh generation and reduce memory usage, helping you eliminate long build times in large levels.
Use Nav Modifier Volumes for Cost Control
Instead of changing collision to block AI, use Nav Modifier Volumes to assign different “Areas.” You can increase the “Cost” of an area (like a swamp or a dangerous zone) to encourage AI to find a path around it, which helps you eliminate “unintelligent” AI movement that ignores environmental hazards.
Limit Dynamic Rebuilds with ‘Dynamic Modifiers Only’
If your level geometry is mostly static but has moving doors or gates, set the Runtime Generation to Dynamic Modifiers Only. This module will then only rebuild the NavMesh for specific areas marked by modifiers, helping you eliminate the massive CPU overhead of re-calculating the entire level’s geometry.
Leverage Navigation Invokers for Open Worlds
For massive open-world maps, add a Navigation Invoker Component to your players and AI agents. This tells the module to only generate NavMesh in a radius around those actors. This practice helps you eliminate the memory bloat and processing time associated with generating miles of NavMesh that no one is currently using.
Configure NavMesh Resolution Tiers
Use the NavMesh Resolution Params to define different cell sizes for different areas of your game. You can use high-resolution NavMesh for tight interiors and low-resolution for open fields, which helps you eliminate unnecessary precision in areas where simple movement suffices.
Utilize the ‘Project Point to Navigation’ Query
When spawning items or characters, use the ProjectPointToNavigation function provided by this module. This snaps a 3D coordinate to the nearest walkable surface, helping you eliminate bugs where actors are spawned inside walls or floating in the air.
Implement Nav Links for Non-Standard Traversal
For jumping across gaps, climbing ladders, or using teleporters, use Nav Link Proxies. These create a “bridge” between two points on the NavMesh that aren’t physically connected. This allows the pathfinder to include these actions in its calculations, helping you eliminate “stuck” AI that cannot navigate verticality.
Properly Handle Agent Elimination
When an AI agent is defeated (the “elimination” of the actor), ensure you stop any active pathfinding requests and unregister the actor from the Crowd Manager if using detour avoidance. This ensures the module doesn’t waste CPU cycles calculating paths for non-existent entities, helping you eliminate performance leaks in long gameplay sessions.