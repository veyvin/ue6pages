---
layout: default
title: AdvancedPreviewScene
---


<h1>AdvancedPreviewScene</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AdvancedPreviewScene/AdvancedPreviewScene.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CommonMenuExtensions, Core, CoreUObject, EditorFramework, EditorInteractiveToolsFramework, Engine, InputCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e high-fidelity, isolated 3D preview environments within custom editor windows. It extends the base FPreviewScene by adding standard “look-dev” features such as an HDRI skybox, directional lighting, post-processing, and a customizable floor mesh.

It is the engine’s standard for building asset-specific viewports (like those found in the Static Mesh or Material Editors), providing a consistent environment where developers can inspect assets without the lighting or post-processing of the active game level interfering.

Practical Usage Tips and Best Practices
1. Configure Editor-Only Module Dependencies

Because this module is intended for tools, you must wrap its dependency in an editor check within your [Project].Build.cs file. This prevents packaging errors during the build process.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { 

	        "AdvancedPreviewScene", 

	        "UnrealEd", 

	        "InputCore" 

	    });

	}

	```

	 

	#### 2. Manual World Ticking

	While `FAdvancedPreviewScene` inherits from `FTickableEditorObject` to update its own environment (like sky rotation), the underlying **World** often needs a manual tick to process component animations, physics, or Niagara effects. In your custom `FEditorViewportClient`:

	 

	```cpp

	void FMyViewportClient::Tick(float DeltaSeconds)

	{

	    FEditorViewportClient::Tick(DeltaSeconds);

	 

	    // Ensure the preview world updates logic/animations

	    if (PreviewScene)

	    {

	        PreviewScene->GetWorld()->Tick(LEVELTICK_All, DeltaSeconds);

	    }

	}

	```

	 

	#### 3. Link Settings to a Details Panel

	The scene's state is stored in `UAdvancedPreviewSceneSettings`. For a professional UI, expose these settings in an `IDetailsView` widget so users can adjust lighting and the HDRI.

	 

	```cpp

	// Inside your Editor Toolkit or Slate Widget

	FPropertyEditorModule& EditModule = FModuleManager::Get().GetModuleChecked<FPropertyEditorModule>("PropertyEditor");

	TSharedPtr<IDetailsView> DetailsView = EditModule.CreateDetailView(DetailsViewArgs);

	 

	// Link the settings object from your AdvancedPreviewScene

	DetailsView->SetObject(MyAdvancedPreviewScene->GetSettings());

	```

	 

	#### 4. Manage Component Lifecycles

	When switching the asset being previewed (e.g., selecting a different Mesh), always call `PreviewScene->RemoveComponent()` on the old mesh before adding the new one. Failure to do so will result in "ghost" meshes or memory leaks within the transient preview world.

	 

	#### 5. Respect Feature Levels and RHIs

	Ensure your `ConstructionValues` for the preview scene match the target platform's feature level. If you are developing mobile-specific tools, initialize the scene with `ERHIFeatureLevel::ES3_1` to ensure shaders and lighting approximate the mobile device's look.

	 

	#### 6. Utilize Environment Profiles

	The system supports `FPreviewSceneProfile`. You can define multiple profiles (e.g., "Night Street," "High Noon," "Studio") in your editor settings. This allows users to quickly verify that their materials or VFX look correct under varying lighting conditions with a single dropdown selection.

	 

	#### 7. Clean Up on Shutdown

	Preview scenes are heavy. Ensure that when your tab or window is closed, the `FAdvancedPreviewScene` instance is deleted. Because it is a C++ class (not a `UObject`), it must be managed via a `TUniquePtr` or explicitly deleted in your toolkit's destructor to free up GPU resources.

	 

	#### 8. Prevent Unnecessary Ticking

	To optimize editor performance, check if your viewport is actually visible before ticking the preview scene. You can use `FSlateApplication::Get().IsNormalExecution()` or check the visibility state of your parent Slate tab to throttle the tick rate when the window is obscured.
Copy code
2. Manual World Ticking

While FAdvancedPreviewScene updates its own environment (like sky rotation), the underlying World needs a manual tick to process component logic, animations, or Niagara effects. In your custom FEditorViewportClient:

C++
	void FMyViewportClient::Tick(float DeltaSeconds)

	{

	    FEditorViewportClient::Tick(DeltaSeconds);

	 

	    // Ensure the preview world updates logic and component animations

	    if (PreviewScene)

	    {

	        PreviewScene->GetWorld()->Tick(LEVELTICK_All, DeltaSeconds);

	    }

	}
Copy code
3. Link Settings to a Details Panel

The scene’s state is stored in UAdvancedPreviewSceneSettings. For a professional UI, expose these settings in an IDetailsView widget so users can adjust lighting and the HDRI directly within your tool.

C++
	FPropertyEditorModule& EditModule = FModuleManager::Get().GetModuleChecked<FPropertyEditorModule>("PropertyEditor");

	TSharedPtr<IDetailsView> DetailsView = EditModule.CreateDetailView(DetailsViewArgs);

	 

	// Link the settings object from your AdvancedPreviewScene instance

	DetailsView->SetObject(MyAdvancedPreviewScene->GetSettings());
Copy code
4. Manage Component Lifecycles

When switching the asset being previewed (e.g., selecting a different mesh), always call PreviewScene->RemoveComponent() on the old mesh before adding the new one. Failure to do so will result in “ghost” meshes or memory leaks within the transient preview world.

5. Utilize Environment Profiles

The system supports FPreviewSceneProfile. You can define multiple profiles (e.g., “Night,” “High Noon,” “Studio”) in your editor settings. This allows users to quickly verify that their materials or VFX look correct under varying lighting conditions with a single dropdown selection.

6. Clean Up on Shutdown

Preview scenes are resource-heavy. Ensure that when your tab or window is closed, the FAdvancedPreviewScene instance is deleted. Because it is a native C++ class (not a UObject), it should be managed via a TUniquePtr or explicitly deleted in your toolkit’s destructor to free up GPU resources.

7. Handle Actor Elimination Logic

If your tool allows for spawning temporary test actors within the preview scene that need to be removed, ensure you call DestroyActor() on the actor and immediately remove its components from the scene to ensure total elimination of the object from the preview world’s memory.

8. Prevent Unnecessary Ticking

To optimize editor performance, check if your viewport is actually visible before ticking. Use the visibility state of your parent Slate tab to throttle or pause the tick rate when the window is obscured or hidden, preventing wasted GPU/CPU cycles.