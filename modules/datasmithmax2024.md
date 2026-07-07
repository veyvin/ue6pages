---
layout: default
title: DatasmithMax2024
---

<!-- ai-generation-failed -->

<h1>DatasmithMax2024</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/DatasmithMax2024.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>DatasmithMaxBase</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

3ds Max 2024. It facilitates high-fidelity scene translation from 3ds Max into Unreal Engine 5, ensuring that geometry, complex materials (including V-Ray and Corona), lights, cameras, and scene hierarchies are preserved.

It supports two primary workflows: exporting a static .udatasmith file for manual import and the Direct Link system, which allows for real-time synchronization between the 3ds Max viewport and the Unreal Editor.

1. Utilize Direct Link for Rapid Iteration

Instead of manually exporting files every time you move an object, use the Direct Link feature.

Best Practice: Open the Datasmith tab in 3ds Max and click Synchronize. In Unreal Engine, use the Direct Link Import tool to establish a live connection. This allows you to see lighting and layout changes in the engine immediately, eliminating the need for constant re-imports.
2. Manage the Direct Link Cache

Direct Link uses a local directory to temporarily store data before it is pushed to Unreal.

Tip: If you experience disk space issues or synchronization lag, go to the Connection Status window in 3ds Max and change the Cache Directory to a high-speed NVMe drive. Periodically use the “Reset” button to clear old cache files and eliminate potential data corruption.
3. Configure Animation Export Segments

The 2024 exporter allows for precise control over how 3D transforms are handled.

Best Practice: If your scene contains moving parts, set the animation export to Active Time Segment in the File Export panel. This ensures that only the relevant frames are baked into the Level Sequence in Unreal, preventing bloated file sizes from unused timeline data.
4. Optimize Baked Texture Resolution

When 3ds Max uses procedural maps or complex shaders that Unreal cannot translate natively, Datasmith “bakes” them into images.

Tip: In the Datasmith Settings panel, adjust the Max Texture Size (e.g., to 4K or 8K). Setting this too high can crash your GPU memory, while setting it too low results in blurry materials. Aim for 2K (2048 pixels) for most architectural props to balance quality and performance.
5. Filter Exports via Visibility

Datasmith only exports what is currently visible in the 3ds Max viewport.

Best Practice: Use 3ds Max Layers or Selection Sets to hide high-poly background objects or internal mechanics that the player will never see. By hiding these objects before hitting Export or Sync, you eliminate unnecessary geometry processing and speed up the import time in Unreal.
6. Use the Messages Window for Troubleshooting

The Datasmith Messages Window in 3ds Max provides vital feedback during the conversion process.

Tip: Always check this window after a sync. It will alert you to missing textures, unsupported material types, or overlapping UVs. Fixing these errors in 3ds Max before moving to Unreal is the most efficient way to ensure visual consistency.
7. Enable Statistics for Direct Link

By default, the detailed statistics shown during file exports are disabled for Direct Link to save time.

Tip: If you are debugging a slow synchronization, open the MaxScript console and enter Datasmith_SetExportOption_StatSync true. This will force the exporter to output detailed timing data to the Messages window, helping you identify which specific object is slowing down the link.
8. Include XRef Scenes for Large Projects

If your master 3ds Max file references external .max files (XRefs), ensure they are included in your export.

Best Practice: Check the Include XRefs toggle in the Datasmith Settings. This allows you to maintain a modular workflow where different team members work on different parts of a building or environment, while still allowing for a single, unified Datasmith export into the engine.