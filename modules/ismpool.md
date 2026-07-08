---
layout: default
title: ISMPool
---

<!-- ai-generation-failed -->

<h1>ISMPool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ISMPool/ISMPool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ystem in Unreal Engine designed to optimize the use of Instanced Static Meshes (ISM). Rather than each Actor or Component creating and managing its own individual InstancedStaticMeshComponent, the pool allows multiple systems to share a centralized, managed array of mesh instances.

This module is primarily utilized by the Geometry Collection (Chaos Destruction) system and the Procedural Content Generation (PCG) framework. It facilitates the elimination of the massive overhead caused by thousands of unique components, instead batching them into a single, high-performance rendering stream.

Practical Usage Tips and Best Practices
1. Use for High-Fidelity Chaos Debris

When large buildings fracture, they generate thousands of small, repetitive pieces (like bricks or splinters). By enabling ISM Pooling on your Geometry Collections, these “debris particles” are funneled into the pool. This practice leads to the elimination of draw-call spikes during large-scale destruction events.

2. Optimize PCG with Shared Pools

In dense procedural environments, the PCG system can use the ISMPool to manage foliage and props. Instead of every PCG Partition having its own ISM component, the pool shares the same instance buffer across partition boundaries. This leads to the elimination of redundant state changes on the GPU, significantly improving the frame rate in open-world scenes.

3. Minimize Level Streaming Hitches

Registering a single InstancedStaticMeshComponent with 10,000 instances can cause a significant hitch during level streaming. By using the ISMPool, the engine can manage the “hydration” of these instances more granularly. This assists in the elimination of frame drops as the player moves between World Partition cells.

4. Leverage “Elimination” of Unique Scene Proxies

Every standard component creates a “Scene Proxy” on the Render Thread. If you have 500 unique fractured pillars, that creates 500 proxies. Using the ISMPool collapses these into a shared pool renderer. This facilitates the elimination of the CPU overhead required to manage thousands of individual proxy objects in the renderer.

5. Monitor via “stat ISMPool”

To verify that your assets are being correctly pooled, use the console command stat ISMPool. This displays a real-time breakdown of how many instances are active and how many “descriptors” (unique mesh/material combinations) are currently in use. Checking these stats is a best practice for the elimination of misconfigured assets that are failing to pool.

6. Combine with Custom Primitive Data (CPD)

Since the pool batches many instances together, you cannot easily change individual actor parameters. Use Custom Primitive Data to pass unique values (like color or wear) to specific instances within the pool. This allows for visual variety while maintaining the elimination of unique material instances.

7. Configure Async Physics State Creation

As of UE 5.6+, pooling can be combined with asynchronous physics initialization. Setting p.Chaos.EnableAsyncInitBody=True allows the ISMPool’s collision data to be built on a background thread. This practice leads to the elimination of “Game Thread stalls” when spawning a massive amount of pooled debris at once.

8. Verify Module Dependencies in C++

If you are implementing a custom system that needs to interface with the pool (e.g., a custom destruction wrapper), you must add "ISMPool" to your Build.cs. Proper module referencing is required for the elimination of linker errors when trying to access the FISMPool or FISMComponentPool structures in your native code.