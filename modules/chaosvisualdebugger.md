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

nd inspect the state of the Chaos Physics system. Unlike the standard viewport which shows the visual representation of actors, CVD captures the raw data as the physics engine sees it—including particles, collision contacts, constraints, and scene queries. It is a critical tool for debugging complex physical interactions, jittering, or unexpected behavior in simulations.

Practical Usage Tips & Best Practices
1. Filter Data via Data Channels

CVD can record a massive amount of information, which significantly impacts file size and performance.

Best Practice: Use the Data Channels menu to enable only what you need. For example, if you are debugging a character falling through the floor, enable “Collision” and “Scene Queries” but disable “Joint Constraints” to keep the trace file manageable.
2. Utilize Sub-Step Inspection

Chaos often runs multiple sub-steps within a single game frame to maintain stability.

Tip: Use the CVD timeline to scrub through individual solver stages (e.g., Integrate, Collision Detection, Post-Solve). This allows you to identify exactly which stage is causing a particle to explode or teleport, leading to the rapid elimination of math-related bugs.
3. Debug Network De-syncs with “Network Tick Sync”

In multiplayer projects, physics can often diverge between the client and server.

Best Practice: Use the Network Tick Sync mode introduced in UE 5.5+. This mode synchronizes the client and server recordings based on the physics tick rather than a timestamp. Any visual divergence you see in CVD is a confirmed network de-sync that requires investigation.
4. Leverage the Scene Query Browser

If your raycasts or sweeps (LineTraces) are not hitting targets correctly, use the dedicated Scene Query Browser within CVD. You can search by tag or type to see every query performed in a frame, including the exact start/end points and the specific collision shapes that were hit or ignored.

5. Record Custom Debug Shapes

You can “inject” your own visual data into a CVD recording using C++ macros or Blueprint nodes.

Tip: Use this to draw lines or spheres representing your custom logic (like AI pathing or explosion radii) directly into the physics timeline. This helps correlate your high-level gameplay logic with the low-level physics state.
6. Use the Standalone Debugger for Performance

Running the debugger inside the Editor while playing the game can be taxing on the CPU.

Best Practice: For heavy simulations or packaged builds, run the ChaosVisualDebugger.exe as a standalone program. You can connect it to a running game instance via a network connection or by loading a saved .cvd file recorded during a previous session.
7. Correlate with the Recorded Output Log

The CVD interface includes a Recorded Output Log that is synced with the playback timeline. When you scrub to a specific moment of physical instability, the log will automatically highlight the messages generated at that exact tick. This is essential for finding the elimination event or error message that triggered a physics failure.

8. Project-Independent Troubleshooting

CVD recordings are self-contained and do not require the original project files or assets to be viewed.

Tip: This makes them ideal for collaboration. A QA tester can record a physics bug and send the .cvd file to a programmer, who can inspect the raw collision geometry and solver state without needing to sync the entire project or rebuild the environment.