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

n Unreal Engine designed to record, play back, and inspect Chaos Physics simulations with high precision.

Description and Purpose

This module provides a “Physics DVR” system that captures the internal state of the Chaos solver—including particles, collision constraints, joint settings, and scene queries—directly from the physics thread. Unlike standard visualizers that show what is happening on the Game Thread, CVD allows developers to see exactly what the physics engine sees. Its primary purpose is to help developers identify and debug complex physical issues like jittering, collision failures, and network de-syncs by providing a frame-by-frame, scrubbable timeline of the simulation independent of the project’s rendering state.

Practical Usage Tips and Best Practices
Launch via Tools Menu
You can quickly access the debugger by navigating to Tools > Debug > Chaos Visual Debugger. It can run as an integrated editor window or as a standalone program, which is useful for debugging packaged builds without the overhead of the full Unreal Editor.
Debug Network De-syncs with “Network Tick” Sync
In UE 5.5 and 5.6, CVD introduced a “Network Tick” sync mode. Use this to visualize server and client physics data side-by-side. If you see a divergence between the two representations, you have identified a network de-sync, allowing you to eliminate the root cause of “teleporting” objects in multiplayer.
Analyze Elimination Ragdolls
When a character undergoes an elimination and transitions to a ragdoll, use the CVD to inspect the “Post-Solve” stage. If the ragdoll experiences “jitter” or “explosive” forces, the debugger will show you exactly which collision constraints are overlapping or fighting, helping you eliminate the physics artifacts.
Utilize the Scene Query Browser
The debugger includes a dedicated browser for Scene Queries (line traces, sweeps, and overlaps). You can search by tag name or type to see every query made in a specific frame. This is essential for finding “invisible” performance killers like redundant traces that need to be eliminated.
Inspect Character Ground Constraints
For projects using Physics-Based Character Movement, CVD can record and visualize Ground Constraints. This allows you to see exactly how the character is interacting with the floor and why they might be sliding or getting stuck on geometry.
Minimize Recording Overhead
Recording physics data uses the Unreal Trace system, which is high-performance but not free. To eliminate performance hitches during recording, use the “Data Channels” settings in the CVD toolbar to only record the specific systems you are investigating (e.g., record only “Joints” and “Particles” but disable “Scene Queries”).
Use Generic Debug Draw Macros
You can record custom debug shapes (Spheres, Boxes, Lines) into the CVD timeline using C++ macros or Blueprint nodes. This is helpful for correlating gameplay events—like the exact moment an elimination trigger is activated—with the resulting physics behavior in the same timeline.
Scrub the Solver Stages
The CVD timeline allows you to see the physics state at different stages: Begin, Integrate, Detect Collisions, Pre-Solve, and Post-Solve. If an object falls through the floor, scrubbing through these stages helps you determine if the collision was never detected or if the solver failed to resolve it during the “Solve” phase.