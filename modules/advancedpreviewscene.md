---
layout: default
title: AdvancedPreviewScene
---

<!-- ai-generation-failed -->

<h1>AdvancedPreviewScene</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AdvancedPreviewScene/AdvancedPreviewScene.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CommonMenuExtensions, Core, CoreUObject, EditorFramework, EditorInteractiveToolsFramework, Engine, InputCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

used to create feature-rich 3D preview environments within custom tool windows. It extends the basic FPreviewScene to provide standardized “look-dev” features like HDRI skyboxes, customizable floor meshes, and environment lighting controls.

It is primarily used by engine tools—such as the Static Mesh, Material, and Animation editors—to allow developers to inspect assets in a controlled, isolated 3D world without the interference of the active level.

Practical Usage Tips and Best Practices
1. Configure Module Dependencies

Because this is an Editor-specific system, you must include the module in your project’s .Build.cs file within an Editor-only block. This prevents compilation errors when packaging your game.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "AdvancedPreviewScene", "UnrealEd" });

	}

	```

	 

	#### 2. Synchronize with UAdvancedPreviewSceneSettings

	The scene's visual state (brightness, background, floor visibility) is controlled by a `UAdvancedPreviewSceneSettings` object. To make these settings editable by the user, expose them via a `IDetailsView` in your custom editor.

	```cpp

	// Inside your Viewport implementation

	TSharedPtr<FAdvancedPreviewScene> PreviewScene;

	// Access the settings object to update or read environment state

	UAdvancedPreviewSceneSettings* Settings = PreviewScene->GetSettings();

	```

	 

	#### 3. Manually Tick the Preview Scene

	Unlike the main level, components in a preview scene often require manual ticking to animate (e.g., rotating a shader ball or skeletal mesh). Override your viewport client’s `Tick` function to propagate the delta time.

	```cpp

	void FMyViewportClient::Tick(float DeltaSeconds)

	{

	    FEditorViewportClient::Tick(DeltaSeconds);

	    // Ensure the preview world ticks so animations and physics-simulated components update

	    PreviewScene->GetWorld()->Tick(LEVELTICK_All, DeltaSeconds);

	}

	```

	 

	#### 4. Handle Component Ownership Carefully

	When adding components to the scene (e.g., using `PreviewScene->AddComponent()`), the scene takes management responsibility, but you should still ensure they are cleaned up or replaced properly when the asset being edited changes to avoid "ghost" meshes in the viewport.

	 

	#### 5. Leverage the Default Floor and Sky

	Use the built-in helper methods to toggle standard environment pieces. This maintains a consistent "Unreal" look for your tools without manual setup of sky spheres.

	```cpp

	PreviewScene->SetFloorVisibility(true);

	PreviewScene->SetEnvironmentOpacity(1.0f);

	```

	 

	#### 6. Match Feature Levels for Consistency

	Ensure your preview scene matches the shading path of the project. If your game uses mobile rendering or specific Nanite settings, initialize the scene with the correct `ERHIFeatureLevel` to ensure the preview looks identical to the in-game result.

	 

	#### 7. Use Profiles for Different Lighting Scenarios

	`FAdvancedPreviewScene` supports profiles (saved in `EditorPerProjectUserSettings`). Allow users to save and switch between "Night," "Interior," or "Outdoor" setups by leveraging the `FPreviewSceneProfile` struct, which is natively supported by the module.

	 

	#### 8. Optimize for Background Rendering

	If your custom editor is hidden or minimized, stop ticking the preview scene. Checking `IsVisible()` in your Slate viewport widget before calling the scene's tick can save significant GPU resources during multi-tasking.
Copy code
2. Synchronize with Settings Objects

The scene’s visual state (brightness, background, floor visibility) is managed by UAdvancedPreviewSceneSettings. To provide a professional UI, link this settings object to a Details Panel (IDetailsView) in your custom editor. This allows users to tweak the environment directly.

3. Manually Tick the Preview World

Unlike the main Editor world, components in a preview scene often require a manual tick to process animations or physics. Call Tick() on the preview world inside your Viewport Client’s tick function:

C++
	void FMyViewportClient::Tick(float DeltaSeconds)

	{

	    FEditorViewportClient::Tick(DeltaSeconds);

	    PreviewScene->GetWorld()->Tick(LEVELTICK_All, DeltaSeconds);

	}
Copy code
4. Manage Component Lifecycles

When switching between assets in your custom tool, use PreviewScene->RemoveComponent() before adding a new one. Failing to manage the lifecycle of components added via AddComponent() can lead to overlapping meshes or “ghost” artifacts in the viewport.

5. Utilize Environment Profiles

The module supports FPreviewSceneProfile, which stores lighting and skybox configurations. Use this to allow users to quickly swap between different scenarios (e.g., “Daylight,” “Night,” or “Studio”) to ensure assets look correct in all lighting conditions.

6. Handle Interaction and Elimination Logic

If your preview scene involves interactive elements where actors are destroyed (e.g., testing projectile impacts on a mesh), ensure you use the proper elimination flow for the preview world. Use World->DestroyActor() and verify that any references in your Viewport Client are cleared to prevent null pointer crashes.

7. Match Feature Levels

Ensure your preview scene is initialized with the correct ERHIFeatureLevel (e.g., SM6 or ES3_1). If the preview scene feature level does not match your target platform or project settings, shaders may render incorrectly or fail to show Nanite/Lumen effects.

8. Optimize GPU Overhead

Preview scenes can be expensive if left running in the background. Implement a check in your Slate widget to stop ticking the FAdvancedPreviewScene when the tab is not visible or the window is minimized to save system resources.