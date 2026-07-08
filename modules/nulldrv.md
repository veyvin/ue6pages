---
layout: default
title: NullDrv
---

<!-- ai-generation-failed -->

<h1>NullDrv</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NullDrv/NullDrv.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

face (RHI) implementation that allows Unreal Engine to run without a physical graphics card or a valid display connection. It acts as a “dummy” renderer that acknowledges draw commands but does not execute them on any hardware, essentially tricking the engine into believing it is rendering frames.

This module is the backbone for headless execution. It is primarily used for dedicated servers, automated commandlets, and Continuous Integration (CI) environments where actual pixel output is unnecessary. By bypassing the need for a GPU, it facilitates the elimination of hardware-related driver crashes and significantly reduces resource overhead in non-visual environments.

Practical Usage Tips and Best Practices
1. Activate via the -NullRHI Command Line

To force the engine to use the NullDrv module, you must launch your executable with the -nullrhi command-line argument. This is essential for the elimination of “No compatible GPU found” errors when running the engine on cloud servers or virtual machines that lack dedicated graphics hardware.

2. Combine with -NoSound for Headless Servers

When running a dedicated server, use -nullrhi in conjunction with -nosound. This ensures the elimination of both the rendering and audio processing overhead, allowing the CPU to dedicate 100% of its cycles to gameplay logic, physics, and networking.

3. Use for Automated Testing and CI/CD

In a DevOps pipeline, use the NullRHI to run Functional Tests and Automation Specs. Because the engine doesn’t have to initialize a DirectX or Vulkan context, the startup time is significantly faster. This practice leads to the elimination of long wait times for build validation on build farm agents.

4. Avoid GPU-Dependent Logic

Since NullDrv does not actually process shaders or textures, any code that relies on reading back data from the GPU (such as FRenderTarget::ReadPixels) will return empty or zeroed data. Designing your logic to detect the NullRHI leads to the elimination of null pointer crashes in systems that expect valid GPU buffers.

5. Leverage for Data-Only Commandlets

When running commandlets to audit assets, export Data Tables, or perform bulk property edits, always use -nullrhi. This assists in the elimination of unnecessary VRAM allocation, allowing you to run multiple instances of the editor simultaneously for parallel data processing.

6. Optimize Server Frame Rates

Even with the NullRHI active, the engine still goes through the motions of the “Rendering Thread.” To achieve maximum server performance, ensure you set t.MaxFPS to a reasonable value (e.g., 30 or 60). This prevents the CPU from “spinning” too fast, leading to the elimination of wasted energy and thermal throttling on server hardware.

7. Monitor for Slate Errors

The engine’s UI system, Slate, usually requires a renderer. When using -nullrhi, Slate uses the SlateNullRenderer. If you are developing custom Editor Utility Widgets, test them with the NullRHI to ensure the elimination of UI-related crashes when the editor is launched in a headless state.

8. Verify Module Dependencies

If you are writing a custom C++ module that must work in headless mode, ensure you do not have hard dependencies on platform-specific RHIs like D3D12RHI. Relying solely on the base RHI and RenderCore modules facilitates the elimination of linker errors when the engine falls back to NullDrv.