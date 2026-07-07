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

odule in Unreal Engine used specifically to manage Distributions. Distributions are a specialized data type (inheriting from UDistribution) that define how a value—such as a float or a vector—changes over time or within a specific range.

While modern systems like Niagara and Sequencer use the newer CurveEditor module, the DistCurveEditor remains essential for maintaining legacy systems like Cascade (the older particle system) and certain actor components that rely on the FDistribution struct for property animations.

Practical Usage Tips and Best Practices
1. Understand the Distribution Types

The editor behaves differently based on the type of distribution being edited.

Best Practice: Choose the correct type before editing. Use Constant for a single value, Uniform for a random range between two values, and Curve for values that change over a timeline. Identifying the right type early helps eliminate unnecessary keyframe complexity.
2. Send Properties to the Editor via the “Curve” Icon

Properties that support distributions often have a small “graph” icon next to them in the Details Panel.

Tip: Clicking this icon “pushes” that specific property into the DistCurveEditor tab. This is the fastest way to populate the graph, eliminating the need to manually search through a list of available curves.
3. Manage Tab Clutter

The DistCurveEditor can collect many different curves in its tab list if you click multiple properties in a row.

Action: Regularly use the Remove All Curves (the “X” icon) or right-click specific tabs to remove them once you are done. Keeping the workspace clean helps eliminate visual confusion when trying to distinguish between similar vector channels (like Velocity vs. Size).
4. Use Color-Coding for XYZ and RGB

The editor follows standard Unreal conventions for vector data: Red for X, Green for Y, and Blue for Z.

Tip: If you are editing a color distribution, these represent Red, Green, and Blue channels respectively. Use the checkbox toggles next to the curve names to hide specific channels, allowing you to focus on one axis at a time and eliminate accidental edits to the wrong channel.
5. Leverage the ‘Fit’ Commands

When you first open a curve, it may be zoomed in too far or completely off-screen.

Action: Use the Fit Horizontally and Fit Vertically buttons (or the ‘F’ hotkey) to instantly frame all keyframes. This helps you eliminate time wasted manual-scrolling to find your data points.
6. Smart Keyframe Reduction

Manual keyframing in the DistCurveEditor can often lead to “noisy” curves with more points than necessary.

Best Practice: Periodically review your curves and delete redundant keys that don’t contribute to the shape of the spline. Reducing the number of keys helps eliminate memory overhead and makes the distribution easier to tweak later.
7. Toggle Between Linear and Curve Interpolation

By default, some distributions might use linear (straight) lines between points, which can look “robotic” in motion.

Tip: Right-click a keyframe to change its interpolation mode (e.g., to Curve/Cubic). This allows for smoother transitions in particle behavior or property fades, helping you eliminate abrupt, jarring visual jumps.
8. Use for Cascade Performance Tuning

In legacy Cascade emitters, the DistCurveEditor is the primary tool for optimizing “Spawn Per Unit” or “Lifetime” ranges.

Action: If a particle system is causing a performance hit, check the distributions. Often, a Constant distribution is more performant than a complex Curve. Replacing unnecessary curves with constants helps eliminate per-frame calculation costs on the CPU.