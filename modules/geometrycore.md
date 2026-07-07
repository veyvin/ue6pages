---
layout: default
title: GeometryCore
---

<!-- ai-generation-failed -->

<h1>GeometryCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GeometryCore/GeometryCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

providing the fundamental data structures and algorithms for advanced mesh manipulation and geometric processing in Unreal Engine.

Description and Purpose

Unlike the higher-level GeometryScripting plugin which is designed for Blueprints, GeometryCore is a pure C++ module (largely header-only) that serves as the engine’s “geometric kernel.” It provides the FDynamicMesh3 data structure, which is much more flexible than a standard UStaticMesh because it supports fast, dynamic changes to topology (adding/removing vertices and triangles). This module is the foundation for the Modeling Mode tools and is used for complex operations like mesh simplification, Boolean operations, AABB tree spatial queries, and surface point sampling.

Practical Usage Tips and Best Practices
Prefer FDynamicMesh3 for Real-time Edits
If you need to modify a mesh every frame or through complex procedural logic, use FDynamicMesh3. It uses an adjacency-based representation that allows you to eliminate and add triangles far more efficiently than the standard FMeshDescription used for static assets.
Use TMeshAABBTree3 for Fast Spatial Queries
When you need to find the closest point on a complex mesh or perform raycasts against a dynamic object, build a TMeshAABBTree3. This spatial data structure helps you eliminate expensive brute-force searches by quickly narrowing down which triangles are near your query point.
Leverage FDynamicMeshEditor for High-Level Operations
Instead of manually manipulating vertex buffers, use the FDynamicMeshEditor class. It provides “wrapper” functions for common tasks like appending meshes, welding vertices, or stitching edges. This helps you eliminate boilerplate code and reduces the risk of creating non-manifold geometry.
Utilize Mesh Simplification Algorithms
The module includes FQEMeshSimplification, which uses Quadric Error Metrics to reduce polycount while preserving shape. Use this to procedurally generate LODs or to eliminate unnecessary detail from high-density scans at runtime to maintain performance.
Process Meshes in Background Threads
FDynamicMesh3 is not a UObject, meaning it is not bound to the Game Thread’s garbage collection. You can perform heavy geometric computations—such as a complex mesh Boolean or an elimination of interior geometry—on a background thread via the Tasks System to avoid hitching the main game loop.
Apply Mesh Smoothing to Clean Noisy Data
Use the FMeshSmoothing implementations (like Cotan or Mean Value coordinates) to relax vertices. This is particularly useful after a Boolean operation to eliminate jagged edges or artifacts created during the intersection of two complex meshes.
Sampling and Point Clouds
Use the FMeshSurfaceSampler to generate points evenly across the surface of a mesh. This is ideal for spawning Niagara particles or foliage instances on a character, helping you eliminate the “clumping” effect that occurs with simple random sampling.
Avoid Constant Conversions
Converting between UStaticMesh and FDynamicMesh3 is computationally expensive as it involves copying all vertex and index data. To optimize performance, keep your geometry in the FDynamicMesh3 format for as long as possible during your processing pipeline to eliminate redundant memory allocations.