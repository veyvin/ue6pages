---
layout: default
title: DatasmithMax2025
---

<!-- ai-generation-failed -->

<h1>DatasmithMax2025</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/DatasmithMax2025.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>DatasmithMaxBase</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ned to facilitate the translation of high-fidelity scenes from Autodesk 3ds Max 2025 into Unreal Engine. It serves as the backend for the Datasmith Exporter plugin, specifically updated to support the latest 3ds Max APIs and the Unreal Engine 5.6 pipeline.

This module is primarily used to convert 3ds Max-specific data—such as V-Ray or Corona materials, complex geometric hierarchies, and physical cameras—into a format Unreal Engine can ingest. It also manages the Direct Link functionality, which allows for real-time synchronization between the 3ds Max viewport and the Unreal Editor, helping to eliminate the need for repetitive manual exports.

Practical Usage Tips and Best Practices
Utilize the Direct Link Workflow
Instead of exporting static .udatasmith files, use the Direct Link feature managed by this module. This allows you to see changes in Unreal Engine almost instantly after a “Sync” command in 3ds Max, which helps to eliminate the time-consuming cycle of exporting and re-importing assets during the look-dev phase.
Manage Texture Baking Limits
The module includes settings to bake procedural maps into textures. Use the “Bake Resolution” setting in the 3ds Max ribbon to cap these at 4K or 8K. This ensures you eliminate excessive memory usage while maintaining enough detail for architectural visualizations.
Handle Animated Transforms via the Timeline
When exporting, you can choose “Active Time Segment” to capture 3D transform animations. This module converts these into a Level Sequence in Unreal. Ensure your keys are baked or simplified before export to eliminate jittery motion caused by overly dense keyframe data.
Optimize Geometry with XRef Scenes
The module supports “XRef Scenes” (externally referenced files). When working on massive environments, keep your furniture or foliage in XRef scenes and ensure “Include XRef” is enabled in the Datasmith settings. This helps eliminate file bloat in your main 3ds Max working file while still exporting the complete scene.
Validate Material Compatibility
While the module is excellent at converting V-Ray and Corona materials, some complex procedural nodes may not translate perfectly. Use the “Datasmith Attributes” modifier in 3ds Max to specify how certain objects should be treated, which helps to eliminate visual discrepancies after the import process.
Check for Plugin Version Mismatch
Since this is version-specific (2025), ensure that the Datasmith Exporter plugin installed in 3ds Max matches the version of the engine you are using. Using a 2024 plugin with the 2025 module can lead to stability issues; keeping these synchronized will eliminate unexpected crashes during the translation process.
Control Pivot Points for Interactivity
Datasmith generally preserves the pivot points established in 3ds Max. Before exporting, ensure your pivots are logically placed (e.g., at the base of a door). This allows you to eliminate the need for manual pivot adjustments in Unreal Engine when setting up gameplay or interactive elements.
Use Global Stats to Monitor Scene Heaviness
Before initiating a sync, check the “Stats” provided by the Datasmith ribbon in 3ds Max. If your polygon count is in the tens of millions without using Nanite, use the module’s export settings to “eliminate” high-poly background objects or replace them with proxy geometry to maintain editor performance.