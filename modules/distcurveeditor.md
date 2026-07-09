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

tor module in Unreal Engine primarily responsible for managing and visualizing Distributions. While modern systems like Niagara and Sequencer use the newer CurveEditor module, the DistCurveEditor is the core interface for legacy systems, most notably the Cascade particle editor and certain legacy Sound Cue nodes.

It provides a graph-based interface to manipulate floating-point and vector values over time, allowing for the “elimination” of static values in favor of dynamic, interpolated behavior in legacy assets.

Practical Usage Tips and Best Practices
Identify Legacy Contexts Use this module specifically when working with Cascade or Sound Cues. If you are working in Niagara or Sequencer, you should “eliminate” the use of this module in favor of the modern Curve Editor, which offers more robust tangent controls and performance optimizations.
Toggle Curve Visibility via the Outliner In the DistCurveEditor panel, use the checkbox next to the curve names to “eliminate” visual clutter. When dealing with a Vector distribution (like Velocity), turning off the X and Y curves while focusing on the Z curve makes precise value adjustments significantly easier.
Utilize the “Fit” Commands If your curve points are outside the current view, use the Fit Horizontal (H) and Fit Vertical (V) buttons. This “eliminates” the need for manual panning and zooming, instantly framing all active keys within the editor window.
Master Tangent Modes Right-click on keyframes to switch between Auto, User, and Break. Using “Break” tangents allows you to “eliminate” smooth interpolation at a specific point, creating sharp “v-shaped” changes in particle behavior or sound pitch.
Synchronize with the Details Panel The DistCurveEditor is bidirectionally linked with the Details panel of the asset you are editing. If you “eliminate” a keyframe in the graph, it is instantly removed from the array in the Details panel. It is best practice to keep both open to verify exact numerical values while visually shaping the curve.
Use the Tab Key for Navigation When a keyframe is selected, use the Tab key to cycle through its time and value fields. This “eliminates” the need to click back and forth between the mouse and keyboard, allowing for rapid-fire data entry for complex distributions.
Avoid Over-Keying for Performance While it is tempting to add many keys for a complex shape, it is a best practice to “eliminate” unnecessary keyframes. Every key in a Distribution adds a small amount of computational overhead during runtime interpolation; use the simplest curve possible to achieve the desired effect.
Manage Color-Coded Vectors By default, the editor uses Red, Green, and Blue for X, Y, and Z axes. This “elimination” of ambiguity helps you quickly identify which axis you are modifying in a DistributionVector. Always verify the color before dragging a tangent to avoid corrupting the wrong axis.