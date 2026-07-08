---
layout: default
title: GeometryCollectionEngine
---

<!-- ai-generation-failed -->

<h1>GeometryCollectionEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/GeometryCollectionEngine/GeometryCollectionEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ChaosSolverEngine, Core, CoreUObject, DataflowCore, DataflowEngine, EditorFramework, Engine, FieldSystemEngine, GeometryCore, ISMPool, IntelISPC, MeshConversion, MeshDescription, NetCore, PhysicsCore, RHI, RenderCore, Renderer, SkeletalMeshDescription, SkeletalMeshUtilitiesCommon, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tering, and the propagation of damage through a structural hierarchy.

It is responsible for translating a static mesh into a collection of rigid bodies (Geometry Collection), facilitating the elimination of static environments in favor of fully destructible, physically reactive worlds.

Practical Usage Tips and Best Practices
1. Optimize Performance with Clustering

Chaos uses a hierarchical clustering system where multiple fractured pieces are treated as a single rigid body until enough force is applied. Properly setting up these clusters in the Geometry Collection asset leads to the elimination of excessive active physics bodies, significantly improving CPU performance during large-scale destruction.

2. Use Sleep and Disable Fields

To prevent the physics solver from wasting resources on debris that has already fallen, place Sleep or Disable Physics Fields just above or on the ground. This forces slow-moving fragments to stop simulating, aiding in the elimination of jitter and “physics popping” once the initial destruction event is over.

3. Leverage “Remove on Sleep” for Debris

In the Geometry Collection asset settings, enable Remove on Sleep. This will automatically delete small fragments once they have settled and stopped moving. This is a vital practice for the elimination of persistent physics actors that would otherwise clutter the scene and degrade performance over time.

4. Simplify Collision Proxies

By default, Chaos may use complex convex hulls for every fragment. For smaller debris, switch the Collision Proxy to simpler shapes like Boxes or Spheres. Using less expensive collision primitives leads to the elimination of complex contact calculations, which is essential for maintaining high frame rates in dense destruction scenarios.

5. Control Damage via Propagation Factor

The Damage Propagation Factor determines how strain moves through the connection graph of a fractured object. Tuning this value allows you to control whether a building collapses entirely from one hit or loses only a small chunk. Proper tuning assists in the elimination of “glass-like” behavior where objects shatter too easily.

6. Automate with Dataflow

For projects requiring many destructible assets, use the Dataflow graph (a node-based procedural system) to automate fracturing and clustering. This procedural approach ensures a consistent destruction quality across your project and facilitates the elimination of manual, repetitive fracturing tasks for every unique mesh.

7. Implement One-Way Interaction (Debris System)

Enable One-Way Interaction for small fragments (debris). This allows small pieces to be hit by the player or large chunks without the small pieces pushing back on the larger, more important simulation actors. This helps in the elimination of “jittery” physics interactions between massive objects and tiny rubble.

8. Cache Complex Simulations

For cinematic destruction that must look perfect every time, use the Chaos Cache Manager to record the simulation. Playing back a cached simulation instead of running it live leads to the elimination of non-deterministic physics behavior and provides a significant performance boost for linear content or trailers.