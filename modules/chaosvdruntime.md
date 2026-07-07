---
layout: default
title: ChaosVDRuntime
---

<!-- ai-generation-failed -->

<h1>ChaosVDRuntime</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosVisualDebugger/ChaosVDRuntime.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, TraceBasedDebuggers, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

m. Its primary purpose is to capture, serialize, and transmit physics simulation data from a running game (Client, Server, or Editor) to the CVD tool for inspection.

Unlike traditional debug drawing, this module records the exact state of the physics engine at various stages of a single frame—such as before and after integration or collision resolution. This allows developers to “rewind” and “scrub” through physics events to diagnose issues like tunneling, jittering, or incorrect constraint behavior.

1. Enable Data Channels for Performance

Recording every piece of physics data is resource-intensive. The module uses “Data Channels” to toggle specific categories of information.

Best Practice: Only enable the channels you need (e.g., SceneQueries for line traces or Joints for ragdolls). Use the console command: p.Chaos.VD.SetCVDDataChannelEnabled true [ChannelName] to toggle data without restarting the session.
2. Capture Multiple Simulation Stages

One of the most powerful features of this module is its ability to record “snapshots” within a single physics tick.

Tip: If you are debugging why a character is clipping through a floor, enable the PostIntegrate and PostSolve channels. This allows you to see if the character was moved into the floor by gravity (Integrate) and whether the collision solver successfully pushed them out (Solve).
3. Use for Remote Server Debugging

The module is built on top of Unreal Insights (Trace), making it network-aware.

Best Practice: You can record a session from a headless Linux server or a console build. Use the command: p.Chaos.StartVDRecording Server [YourWorkstationIP] to stream live physics data to your local machine for real-time debugging of networked physics.
4. Inject Custom Debug Shapes

You can record your own visual context directly into the CVD timeline using C++ macros provided by the runtime.

Tip: Use TraceDebugDrawLine or TraceDebugDrawSphere. These shapes are synchronized with the physics timeline, allowing you to see exactly where your gameplay logic was applying a force relative to where the physics objects were at that exact millisecond.
5. Debug Mover 2.0 and Character Constraints

This module includes specific support for Character Ground Constraints used in the new Mover 2.0 system.

Best Practice: When debugging floating or jittering characters, enable the CharacterGroundConstraints data channel. This will visualize the “Ground Constraint” logic, showing you the projected floor location and the hit result the movement component is currently using.
6. Manage File Size and Performance Overhead

Because the module serializes physics data, it can impact frame rate and generate large .utrace files.

Tip: Never leave a recording running in a performance-critical test. Use the p.Chaos.StopVDRecording command as soon as you have captured the problematic event to eliminate unnecessary CPU overhead and disk usage.
7. Inspect Scene Queries (Raycasts/Sweeps)

The runtime records the parameters and results of every LineTrace, Sweep, and Overlap performed by the physics engine.

Tip: If an AI isn’t “seeing” a player, check the SceneQueries in CVD. You can see the start/end points of the trace and exactly what geometry it hit (or missed), which is much more reliable than standard DrawDebugLine.
8. Use in Non-Shipping Builds Only

The ChaosVDRuntime is compiled out of Shipping builds to protect performance and prevent reverse-engineering of physics data.

Best Practice: Always test your physics debugging workflows in Development or Test configurations. If your logic depends on macros from this module, wrap them in #if WITH_CHAOS_VISUAL_DEBUGGER to ensure your code compiles correctly for final release.