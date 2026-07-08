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

amework for the specialized suite of animation tools in Unreal Engine, collectively known as Persona. This module handles the UI, viewport logic, and asset interaction for the Skeleton Editor, Skeletal Mesh Editor, Animation Sequence Editor, and Animation Blueprint Editor.

It is the primary module used when developers need to extend the animation editing environment, such as adding custom tabs to the Persona toolkit, creating custom viewport overlays, or building specialized animation authoring tools.

Practical Usage Tips and Best Practices
Scoping for Editor Modules Since this module is strictly for the Unreal Editor, it must only be included in your project’s Editor module Build.cs. Including it in a runtime module will result in a failed build during packaging as the module is “eliminated” for shipping.
C++
	// YourProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AnimationEditor", "AnimGraph", "Persona" });

	}

	```

	 

	#### 2. Extend UAnimGraphNode_Base for Custom Logic

	When creating custom Animation Blueprint nodes, you must split the logic. The **Runtime** node (inheriting from `FAnimNode_Base`) handles the math, while the **Editor** node (inheriting from `UAnimGraphNode_Base`) handles the visual representation in the graph.

	*   **Best Practice:** Use `GetNodeTitleColor()` to color-code your nodes (e.g., Blue for IK, Green for Math) to help animators navigate complex graphs.

	 

	#### 3. Leverage Pose Watching for Debugging

	While in the Animation Blueprint Editor, you can right-click any node and select **Toggle Pose Watch**. This allows you to visualize the skeletal pose at that specific point in the graph, making it significantly easier to "eliminate" blending errors or unwanted bone rotations.

	 

	#### 4. Use Metadata for Pin Control

	In your runtime `FAnimNode` struct, use `UPROPERTY` metadata to control how properties appear in the Editor.

	*   `meta = (PinShownByDefault)`: Forces the variable to appear as a pin immediately.

	*   `meta = (AlwaysAsPin)`: Prevents the user from hiding the pin, ensuring critical data is always visible.

	 

	#### 5. Implement PostEditChangeProperty Validation

	In your `UAnimGraphNode`, override `PostEditChangeProperty` to validate user input. For example, if your node requires a specific bone name, you can check if that bone exists in the current skeleton and display an error icon on the node if it doesn't.

	 

	#### 6. Utilize Persona Viewport Clients

	If you are building a custom editor tool that requires a 3D preview of a character, use `FAnimationViewportClient`. It provides a specialized viewport already configured for skeletal mesh rendering, bone manipulation, and animation playback.

	 

	#### 7. Keep Runtime Nodes "Lean"

	Never include headers from the `AnimationEditor` module in your runtime `FAnimNode` source files. The runtime node should contain only the data and execution logic; keep all UI-related logic (like context menus or node descriptions) strictly inside the `UAnimGraphNode` within your Editor module.

	 

	#### 8. Optimize via Preview Scene Settings

	Use the **Preview Scene Settings** tab within the Animation Editor to toggle "Show Bones" or "Show Sockets." For performance-heavy skeletal meshes, you can "eliminate" viewport lag by disabling high-quality post-processing or reducing the level of detail (LOD) directly in the preview window.
Copy code
Extend via IAnimationEditor When building tools that need to react to what a user is doing in the animation window, use the IAnimationEditor interface. This allows your code to identify which asset is currently being edited and provides hooks to refresh the UI when an “elimination” of a keyframe or a bone modification occurs.
Utilize Persona Viewport Overlays If you need to draw custom debug information (like custom hitboxes or trajectory paths) in the animation preview, leverage the FAnimationViewportClient. This allows you to “eliminate” the need for separate debug actors by drawing directly into the Persona viewport using its specialized canvas.
Leverage Pose Watching for Logic Verification While working in the Animation Blueprint Editor (part of the AnimationEditor toolset), right-click nodes and select Toggle Pose Watch. This is the most effective way to “eliminate” bugs in complex blending logic by visualizing exactly how a pose looks at any specific point in the graph.
Custom Context Menu Actions You can extend the right-click menus in the Animation Editor by using the FExtender class. This is useful for adding custom “batch” actions, such as automatically renaming animation notifies or applying specific retargeting settings to a group of selected bones.
Lean Runtime Nodes Always maintain a strict separation between your runtime animation logic and the editor representation. Your runtime FAnimNode should never reference the AnimationEditor module. Instead, put all visual logic, like node colors or custom pin behavior, in a companion UAnimGraphNode class within your Editor module.
Preview Scene Settings for Performance In the Animation Editor’s Preview Scene Settings, you can toggle features like “Show Bones” or “Show Sockets.” For developers working with extremely high-poly meshes, “eliminating” the rendering of the grid, floor, or complex shadows in this tab can significantly improve editor frame rates.
Handle Asset Synchronization If your custom tool modifies skeletal data in the background, use the OnPostEditChange delegates provided by the editor classes. This ensures that the Persona viewport and all open animation tabs refresh immediately, preventing the user from seeing stale or corrupted animation data.