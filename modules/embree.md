---
layout: default
title: Embree
---

<!-- ai-generation-failed -->

<h1>Embree</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Intel/Embree/Embree.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">IntelTBB</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

mance ray tracing kernels into Unreal Engine. It serves as the “mathematical engine” for CPU-based ray intersections, providing highly optimized paths for calculating how light and visibility rays interact with geometry.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/Intel/Embree, this module is a library of kernels designed for x86 CPUs. It utilizes advanced instruction sets (like AVX2 and AVX-512) to accelerate ray tracing tasks that occur within the Editor or during the build process.

Primary uses include:

CPU Lightmass: Powering the core calculations for static light baking, including global illumination, soft shadows, and ambient occlusion.
NavMesh Generation: Accelerating the ray-casts required to determine walkable surfaces and obstacles during AI navigation builds.
Visibility Auditing: Supporting “Precomputed Visibility” by rapidly tracing rays to determine which actors are visible from specific cells.
Mesh Distance Fields: Assisting in the generation of Signed Distance Fields (SDF) by calculating the closest point on a mesh surface.
Practical Usage Tips and Best Practices
1. Maximize CPU Thread Allocation

Since Embree is a CPU-bound library, its performance scales almost linearly with core count. When baking lights or building navigation, ensure your Swarm Agent (for Lightmass) or Engine settings are not artificially capped. Higher thread counts directly lead to the elimination of long “Waiting for Build” times.

2. Utilize Modern CPU Architectures

Embree is heavily optimized for Intel and AMD CPUs that support AVX2 or AVX-512. If you are building a workstation for lighting artists, prioritize CPUs with high SIMD (Single Instruction, Multiple Data) performance. The Embree module will automatically detect and use the widest instruction set available on the host machine.

3. Optimize Geometry for “Alpha Masking”

Ray tracing through masked materials (like foliage) is significantly slower than tracing through opaque geometry. To improve Embree’s efficiency during light bakes, keep your masked areas tight to the texture. Overly large transparent “quads” force Embree to perform more intersection tests, slowing down the build.

4. Distribute Work via Swarm

For CPU Lightmass, the Embree module works in tandem with Unreal Swarm. You can distribute Embree-based ray tracing tasks across a local network of PCs. This is a best practice for studios; by sharing the ray tracing load, you can achieve the elimination of local workstation bottlenecks during heavy bakes.

5. Monitor Memory During Complex Bakes

Embree builds an internal acceleration structure (BVH) for your scene’s geometry. For massive levels with millions of triangles, this BVH can consume significant RAM. If your builds are failing, check your system memory usage. You may need to simplify your “Static” geometry or break the level into smaller sub-levels.

6. Use for Accurate Offline Audits

If you are developing custom C++ tools for scene analysis (e.g., a tool to check if a camera can see a specific object), consider using the Embree-backed pathways in the engine. It provides a “ground truth” level of accuracy for ray intersections that is often more precise than the simplified physics-based ray-casts.

7. Keep Geometry “Water-Tight”

Embree performs best when meshes are “water-tight” (no holes). While it can handle open geometry, intersecting rays with inverted normals or broken topology can occasionally cause artifacts in lightmaps. Ensure your static meshes have clean topology to get the most consistent results from the Embree kernels.

8. Strategic Elimination of Unnecessary Static Shadows

Every object set to “Static” with “Cast Shadow” enabled must be processed by Embree during a light bake. To save time, disable “Cast Static Shadow” for small, insignificant props. This reduces the size of the BVH structure Embree has to build and traverse, resulting in significantly faster iteration loops.