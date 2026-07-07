---
layout: default
title: CADKernelEditor
---

<!-- ai-generation-failed -->

<h1>CADKernelEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Datasmith/CADKernel/Editor/CADKernelEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CADKernel, CADKernelEngine, ContentBrowser, Core, CoreUObject, EditorFramework, Engine, Slate, SlateCore, StaticMeshEditor, ToolMenus</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

al Engine’s proprietary CAD (Computer-Aided Design) kernel. Introduced in UE 5.1 and becoming the default in 5.3, this module provides the logic and UI integration for the high-fidelity tessellation engine used by Datasmith to convert parametric CAD data (like CATIA, SolidWorks, or Rhino) into Unreal-compatible triangular meshes.

While the core CADKernel handles the math, CADKernelEditor manages how these tools appear in the Datasmith import dialogs, handles re-tessellation workflows, and integrates the kernel with the Unreal Editor’s caching systems.

1. Leverage CADKernel for Better Mesh Quality

CADKernel generally provides superior results compared to the “Legacy” tessellator. It is specifically designed to produce fewer T-junctions and open edges, which is critical for a smooth Nanite conversion.

Best Practice: Keep the default setting (CADKernel enabled) for most automotive or industrial data to ensure a clean surface for complex materials like carpaint.
2. Control Tessellation via Console Variables

If you need to troubleshoot or force a specific behavior during an editor session, you can use the ds.CADTranslator CVARs.

Tip: If you encounter a bug with a specific file, you can temporarily revert to the old system using: ds.CADTranslator.DisableCADKernelTessellation 1.
3. Master the Primary Tessellation Parameters

When importing through the CADKernelEditor interface, focus on these three values to balance performance and quality:

Chord Tolerance: The max distance between the mesh and the original surface. Lower values = smoother curves.
Max Edge Length: Limits the size of a single triangle edge. Essential for preventing long, thin triangles that cause lighting artifacts.
Normal Tolerance: Controls the angular difference between triangles. Lower values create denser meshes on curved corners.
4. Use “Sew Mesh” for Open Surfaces

Some CAD files come with “unstitched” surfaces that result in gaps in Unreal.

Tip: Enable ds.CADTranslator.SewMeshIfNeeded 1. This adds a post-tessellation pass that attempts to bridge small gaps and stitch edges together, effectively eliminating light leaks and visual cracks in the geometry.
5. Utilize the CAD Cache for Rapid Re-imports

The module manages a subfolder in your project called DatasmithCADCache. This stores pre-processed versions of your CAD files.

Best Practice: Do not delete this folder manually. The cache allows you to re-tessellate or re-import a file without having to re-read the entire heavy source SDK format, significantly reducing iteration time.
6. Fine-Tune Geometry with Re-tessellation

You don’t need to re-import the entire assembly to fix one jagged part.

Tip: Select a Static Mesh asset in the Content Browser or a Datasmith Scene Actor, and look for the “Retessellate” option in the details panel. This invokes the CADKernelEditor logic to re-calculate only that specific mesh with higher quality settings.
7. Manage Multi-Threaded Import Performance

CADKernel is highly multi-threaded. While this speeds up imports, it can saturate your CPU and make the editor unresponsive.

Tip: Use ds.CADTranslator.MaxImportThreads to limit how many cores the kernel uses. This is helpful if you need to continue working in other applications while a large assembly is importing.
8. Match Stitching Tolerance to Model Scale

If your model has tiny details that are being merged or “melted” together, check your Stitching Tolerance.

Best Practice: If you are importing a small engine part in millimeters, ensure your tolerance is tight. If you are importing a large architectural structure, you can loosen the tolerance to eliminate micro-gaps without losing important detail.