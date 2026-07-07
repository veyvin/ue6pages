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

ite designed specifically for the Mass Framework, Unreal Engine’s high-performance Entity Component System (ECS).

Description and Purpose

This module provides a visual interface to inspect the state of thousands of entities that would otherwise be invisible or difficult to track via standard actor-based debugging. Its primary purpose is to allow developers to view “Fragments” (data) and “Tags” (states) associated with entities in real-time, as well as monitor the execution flow of “Processors.” By using the Mass Entity Debugger, you can eliminate the guesswork involved in data-oriented programming, ensuring that your logic is correctly iterating over the intended archetypes.

Practical Usage Tips and Best Practices
Launch via the Tools Menu
Access the debugger by navigating to Tools > Debug > Mass Debugger. If you have updated your engine version and the UI appears missing, use Window > Reset Layout within the debugger window to eliminate UI glitches and restore the latest tabs.
Utilize the Environment Picker
Mass can run in different “environments” (e.g., Editor vs. PIE). Always ensure the correct environment is selected in the picker at the top of the debugger. This is the only way to eliminate “No Entities Found” errors when you are looking for data while the game is actively running.
Inspect Processor Overlaps
In the Processors Tab, use the “Show Fragment Access” button. The debugger will highlight processors in green (Read-only) or red (Read/Write). This helps you eliminate race conditions by identifying multiple processors attempting to write to the same fragment simultaneously.
Set Fragment Write Breakpoints
You can set a breakpoint on a specific fragment for a specific entity in the Entities Tab. This will cause the engine to break into your C++ IDE whenever that piece of data is modified, helping you eliminate difficult-to-trace logic bugs where data is being overwritten unexpectedly.
Select Fragments for Data Inspection
In the Entities Tab, use the “Select Fragments” dropdown to choose which data members to monitor. Note that only variables marked with the UPROPERTY macro will be visible. Ensuring your C++ structs are reflected properly is the best way to eliminate “missing” data in the debugger.
Toggle Gameplay Debugger Categories
While in-game, press the backtick (`) key to open the Gameplay Debugger, then press Shift+O for the Mass Overview or Shift+V for Avoidance. This allows you to see steering and move targets in the 3D viewport, which helps you eliminate navigation artifacts in large crowds.
Filter by Archetype
Use the filtering options to narrow down the entity list to specific archetypes. Instead of scrolling through thousands of agents, focusing on a single archetype allows you to eliminate noise and find the specific entity that is failing its logic checks.
Monitor Chunk Fragmentation
Mass organizes entities into memory chunks. Use the debugger to ensure entities are being packed into archetypes as expected. Proper archetype management is essential to eliminate unnecessary memory overhead and maintain high cache-hit ratios for your processors.