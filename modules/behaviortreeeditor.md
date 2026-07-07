---
layout: default
title: BehaviorTreeEditor
---

<!-- ai-generation-failed -->

<h1>BehaviorTreeEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/BehaviorTreeEditor/BehaviorTreeEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIGraph, AIModule, ApplicationCore, AssetDefinition, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, GameplayTags, GraphEditor, InputCore, KismetWidgets, PropertyEditor, RewindDebuggerInterface, Slate, SlateCore, ToolMenus, TraceServices, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

sponsible for the visual graph interface used to script Artificial Intelligence (AI) in Unreal Engine. It extends the base Graph Editor to provide the specific logic, UI, and node-handling required for Behavior Tree assets and Blackboard assets.

This module manages the creation and connection of Composites (Selector, Sequence), Tasks, Decorators (conditionals), and Services. It also handles the runtime debugger integration, allowing developers to see the “active” path of the AI logic while the game is running.

Practical Usage Tips & Best Practices
1. Module Dependency for Custom Nodes

If you are developing custom C++ Behavior Tree nodes (Tasks, Decorators, or Services) that require custom UI or specialized property handling in the editor, you must include this module in your Editor Build.cs.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "BehaviorTreeEditor", "GraphEditor" });

	}
Copy code
2. Leverage the Runtime Debugger

While the game is running, you can open the Behavior Tree Editor to see a live execution flow. Use the “Step Back” and “Step Forward” features in the editor toolbar to analyze recent decisions made by the AI. This is the most efficient way to identify why a specific branch was “eliminated” or skipped during execution.

3. Use Decorators for Conditional Logic

Avoid putting complex “If/Else” logic inside a Task. Instead, use the Decorator system (the blue nodes attached to the top of Composites or Tasks). The Behavior Tree Editor is optimized to evaluate Decorators efficiently to decide whether a branch should even be entered, keeping your Task nodes focused on single actions.

4. Optimize Graph Readability with Services

Use Services (the green nodes) to update Blackboard data at regular intervals. The editor allows you to attach these to any Composite node. This centralizes data updates (like “Find Closest Enemy”) so that multiple sub-branches can share the same information without repeating the same calculation logic.

5. Blackboard Key Selectors

When writing custom C++ nodes, always use FBlackboardKeySelector for variable members. This tells the Behavior Tree Editor to provide a dropdown menu in the Details panel, allowing designers to easily pick which Blackboard variable (Key) the node should read from or write to.

6. Utilize Search and Focus

Behavior Trees can become massive. Use the Find Results tab (Ctrl+F within the editor) to search for specific nodes or Blackboard keys. Clicking a search result will focus the camera directly on that node, which is essential for navigating large, complex AI hierarchies.

7. Node Instancing Policy

Be mindful of the Node Instancing Policy set in the Details panel. By default, nodes are shared across all AI agents to save memory. If your node needs to store unique data (like a timer), set it to Instanced in the editor. Incorrect instancing settings can lead to one AI agent’s actions accidentally triggering the elimination of logic for another agent.

8. Modularize with Run Behavior Nodes

If a specific section of your tree is becoming too cluttered, use the Run Behavior task. This allows you to call another Behavior Tree asset as a sub-tree. The Behavior Tree Editor supports double-clicking these nodes to instantly open the referenced asset, promoting clean, reusable AI architecture.