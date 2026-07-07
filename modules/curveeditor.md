---
layout: default
title: CurveEditor
---

<!-- ai-generation-failed -->

<h1>CurveEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CurveEditor/CurveEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AppFramework, ApplicationCore, Core, CoreUObject, EditorFramework, Engine, InputCore, PropertyEditor, SequencerWidgets, Slate, SlateCore, TimeManagement, ToolMenus, TraceLog, UMG</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ion of animation curves, keys, and tangents across Unreal Engine.

Description and Purpose

This module serves as the shared framework for all “spline-based” editing in the editor. It powers the Curve Editor found in Sequencer, the Niagara Curve Editor, and standalone Curve Assets. Its primary purpose is to allow developers to fine-tune how values change over time using a visual 2D graph. By providing precise control over interpolation (Linear, Constant, Cubic) and tangent weights, it enables animators and technical artists to create smooth, natural transitions for everything from camera movement to material parameters.

Practical Usage Tips and Best Practices
Utilize Normalized View Mode
When editing multiple curves with vastly different value ranges (e.g., a Rotation curve ranging from 0–360 and a Scale curve from 0–1), switch to Normalized View. This scales all visible curves to fit the same vertical space, helping you eliminate excessive zooming and allowing you to compare the timing of curves regardless of their raw values.
Leverage Buffered Curves for Comparison
Use the Buffer Curve feature (found in the Curve Editor toolbar) to take a “snapshot” of your current curve before making experimental changes. If you are unhappy with your adjustments, you can visually compare the new curve against the buffered version or swap back to it, which helps eliminate the risk of losing a polished animation state.
Master the Lattice Tool for Group Editing
The Lattice Tool (introduced/refined in UE 5.6) allows you to select a group of keys and deform them within a bounding box. You can stretch, squash, or skew entire sections of an animation at once. This is much faster than moving individual keys and helps you eliminate tedious manual adjustments when retiming a sequence.
Apply Filters to Clean Dense Data
If you have “baked” animation data with a key on every single frame, use the Curve Editor Filters (such as the Butterworth or Simplify filters). These algorithms remove redundant keys while maintaining the curve’s shape, which helps eliminate unnecessary data overhead and makes the curve easier to edit manually.
Smooth Transitions in Elimination Sequences
When creating a cinematic for a player elimination, use Weighted Tangents on the camera or character movement curves. By pulling the tangent handles further out, you can create a “slow-in/slow-out” effect that adds weight and impact to the moment of elimination, making the animation feel more professional.
Use Smart Snapping to Maintain Precision
Enable Smart Key Snapping to ensure your keys stay aligned with whole frames or specific value increments. This is critical for preventing “sub-frame” keys that can cause jitter in the simulation. Keeping your keys snapped helps eliminate micro-stuttering in your final exported cinematics.
Store Reusable Curves as Assets
If you find yourself creating the same “ease-in” curve frequently, right-click the curve and export it as a Curve Asset (Float, Vector, or Linear Color). You can then reference this asset in Blueprints via a Timeline or a Get Float Value node, allowing you to eliminate redundant work by reusing the same math across multiple systems.
Fix Rotation Flips with the Euler Filter
If a character’s limb or a camera does a “360-degree flip” between two keys (common in imported FBX data), apply the Euler Filter. This filter recalculates the rotation values to find the shortest path between keys, which will eliminate “gimbal lock” artifacts and erratic spinning.