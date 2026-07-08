---
layout: default
title: CurveTableEditor
---

<!-- ai-generation-failed -->

<h1>CurveTableEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CurveTableEditor/CurveTableEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, CurveEditor, EditorFramework, EditorWidgets, Engine, InputCore, Slate, SlateCore, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t provides the interface and functionality for managing Curve Tables. It is a specialized sibling to the Data Table Editor, designed specifically for handling floating-point data over time or across specific ranges.

What it is and What it’s used for

Curve Tables are data assets that store multiple curves in a spreadsheet-like format. The CurveTableEditor module allows developers to visualize these curves graphically, edit keys directly, and manage the relationship between different data rows.

Primary uses include:

Gameplay Balancing: Storing scaling data, such as weapon damage falloff over distance or XP requirements per character level.
External Data Integration: Importing and exporting data from Excel or Google Sheets via .csv or .json formats.
Interpolation Control: Defining how values transition between data points (Linear, Constant, or Cubic).
Visual Debugging: Using the Curve Table View to compare multiple data rows visually to ensure smooth scaling and the elimination of unwanted spikes in gameplay values.
Practical Usage Tips and Best Practices
1. Export Before You Import

When creating a Curve Table from an external spreadsheet, always create a dummy Curve Table in Unreal first, add one row of sample data, and Export as CSV. This provides you with the exact header format and column syntax required by the engine, preventing import errors caused by missing row names or incorrect formatting.

2. Choose the Correct Interpolation Mode

When importing a CSV, you must choose between Linear, Constant, or Cubic.

Use Constant for discrete steps (e.g., character level-ups).
Use Linear for straightforward scaling (e.g., damage falloff).
Use Cubic for smooth, natural curves (e.g., vehicle acceleration). Note that you cannot mix interpolation types within a single Curve Table; if you need different types, split them into separate assets.
3. Use the Curve View for Visual Verification

Inside the editor, toggle the Curve View (the graph icon). This allows you to see all rows superimposed on a single graph. This is the best way to catch “rogue” data points where a typo in a spreadsheet might have created a massive performance spike or a sudden drop in a character’s stats.

4. Leverage Composite Curve Tables

For large projects, use Composite Curve Tables. These allow you to merge multiple individual tables into one runtime object. This is a best practice for modular development, as it allows different designers to work on different stat categories (e.g., “WarriorStats” and “MageStats”) without causing merge conflicts in source control.

5. Integrate with Scalable Floats

The most powerful way to use Curve Table data is via the FScalableFloat struct. This allows you to reference a specific row in a Curve Table directly in a Blueprint or C++ class. It provides a built-in “Preview” slider in the Details panel so you can see the value at a specific “Level” or “Time” without running the game.

6. Rename and Delete via Right-Click

The Curve Table Editor allows for internal organization. You can right-click any curve in the list to Rename or Delete it. Renaming a curve in the editor is safer than doing it in a CSV, as Unreal will attempt to maintain references to that row name throughout your project.

7. Keep Row Names Short and Standardized

Because curves are often accessed via FName lookups, establish a strict naming convention (e.g., Dmg_Pistol_Base). This reduces the chance of typos when calling the data in Blueprints and ensures that your search filters in the Curve Table Editor remain effective as your project grows.

8. Use for Non-Linear Logic

Avoid using complex If/Else branches for scaling logic. Instead, map your logic to a Curve Table. For example, instead of calculating complex math for an “Elimination Multiplier” based on player health, simply look up the health percentage on a curve. This moves the balancing logic out of code and into a designer-friendly asset.