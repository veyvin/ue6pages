---
layout: default
title: DatasmithMaxBase
---

<!-- ai-generation-failed -->

<h1>DatasmithMaxBase</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/DatasmithMax2022.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">DatasmithExporter, DatasmithExporterUI, IntelTBB, Slate, SlateCore, UEOpenExr, UdpMessaging</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

all versions of the Unreal Datasmith exporter for Autodesk 3ds Max. It contains the core logic and utility functions used to translate Max-specific data into the Datasmith scene format.

What it is and What it’s used for

Rather than rewriting the export logic for every version of 3ds Max (2021, 2022, 2023, etc.), Epic Games uses DatasmithMaxBase to house the common “translation” engine. It handles the heavy lifting of converting 3ds Max scene entities—such as geometry, materials, lights, and cameras—into a universal Datasmith representation.

Primary uses include:

Common Translation Logic: Providing shared code for converting complex 3ds Max objects (like RailClone or Forest Pack) into Unreal-compatible instances.
Material Parsing: Managing the base logic for interpreting shader networks from popular renderers like V-Ray, Corona, and Arnold.
Direct Link Management: Handling the shared communication protocols used to synchronize scenes between 3ds Max and Unreal Engine via the Datasmith Hub.
UI Framework: Providing the standardized ribbon menus, settings dialogs, and logging windows that remain consistent across all supported Max versions.
Practical Usage Tips and Best Practices
1. Prioritize Instancing in Max

The base module is highly optimized to recognize 3ds Max “Instances.” To ensure the elimination of redundant memory usage in Unreal, always use the Instance copy method in Max rather than “Copy.” DatasmithMaxBase will correctly identify these and create a single Static Mesh asset in Unreal with multiple Actor instances.

2. Utilize the Datasmith_Log Commands

When automating your pipeline using MAXScript, leverage the logging functions provided by the base module (e.g., Datasmith_LogInfo, Datasmith_LogWarning). These allow you to push custom messages to the Datasmith Messages window, making it easier to debug automated export routines for complex scenes.

3. Standardize Scene Units

To avoid scaling issues, ensure your 3ds Max “System Units” are set to Centimeters. While DatasmithMaxBase attempts to handle unit conversion, keeping Max in centimeters (the native Unreal unit) ensures the most accurate translation of light intensities and physical dimensions.

4. Handle Groups and Layers Logically

DatasmithMaxBase preserves the 3ds Max hierarchy. Grouping objects in Max will result in nested Actor hierarchies in Unreal. For a cleaner “Outliner” experience, organize your scene into logical layers and groups before exporting; this makes the imported scene much easier for level designers to navigate.

5. Monitor the “Quiet” Export Mode

If you are performing batch exports via script, use the quiet:true flag in the Datasmith_Export command. This utilizes the base module’s headless mode, which suppresses UI pop-ups and progress bars, allowing your automation scripts to run without manual intervention.

6. Coordinate with Visual Dataprep

Since DatasmithMaxBase attaches 3ds Max object properties as metadata, you can use Unreal’s Visual Dataprep to filter objects based on these attributes. For example, you can create a rule to automatically replace all Max objects with the “Collision” prefix with Unreal collision volumes during the import process.

7. Keep Geometry Clean (No Non-Orthogonal Scaling)

A common pitfall the base module encounters is non-orthogonal scaling (scaling an object differently on X, Y, and Z at the object level). This can cause “flipped” faces or skewed transforms in Unreal. Always Reset XForm on your objects in Max before exporting to ensure a clean transform matrix.

8. Verify Material “Baking” Settings

If you use complex procedural maps that don’t have a direct PBR equivalent, the base module will “bake” them into textures. Check your Settings panel to ensure the Max Texture Size is sufficient (e.g., 2048 or 4096) for your specific project’s quality requirements before initiating the export.