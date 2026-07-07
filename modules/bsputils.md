---
layout: default
title: BSPUtils
---

<!-- ai-generation-failed -->

<h1>BSPUtils</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/BSPUtils/BSPUtils.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

vel functions for manipulating Binary Space Partitioning (BSP) geometry. While BSP (commonly referred to as “Brushes” or “Geometry Brushes”) is largely a legacy system in UE5—superseded by the Modeling Tools and Static Meshes—it remains the underlying technology for Volumes (Trigger, KillZ, etc.) and rapid level blocking.

This module contains the logic for Constructive Solid Geometry (CSG) operations, such as adding, subtracting, and intersecting brush volumes, as well as the logic for converting these brushes into Static Mesh assets.

Practical Usage Tips & Best Practices
1. Module Dependency and Headers

BSPUtils is a developer/editor module. You must include it in your Build.cs only for Editor or Developer targets. Attempting to use it in a Shipping build will cause compilation errors as the module is stripped from the runtime.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("BSPUtils");

	}

	```

	**Required Header:** `#include "BSPUtils.h"`

	 

	#### 2. Programmatic Brush-to-Mesh Conversion

	The most common modern use for this module is automating the conversion of blockout geometry into Static Meshes. Use `FBSPUtils::CreateStaticMeshFromBrush` to generate a new `UStaticMesh` asset from an `ABrush` actor. This is essential for tools that convert designer blockouts into artist-ready assets.

	 

	#### 3. Rebuilding the BSP Tree

	If you programmatically modify a brush's vertices or transform, the visual geometry (the "Model") will not update until the BSP is rebuilt. Use `FBSPUtils::bspBuild` to trigger the CSG recalculation. Be cautious: this is a computationally expensive operation and should be done sparingly, ideally after a batch of changes.

	 

	#### 4. Managing UModel Pointers

	Every `ABrush` actor has an associated `UModel` (the raw geometry data). `BSPUtils` functions often require a `UModel*`. When working with these, ensure the Model is not null and is marked as "dirty" (`Model->Modify()`) before performing operations to ensure the Editor’s Undo/Redo system tracks the changes.

	 

	#### 5. Handling Texture Alignment

	When manipulating BSP surfaces via C++, use the utilities to fix or reset surface alignment. BSP surfaces often lose their UV mapping during programmatic scale changes; `FBSPUtils` provides logic to snap textures to the brush's coordinate system, preventing "stretching" on blockout geometry.

	 

	#### 6. Convert Static Meshes back to Brushes

	If you need to turn an existing Static Mesh into a Volume (e.g., turning a complex mesh into a custom-shaped Trigger Volume), use `FBSPUtils::CreateModelFromStaticMesh`. This allows you to leverage the simple geometry of a mesh to define the bounds of a BSP-based volume.

	 

	#### 7. Use the Editor Actor Subsystem Wrapper

	For high-level operations (like merging multiple brushes), it is often easier to use the `UEditorActorSubsystem::ConvertBrushesToStaticMesh` wrapper, which internally calls `BSPUtils`. This handles the package creation and actor replacement logic automatically, reducing the amount of boilerplate code you need to write.

	 

	#### 8. Validation and Cleanup

	Always call `FBSPUtils::bspCleanup` after a series of complex CSG operations. BSP can accumulate "phantom" surfaces or degenerate triangles during frequent subtractions and additions. This function purges invalid geometry and optimizes the resulting tree, preventing editor instability and rendering artifacts.
Copy code

Required Header: #include "BSPUtils.h"

2. Programmatic Brush-to-Mesh Conversion

The most common modern use for this module is automating the conversion of blockout geometry into Static Meshes. Use FBSPUtils::CreateStaticMeshFromBrush to generate a new UStaticMesh asset from an ABrush actor. This is essential for tools that convert designer blockouts into artist-ready assets.

3. Rebuilding the BSP Tree

If you programmatically modify a brush’s vertices or transform, the visual geometry (the “Model”) will not update until the BSP is rebuilt. Use FBSPUtils::bspBuild to trigger the CSG recalculation. Be cautious: this is a computationally expensive operation and should be done sparingly, ideally after a batch of changes.

4. Managing UModel Pointers

Every ABrush actor has an associated UModel (the raw geometry data). BSPUtils functions often require a UModel*. When working with these, ensure the Model is not null and is marked as “dirty” (Model->Modify()) before performing operations to ensure the Editor’s Undo/Redo system tracks the changes.

5. Handling Texture Alignment

When manipulating BSP surfaces via C++, use the utilities to fix or reset surface alignment. BSP surfaces often lose their UV mapping during programmatic scale changes; FBSPUtils provides logic to snap textures to the brush’s coordinate system, preventing “stretching” on blockout geometry.

6. Convert Static Meshes back to Brushes

If you need to turn an existing Static Mesh into a Volume (e.g., turning a complex mesh into a custom-shaped Trigger Volume), use FBSPUtils::CreateModelFromStaticMesh. This allows you to leverage the simple geometry of a mesh to define the bounds of a BSP-based volume.

7. Use the Editor Actor Subsystem Wrapper

For high-level operations (like merging multiple brushes), it is often easier to use the UEditorActorSubsystem::ConvertBrushesToStaticMesh wrapper, which internally calls BSPUtils. This handles the package creation and actor replacement logic automatically, reducing the amount of boilerplate code you need to write.

8. Validation and Cleanup

Always call FBSPUtils::bspCleanup after a series of complex CSG operations. BSP can accumulate “phantom” surfaces or degenerate triangles during frequent subtractions and additions. This function purges invalid geometry and optimizes the resulting tree, preventing editor instability and rendering artifacts. The removal and elimination of these “invisible” faces is crucial for maintaining level performance.