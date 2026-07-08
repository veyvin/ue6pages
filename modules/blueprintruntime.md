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

cessing of Blueprints during gameplay. It acts as the bridge between the visual scripting logic created in the editor and the machine-executable instructions used by the engine at runtime.

Description

This module contains the Kismet Virtual Machine (VM), which interprets the bytecode generated when a Blueprint is compiled. It manages the execution flow of nodes, variable state, and function calls. Specifically, it handles the UBlueprintGeneratedClass, the class type that holds all the runtime data for an Actor or Object created via Blueprints. Without this module, the engine would be unable to translate visual “wires” and “nodes” into actual gameplay behavior.

Practical Usage Tips and Best Practices
1. Understand the VM Overhead

Every Blueprint node execution involves a small overhead as it passes through the Kismet VM. While insignificant for single events, this adds up in “tight loops” or functions that run every frame. To maintain high performance, move heavy mathematical computations or complex array sorting into C++ and expose them as a single BlueprintCallable function to eliminate unnecessary VM “hopping.”

2. Avoid “Tick” for Logic

Since the BlueprintRuntime must process the graph every frame for a Tick event, it is one of the most common performance bottlenecks. Use Timers, Delegates, or Event Dispatchers to trigger logic only when needed. This significantly reduces the per-frame load on the Blueprint interpreter.

3. Optimize Pure Functions

“Pure” functions (nodes without execution pins) are re-evaluated every time one of their output pins is used. If a pure function performs a complex calculation and you plug its result into five different nodes, the BlueprintRuntime will execute that function five times. To optimize, save the result of a pure function into a local variable once and use that variable instead.

4. Leverage “BlueprintPure” in C++

When creating helper functions in C++ for use in Blueprints, use the BlueprintPure specifier for functions that do not change state (like “Get” functions). However, ensure these functions are extremely fast, as the runtime will call them frequently. For expensive logic, always use execution pins to give the designer control over when the code runs.

5. Monitor the “Blueprint Time” in Insights

Use Unreal Insights or the stat Game console command to monitor how much time the BlueprintRuntime is consuming. Look specifically for “Blueprint Time.” If this value is high, it indicates that your visual scripting logic is too heavy and some parts should be nativized to C++.

6. Minimize Casting

The Cast To node is a common runtime operation. Frequent casting (especially inside a Tick or a loop) can be expensive because the BlueprintRuntime must verify the class hierarchy. Use Blueprint Interfaces to communicate between classes instead; this is faster and creates a “decoupled” architecture that is easier for the runtime to manage.

7. Properly Handle Actor Elimination

When an Actor is eliminated (Destroyed), the BlueprintRuntime clears its associated variables and stops its active latent actions (like “Delay” or “Retriggerable Delay”). Always ensure you use the IsValid node before accessing references to other Actors to prevent the runtime from attempting to access “Pending Kill” memory, which can lead to crashes or unstable behavior.

8. Use Data Assets for Static Data

If your Blueprint contains large arrays of constant data (like item stats or level configurations), do not store them as variables within the Blueprint graph. This increases the memory footprint of the UBlueprintGeneratedClass. Instead, use Data Assets or Data Tables. This allows the BlueprintRuntime to simply point to an external data source rather than loading and managing that data within the script class itself.