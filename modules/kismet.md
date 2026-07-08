---
layout: default
title: Kismet
---

<!-- ai-generation-failed -->

<h1>Kismet</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Kismet/Kismet.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimGraph, AppFramework, ApplicationCore, BlueprintEditorLibrary, BlueprintGraph, Core, CoreUObject, DesktopPlatform, DeveloperSettings, DeveloperToolSettings, EditorFramework, EditorStyle, EditorViewport, EditorWidgets, Engine, EngineSettings, FieldNotification, GameplayTags, GraphEditor, HotReload, InputCore, InteractiveToolsFramework, Json, JsonObjectGraph, JsonUtilities, KismetCompiler, KismetWidgets, LiveCoding, MessageLog, Projects, PropertyEditor, SharedSettingsWidgets, Slate, SlateCore, Sockets, SourceControl, SubobjectDataInterface, SubobjectEditor, ToolMenus, ToolWidgets, TraceLog, TypedElementRuntime, UMG, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rint Visual Scripting system. While the user-facing system is called “Blueprints,” the underlying engine architecture still uses the “Kismet” moniker—a legacy carryover from Unreal Engine 3’s scripting system.

What it is and What it’s used for

Located in Engine/Source/Runtime/Engine/Classes/Kismet (for libraries) and Engine/Source/Editor/Kismet (for the compiler), this module acts as the bridge between visual nodes and executable bytecode. It manages the Kismet Virtual Machine (VM), which interprets the graphs you create in the editor.

Primary uses include:

Blueprint Compilation: Translating the visual node graphs into FKismetCompiledStatement objects that the engine can execute at runtime.
Static Math & System Libraries: Providing global utility functions (like KismetMathLibrary or KismetSystemLibrary) that appear as the standard nodes for Math, Traces, and Strings.
Bytecode Execution: Managing the instruction set that allows Blueprints to interact with native C++ properties and functions.
The Blueprint Compiler: Handling the “Compile” button logic, including variable scoping, pin connectivity validation, and error reporting.
Practical Usage Tips and Best Practices
1. Prefer Kismet Libraries in C++ for Convenience

When writing C++, you can include libraries like Kismet/KismetMathLibrary.h to access the exact same functions available in Blueprints (like RInterpTo or GetDirectionVector). This is a best practice for ensuring the elimination of logic discrepancies between your C++ code and your team’s Blueprints.

2. Monitor Blueprint VM Overhead

Every Blueprint node has a small “VM overhead” cost. For logic that runs every frame (Tick), the cumulative cost of these transitions can be high. Use the Unreal Insights profiler to check the “Blueprint” track; if the VM cost is too high, it is a best practice to move that specific logic to C++ for the elimination of performance bottlenecks.

3. Use “Pure” Functions Strategically

The Kismet compiler treats “Pure” nodes (nodes without execution pins) differently—they are re-evaluated every time an output pin is used. If a Pure node performs a heavy calculation, it is a best practice to cache the result in a variable to ensure the elimination of redundant, expensive calculations.

4. Leverage Kismet System Library for Debugging

The UKismetSystemLibrary contains essential debugging tools like DrawDebugSphere and PrintString. These are optimized to work with the Kismet VM’s lifetime management, ensuring the elimination of manual memory cleanup for temporary debug visuals.

5. Understand the “K2” Prefix

Inside the module, you will often see “K2” (short for Kismet 2). Nodes like K2_Node_Event or K2_Node_CallFunction are the specific classes that represent Blueprint nodes in the editor. If you are creating custom graph nodes, you will derive from these K2 classes to interface with the Kismet compiler.

6. Optimize with Blueprint Nativization (If Available)

Though deprecated in favor of better C++ practices in UE 5.x, the spirit of “Nativization” was to convert Kismet bytecode into machine code. The best modern practice is to manually “nativize” your heaviest Blueprint Function Libraries by rewriting them as C++ UBlueprintFunctionLibrary classes, leading to the elimination of VM overhead.

7. Avoid Giant “UberGraphs”

The Kismet compiler merges all Event Graph logic into one large “UberGraph” during compilation. For massive Blueprints, this can lead to slow compile times and complex debugging. A best practice is to move logic into Functions or Macros, which are compiled as separate contexts, aiding in the elimination of compiler slowdowns.

8. Strategic Elimination of Casts

Frequent “Casting” in Blueprints via the Kismet VM creates “Hard References,” loading the target class into memory. To prevent your memory usage from ballooning, use Blueprint Interfaces (which the Kismet module handles via a fast virtual lookup). This is the primary method for the elimination of unnecessary asset loading and circular dependencies.