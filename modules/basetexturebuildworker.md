---
layout: default
title: BaseTextureBuildWorker
---

<!-- ai-generation-failed -->

<h1>BaseTextureBuildWorker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BaseTextureBuildWorker/BaseTextureBuildWorker.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TextureBuildWorker</code></span></li><li><span class="label">依赖</span><span class="value">Core, TextureBuild, TextureBuildUtilities, TextureFormat, TextureFormatASTC, TextureFormatETC2, TextureFormatOodle, TextureFormatUncompressed</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine that handles the background processing of texture data during the build and cook process.

Description and Purpose

This module serves as the foundational worker logic for the Texture Build system. When Unreal Engine needs to compress or transcode a texture (e.g., converting a .tga source into a platform-specific format like ASTC or BC7), it offloads the work to these worker modules. It acts as an interface between the high-level Texture Build system and the specific encoders. Its primary purpose is to enable parallelized texture processing, allowing the engine to utilize all available CPU cores or distributed build systems (like Zen or XGE) to accelerate texture compilation times.

Practical Usage Tips and Best Practices
Monitor Background Task Progress
Texture building often happens in the background while the Editor is open. You can monitor the activity of these workers by clicking the “Tasks” icon in the bottom right of the Unreal Editor. If the worker is busy, you may see lower-resolution “placeholder” textures until the build is complete.
Optimize for Local DDC Speed
The workers feed results into your Derived Data Cache (DDC). To ensure these workers perform efficiently, always host your local DDC on a fast NVMe drive. This helps eliminate the “waiting for textures” bottleneck where the worker has finished the build but is blocked by slow disk I/O.
Enable Distributed Texture Building
For large teams, ensure your project is configured to use Unreal Cloud DDC or Zen Store. This allows a single worker on one machine to build a texture and share the result with the entire team, effectively eliminating the need for every developer’s machine to run the same build worker for the same asset.
Configure Worker Priority
If texture building is causing the Editor UI to lag, you can adjust the priority of background workers in the Editor Preferences > General > Experimental > Texture Import/Build settings (or via Console Variables like t.Texture.ParallelBuild). Lowering the priority allows for a smoother editing experience at the cost of slower texture updates.
Debug via LogTextureBuildWorker
If textures are failing to compile or appearing corrupted, check the Output Log for the LogTextureBuildWorker category. This will provide specific error codes from the underlying encoders (like Oodle or ASTCenc) that the worker is currently managing.
Utilize for High-Speed Iteration
In UE 5.6 and 5.7, these workers are more efficient at “on-demand” builds. When you change a texture setting (like changing a “Normal Map” to “Masks”), the worker triggers immediately. Use this for rapid look-dev; the worker will build only the necessary mip levels first to give you a quick visual preview.
Elimination of Build Redundancy
When a texture-heavy character is updated—for example, during the design of a player elimination effect—the worker only rebuilds the modified layers. To keep these builds fast, keep your source textures at the power-of-two dimensions they will use in-game, which allows the worker to eliminate unnecessary scaling steps during the transcode process.
Clean Up Stale Worker Data
If you experience persistent visual glitches in your textures, it may be due to “poisoned” worker output in the cache. Use the commandlet -run=DerivedDataCache -fill or manually clear your DerivedDataCache folder to force the BaseTextureBuildWorker to re-process all assets from their raw source data.