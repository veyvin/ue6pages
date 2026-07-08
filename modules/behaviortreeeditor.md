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

nreal Engine that provides the visual interface and tools for creating, modifying, and debugging AI logic via the Behavior Tree (BT) system.

What it is and What it’s used for

This module extends the Unreal Editor’s framework to handle the unique requirements of AI graph editing. While the AIModule handles the runtime execution of Behavior Trees, the BehaviorTreeEditor manages the graph-to-asset serialization and the visual node-based experience.

Primary uses include:

Graph Authoring: Providing the specialized canvas for connecting Composites (Selectors, Sequences), Tasks, Decorators, and Services.
Blackboard Integration: Syncing the Behavior Tree with its associated Blackboard asset, ensuring keys are correctly mapped to node properties.
Visual Debugging: Displaying real-time execution flow during Play In Editor (PIE), highlighting the active branch and node status (Success, Failure, or Running).
Editor Customization: Allowing developers to extend the context menus and visual appearance of custom BT nodes.
Practical Usage Tips and Best Practices
1. Use BTGraph and BTGraphNode for Extensions

If you are building a custom tool that needs to programmatically generate or modify trees, look at UBTGraph and UBTGraphNode. These are the editor-only counterparts to the runtime UBehaviorTree and UBTNode classes.

2. Leverage the “Execution Index” for Debugging

When viewing a tree in the editor during PIE, notice the numbers in the top-right corner of each node. This is the Execution Index. The BehaviorTreeEditor uses this to show the priority of execution (left-to-right). If your AI is behaving unexpectedly, check this index to ensure your high-priority “Eliminate Target” branches are actually to the left of “Patrol” branches.

3. Optimize with Shared Node Instances

The editor encourages the use of Shared Instances by default to save memory. If you are creating custom C++ Tasks, ensure they are thread-safe and don’t store agent-specific data in member variables. If a task must store state, use the GetInstanceMemorySize and NodeMemory system defined by the UBTNode base class.

4. Custom Node Icons and Colors

To make your custom AI nodes more readable for designers, you can override GetNodeIcon or GetNodeTitleColor within your node class. The BehaviorTreeEditor uses these to visually distinguish between different types of tasks (e.g., coloring “Combat” nodes red and “Navigation” nodes green).

5. Blackboard Key Filters

When creating a custom Task or Decorator in C++, use the FBlackboardKeySelector struct. In the editor, you can use the AllowedTypes metadata to filter which keys appear in the dropdown (e.g., only showing “Vector” keys for a “MoveTo” task). This prevents designers from picking invalid data types.

6. Utilize Search and Navigate

Large Behavior Trees can become complex. Use the “Search” tab (Ctrl+F) within the Behavior Tree Editor to quickly find specific Tasks or Blackboard keys. The editor will highlight the node and center the view, which is essential for the elimination of time wasted hunting through massive graphs.

7. Avoid Logic in Decorators

A best practice enforced by the editor’s design is to keep Decorators (blue nodes) as pure conditionals. If a Decorator needs to perform heavy calculations to decide a branch’s validity, move that logic into a Service (green node) that updates a Blackboard key, then have the Decorator simply check that key.

8. Verify Graph Consistency

The BehaviorTreeEditor performs a “validation” pass before saving. Pay attention to the compiler results in the editor; it will catch errors such as a Root node with no children or Decorators attached to nodes that don’t support them. Fixing these in the editor prevents runtime AI crashes.