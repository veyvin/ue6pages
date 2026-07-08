---
layout: default
title: SlateRHIRenderer
---

<!-- ai-generation-failed -->

<h1>SlateRHIRenderer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/SlateRHIRenderer/SlateRHIRenderer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, Engine, HeadMountedDisplay, ImageCore, PreLoadScreen, RHI, RenderCore, Renderer, Slate, SlateBaseRenderer, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the engine’s Render Hardware Interface (RHI). It is responsible for translating the abstract draw elements produced by the Slate UI tree (text, brushes, and borders) into actual GPU commands.

This module handles the batching of draw calls, vertex buffer management, and the execution of Slate-specific shaders. It also manages Slate Post-Processing, allowing for effects like background blur and UI-specific materials. By handling these low-level tasks, it helps you eliminate the complexity of manually rendering 2D interfaces within a 3D engine.

Practical Usage Tips and Best Practices
Enable Slate Postbuffers for Advanced Effects
To use features like background blur behind widgets, you must enable the Slate postbuffer system. Add Slate.CopyBackbufferToSlatePostRenderTargets=1 to your DefaultEngine.ini. This allows the renderer to capture the game scene for UI materials, helping you eliminate visual flat-ness in your menus.
Implement Custom Slate Post-Processors
You can derive from USlateRHIPostBufferProcessor in C++ to create custom global UI effects. This is more performant than per-widget shaders because it operates on the final UI backbuffer. Using this helps you eliminate redundant GPU calculations when applying a single effect (like a color grade) to the entire HUD.
Minimize Draw Call Batches
The SlateRHIRenderer attempts to batch widgets that share the same texture and material. To help the renderer eliminate excessive draw calls, use Texture Atlases (via Sprite Actions) for your UI icons. When multiple icons share one atlas, the renderer can draw them in a single GPU pass.
Use Invalidation Boxes to Save GPU Time
Slate widgets normally re-generate their draw commands every frame. By wrapping complex UI in an Invalidation Box, the SlateRHIRenderer caches the vertex and index buffers. This helps you eliminate the CPU-to-GPU transfer overhead for static UI elements like maps or inventory backgrounds.
Optimize Resolution via Project Settings
In the Slate RHIRenderer Settings, you can set post-processing buffers to run at half resolution. If you are only using the buffer for heavy blurs, lowering the resolution helps you eliminate significant video memory (VRAM) usage and improves performance on mobile or lower-end consoles.
Monitor Performance with Slate Insights
Use the Unreal Insights tool with the “Slate” trace enabled to see how the renderer spends its time. Identifying “Batching” or “Layer” overhead in the trace allows you to restructure your widget hierarchy to eliminate unnecessary rendering layers that force draw-call breaks.
Avoid Overusing ‘Retainer Panels’
While Retainer Panels can improve performance by rendering UI at a lower framerate, they each require a unique Render Target. Overusing them can lead to memory exhaustion. Use them sparingly for specific high-cost widgets to eliminate framerate hitches without crashing the GPU.
Handle Resource Cleanup on Elimination
The SlateRHIRenderer relies on specific RHI resources that must be released when a window is closed. When managing custom Slate viewports, ensure that your FSlateRHIRenderer instance is properly shut down during the “elimination” of the application window to eliminate memory leaks and RHI device errors.