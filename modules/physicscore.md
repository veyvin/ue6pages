---
layout: default
title: PhysicsCore
---

<!-- ai-generation-failed -->

<h1>PhysicsCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/PhysicsCore/PhysicsCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides platform-independent types, interfaces, and shared logic for the physics system. It serves as the bridge between the high-level gameplay code (like Actors and Components) and the underlying physics solver (primarily Chaos).

While modules like PhysicsUtilities or Chaos handle complex simulations, PhysicsCore defines the essential “DNA” of physics objects, including collision profiles, surface types (Physical Materials), and the basic interfaces for scene queries like line traces and overlaps.

Practical Usage Tips and Best Practices
1. Manage Physical Materials for Surface Logic

The UPhysicalMaterial class is defined within PhysicsCore. This is the primary way to drive gameplay logic based on impact.

Best Practice: Use Physical Material Masks on complex meshes to assign different surface types (e.g., metal vs. wood) to a single material. This allows your trace logic to accurately identify the surface, helping you eliminate the need for multiple material slots just for collision detection.
2. Optimize Collision Profiles

PhysicsCore manages the global Collision Profiles (defined in Project Settings).

Tip: Create specific profiles like “Projectile” or “EnvironmentalDecoration” instead of using “BlockAll.” By narrowing down the object types a component checks against, you can eliminate unnecessary collision calculations and significantly improve CPU performance.
3. Utilize FPhysicsInterface for Custom Queries

If you are writing high-performance C++ code that needs to perform many scene queries (like a custom movement component):

Action: Use the FPhysicsInterface class. This provides a direct, low-level way to interact with the physics scene without the overhead of standard Blueprint-friendly nodes. This helps you eliminate the performance cost of wrapper functions during high-frequency checks.
4. Handle Contact Modification

PhysicsCore provides the infrastructure for Contact Modification, allowing you to change how the physics engine resolves a collision at the moment it happens.

Tip: Use FContactModifyCallback to create “one-way” platforms or custom friction behavior. This allows you to ignore or modify a collision dynamically, eliminating the need for complex trigger-box logic to manage physical interactions.
5. Include as a Dependency for Low-Level Tools

If you are building an engine plugin that interacts with raycasting or custom collision geometry:

Action: Add "PhysicsCore" to your PrivateDependencyModuleNames in your *.Build.cs. This ensures you have access to fundamental types like FHitResult and ECollisionChannel, which helps you eliminate compilation errors when referencing physics data structures.
6. Leverage BodySetup for Asset Optimization

The UBodySetup class, defined in this module, handles how collision geometry is cooked for a specific asset.

Best Practice: Check the “Collision Complexity” setting in the Static Mesh Editor. Setting it to “Project Default” or “Simple And Complex” correctly helps the engine eliminate the overhead of checking high-poly triangles when a simple box or sphere would suffice.
7. Profile with “Stat Physics”

Because PhysicsCore is the entry point for many queries, its performance impact is visible in the engine’s built-in profiler.

Action: Use the console command stat physics. This displays the time spent on scene queries and constraints. Monitoring these metrics allows you to eliminate “expensive” actors that are performing too many line traces per frame.
8. Implement Trace Channels Sparingly

Every custom Trace Channel added to the engine increases the bitmask size used in collision filtering.

Best Practice: Reuse existing channels by renaming them in the Project Settings rather than creating dozens of new ones. Keeping your channel count low helps you eliminate memory bloat and keeps the physics filtering logic efficient on the CPU.