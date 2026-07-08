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

data (screenshots, render target captures, or procedural textures) to disk. It acts as a specialized task manager that offloads the heavy work of image compression (PNG, JPEG, EXR, BMP) and file I/O to background threads.

By using this module, you can eliminate the significant “hitches” or frame-rate spikes that occur when the Game Thread is forced to wait for slow disk operations. It is the standard way to implement high-quality photo modes or diagnostic logging without interrupting the player’s experience.

Practical Usage Tips and Best Practices
Add Module Dependency
To use this in C++, you must add "ImageWriteQueue" to your PrivateDependencyModuleNames in your project’s Build.cs file. Also, include ImageWriteQueueModule.h and ImageWriteTask.h in your source code to access the IImageWriteQueue interface.
Utilize TUniquePtr for Task Ownership
The Enqueue function requires a TUniquePtr<FImageWriteTask>. This ownership model helps you eliminate memory leaks, as the queue automatically handles the cleanup of the task and its associated pixel data once the file has been successfully written to disk.
Move Pixel Data to Avoid Copies
When populating your FImageWriteTask, use MoveTemp to transfer your array of pixel data into the task. This helps eliminate redundant memory allocations and large-scale data copies, ensuring the background thread takes direct ownership of the buffer.
Leverage the OnCompleted Callback
Instead of polling the file system to see if an image is ready, assign a lambda or function to the OnCompleted delegate. This allows you to safely notify the player or update a UI gallery only after the image is confirmed to be on disk, helping you eliminate “File Not Found” errors.
Select the Appropriate Format
Choose your format based on the data type:
PNG/JPEG: Standard 8-bit screenshots.
EXR: Essential for HDR data or linear color space captures (16⁄32-bit).
Using the wrong format for high-bitrate data will eliminate precision, so ensure your format matches your Render Target’s bit depth.
Set Task Priority
The queue supports different priority levels. For user-initiated actions (like a “Save Screenshot” button), use a high priority. For background diagnostic logging, use a lower priority to eliminate any contention with critical system tasks.
Limit Queue Depth
While the queue is asynchronous, enqueuing hundreds of 4K images at once can consume a massive amount of RAM. Implement a simple counter to eliminate the risk of Out-Of-Memory (OOM) crashes by preventing new tasks if too many are already pending.
Readback on the Render Thread
When capturing a URenderTarget2D, perform the ReadPixels operation on the Render Thread. Immediately hand the resulting data to the ImageWriteQueue to eliminate any synchronization stalls between the GPU and the Game Thread.