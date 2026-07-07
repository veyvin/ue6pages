---
layout: default
title: ScriptDisassembler
---

<!-- ai-generation-failed -->

<h1>ScriptDisassembler</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ScriptDisassembler/ScriptDisassembler.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed to translate compiled Blueprint bytecode into human-readable text.

Description and Purpose

When a Blueprint is compiled, its graph logic is converted into a series of low-level virtual machine (VM) instructions, known as bytecode, which the engine’s Script VM executes at runtime. The ScriptDisassembler module provides the tools—specifically the FKismetBytecodeDisassembler class—to reverse this process for debugging and optimization purposes. Its primary purpose is to allow developers to inspect exactly what the Blueprint compiler has generated “under the hood.” By analyzing this output, developers can eliminate inefficient logic chains, identify hidden overhead in complex nodes, and verify how variables are being accessed or replicated at the instruction level.

Practical Usage Tips and Best Practices
Use the Kismet.Disassemble Console Command
The easiest way to invoke this module is via the console. Type Kismet.Disassemble [BlueprintName] in the editor. This will output the full bytecode breakdown to the log, helping you eliminate the need for custom C++ code just to see the VM instructions for a specific asset.
Analyze High-Cost Loops
If a Blueprint loop is causing performance hitches, use the disassembler to check the number of instructions per iteration. Identifying “Instruction Bloat” (where a single node expands into dozens of VM commands) is a best practice to eliminate CPU-bound bottlenecks in your gameplay logic.
Debug Blueprint Compilation Issues
When a Blueprint behaves differently in a packaged build than in the editor, use the disassembler to compare the bytecode. This helps you eliminate “ghost” bugs where the compiler might have optimized away a node that it perceived as unreachable.
Optimize Variable Access
The disassembler reveals whether the VM is using “Local” versus “Member” variable access. To eliminate unnecessary overhead in high-frequency functions (like those on a Timer), use the disassembler to verify that frequently used values are stored in local variables rather than being pulled from a distant component every instruction.
Verify “Pure” Function Overhead
Pure functions (nodes without execution pins) are re-evaluated every time they are called. Use the ScriptDisassembler to see how many times a single Pure node is actually being executed. This often reveals redundant math that you can eliminate by caching the result in a variable instead.
Check for Script VM Exceptions
If you encounter a “Script Stack Overflow” or an “Infinite Loop” error, the disassembler can show you exactly which bytecode instruction triggered the elimination of the script’s execution. Match the instruction offset in the error log to the disassembled text to find the culprit node.
Keep Output Logs Clean
Disassembling a complex Blueprint can generate thousands of lines of text. Use a dedicated text editor (like VS Code or Notepad++) to search the output for specific keywords like JumpIfNot or CallMath. This allows you to eliminate noise and focus on the specific logic branch you are investigating.
Restrict to Non-Shipping Builds
Because this module deals with the internal structure of your script logic, it is not included in Shipping builds. Only use it during the development and testing phases to eliminate any risk of exposing your project’s logic structure or increasing the final binary size.