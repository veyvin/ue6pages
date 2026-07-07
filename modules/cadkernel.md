---
layout: default
title: CADKernel
---

<!-- ai-generation-failed -->

<h1>CADKernel</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Datasmith/CADKernel/Base/CADKernel.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, GeometryCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

geometry processing engine designed specifically for the Datasmith and Interchange CAD import pipelines. Introduced to replace legacy third-party tessellators, it specializes in converting B-Rep (Boundary Representation) and NURBS data from formats like CATIA, SolidWorks, and Rhino into optimized triangle meshes.

It provides a multi-threaded, engine-native way to handle complex CAD topologies, ensuring high-fidelity surfaces with minimal “T-junctions” (cracks between surfaces) while maintaining compatibility with modern engine features like Nanite.

Practical Usage Tips & Best Practices
1. Module Dependency and Scoping

Since CADKernel is a developer-centric module used for asset processing, it should only be included in Editor or Developer modules. Using it in a runtime/shipping build is not supported as CAD translation is an offline process.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    // Required for CAD translation and tessellation logic

	    PrivateDependencyModuleNames.AddRange(new string[] { "CADKernel", "CADKernelSurface" });

	}

	```

	 

	#### 2. Optimize for Nanite via Stitching

	To make CAD data compatible with Nanite, you must eliminate "open edges" (gaps). In the Datasmith import settings (or via C++), prioritize the **Stitching** options provided by the CADKernel. Use the `ds.CADTranslator.SewMeshIfNeeded 1` CVar to ensure that individual NURBS patches are topologically fused into a single watertight manifold during the tessellation phase.

	 

	#### 3. Balancing Chord and Normal Tolerance

	The quality of the output depends on two primary parameters:

	*   **Chord Tolerance:** The maximum distance between the generated triangle and the original NURBS surface. Lower values increase polycount.

	*   **Normal Tolerance:** The maximum angle between adjacent triangles. 

	**Best Practice:** For large structural parts (pipes, frames), favor a higher Normal Tolerance to save triangles. For aesthetic surfaces (car bodies), lower both to prevent visible faceting.

	 

	#### 4. Leverage Multi-Threaded Import

	`CADKernel` is designed to be highly parallel. You can control how much of your CPU is dedicated to the CAD import process to prevent system-wide hangs during large assembly imports.

	*   **CVar:** `ds.CADTranslator.MaxConcurrentTasks [Number]`

	Adjust this value based on your workstation's core count to balance import speed against editor responsiveness.

	 

	#### 5. Utilize the CAD Cache for Iteration

	The kernel uses a hashing system (size, name, timestamp) to cache processed geometry in the `Intermediate/Datasmith/CADCache` folder. 

	**Best Practice:** When re-importing a modified assembly, do not delete this folder. The kernel will only re-tessellate the specific components that changed, significantly reducing iteration time for large datasets.

	 

	#### 6. Toggle for Bug Isolation

	If you encounter "exploding" geometry or missing faces on specific complex models, you can temporarily revert to the legacy third-party tessellator to identify if the issue is in the source file or the kernel.

	*   **CVar:** `ds.CADTranslator.DisableCADKernelTessellation 1` (Set back to `0` to re-enable).

	 

	#### 7. Set Maximum Edge Length for Consistent Density

	Unlike legacy tessellators, `CADKernel` supports a **Max Edge Length** parameter. This is critical for Nanite and Lumen, as it prevents the creation of extremely long, thin triangles which can cause artifacts in virtualized geometry and software ray tracing. Set a reasonable max edge length (e.g., 50.0 units) to ensure a uniform mesh density.

	 

	#### 8. Debugging Topology via C++

	If you are writing custom CAD translators, you can use the `UE::CADKernel::EStatut` enum to inspect the topological state of faces (Interior, Exterior, Border). This is useful for programmatically identifying "holes" in a model before finalizing the mesh factory step. Use `FSystem::PrintHeader()` to log the kernel's initialization state and versioning for diagnostic purposes.
Copy code
2. Optimize for Nanite via Stitching

To make CAD data compatible with Nanite, you must eliminate “open edges” (gaps). In the Datasmith import settings (or via C++), prioritize the Stitching options provided by the CADKernel. Use the ds.CADTranslator.SewMeshIfNeeded 1 CVar to ensure that individual NURBS patches are topologically fused into a single watertight manifold during the tessellation phase.

3. Balancing Chord and Normal Tolerance

The quality of the output depends on two primary parameters:

Chord Tolerance: The maximum distance between the generated triangle and the original NURBS surface. Lower values increase polycount.
Normal Tolerance: The maximum angle between adjacent triangles. Best Practice: For large structural parts (pipes, frames), favor a higher Normal Tolerance to save triangles. For aesthetic surfaces (car bodies), lower both to prevent visible faceting.
4. Leverage Multi-Threaded Import

CADKernel is designed to be highly parallel. You can control how much of your CPU is dedicated to the CAD import process to prevent system-wide hangs during large assembly imports.

CVar: ds.CADTranslator.MaxConcurrentTasks [Number] Adjust this value based on your workstation’s core count to balance import speed against editor responsiveness.
5. Utilize the CAD Cache for Iteration

The kernel uses a hashing system (size, name, timestamp) to cache processed geometry in the Intermediate/Datasmith/CADCache folder. Best Practice: When re-importing a modified assembly, do not delete this folder. The kernel will only re-tessellate the specific components that changed, significantly reducing iteration time for large datasets.

6. Toggle for Bug Isolation

If you encounter “exploding” geometry or missing faces on specific complex models, you can temporarily revert to the legacy third-party tessellator to identify if the issue is in the source file or the kernel.

CVar: ds.CADTranslator.DisableCADKernelTessellation 1 (Set back to 0 to re-enable).
7. Set Maximum Edge Length for Consistent Density

Unlike legacy tessellators, CADKernel supports a Max Edge Length parameter. This is critical for Nanite and Lumen, as it prevents the creation of extremely long, thin triangles which can cause artifacts in virtualized geometry and software ray tracing. Set a reasonable max edge length (e.g., 50.0 units) to ensure a uniform mesh density.

8. Debugging Topology via C++

If you are writing custom CAD translators, you can use the UE::CADKernel::EStatut enum to inspect the topological state of faces (Interior, Exterior, Border). This is useful for programmatically identifying “holes” in a model before finalizing the mesh factory step. Use FSystem::PrintHeader() to log the kernel’s initialization state and versioning for diagnostic purposes.