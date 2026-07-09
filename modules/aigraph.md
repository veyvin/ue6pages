---
layout: default
title: AIGraph
---

<!-- ai-generation-failed -->

<h1>AIGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AIGraph/AIGraph.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, ApplicationCore, BlueprintGraph, Core, CoreUObject, EditorFramework, EditorStyle, Engine, GraphEditor, InputCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ned to facilitate the creation of custom visual graph editors for AI-related assets. It provides the base framework used by systems like Behavior Trees and Environment Query System (EQS), offering specialized classes for nodes, pins, and graph schemas that handle AI-specific logic like execution flow, parent-child hierarchies, and sub-node attachments (e.g., Decorators or Services).

Practical Usage Tips and Best Practices
Configure Module Dependencies Since AIGraph is an editor-specific module, it should be added to your project’s .Build.cs file within the Editor module target. It is used to extend the Unreal Editor’s functionality rather than for runtime gameplay code.
C#
	    // In YourProjectEditor.Build.cs

	    PublicDependencyModuleNames.AddRange(new string[] { "AIGraph", "GraphEditor", "UnrealEd" });

	    ```

	 

	*   **Inherit from UAIGraphNode for Logic Mapping**

	    Always inherit from `UAIGraphNode` for your visual nodes. This class includes a `NodeInstance` pointer, which is crucial for syncing the visual editor node with the actual runtime AI object (e.g., a `UBTTaskNode`). This allows the editor to reflect property changes in real-time.

	 

	*   **Implement Schema Constraints in UAIGraphSchema**

	    Use your custom `UAIGraphSchema` (inherited from `UAIGraphSchema`) to define connection rules. AI graphs are often strict (e.g., a decorator can only be attached to a composite). Overriding `CanCreateConnection` ensures designers cannot create invalid AI logic paths.

	 

	*   **Utilize Execution Order Visuals**

	    A key feature of `AIGraph` is the ability to display execution indices (the small numbers on Behavior Tree nodes). Ensure your custom nodes call `UpdateVisualNode()` when the graph topology changes so that execution indices remain accurate and visible to the designer.

	 

	*   **Manage Sub-Node Logic (Decorators/Services)**

	    If your AI system uses "sub-nodes" (like Behavior Tree Decorators), use the `SubNodes` array within `UAIGraphNode`. This allows you to stack multiple logic blocks on a single visual node without cluttering the graph with infinite wires.

	 

	*   **Implement PostEditChangeProperty Hooks**

	    To ensure your runtime AI assets stay in sync with the visual graph, override `PostEditChangeProperty` in your `UAIGraphNode`. This allows you to push changes from the editor node's details panel directly into the runtime object instance immediately.

	 

	*   **Customizing Node Appearance with SGraphNodeAI**

	    For specialized UI (like the unique shape of EQS nodes), you will need to pair your `UAIGraphNode` with a Slate widget inherited from `SGraphNodeAI`. This gives you full control over the node’s color, icons, and "pinned" property visibility.

	 

	*   **Handle Copy-Paste via Component Serialization**

	    When implementing copy-paste for custom AI graphs, ensure that your `UAIGraphNode` correctly handles the duplication of its `NodeInstance`. Use `StaticDuplicateObject` to ensure that pasted nodes get their own unique runtime object instances rather than sharing references with the original.
Copy code
Inherit from UAIGraphNode for Data Syncing When creating a custom AI graph tool, inherit your visual nodes from UAIGraphNode. This class includes a NodeInstance pointer, which is essential for maintaining a link between the visual node in the graph and the actual runtime AI object it represents.
Implement Connection Constraints in the Schema Use a custom UAIGraphSchema to define strict rules for your AI logic. For example, you can override CanCreateConnection to ensure that a “Sensor” node can only be connected to a “Logic” node, preventing designers from creating invalid execution paths.
Utilize Sub-Nodes for Modular Logic The AIGraph module supports “Sub-Nodes,” which allow you to attach logic blocks (like Decorators in a Behavior Tree) directly onto a parent node. Use the SubNodes array in UAIGraphNode to manage these without creating extra wires, keeping the graph clean.
Override GetNodeTitle and GetNodeTitleColor To make your custom AI graph readable, override GetNodeTitle and GetNodeTitleColor. Use distinct colors for different node types (e.g., green for “Sensors,” red for “Elimination” logic, blue for “Actions”) so designers can identify node purposes at a glance.
Handle Order of Operations AI graphs often rely on a specific execution order (left-to-right). Ensure your custom graph calls UpdateVisualNode() or triggers a re-sort of child nodes whenever a connection is moved, ensuring the execution index displayed on the node is always accurate.
Manage Copy-Paste with StaticDuplicateObject When implementing copy-paste functionality for your custom AI graph, ensure that you use StaticDuplicateObject to clone the NodeInstance. This prevents the “pasted” node from sharing the same data instance as the “copied” node, which would cause unintended shared state bugs.
Use SGraphNodeAI for Custom UI If your node needs specialized visuals (like the icons or state indicators found in the State Tree editor), create a Slate widget inheriting from SGraphNodeAI. This allows you to customize the node’s “body” and add extra UI elements like progress bars or status toggles.