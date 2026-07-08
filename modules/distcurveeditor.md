---
layout: default
title: DistCurveEditor
---

<!-- ai-generation-failed -->

<h1>DistCurveEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DistCurveEditor/DistCurveEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AppFramework, Core, CoreUObject, EditorFramework, Engine, InputCore, LevelEditor, RenderCore, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

zed editor framework designed specifically to manage and visualize Distributions. Distributions are a legacy data-driven math system in Unreal Engine (primarily used by the Cascade particle system and older Sound Cues) that allows values to change over time using curves, constants, or random ranges.

Unlike the modern, generalized Curve Editor used in Sequencer or Niagara, the DistCurveEditor is tightly coupled with the UDistribution class hierarchy. It provides the graph UI that allows developers to “eliminate” static values in favor of dynamic, time-based behaviors for legacy assets.

Practical Usage Tips and Best Practices
Distinguish from the Modern Curve Editor
The DistCurveEditor is specifically for the UDistribution type. If you are working with Niagara or Sequencer, you should use the standard CurveEditor module instead. Keeping these separate helps eliminate confusion when trying to extend the editor for different asset types.
Enable the Tab via Cascade
To access this editor, you typically click the “Graph” icon on a module in the Cascade Particle Editor. This sends the distribution data to the DistCurveEditor. Use this to visualize how values like “Size Over Life” scale, helping you eliminate trial-and-error when adjusting particle behavior.
Manage Keyframe Density
When creating complex curves in the DistCurveEditor, avoid over-populating keyframes. Excessive keys in a distribution can lead to minor performance hits in legacy systems. Use the “Clean” or “Optimize” functions where available to eliminate redundant points while maintaining the curve’s shape.
Use the “Fit” Commands
The DistCurveEditor has specific shortcuts to “Fit Horizontally” and “Fit Vertically.” Use these frequently to eliminate time spent manually panning and zooming the graph, especially when dealing with distributions that have very large or very small value ranges.
Locking Axes for Precision
When dragging keys, hold the modifier keys (typically Shift or Ctrl) to lock movement to a specific axis. This allows you to change the time of a key without altering its value, or vice versa, helping to eliminate accidental data corruption during fine-tuning.
Wrap C++ Extensions in Editor Guards
If you are writing C++ that interacts with FDistCurveEditor, ensure the code is wrapped in #if WITH_EDITOR. This module is not required for runtime playback of distributions and must be eliminated from your shipping builds to ensure successful packaging.
Color-Code Multiple Curves
If you are editing Vector distributions (X, Y, and Z), use the visibility toggles in the DistCurveEditor outliner to isolate specific channels. This focus helps you eliminate visual clutter and ensures you are editing the correct coordinate (e.g., only the vertical Z-velocity of a spark).
Transition to Niagara for New Projects
Because the DistCurveEditor is tied to legacy systems, it does not support modern features like GPU simulation or advanced data interfaces. To eliminate technical debt, use Niagara and its integrated Curve Editor for all new VFX work, reserving this module only for maintaining older projects.