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

r Unreal Engine’s physics system. It is independent of the specific physics solver (like Chaos), providing the common interfaces, data structures, and settings used across the engine to define how objects interact physically.

This module is primarily used to manage Physical Materials, Surface Types, and global physics state. By acting as a bridge between the high-level Engine module and the low-level simulation, it helps you eliminate the complexity of managing physics properties individually for every actor, allowing for a centralized, data-driven approach to physical interactions.

Practical Usage Tips and Best Practices
Centralize Surface Types in DefaultEngine.ini
Define your project-specific surface types (e.g., Grass, Wood, Metal) in the DefaultEngine.ini file under the [PhysicalMaterial.SurfaceTypes] section. This module maps these names to enums, helping you eliminate “magic strings” in your code when determining which impact sound or particle effect to play.
Leverage Physical Material Masks
In your Materials, use Physical Material Masks to assign different physical properties to different parts of a single mesh based on a texture. This allows a single character model to have different footstep sounds for boots vs. armor, helping you eliminate the need to split meshes into multiple components for sound logic.
Optimize Sleep Thresholds for Performance
Adjust the Sleep Threshold Multiplier within a Physical Material to dictate when a moving object should stop simulating. By raising these values for small, unimportant debris, you can eliminate unnecessary CPU calculations for objects that are barely moving, significantly improving performance in scenes with high actor counts.
Enable ‘Tick Async Physics’ for Determinism
In the Physics settings (managed by this module), enable Tick Async Physics (UE5+). This runs the physics simulation on a dedicated thread at a fixed rate, which helps you eliminate “jitter” or inconsistent behavior caused by variable frame rates, which is especially critical for networked multiplayer.
Configure Friction and Restitution Models
Use the Friction Combine Mode and Restitution Combine Mode settings within Physical Materials to decide how two interacting objects calculate their bounce. Setting these to “Min” or “Max” rather than “Average” can help you eliminate unpredictable bouncing behavior for specific gameplay items like grenades or bouncy balls.
Use ‘Project Point to Navigation’ with Physics Checks
When spawning items that must fall naturally, use the physics core logic to find the nearest floor. Combining this with a short LineTraceByChannel (using the ECC_Visibility or a custom Physics Channel) helps you eliminate actors spawning “inside” the floor or falling through the world.
Filter Collision via Object Channels
Avoid using “Block All” for every actor. Define custom Object Channels (like Projectile or AI_Trigger) in the Physics settings. Properly filtering which objects can interact helps you eliminate performance-heavy collision checks between actors that never need to touch.
Clean Up Physical Constraints on Elimination
When a simulated actor is destroyed (the “elimination” of the physics body), ensure that any Physics Constraints attached to it are also cleared. Leaving “broken” constraints active in the scene can cause the physics solver to work on null pointers or invalid references, which you should eliminate to prevent crashes.