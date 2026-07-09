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

ne that provides the shared infrastructure for the engine’s suite of animation tools. It defines the base interfaces and logic for the specialized windows used to edit Animation Sequences, Skeletal Meshes, Skeletons, and Animation Blueprints.

As part of the Persona ecosystem, this module acts as the “glue” that allows different animation sub-editors to share common features like the viewport, playback controls, and asset browsing while maintaining a unified user experience.

Practical Usage Tips and Best Practices
Implement Custom Asset Editors
If you are developing a custom animation asset type (e.g., a specialized dialogue-driven pose system), your editor should inherit from IAnimationEditor. This ensures your tool integrates with the standard Persona layout and gains access to the toolbar and asset picker automatically.
Configure Module Dependencies
Since this is an editor module, add it only to your YourProjectEditor.Build.cs. It is often used in conjunction with the Persona and UnrealEd modules.
C#
	// In YourProjectEditor.Build.cs

	if (Target.bBuildEditor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AnimationEditor", "Persona", "UnrealEd" });

	}
Copy code
Synchronize Data via IPersonaPreviewScene
When creating custom nodes or tools, use the IPersonaPreviewScene provided by the Animation Editor framework. This allows you to “eliminate” the need for custom rendering code by leveraging the existing skeletal mesh preview logic, including LOD toggling and debug skeleton drawing.
Extend Viewport Functionality
Use the FAnimationEditorViewportClient class to add custom overlays or interaction widgets to the animation viewport. This is ideal for creating visual handles for custom IK solvers or displaying hit-box data for an “elimination” system.
Leverage Persona Modes
The Animation Editor uses “Modes” (e.g., Skeleton Mode vs. Mesh Mode). If your tool requires a different layout for “Rigging” vs “Previewing,” implement a custom FApplicationMode. This allows you to show or hide specific tabs and toolbars depending on the user’s current task.
Handle Asset Deletion Gracefully
When your custom editor is open, it should listen for asset deletion events. Use the module’s hooks to ensure that if a Skeletal Mesh is “eliminated” from the Content Browser, the editor closes or refreshes immediately to prevent memory access violations.
Optimize UI via Common Commands
The module provides a centralized command list for playback (Play, Pause, Scrub). Instead of creating your own buttons for these, register your UI with the existing FPersonaCommonCommands to ensure your tool feels native and responds to standard keyboard shortcuts.
Use the Tab Manager for Modular Layouts
When building a tool within the Animation Editor framework, use the FTabManager to define your layout. This allows designers to dock and undock tabs (like the Anim Asset Details or the Skeleton Tree) according to their personal workflow, which helps “eliminate” clutter in the workspace.