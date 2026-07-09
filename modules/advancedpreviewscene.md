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

& Best Practices

	 

	#### 1. Prefer `FAdvancedPreviewScene` over `FPreviewScene`

	Unless you need a strictly empty world with zero default actors, always prefer `FAdvancedPreviewScene`. It handles the boilerplate of creating a `DirectionalLight`, `SkyLight`, and `PostProcessVolume`, saving you from manual setup while providing a "standard" look that matches other engine tools.

	 

	#### 2. Utilize the Profile System

	The advanced scene uses `UAdvancedPreviewSceneSettings` to store configuration. You can save and load different "Profiles" (e.g., "Daylight", "Studio", "Night"). This allows users to switch lighting environments instantly.

	*   **Tip:** Use `GetSettings()` on your scene instance to access and modify these properties at runtime.

	 

	#### 3. Handle Component Lifetimes Carefully

	When adding preview components (like a `UStaticMeshComponent`) to the scene, always use the `AddComponent` method of the `FPreviewScene` base.

	```cpp

	// Correct way to add a mesh to your custom viewport scene

	PreviewMeshComponent = NewObject<UStaticMeshComponent>(GetTransientPackage());

	MyAdvancedScene->AddComponent(PreviewMeshComponent, FTransform::Identity);

	```

	Ensure you call `RemoveComponent` in your cleanup phase to prevent memory leaks or ghost components in the editor world.

	 

	#### 4. Synchronize Environment and Light Rotation

	A common pitfall is having the Skybox rotation out of sync with the Directional Light. The Advanced Preview Scene provides built-in logic to rotate the environment (HDRI) and the sun light together. If you implement a custom UI slider for rotation, bind it to `FAdvancedPreviewScene::SetEnvironmentRotation`.

	 

	#### 5. Proper Floor Management

	The "Floor" in an advanced scene is a specific internal component. If your asset is very large or very small, the default floor might clip or look incorrect.

	*   **Best Practice:** Use `SetFloorLocation` to offset the floor based on the bounding box of the asset you are previewing. This ensures the asset always appears to be "sitting" on the ground regardless of its origin.

	 

	#### 6. Performance: Disable Physics if Unnecessary

	By default, preview scenes can incur overhead if physics simulation is active. When initializing your scene, use the `ConstructionValues` struct to disable physics unless your tool specifically requires it (e.g., a PhAT editor).

	```cpp

	FPreviewScene::ConstructionValues CVS;

	CVS.bCreatePhysicsScene = false; // Optimization

	MyAdvancedScene = MakeShareable(new FAdvancedPreviewScene(CVS));

	```

	 

	#### 7. Integration with Slate Viewports

	To actually see the scene, you must wrap it in an `SViewport` and a `FAssetEditorViewportClient`. The `FAdvancedPreviewScene` instance should be passed to your custom `FEditorViewportClient` constructor. This linkage allows Slate to pipe input (like Alt+Drag to rotate lights) directly into the scene settings.

	 

	#### 8. Use `PostProcessVolume` for Color Grading

	If you are building a tool for look-dev (like a Material editor), expose the `PostProcessSettings` within your tool’s details panel. `FAdvancedPreviewScene` contains a dedicated `UPostProcessVolume` that you can manipulate to test how assets look under different exposure or color-grading conditions.
Copy code
2. Practical Usage Tips & Best Practices
Initialize with Construction Values

When creating your scene, use the ConstructionValues struct to toggle heavy features. If your preview doesn’t require physics, disabling it can improve the performance of your editor tool.

C++
	FPreviewScene::ConstructionValues CVS;

	CVS.bCreatePhysicsScene = false; // Disable to save resources

	TSharedPtr<FAdvancedPreviewScene> MyScene = MakeShareable(new FAdvancedPreviewScene(CVS));
Copy code
Synchronize Lighting and Skybox

Users expect the light to match the visual “Sun” in the HDRI. Use the built-in environment rotation features rather than rotating lights manually. This ensures that the SkyLight and DirectionalLight stay synced with the background cubemap.

Leverage the Profile System

FAdvancedPreviewScene automatically integrates with the Preview Scene Settings tab. By using this module, you allow users to save and load their own “Profiles” (HDRI, brightness, and color settings), providing a familiar workflow used across all standard Unreal editors.

Dynamic Floor Offsetting

Prevent your meshes from clipping through the floor by calculating the asset’s bounding box and adjusting the floor height dynamically.

Tip: Use MyScene->SetFloorLocation(FVector(0, 0, MeshBounds.BoxExtent.Z * -1)) to keep the asset perfectly grounded regardless of its size.
Avoid “Elimination” of the Scene Early

In custom Editor Standalone Windows, ensure the lifetime of your FAdvancedPreviewScene is tied to the SViewport or the Toolkit. If the scene is destroyed while the Slate widget still tries to render it, it will lead to access violations. Always use TSharedPtr for management.

Manual Tick Control

If your preview scene contains animated elements (like Niagara or skeletal meshes), remember that preview scenes do not tick by default like the game world. You must manually call MyScene->GetWorld()->Tick(DeltaTime) within your Viewport Client’s Tick function.

Use Post-Process for Look-Dev

Don’t bake lighting into your preview materials. Instead, use the PostProcessVolume built into the FAdvancedPreviewScene to test how assets respond to different Exposure, Bloom, and Tone Mapping settings. This is critical for ensuring materials are “Energy Conserving” and PBR-compliant.

Use Component Tags for Cleanup

When spawning temporary visualizers or helper actors in the preview world, tag them. This makes it easier to “eliminate” specific debug helpers without resetting the entire scene when the user changes a setting in your tool.