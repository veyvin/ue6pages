---
layout: default
title: AnimationEditor
---

<!-- ai-generation-failed -->

<h1>AnimationEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationEditor/AnimationEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimGraph, Core, CoreUObject, EditorFramework, Engine, InputCore, Kismet, Persona, SkeletonEditor, Slate, SlateCore, ToolMenus, TypedElementRuntime, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rastructure responsible for the visual manipulation and previewing of animation assets. It provides the framework for the Skeletal Mesh Editor, Animation Sequence Editor, Skeleton Editor, and Animation Blueprint Editor.

This module manages the viewport logic, the asset browser, and the synchronization between the skeletal hierarchy (Skeleton Tree) and the visual preview. It allows developers to modify animation curves, set up notifies, adjust LOD settings, and preview how animations will blend before they are deployed in-game.

Practical Usage Tips and Best Practices
1. Configure Editor Module Dependencies

If you are building custom editor tools, such as a specialized animation compression analyzer or a custom notify graph, you must include this module in your editor-specific Build.cs.

C#
	// In YourProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { 

	        "AnimationEditor", 

	        "Persona", 

	        "EditorFramework" 

	    });

	}
Copy code
2. Utilize the Preview Scene Settings

The Animation Editor provides a Preview Scene Settings tab that is often overlooked.

Best Practice: Use this to swap the Preview Mesh or apply a Post Process Cube Map. This allows you to verify how animations look under different lighting conditions or on different character variants without changing the actual asset defaults.
3. Extend the Toolbar via IAnimationEditor

If your project requires custom workflow actions (e.g., “Export to Maya” or “Auto-generate Footsteps”), you can access the IAnimationEditor interface to inject custom buttons or menus into the animation editor toolbar. This is handled via the FPersonaModule and IAnimationEditor::GetToolbarBuilder.

4. Optimize Workflow with the Asset Browser Filters

The Asset Browser within the Animation Editor includes a “Other Developers” filter.

Tip: In large-scale team environments, toggle this to eliminate clutter from your view. It helps you focus solely on the assets currently checked out or relevant to your current task in the animation pipeline.
5. Debugging with “Record” in the Viewport

The Animation Editor Viewport has a Record feature that allows you to capture the current state of a skeletal mesh into a new Animation Sequence.

Best Practice: Use this to “bake” complex logic. For example, if you have a complex Animation Blueprint with procedural IK, you can record the result in the editor to create a static animation, which saves CPU cycles by eliminating the need for real-time IK calculation for that specific sequence.
6. Manage Skeleton Tree Bone Coloration

Within the Skeleton Tree (managed by this module), you can right-click bones to add Sockets or change visibility.

Tip: Use the search filter in the Skeleton Tree to quickly isolate specific bone chains (like “arm” or “leg”). This is essential for large skeletons with hundreds of bones to prevent UI fatigue and selection errors.
7. Validate Animation Curves

The Animation Sequence Editor (powered by this module) allows for granular curve editing.

Best Practice: Periodically check the Curve Metadata tab. Ensure that deprecated or unused curves are eliminated, as an excessive number of active curves can increase the memory footprint and processing time for the animation evaluation on the game thread.
8. Leverage “Edit Raw Curve Data” for Precision

While the visual graph is useful, the Animation Editor allows you to view raw keys.

Tip: If an animation appears to “jitter” or “pop” at a specific frame, switch to the raw data view to identify and eliminate duplicate keys or extreme tangents that may be causing interpolation issues.