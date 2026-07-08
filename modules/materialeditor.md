---
layout: default
title: MaterialEditor
---

<!-- ai-generation-failed -->

<h1>MaterialEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MaterialEditor/MaterialEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AdvancedPreviewScene, AppFramework, ApplicationCore, AssetRegistry, ContentBrowser, ContentBrowserData, Core, CoreUObject, DeveloperToolSettings, EditorFramework, EditorStyle, EditorSubsystem, EditorViewport, Engine, GraphEditor, InputCore, Kismet, Landscape, MainFrame, MaterialUtilities, PhysicsCore, Projects, PropertyEditor, RHI, RenderCore, Slate, SlateCore, SourceControl, ToolMenus, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed tools and UI required to author shaders within Unreal Engine. It acts as the visual frontend for the engine’s underlying HLSL (High-Level Shading Language) generation system.

What it is and What it’s used for

Located in Engine/Source/Editor/MaterialEditor, this module manages the Material Graph, where developers connect nodes (Material Expressions) to define surface properties. It translates these node networks into shader code that the GPU can execute.

Primary uses include:

Graph Editing: Managing the node-based workspace (UMaterialGraph) and the logic for connecting inputs like Base Color, Metallic, and Roughness.
Real-time Compilation: Handling the background compilation of shaders so changes can be previewed instantly in the viewport.
Asset Management: Providing the interface for Material Instances, allowing for rapid iteration of parameters without recompiling the base shader.
Optimization Tools: Providing the “Shader Code” view and instruction counts to help artists balance visual quality with performance.
Practical Usage Tips and Best Practices
1. Prioritize Material Instancing

Always create a “Master Material” and use Material Instances for individual assets. Modifying a Master Material requires a full recompile of all dependent assets, whereas changing a parameter in an instance is instantaneous. This is the most effective workflow for the elimination of wasted compilation time.

2. Monitor Instruction Counts

Use the Stats panel at the bottom of the Material Editor to keep an eye on “Base Pass Shader Instructions.” High counts directly impact GPU performance. Aim for the elimination of unnecessary math or texture samples to keep your shaders within a reasonable performance budget for your target hardware.

3. Use Named Reroute Nodes for Cleanliness

Large material graphs can quickly become a “spaghetti” of wires. Use Named Reroute Declaration and Usage nodes to transport data across the graph without visible wires. This practice is essential for the elimination of visual clutter, making the logic easier for other team members to read.

4. Leverage “Flatten Material” for Complex Shaders

If a material has dozens of layers and heavy math, use the Material Analyzer and the “Flatten” tool to bake the logic into a single texture. This leads to the elimination of heavy runtime overhead for assets that are far away or used in large quantities.

5. Implement Material Functions for Reusability

If you find yourself building the same logic (like a specific type of wind or texture panning) in multiple materials, move that logic into a Material Function. This allows for the elimination of redundant node setups and ensures that a single update to the function propagates everywhere.

6. Utilize the “Stop” Feature on Previews

If you are working on a complex shader that causes editor lag, click the “Stop” icon on the preview viewport or disable “Live Preview.” This results in the elimination of constant GPU updates, allowing you to move nodes and build logic smoothly on lower-end machines.

7. Verify Results with Buffer Visualization

While in the Material Editor, use the Viewport Lit/Unlit dropdown to check specific buffers like “Roughness” or “World Normal.” Inspecting these individual channels is a best practice for the elimination of subtle material bugs that are masked by lighting and reflections.

8. Strategic Elimination of Unused Parameters

Unused parameters and “Static Switches” that aren’t hooked up still take up space in the UI and can lead to confusion. Periodically clean your graph and perform the elimination of disconnected nodes. This keeps the Material Instance editor clean and ensures the generated shader code is as lean as possible.