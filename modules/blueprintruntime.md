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

print visual scripting in Unreal Engine. While the KismetCompiler module is responsible for turning nodes into bytecode during development, the BlueprintRuntime module is the “Virtual Machine” (VM) that interprets and executes that bytecode during gameplay. It handles the logic for node execution, variable access, flow control (branches, loops), and the communication between Blueprints and native C++ code.

Practical Usage Tips & Best Practices
1. Understand the “Node Overhead”

Every node in a Blueprint represents a function call within the Blueprint VM. This results in a small amount of overhead compared to native C++.

Best Practice: For logic that must run every frame (like complex math in a Tick function), move the heavy calculations to C++. Use Blueprints to call that C++ function once, which results in the elimination of the overhead caused by dozens of individual math nodes.
2. Avoid Deep Nesting and Long Loops

The Blueprint VM has a “Runaway Loop” protection limit. If a loop (like a ForEachLoop) runs too many iterations in a single frame, the BlueprintRuntime will terminate the execution to prevent the engine from freezing.

Tip: If you need to process thousands of items, use the C++ Task System or a For loop in C++ to handle the data, then pass the result back to the Blueprint.
3. Minimize “Pure” Node Redundancy

Pure nodes (nodes without execution pins, like “Get Actor Location”) are re-evaluated every time an output pin is used.

Best Practice: If you are plugging the output of one Pure node into five different places, the BlueprintRuntime will execute that node five times. Instead, promote the result to a local variable and use that variable instead. This leads to the elimination of redundant calculations.
4. Leverage Blueprint Nativization (Legacy) vs. Best Practices

In older versions of Unreal, Nativization was used to convert Blueprints to C++ at cook time. In modern UE5, the focus has shifted to modularity.

Tip: If the BlueprintRuntime is showing up as a bottleneck in Unreal Insights, identify the specific “hot” functions and manually rewrite them in C++. The engine is designed for this “hybrid” workflow where C++ handles the performance-heavy lifting and Blueprints handle the high-level logic.
5. Profile with the “Blueprint Breadcrumb”

When debugging performance, use the Unreal Insights tool. The BlueprintRuntime module provides “Breadcrumb” data that allows you to see exactly which Blueprint and which specific node was executing when a performance spike occurred. This is essential for the elimination of mysterious hitches in your game thread.

6. Optimize Casting with Interfaces

Casting (Cast To MyCharacter) requires the BlueprintRuntime to verify the class hierarchy, which can be expensive and creates hard asset dependencies.

Best Practice: Use Blueprint Interfaces. Calling an interface function is a lightweight operation for the runtime VM and avoids loading unnecessary assets into memory, effectively streamlining the execution path.
7. Handle Elimination Events Efficiently

When an actor undergoes elimination, avoid running complex logic in the Destroyed event or EndPlay via Blueprints if possible. Because the BlueprintRuntime must manage the cleanup of visual script state, keeping these “teardown” events simple ensures that the garbage collector can reclaim the memory quickly without frame-rate stutters.

8. Use Event Dispatchers for “One-to-Many” Communication

Instead of having a “Boss” Blueprint loop through an array of “Minion” Blueprints to call a function on each, use an Event Dispatcher. This allows the BlueprintRuntime to handle the notification logic internally, which is more efficient than manual script-side loops and reduces the total node count in your graphs.