---
layout: default
title: CurveAssetEditor
---

<!-- ai-generation-failed -->

<h1>CurveAssetEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CurveAssetEditor/CurveAssetEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, CurveEditor, EditorFramework, Engine, InputCore, Slate, SlateCore, TimeManagement, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

icated window specifically for assets stored in the Content Browser.

This module is used to author time-to-value data that drives non-linear gameplay logic, such as engine torque curves, camera shakes, UI fades, and complex material parameters.

Practical Usage Tips and Best Practices
1. Conditional Build.cs Dependency

Since this is an editor-only module, you must wrap its inclusion in your Build.cs file. Including it in a runtime build will cause packaging errors. Use it only when extending the editor or creating custom asset actions:

C#
	if (Target.bBuildEditor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "CurveAssetEditor", "UnrealEd" });

	}

	```

	 

	#### 2. Programmatic Editor Invocation

	If you are building a custom data asset that contains an internal curve and you want to provide a button to edit it, you can invoke this module directly in C++. Get the module and call `CreateCurveAssetEditor` to open the standard curve editing window for a specific `UCurveBase` object:

	```cpp

	// Example C++ call to open the editor

	FCurveAssetEditorModule& CurveEditorModule = FModuleManager::LoadModuleChecked<FCurveAssetEditorModule>("CurveAssetEditor");

	CurveEditorModule.CreateCurveAssetEditor(EToolkitMode::Standalone, EditArgs.ToolkitHost, MyCurveAsset);

	```

	 

	#### 3. Normalize Curve Ranges (0 to 1)

	For maximum reusability, author your curves in the editor within a **0.0 to 1.0** range for both time and value. In your gameplay code, you can then multiply the output value by a "Scale" variable and the input time by a "Duration" variable. This results in the **elimination** of the need to re-author curves every time a gameplay value (like movement speed) changes.

	 

	#### 4. Optimize Performance via Baking

	Evaluating complex cubic curves every frame can be more expensive than a simple linear lookup. For high-performance systems (like Niagara particles or complex material animations), consider using **Curve Atlases**. This module supports the conversion of curve assets into textures, allowing for the **elimination** of CPU-side evaluation in favor of highly optimized GPU texture lookups.

	 

	#### 5. Leverage Tangent Modes for Control

	When editing in the UI, use **Auto Tangents** for smooth easing (Bezier) and **Stepped Tangents** for instant value jumps (useful for logic gates or discrete state changes). If you need an abrupt change in direction without a curve, use **Broken Tangents**. Properly choosing these modes ensures the **elimination** of unwanted "drifting" values between your keyframes.

	 

	#### 6. Data-Driven Workflow via CSV/JSON

	If you have complex mathematical data (e.g., real-world ballistic data or engine dyno results), do not plot points manually. The Curve Asset Editor supports importing `.csv` and `.json` files. This allows for the **elimination** of human error and ensures that your in-game curves perfectly match your external source data.

	 

	#### 7. Use "External Curves" in Timelines

	When using Timelines in Blueprints or C++, prefer referencing a standalone **Curve Asset** rather than using an "Internal Curve." Standalone assets edited via the CurveAssetEditor can be shared across multiple Actors. If you update the curve asset, all instances update simultaneously, facilitating the **elimination** of redundant work across similar actors.

	 

	#### 8. Verify Extrapolate Settings

	Always check the **Pre-Infinity** and **Post-Infinity** settings in the editor. By default, curves often return the first or last keyframe value when sampled outside their time range. Setting these to **Cycle** or **Oscillate** allows you to create looping animations or repeating patterns without adding extra keyframes, leading to the **elimination** of cluttered curve graphs.
Copy code
2. Open the Editor via C++

If you are developing a custom data asset or a specialized editor tool that needs to trigger the curve editor window programmatically, you can do so by loading the module and passing the curve asset to it:

C++
	FCurveAssetEditorModule& CurveEditorModule = FModuleManager::LoadModuleChecked<FCurveAssetEditorModule>("CurveAssetEditor");

	CurveEditorModule.CreateCurveAssetEditor(EToolkitMode::Standalone, EditArgs.ToolkitHost, MyCurveAsset);
Copy code
3. Normalize for Reusability

A best practice when using this editor is to keep your time (X-axis) and value (Y-axis) ranges between 0.0 and 1.0. You can then scale these values in your gameplay code. This results in the elimination of the need to recreate curve assets if your gameplay timings or intensity values change later in development.

4. Optimize via Curve Atlases

For performance-critical systems like Materials or Niagara, use the Curve Atlas asset to bake multiple curves into a single texture. This allows the GPU to sample the curve data via a texture lookup, leading to the elimination of expensive CPU-side evaluations for every pixel or particle.

5. Leverage Tangent Modes

Use the editor’s tangent controls to define the “feel” of the interpolation. Use Auto for smooth easing, Linear for constant change, and Constant (Stepped) for immediate state changes. Selecting the correct mode ensures the elimination of “drifting” values between your defined keyframes.

6. Import Data from CSV/JSON

If you have high-precision data from external tools (like Excel or physics simulation software), do not manually plot the points. The Curve Asset Editor supports importing .csv or .json files. This facilitates the elimination of human error and ensures your in-game curves perfectly match your source data.

7. Set Pre/Post-Infinity Extrapolation

Within the editor, always define what happens before the first key and after the last key. Setting these to Cycle or Oscillate allows you to create infinitely looping behaviors (like a blinking light or a bobbing platform) without adding extra keyframes, contributing to the elimination of cluttered graphs.

8. Utilize External Curves in Timelines

In Blueprints, when using a Timeline node, prefer using “External Curves” created in the CurveAssetEditor over internal ones. This allows multiple Actors to share the same curve data. If the curve needs a tweak, you only edit it once in the CurveAssetEditor, ensuring the elimination of redundant edits across dozens of separate Blueprints.