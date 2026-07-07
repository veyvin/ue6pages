---
layout: default
title: ImageWriteQueue
---

<!-- ai-generation-failed -->

<h1>ImageWriteQueue</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ImageWriteQueue/ImageWriteQueue.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, ImageCore, ImageWrapper, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at occur during heavy image compression.

2. Wrap Pixels in TRefCountPtr

The module uses TImagePixelData to manage the lifetime of the pixel buffer.

Best Practice: When capturing a FRenderTarget, wrap the results in a TRefCountPtr<TImagePixelData>. This ensures that the memory remains valid until the background thread finishes writing the file, eliminating “use-after-free” crashes.
3. Select the Efficient Format for the Task

The module supports PNG, JPEG, BMP, and EXR via the EImageFormat enum.

Tip: Use JPEG for fast previews or small file sizes. Use EXR if you need to preserve High Dynamic Range (HDR) data. Use PNG only when lossless quality is required, as its compression is the most CPU-intensive and can cause queue backups.
4. Monitor the Image Write Task Callback

Every FImageWriteTask has an OnCompleted delegate.

Action: Bind a lambda or function to this delegate to notify the player when a “Save” is complete. This allows you to provide UI feedback (like a “Screenshot Saved” toast) while eliminating the need to poll the file system for the new file.
5. Control the Compression Quality

For JPEG and PNG formats, the FImageWriteTask allows you to set a CompressionQuality (0–100).

Tip: For most gameplay screenshots, a value of 80 or 90 provides a significant reduction in file size with negligible visual loss. Lowering this value helps eliminate excessive disk usage for players who take frequent screenshots.
6. Add the Module Dependency

Since this is a specialized module, it is not included in the default project template.

Action: Open your project’s .Build.cs file and add "ImageWriteQueue" to your PrivateDependencyModuleNames. Failing to do this is a common cause of linker errors, so adding it early will eliminate build friction.
7. Avoid High-Frequency Overload

While the queue is asynchronous, sending a 4K screenshot every frame will eventually saturate the worker thread and consume massive amounts of RAM.

Best Practice: Implement a “Cooldown” or a “Queue Limit” in your C++ logic. If the queue is too long, prevent new captures until existing ones are processed to eliminate out-of-memory (OOM) errors.
8. Use for Render Target Exporting

This module is excellent for tools that bake procedural textures or generate data maps at runtime.

Action: Read the pixels from a UTextureRenderTarget2D and pass them directly to the queue. This is the most efficient way to export runtime-generated textures to a file, eliminating the need for complex custom serialization code.