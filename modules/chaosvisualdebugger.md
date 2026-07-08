---
layout: default
title: ChaosVisualDebugger
---

<!-- ai-generation-failed -->

<h1>ChaosVisualDebugger</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AgilitySDK, ApplicationCore, ChaosVD, Core, CoreUObject, DerivedDataCache, EditorViewport, Engine, InputCore, InstallBundleManager, MediaUtils, Messaging, MoviePlayer, MoviePlayerProxy, PreLoadScreen, ProfileVisualizer, Projects, PropertyAccessEditor, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolWidgets, TraceLog, UnixCommonStartup, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rectly from the physics thread (Rigid Solvers and RBAN). It captures a wealth of information—including particles, collision geometry, contact manifolds, scene queries, and joint constraints—that is often invisible during standard gameplay. By separating physics data from the main rendering loop, CVD allows you to inspect the “truth” of what the physics engine sees, making it indispensable for debugging jitter, tunneling, or complex interaction issues.

Practical Usage Tips and Best Practices
1. Launch via the Tools Menu

To open the debugger, navigate to Tools > Debug > Chaos Visual Debugger. You can also run it as a standalone program (located in Engine/Binaries/Win64/ChaosVisualDebugger.exe) if you need to debug a build without the full Unreal Editor overhead, which is useful for remote debugging or cross-team collaboration.

2. Use Data Flags to Filter Noise

The CVD viewport can become cluttered in complex scenes. Use the Show menu in the Viewport Toolbar to toggle specific data flags (e.g., Collision Data, Scene Queries, or Joint Constraints). If you are only investigating a character’s floor collision, disabling particle velocities and joint data will eliminate visual noise and improve the debugger’s performance.

3. Analyze Multi-Stage Solver Data

One of the most powerful features of CVD is the ability to see the simulation at different stages: Integrate, Collision Detection, Pre-Solve, and Post-Solve. If an object is clipping through a wall, check the Pre-Solve stage to see if the contact was correctly detected, then check Post-Solve to see if the solver’s correction was sufficient to eliminate the overlap.

4. Debug Multiplayer Desyncs (Network Tick Sync)

In UE 5.5+, CVD introduced Network Tick Sync. When recording a client/server session in PIE, use this mode to calculate the required offsets between the two. If you see a divergence between the client and server visualizations in the CVD viewport, it confirms a physics de-sync, allowing you to pinpoint the exact frame where the simulation diverged.

5. Inspect Scene Queries (Line Traces/Sweeps)

If a weapon hit isn’t registering, use the Scene Query Browser. CVD records all line traces, sweeps, and overlaps. You can search by tag name or type to find a specific query and see exactly what it hit (or missed) in the physics world, which is much more reliable than using standard DrawDebugLine nodes.

6. Color-Code for Identification

CVD allows you to customize particle colorization. Use different schemes to visually differentiate between Dynamic, Kinematic, and Static bodies. This helps you quickly identify if an object that should be stationary is accidentally marked as Kinematic, which could be wasting CPU cycles on the physics thread.

7. Investigate Logic on Elimination

Physics-based elimination effects (like ragdolls or fracturing geometry) can be difficult to debug in real-time. Use CVD to record the moment of elimination. You can inspect the impulse forces applied during the event and check the Collision Geometry Inspector to ensure that the character’s collision shapes are correctly transitioning to the ragdoll state without exploding or falling through the floor.

8. Monitor Performance via Standalone Mode

Recording physics data adds a small amount of overhead. If you are profiling a performance-critical section of your game, run CVD as a standalone executable and connect to your game instance via the Session Discovery System. This isolates the debugging UI from the game’s process, helping to eliminate performance interference and providing a more accurate look at the simulation’s impact on the CPU.