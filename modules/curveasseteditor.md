---
layout: default
title: CurveAssetEditor
---

<!-- ai-generation-failed -->

<h1>CurveAssetEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CurveAssetEditor/CurveAssetEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, CurveEditor, EditorFramework, Engine, InputCore, Slate, SlateCore, TimeManagement, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r interface and toolset for creating and modifying standalone Curve assets (UCurveFloat, UCurveVector, and UCurveLinearColor). Unlike the Curve Editor found within Sequencer, this module focuses on assets that exist independently in the Content Browser and are typically used for data-driven gameplay, material parameters, or timeline interpolation.

It enables developers to define mathematical relationships between a time/input value (X) and an output value (Y), providing a visual graph for the elimination of hard-coded interpolation logic.

Practical Usage Tips and Best Practices
1. Use the Right Curve Class

When creating a new Curve asset from the Miscellaneous category, choose the class that fits your data:

CurveFloat: Best for simple values like damage falloff or movement speeds.
CurveVector: Ideal for 3D paths or RGB scaling.
CurveLinearColor: Specifically designed for color gradients and Material integration. Choosing the correct type leads to the elimination of complex “Break Vector” logic in your Blueprints.
2. Master Tangent Types for Smoothness

Select your keys and use the toolbar to switch between tangent modes. Use Auto for smooth, natural curves, or Constant (stepped) if you need values to jump instantly at specific intervals. Properly tuning tangents ensures the elimination of “linear” or robotic-looking transitions in your animations.

3. Implement Snap-to-Grid for Precision

Enable both Time Snapping and Value Snapping in the toolbar when you need keys to land on exact integers or frames. This is a best practice for the elimination of floating-point drift, ensuring that a curve meant to end at exactly 1.0 does not end at 0.999.

4. Optimize Material Workflows with Curve Atlases

If you use many CurveLinearColor assets in your materials, group them into a Curve Atlas. This allows the engine to bake the curves into a single texture, resulting in the elimination of expensive per-curve texture lookups and improving GPU performance in material-heavy scenes.

5. Utilize “External Curves” in Timelines

Inside a Blueprint Timeline, you can click the “External Curve” slot to link a standalone Curve asset instead of drawing a local one. This allows multiple actors to share the same interpolation data, facilitating the elimination of redundant curve-editing work across different Blueprints.

6. Use the Retime Tool for Timing Adjustments

If your curve logic is perfect but the animation is too fast or slow, use the Retime Tool (found in the editor toolbar). It allows you to stretch or squash segments of the curve without manually moving every key, leading to the elimination of tedious keyframe management.

7. Leverage Normalized View Mode

When working with multiple curves in one asset (like a CurveVector), toggle Normalized View. This scales all curves to fit the vertical space of the window, regardless of their actual values. This is essential for the elimination of constant scrolling and zooming when one curve has a range of 0–1 and another has a range of 0–1000.

8. Import Data from CSV/JSON

For complex mathematical curves or real-world data, you can right-click a Curve asset and select Reimport. This allows you to import data from external spreadsheet files, aiding in the elimination of manual data entry for complex scientific or balancing tables.