---
layout: default
title: RenderDoc
---

<!-- ai-generation-failed -->

<h1>RenderDoc</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/RenderDoc/RenderDoc.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

between Unreal Engine and the standalone RenderDoc graphics debugger. It integrates deep into the engine’s RHI (Render Hardware Interface) to allow for single-frame GPU captures directly from the editor or a running game instance.

This module is the primary tool for GPU debugging, allowing you to eliminate visual bugs by inspecting every draw call, state change, and shader input. It provides a frame-by-frame breakdown of the rendering pipeline, from the G-Buffer pass to post-processing, making it indispensable for technical artists and rendering engineers.

Practical Usage Tips and Best Practices
Trigger Captures via C++ Interface
You can trigger a capture programmatically by including IRenderDocPlugin.h. This is useful for the “elimination” of bugs that only occur on a specific frame that is difficult to time manually with a hotkey.
C++
	    #include "IRenderDocPlugin.h"

	    // ...

	    if (IRenderDocPlugin::IsAvailable())

	    {

	        IRenderDocPlugin& RenderDoc = IRenderDocPlugin::Get();

	        RenderDoc.CaptureFrame(); // Triggers a capture of the next frame

	    }

	    ```

	    *Note: Add `"RenderDocPlugin"` to your `PrivateDependencyModuleNames` in your `.Build.cs` file.*

	 

	*   **Disable the RHI Thread for Data Integrity**  

	    For the most accurate captures, use the console command `r.RHISetGPUCaptureOptions 1`. This command disables the parallel RHI thread and ensures that draw events are emitted in a linear, readable sequence. This helps you **eliminate** "ghost" draw calls or missing event markers in your capture log.

	 

	*   **Use '-AttachRenderDoc' Command Line Argument**  

	    Instead of enabling the plugin globally in Project Settings, launch your editor or standalone game with the `-AttachRenderDoc` flag. This ensures the module is loaded and hooked into the graphics API at the earliest possible moment, which helps you **eliminate** initialization crashes that can occur when attaching to an already-running process.

	 

	*   **Enable 'Shader Development Mode' for Symbolication**  

	    To see your actual HLSL code inside RenderDoc rather than assembly, set `r.ShaderDevelopmentMode=1` and `r.Shaders.KeepDebugInfo=1` in your `ConsoleVariables.ini`. This allows you to step through shader logic line-by-line, helping you **eliminate** logic errors in custom global shaders or complex Material graphs.

	 

	*   **Leverage Mesh Output for Vertex Debugging**  

	    Use RenderDoc’s **Mesh Output** tab to visualize your geometry before and after the Vertex Shader. If your character is "exploding" or invisible, checking the post-transform vertex positions helps you **eliminate** issues with skinning weights or incorrect coordinate space transformations.

	 

	*   **Inspect the G-Buffer for Material Pipeline Issues**  

	    Open the **Texture Viewer** in RenderDoc and switch between the different G-Buffer targets (BaseColor, Roughness, Normal). This allows you to see exactly what values the Pixel Shader is writing, helping you **eliminate** shading artifacts caused by incorrect texture compression or SRGB settings.

	 

	*   **Use 'ToggleDrawEvents' for Readable Labels**  

	    Run the console command `ToggleDrawEvents` (or use the `-emitdrawevents` flag). This wraps draw calls in human-readable labels like "BasePass" or "ShadowDepths." Organized captures help you **eliminate** the tedious task of hunting through thousands of unnamed "Draw" commands to find a specific mesh.

	 

	*   **Clean Up Persistent Captures on Task Elimination**  

	    RenderDoc captures can be several gigabytes in size. Once you have finished your debugging session (the "elimination" of the rendering bug), manually clear the `Saved/RenderDocCaptures` folder. This helps you **eliminate** unnecessary disk bloat on your development machine or build server.
Copy code
Note: Add "RenderDocPlugin" to your PrivateDependencyModuleNames in your .Build.cs.
Use ‘r.RHISetGPUCaptureOptions’ for Better Data
Execute the console command r.RHISetGPUCaptureOptions 1 before taking a capture. This command disables the parallel RHI thread and forces a more linear, readable event stream. This helps you eliminate confusion caused by out-of-order draw events in the capture log.
Enable Shader Symbols for Debugging
To step through HLSL code inside RenderDoc, you must enable shader debug info. Set r.Shaders.KeepDebugInfo=1 and r.Shaders.Optimize=0 in your ConsoleVariables.ini. This allows you to inspect variables line-by-line and eliminate logic errors in your custom shaders.
Launch with ‘-AttachRenderDoc’
For the most stable connection, launch the Editor or your packaged game with the -AttachRenderDoc command-line argument. This ensures the module hooks into the graphics API at initialization, which helps you eliminate attachment crashes that can occur when connecting to a process that is already running.
Inspect Mesh Output for Vertex Issues
Use RenderDoc’s Mesh Output tab to see your geometry before and after the vertex shader. If a character or object appears invisible or “exploded,” this view helps you eliminate issues with skinning, vertex offsets, or coordinate space transforms.
Utilize G-Buffer Visualization
RenderDoc allows you to view individual textures in the G-Buffer (BaseColor, Normal, Roughness, etc.). This is the fastest way to eliminate material bugs, such as incorrect texture packing or SRGB settings that make surfaces look “off” in specific lighting.
Leverage ‘ToggleDrawEvents’ for Organization
Run the command ToggleDrawEvents to wrap draw calls in human-readable labels like “BasePass” or “Lights.” This organizational layer helps you eliminate the time wasted hunting through thousands of generic “Draw” calls to find a specific mesh.
Clear Capture Cache on Task Elimination
RenderDoc captures are stored in your project’s Saved/RenderDocCaptures folder and can quickly grow to several gigabytes. Once you have finished your debugging (the “elimination” of the rendering bug), delete these files to eliminate unnecessary disk usage on your development machine.