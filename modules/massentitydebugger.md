---
layout: default
title: MassEntityDebugger
---

<!-- ai-generation-failed -->

<h1>MassEntityDebugger</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MassEntityDebugger/MassEntityDebugger.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, Engine, InputCore, Json, MassCore, MassEntity, Projects, Slate, SlateCore, ToolWidgets, UMG, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ized debugging toolset for the Mass Entity framework, Unreal Engine’s high-performance Data-Oriented Design (ECS) system. While the core Mass module handles the simulation of thousands of entities, the debugger provides a visual interface to inspect fragment data, analyze processor execution, and troubleshoot entity archetypes in real-time.

It is essential for developers who need to look “under the hood” of the Mass simulation, as standard Actor-based debugging tools (like the Outliner) do not work for lightweight Mass entities.

Practical Usage Tips & Best Practices
1. Access the Debugger via the Tools Menu

The Mass Debugger is not a separate window that opens automatically.

Tip: Navigate to Tools > Debug > Mass Debugger to launch the interface. If you have updated Unreal Engine recently and the UI looks incorrect, use Window > Reset Layout within the debugger window to ensure all new tabs (like Entities and Processors) are visible.
2. Visualize Processor Overlaps and Access

Mass Entities rely on processors that read and write to specific fragments. Conflicts here can cause data corruption or performance hitches.

Best Practice: In the Processors Tab, use the “Show Fragment Access” button. Green indicates read-only access, while red indicates write access. Using this tool leads to the elimination of race conditions by identifying which processors are competing for the same data simultaneously.
3. Inspect UPROPERTY Fragment Data

Not all data in a fragment is visible by default in the debugger.

Tip: Only member variables within a fragment struct that are marked with the UPROPERTY() macro will appear in the Entities Tab. Ensure your internal simulation variables are reflected to the engine; this ensures the elimination of “invisible state” issues where an entity behaves incorrectly but its data appears empty.
4. Set Fragment Write Breakpoints

If a specific entity is behaving erratically, you need to know exactly which processor is changing its state.

Best Practice: Select an entity in the Entities Tab, find the suspect fragment, and click Set Write Breakpoint. The engine will break in your C++ IDE when that fragment is modified. This facilitates the elimination of logic bugs by pinpointing the exact frame a value is corrupted.
5. Leverage the Gameplay Debugger (GDT)

The Mass Debugger integrates directly with the standard Gameplay Debugger tool used during Play-In-Editor (PIE).

Tip: Press the ` (tilde) key during gameplay, then press Shift+O for the Entity Overview or Shift+V for Avoidance data. This allows for the elimination of guesswork regarding entity movement targets and steering behaviors in a live environment.
6. Debug Sparse Elements and Tags

Recent updates to the Mass framework introduced Sparse Elements, which are fragments that don’t cause an archetype change.

Best Practice: Use the Archetype Details view to inspect the SparseElement bitset. This provides an aggregated view of all elements in a chunk, assisting in the elimination of memory overhead by verifying that tags and sparse data are being applied only where intended.
7. Profile Processor Execution Phases

Mass simulation is divided into phases (e.g., Pre-Physics, Post-Physics).

Tip: Use the Processors Tab to see the execution order within these phases. If a system is lagging, check if it’s waiting on a dependency from a previous phase. Proper phase alignment leads to the elimination of “one-frame-behind” lag in your AI or crowd simulations.
8. Use Console Commands for Visual Overlays

Sometimes a UI window is too heavy for quick checks. The module supports several console commands for on-screen overlays.

Tip: Use mass.debug.FilterBySelectedEntity 1 to isolate debug shapes to only the entity you have selected. This results in the elimination of visual clutter when thousands of entities are on screen, allowing you to focus on a single agent’s logic.