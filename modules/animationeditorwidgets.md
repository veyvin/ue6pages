---
layout: default
title: AnimationEditorWidgets
---

<!-- ai-generation-failed -->

<h1>AnimationEditorWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationEditorWidgets/AnimationEditorWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationCore, ApplicationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd, WidgetRegistration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

a collection of specialized, reusable Slate widgets designed for animation-centric tools. Rather than rebuilding complex UI elements from scratch, this module allows developers to integrate standardized animation controls—such as skeleton trees, track editors, and animation-specific property views—into their custom Persona extensions.

It is primarily used by the Persona (Animation Editor), Skeletal Mesh Editor, and Animation Blueprint Editor to maintain a consistent user interface across all skeletal animation workflows.

1. Module Configuration

To extend animation tools using these widgets, you must include the module in your editor-specific Build.cs file.

C#
	// MyProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { 

	        "AnimationEditorWidgets",

	        "Persona",

	        "Slate",

	        "SlateCore"

	    });

	}
Copy code
2. Practical Usage Tips & Best Practices
Leverage the Skeleton Tree Widget

If you are building a tool that requires bone selection, use the SAnimationSkeletonTree. It is highly optimized for deep hierarchies and includes built-in search filtering and socket management. Avoid building a custom STreeView for bones, as you would lose the native integration with bone “elimination” and retargeting workflows.

Use SAnimAttributeWidgets for Metadata

When working with Animation Attributes (the modern replacement for various curve-based data), use the widgets provided in this module. They handle the complex visual representation of interpolated data types across the animation timeline, ensuring your custom data is displayed exactly like engine-standard attributes.

Synchronize with the Persona Preview Scene

When creating a custom animation editor tab, ensure your widgets are linked to the IPersonaPreviewScene. This allows your UI to react when a user selects a bone in the viewport. For example, selecting a bone in the tree should highlight the same bone in the 3D preview to avoid user confusion.

Implement SAdvancedRotationInput for Precise Rigging

For tools involving Control Rig or IK offsets, use the specialized rotation widgets from this module. These are designed to handle Euler-to-Quaternion conversions gracefully, preventing “Gimbal Lock” visual artifacts in the UI and “eliminating” common math errors in manual coordinate entry.

Standardize Timeline Scrubbers

If your tool needs to move through time, use the SAnimTimeline components. These widgets automatically handle frame-rate snapping and playhead synchronization. Using these ensures that if the user changes the “Display Format” (Seconds vs. Frames) in the main editor preferences, your custom tool will update to match.

Customizing the Detail Panel for Anim Assets

This module contains customizations for how animation properties are drawn. If you are creating a custom UAnimationAsset type, you can use these widgets within a IDetailCustomization to create a “Compact View” of your animation’s curves or notifies, which keeps the UI from becoming overwhelmed.

Efficient Selection State Management

Always use the FRequiredArgs pattern when initializing these widgets. This struct usually requires a pointer to the IEditableSkeleton. By passing this reference, the widgets can automatically “eliminate” invalid bone names from the UI if the skeleton is modified or swapped in the background.

Performance: Handle Large Bone Counts

For complex characters (like those with many cloth or hair bones), ensure you enable the “Deferred Expansion” settings on bone tree widgets. This prevents the editor from hitching when opening a character with hundreds of bones by only generating the Slate elements for the visible portion of the tree.