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

st & Detour navigation libraries within Unreal Engine. While the NavigationSystem module provides the high-level Blueprint and Actor interfaces, the NavMesh module handles the heavy lifting of voxelizing world geometry, generating the navigation polygons, and performing the actual A* pathfinding queries.

It is primarily used by the engine to create the ARecastNavMesh actor and manage the underlying tile-based data structures that AI agents use to navigate the game world.

Practical Usage Tips & Best Practices
1. Balance Cell Size and Cell Height

The CellSize and CellHeight properties define the resolution of the voxels used to build the mesh. Smaller values provide higher precision but significantly increase generation time.

Best Practice: Use the highest values possible that still allow your AI to navigate narrow corridors. Increasing these values leads to the elimination of long “Navigation Building” hangups during development and reduces the memory footprint of the navigation data.
2. Utilize Navigation Mesh Resolutions

UE5 allows for different navigation resolutions (Low, Medium, High) within the same world using Nav Mesh Resolution Volumes.

Tip: Assign “Low” resolution to large, flat open areas and “High” resolution only to complex interior spaces with many obstacles. This results in the elimination of unnecessary polygon density in simple areas, optimizing both pathfinding speed and memory usage.
3. Optimize Tile Size for Dynamic Rebuilds

The NavMesh is divided into square tiles. When an object moves in a “Dynamic” NavMesh, only the affected tiles are rebuilt.

Best Practice: In large open-world maps, use a larger TileSizeUU to reduce the total number of tiles. However, for games with many moving obstacles, smaller tiles are better as they result in the elimination of massive re-computation spikes when a single small prop is moved.
4. Manage Agent Radius and Max Slope

The AgentRadius and AgentMaxSlope settings in the NavMesh generation properties determine where the mesh is actually generated.

Tip: Ensure these settings match your character’s physical capsule and movement capabilities. Properly aligning these values facilitates the elimination of AI “stuck” scenarios where agents try to walk through gaps that are too narrow or up slopes that are too steep.
5. Use Nav Modifier Volumes for Cost Control

Not all walkable surfaces are equal; some areas (like mud or fire) should be avoided by AI unless necessary.

Best Practice: Use Nav Modifier Volumes to assign custom NavArea classes with higher costs to “dangerous” areas. This ensures the elimination of “stupid” AI behavior where agents take the shortest physical path through a hazard instead of a slightly longer, safer route.
6. Minimize Off-Mesh Link Usage

Off-Mesh Links allow AI to jump across gaps or climb ladders where the NavMesh is not contiguous.

Tip: Use them sparingly, as they add complexity to the pathfinding graph. Efficient placement of these links leads to the elimination of “jittery” pathing where the AI constantly evaluates whether to jump or walk around an obstacle.
7. Profile with “Draw Tile Build Times”

If your editor or game is hitching during navigation updates, you need to find the “hot” tiles.

Best Practice: Enable bDrawTileBuildTimes on the RecastNavMesh actor in the Outliner. Visualizing the build cost of each tile allows for the elimination of “invisible” performance sinks caused by overly complex collision geometry in a specific corner of your map.
8. Leverage Navigation Building Locks

During heavy level editing or initial loading, constant NavMesh updates can tank performance.

Tip: Use ENavigationBuildLock::InitialLock or the “Navigation -> Skip Rebuild” editor toggle when performing bulk operations. Proactively locking the system results in the elimination of redundant rebuild cycles, making your level design workflow much smoother.