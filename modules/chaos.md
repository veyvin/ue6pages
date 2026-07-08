---
layout: default
title: Chaos
---

<!-- ai-generation-failed -->

<h1>Chaos</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/Chaos/Chaos.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutoRTFM, ChaosCore, ChaosVDRuntime, Core, CoreUObject, Eigen, GeometryCore, IntelISPC, MeshDescription, NNE, TraceBasedDebuggers, TraceLog, Voronoi</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

g pieces in a cluster until they receive sufficient strain, you significantly reduce the number of active bodies, leading to the elimination of CPU bottlenecks during large destruction events.

3. Utilize the Chaos Visual Debugger (CVD)

If your physics objects are jittering or falling through the floor, open the Chaos Visual Debugger (Tools > Chaos Visual Debugger). It allows you to record a simulation and scrub through it frame-by-frame to inspect contacts, joints, and collision shapes, aiding in the elimination of “invisible” collision bugs.

4. Use Physics Proxies for Complex Meshes

Do not use high-poly visual meshes for collision. For complex props, create a simplified “Physics Proxy” using primitive shapes (boxes, spheres, capsules). This results in a massive elimination of collision detection overhead compared to using complex per-poly collision.

5. Implement Removal and Sleep Fields

To maintain performance during intense destruction, use Field System Actors to define “Sleep” or “Kill” (Elimination) zones. For example, a sleep field placed just above the ground can put fallen debris to rest immediately, while a removal field can trigger the elimination of small debris pieces after a set time.

6. Leverage the Debris System

In the Geometry Collection settings, configure the Debris System to automatically manage small fragments. You can set thresholds based on the size or life-span of a piece to trigger its elimination. This ensures that the scene does not become cluttered with thousands of tiny, high-cost physics bodies.

7. Tune Collision Proxy Scales

Within a Geometry Collection, you can choose different collision types (Convex, Sphere, Box) for different levels of the fracture. Use simpler proxies for smaller, deeper fragments. This provides a better elimination of interpenetration issues (explosions on spawn) while keeping the math cheap.

8. Avoid Physics Scene Bloat with World Partition

If using World Partition, ensure your physics assets are streamed out when not relevant. Use the Physics Scene Size settings to ensure that the engine isn’t trying to simulate actors in unloaded cells, which assists in the elimination of unnecessary background CPU usage.