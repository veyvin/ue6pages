---
layout: default
title: KismetWidgets
---

<!-- ai-generation-failed -->

<h1>KismetWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/KismetWidgets/KismetWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BlueprintGraph, ClassViewer, ContentBrowserData, Core, CoreUObject, EditorFramework, EditorWidgets, Engine, InputCore, Slate, SlateCore, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

designed to provide the “Blueprints look and feel” for custom editor tools. “Kismet” is the internal codename for the Blueprints system, and this module exposes the UI components used within the Blueprint Graph, Material Editor, and various search interfaces.

Its primary purpose is to allow developers to build professional-grade editor extensions that remain visually consistent with the rest of the engine. By using these widgets, you can eliminate the time spent trying to manually recreate complex UI elements like the Blueprint search bar, pin-style selectors, or gradient pickers.

Practical Usage Tips and Best Practices
Implement Native Search with SSearchBox
The SSearchBox included in this module is far more advanced than a standard SEditableText. It includes the magnifying glass icon, a “clear” button, and built-in styling for the Blueprint editor. Use this to eliminate visual friction in your custom utility windows.
C++
	    if (Target.Type == TargetType.Editor)

	    {

	        PrivateDependencyModuleNames.AddRange(new string[] { "KismetWidgets" });

	    }

	    ```

	 

	*   **Prefer SSearchBox for Editor Tools**  

	    The `SSearchBox` widget in this module is much more advanced than a standard text input. It includes the magnifying glass icon, a "clear" button, and built-in styling that matches the Blueprint "Find" results. Use this to **eliminate** the need for manual UI styling in your custom tool search bars.

	 

	*   **Utilize SKismetLinearExpression for Math**  

	    If your tool allows users to input mathematical formulas (like the "Math Expression" node in Blueprints), use `SKismetLinearExpression`. It provides a specialized input field that handles complex horizontal layouts, helping you **eliminate** the clutter of deeply nested UI boxes for simple math logic.

	 

	*   **Leverage SScrubWidget for Timelines**  

	    When building a custom animation or sequencer-like tool, use `SScrubWidget`. It provides the standardized "draggable timeline" functionality seen at the bottom of the Blueprint and Sequencer editors, which helps you **eliminate** the complexity of handling mouse-drag delta math manually.

	 

	*   **Apply Native Graph Styling**  

	    Many widgets in this module reference `FAppStyle::Get()` to pull their brushes and fonts. When using these widgets in your own Slate code, avoid hard-coding colors; instead, use the `FAppStyle` parameters to **eliminate** visual bugs when the user switches between the "Dark" and "Light" editor themes.

	 

	*   **Handle Filtering via SSearchBox Delegates**  

	    When using `SSearchBox`, bind the `OnTextChanged` and `OnTextCommitted` delegates. This allows you to perform real-time filtering of lists or arrays as the user types, helping you **eliminate** "input lag" by ensuring your search logic is optimized for frequent updates.

	 

	*   **Integrate with SLevelEditorGradient**  

	    For tools that require color transitions (like post-process settings or procedural sky tools), use `SLevelEditorGradient`. It provides the standard Unreal gradient bar with draggable stops, helping you **eliminate** the difficulty of writing a custom multi-stop color picker.

	 

	*   **Use SKismetInspector for Data View**  

	    If you need to show a simplified "Details Panel" for a specific set of properties within a custom window, look at `SKismetInspector`. It is a streamlined version of the full Details view, optimized for viewing and editing `UObject` properties in a compact list.
Copy code
Add Module Dependencies
To use these widgets in C++, you must add "KismetWidgets" to your PrivateDependencyModuleNames in your Build.cs file. Since these are editor-only, ensure they are wrapped in an #if WITH_EDITOR block or placed within an Editor-specific module to eliminate packaging errors for your final game build.
Use SKismetLinearExpression for Math UI
If your tool allows users to input mathematical formulas (similar to the Math Expression node), use SKismetLinearExpression. It provides a clean, horizontal layout for complex expressions, helping you eliminate cluttered vertical stacks of input boxes.
Leverage SScrubWidget for Timelines
For any tool requiring a time-based slider (like a custom animation preview or sequence editor), use SScrubWidget. It provides the standardized “draggable timeline” look seen in the Blueprint editor’s timeline component, allowing you to eliminate manual mouse-delta math for slider interactions.
Utilize SLevelEditorGradient for Color Ramps
When creating tools for procedural generation or sky settings, use the SLevelEditorGradient widget. It provides a native interface for managing color stops, which helps you eliminate the difficulty of writing a custom multi-point color picker from scratch.
Apply FAppStyle for Visual Consistency
KismetWidgets are designed to work with FAppStyle. When configuring colors or padding for these widgets, always reference the engine’s style set rather than hardcoding values. This ensures that your UI elements correctly adapt to “Dark Mode” or “Light Mode” and helps you eliminate visual bugs across different editor versions.
Handle Filtering via Delegates
The search and selection widgets in this module rely heavily on delegates (e.g., OnTextChanged, OnSelectionChanged). Always ensure your search logic is optimized to handle these delegates quickly to eliminate input lag when a user is typing in a large project.
Use SKismetInspector for Data Editing
If you need a simplified version of the “Details” panel within a small popup or custom node, look at SKismetInspector. It is a streamlined property editor that helps you eliminate the overhead of spawning a full, heavy-weight Details View when only a few properties need to be exposed.