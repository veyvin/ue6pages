---
layout: default
title: BlueprintRuntime
---

<!-- ai-generation-failed -->

<h1>BlueprintRuntime</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/BlueprintRuntime/BlueprintRuntime.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e execution framework and standard library for Blueprint visual scripting at runtime.

Description and Purpose

While the BlueprintGraph and KismetCompiler modules handle the creation and compilation of Blueprints in the Editor, BlueprintRuntime is responsible for the actual “heavy lifting” during gameplay. It contains the virtual machine logic that interprets Blueprint bytecode and the extensive library of “Kismet” functions (like UKismetSystemLibrary and UKismetMathLibrary) that Blueprints call to perform actions. Its primary purpose is to provide a high-performance, stable environment for executing visual script logic across all platforms.

Practical Usage Tips and Best Practices
Prefer Native C++ for Tight Loops
Because BlueprintRuntime executes via a virtual machine, there is a small overhead for every node. For complex math or logic that runs every frame (Tick), implement the logic in C++ and expose it to Blueprints as a single function call to eliminate script execution bottlenecks.
Utilize Kismet Libraries in C++
The “Kismet” libraries within this module (e.g., UKismetMathLibrary) are not just for Blueprints. They contain highly optimized, static helper functions. You can call these directly in your C++ code to perform common tasks like Lerp, FInterpTo, or LineTrace without reinventing the wheel.
Minimize “Cast To” Nodes
Casting in Blueprints involves a runtime check within this module. Frequent casting can be expensive. Use Blueprint Interfaces to communicate between actors; this allows the BlueprintRuntime to call functions directly without needing to verify the specific class type, which is much more efficient.
Leverage Latent Actions Correctly
This module manages “Latent Actions” like Delay, Retriggerable Delay, and Move Component To. Be careful with these in loops; triggering multiple latent actions on the same actor can lead to unexpected behavior. Always check if a latent action is already running before starting a new one.
Optimization via Blueprint Pure Functions
Mark functions as “Pure” (no execution pin) only if they do not change state. Pure functions are re-evaluated every time their output pin is accessed. If you have a Pure function with expensive logic, the BlueprintRuntime may execute it multiple times in a single frame, so cache the result in a variable instead.
Event-Driven Elimination Logic
When handling a player elimination, avoid checking for “health == 0” in a Tick. Instead, use an Event Dispatcher or a Blueprint Implementable Event. This ensures the BlueprintRuntime only wakes up the elimination script exactly when needed, saving CPU cycles for the rest of the game.
Manage Large Arrays with Care
Operations on large arrays (sorting, filtering, or massive loops) within BlueprintRuntime can cause noticeable frame hitches. If you must process large data sets, consider using the Data Asset system or move the processing to a C++ background task to eliminate game-thread stalling.
Debug with “Print String” and Visual Logging
The Print String node is a part of this module’s system library. While useful, it should be disabled in shipping builds. Use the Development Only pin or wrap your debug logs in a macro to ensure that debug strings are eliminated from the final packaged game for better performance.