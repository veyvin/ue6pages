---
layout: default
title: AnimationWidgets
---

<!-- ai-generation-failed -->

<h1>AnimationWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AnimationWidgets/AnimationWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate, SlateCore, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gine 5 that provides a collection of specialized UI components used to build animation-related editor tools. These are the “building blocks” found in tools like the Persona Animation Editor, Sequencer, and Control Rig.

Rather than being intended for gameplay UI (UMG), this module is used by tool developers and technical artists to create custom editor panels that require complex animation data visualization, such as timelines, bone trees, and attribute inspectors.

1. Leverage SAnimTimeline for Custom Sequencers

If you are building a custom tool that requires a playback head, frame markers, and scrubbing functionality, use the SAnimTimeline widget. It provides the standardized Unreal “look and feel” for time-based data, ensuring your tool remains consistent with the rest of the engine’s animation suite.

2. Use SAdvancedTransformInput for Precise Control

The module contains specialized input widgets like SAdvancedTransformInput. This is ideal for custom animation tools where you need to expose Location, Rotation, and Scale fields that support “Drag-to-Slide” functionality and unit conversion (e.g., converting degrees to radians automatically for internal math).

3. Inspect Data with SAnimAttributeView

When debugging custom animation modifiers or graph data, SAnimAttributeView can be used to create a list of attributes currently flowing through an animation pose. This is essential for verifying that custom metadata or curve data is correctly reaching the final skeletal mesh.

4. Implement SAnimCurvePanel for Visual Tweaking

If your tool involves editing animation curves or weights (like Morph Targets or Material Parameters), the SAnimCurvePanel provides a robust way to visualize these values over time. It handles the rendering of curve segments and allows for intuitive keyframe manipulation.

5. Best Practice: Module Dependency Management

Because this module is part of the Developer category, it must be gated correctly in your Build.cs. Including it in a runtime module will prevent your game from packaging.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AnimationWidgets");

	}
Copy code
6. Reuse SSkeletonTree for Bone Selection

If your custom editor utility needs to allow users to select specific bones or sockets, don’t build a list from scratch. Utilize the widgets in this module that interface with the Skeleton Tree logic to provide a searchable, hierarchical view of the character’s skeleton.

7. Performance: Slate Throttling

When creating complex custom animation timelines with many tracks, use Slate’s attribute binding carefully. Frequent updates to the UI from the animation tick can cause editor performance to degrade.

Tip: Use “Invalidation Panels” or only update the widget’s visual state when the user is actively scrubbing or when an “OnChanged” event is fired.
8. Customizing Widget Appearance

Many widgets in this module rely on the FEditorStyle or FAppStyle. When implementing these widgets in your own tab, ensure you are passing the correct STableRow or SBorder styles to maintain visual parity with the engine. This eliminates visual “clutter” and makes your custom tools feel like native engine features.