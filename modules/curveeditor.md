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

es the visual interface for viewing and manipulating animation curves, splines, and numerical data over time.

Description

This module powers the “graph view” found in several major engine tools, including Sequencer, Niagara, and the Curve Asset editor. It manages the rendering of the grid, the interaction logic for selecting and moving keyframes, and the mathematical calculations for various interpolation modes (Linear, Constant, Cubic). Beyond simple keyframing, the CurveEditor module provides advanced filtering tools to smooth or simplify data, making it essential for technical animators and VFX artists who need precise control over value changes during a simulation or cinematic.

Practical Usage Tips and Best Practices
1. Maximize Vertical Space with Normalized Mode

When editing multiple curves with vastly different scales (e.g., a Rotation curve ranging from 0–360 and a Scale curve ranging from 0–1), use Normalized View Mode. This scales all selected curves to fit the same vertical space in the editor. This is a best practice for identifying timing correlations between different properties without having to scroll up and down constantly.

2. Use “Smart Reduce” to Clean Data

If you have dense keyframe data (often the result of baking an animation or recording a simulation), use the Smart Reduce filter. Found in the Curve Editor toolbar, this tool uses an algorithm to remove redundant keyframes that do not significantly contribute to the curve’s shape. This helps eliminate unnecessary data overhead and makes the curve much easier to edit manually.

3. Leverage Weighted Tangents for Fine Control

By default, curves often use non-weighted tangents. By switching a keyframe to Weighted, you gain control over the “length” of the tangent handle in addition to its angle. This allows you to create much longer, smoother transitions or sharper “eases” that are impossible with standard cubic interpolation, providing a more professional polish to your animations.

4. Utilize Buffered Curves for Comparisons

The Curve Editor allows you to “Buffer” a curve, which takes a snapshot of the current keyframes. As you continue to make edits, the buffered version remains visible as a ghosted line. This is an excellent way to experiment with different timings while maintaining a visual reference of the original state, allowing you to revert or compare results instantly.

5. Master the Lattice Tool for Bulk Edits

For complex curves, the Lattice Tool provides a bounding box over a selection of keyframes. By deforming the corners of this lattice, you can skew, stretch, or compress an entire section of an animation proportionally. This is much faster than moving individual keys and is the preferred method for adjusting the “intensity” of a pre-existing animation sequence.

6. Snap to Frames with Smart Snap

To ensure your keys align perfectly with your project’s frame rate, enable Smart Snap. This prevents keyframes from ending up on “sub-frames” (e.g., frame 10.5), which can cause jitter or unexpected interpolation results during playback. Keeping keys on whole frames is a vital best practice for maintaining consistent animation across different hardware.

7. Performance Gains via Keyframe Elimination

In high-performance scenarios like Niagara particles, every keyframe on a curve adds a small amount of memory and processing cost. Use the Curve Editor to simplify curves by eliminating as many points as possible while still maintaining the desired visual shape. A curve with 3 points is significantly more efficient for a GPU to evaluate than one with 20 points, especially when thousands of particles are involved.

8. Access via ICurveEditorModule in C++

If you are building a custom editor tool, you can integrate the Curve Editor directly by using the ICurveEditorModule interface. This allows you to host a curve graph inside your own Slate widgets, enabling you to provide custom property editing experiences for your specific gameplay systems or plugin tools.