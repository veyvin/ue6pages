---
layout: default
title: DatasmithExporterUI
---

<!-- ai-generation-failed -->

<h1>DatasmithExporterUI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Datasmith/DatasmithExporterUI/DatasmithExporterUI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DatasmithCore, DatasmithExporter, DesktopPlatform, DirectLink, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

k that provides the user interface components and dialog logic for Datasmith export workflows. It acts as the UI bridge between Unreal Engine and external CAD/3D software (like 3ds Max, Navisworks, or SketchUp), managing the presentation of export options, progress bars, and post-export validation reports.

This module is designed to “eliminate” the friction of moving data between different software ecosystems by providing a consistent, user-friendly interface for configuring how geometry, materials, and animations are translated into the .udatasmith format.

Practical Usage Tips and Best Practices
Review the Post-Export Validation Window
After an export finishes, the UI displays a summary of warnings. Use this to identify “invalid objects” or “unsupported materials.” Addressing these early helps “eliminate” visual artifacts or missing geometry before you even open the file in Unreal Engine.
Configure Animated Transform Settings
Within the exporter UI, you can toggle between “Current Frame Only” and “Active Time Segment.” If your goal is to “eliminate” unnecessary file bloat, ensure you only select “Active Time Segment” when you specifically need to preserve object-level animations for the Level Sequence.
Manage Texture Resolution Limits
The UI includes a setting for maximum baked procedural texture resolution (ranging from 4K to 16M). Setting a sensible limit here “eliminates” excessive VRAM usage and long import times for complex procedural materials that need to be flattened into raster images.
Toggle XRef Inclusion
In the Settings panel of the exporter UI, you can choose whether to include XRef (External Reference) scenes. Carefully managing this “eliminates” the accidental export of massive background environments that might already exist in your destination Unreal project.
Utilize the “Visible Objects” Filter
To “eliminate” unwanted clutter from your export, use the UI’s selection filter to export only “Visible Objects” or a specific “Selection.” This is a best practice for modularizing your scene and keeping individual .udatasmith files manageable.
Check the Direct Link Status
The UI provides a Direct Link panel to manage live synchronization. Use the “Auto-Sync” toggle to “eliminate” the need for manual exports every time a change is made, allowing for real-time iteration between your source software and the engine.
Coordinate Origin Points
Many exporters (like the Navisworks plugin) allow you to specify an origin point in the UI. Setting this correctly “eliminates” the “floating geometry” problem where assets appear thousands of units away from the world center in Unreal.
Automate via Scripting to Skip UI
While this module handles the UI, you can use the Datasmith_Export MAXScript or Python interfaces to “eliminate” the UI prompts entirely during batch processing. This is ideal for pipeline engineers who need to process hundreds of assets without manual interaction.