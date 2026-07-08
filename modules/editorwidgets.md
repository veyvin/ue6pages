---
layout: default
title: EditorWidgets
---

<!-- ai-generation-failed -->

<h1>EditorWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EditorWidgets/EditorWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetDefinition, Core, CoreUObject, EditorConfig, Engine, InputCore, Slate, SlateCore, ToolWidgets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

onents designed specifically for use within the Unreal Editor. While the base Slate and SlateCore modules provide generic UI elements (like buttons and text boxes), EditorWidgets contains high-level, “kit-like” widgets that are aware of the editor’s environment, assets, and workflows.

It is often referred to as the “Editor’s Lego Kit,” allowing developers to build custom tools and panels that look and behave identically to native engine features. Unlike ToolWidgets, which are designed to be platform-agnostic, EditorWidgets can have direct dependencies on editor-only systems like the Content Browser and the Actor selection state, facilitating the elimination of manual boilerplate when creating professional-grade editor extensions.

Practical Usage Tips and Best Practices
1. Implement SAssetDropTarget for Drag-and-Drop

Use the SAssetDropTarget widget to allow users to drag assets (like Textures or Meshes) directly from the Content Browser into your custom tool. It handles the complex logic of identifying the dropped asset type, leading to the elimination of custom, fragile drag-and-drop parsing code.

2. Use SSearchBox for Filterable Lists

When building a panel with many items, use the SSearchBox found in this module. It provides the standard Unreal “magnifying glass” styling and includes built-in delegates for text changes and searching. This ensures the elimination of UI inconsistency across your project’s internal tools.

3. Integrate SColorGradientEditor for Visual Control

If your tool requires the user to define color ramps or curves (common in VFX or procedural tools), use the SColorGradientEditor. It provides the same interactive “stop” system used in the Niagara and Material editors, aiding in the elimination of clumsy numeric-only color inputs.

4. Leverage SPositiveActionButton for Primary Tasks

To guide users toward the intended action (like “Import” or “Apply”), use the SPositiveActionButton. This widget automatically applies the standard green styling used for “success” actions in the engine, which assists in the elimination of user confusion in complex toolsets.

5. Nest Widgets within SExpanderArrow

For tools with many sections, use SExpanderArrow to create collapsible headers. This is a best practice for the elimination of “scroll fatigue,” allowing developers to hide advanced settings and keep their custom editor tabs clean and organized.

6. Utilize SBreadcrumbTrail for Deep Navigation

If your editor tool involves navigating through a hierarchy (like a folder structure or a node tree), use the SBreadcrumbTrail widget. It provides a clickable, path-like interface that matches the Content Browser’s look, leading to the elimination of “Back” buttons and simplifying navigation for the user.

7. Combine with SSpinBox for Numeric Precision

The SSpinBox provided in the editor context supports “scrubbing” (clicking and dragging to change values) and math expressions (e.g., typing 512*2). Using this instead of a standard text box leads to the elimination of input friction for technical artists and designers.

8. Verify Dependencies in Build.cs

Because this module is “Editor-Only,” ensure it is only added to your project’s Editor Module. Including it in a runtime module will cause packaging to fail. Correct module separation is essential for the elimination of “Missing Module” errors during the final build process.