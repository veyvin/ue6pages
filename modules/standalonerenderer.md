---
layout: default
title: StandaloneRenderer
---

<!-- ai-generation-failed -->

<h1>StandaloneRenderer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/StandaloneRenderer/StandaloneRenderer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, ImageWrapper, InputCore, SlateCore, SlateNullRenderer</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed for external, lightweight applications that do not require the full Unreal Engine Runtime or the Rendering Hardware Interface (RHI). It provides a platform-native way to render Slate UI using OpenGL or DirectX 11 in a “standalone” fashion.

This module is primarily used for utility programs like the Unreal Insights, Slate Viewer, or custom launcher applications. By using this module, you can eliminate the massive overhead of initializing the entire engine, allowing you to create high-performance, Slate-based tools that start instantly and have a minimal memory footprint.

Practical Usage Tips and Best Practices
Use for Non-RHI Applications
If you are building a tool that doesn’t need 3D world rendering (Lumen, Nanite, etc.), use this module instead of the standard engine renderer. This allows your tool to run on machines with limited graphics capabilities and helps you eliminate dependencies on the Engine and Renderer modules.
Initialize via ‘FSlateStandaloneRenderer’
To start the renderer, you must manually create an instance of FSlateStandaloneRenderer. You can choose the backend (e.g., CreateVulkanStandaloneRenderer or CreateD3DStandaloneRenderer). This explicit control allows you to eliminate unnecessary driver initializations that aren’t relevant to your tool.
Manage the Application Loop Manually
Because you aren’t using the standard FEngineLoop, you must handle the message pump and Slate application tick yourself. Use FSlateApplication::Get().Tick() and FSlateApplication::Get().PollGameDeviceState() within a custom loop to eliminate input lag and keep the UI responsive.
Include in ‘Program’ Targets
This module is most effective when used in a “Program” target (defined in a .Target.cs file with TargetType.Program). This configuration helps you eliminate the inclusion of gameplay systems like Physics or AI, resulting in a very small executable size for your utility.
Leverage for Threaded Tools
StandaloneRenderer is often used in conjunction with FRunnable to create multi-threaded monitoring tools. Ensure your Slate logic remains on the main “Slate Thread” to eliminate race conditions, while the data-gathering logic runs on background threads.
Standalone Styling and Resources
When using this module, you must manually load and provide a ISlateStyle for your widgets. Since you don’t have the UObject system to manage assets, you should use the FSlateGameResources class to eliminate the need for the Content Browser when loading icons and fonts.
Use for ‘Slate Viewer’ Testing
If you are developing complex custom widgets, use the Slate Viewer (which uses this module) to test them in isolation. This helps you eliminate long iteration times by avoiding a full Editor restart every time you change a piece of C++ Slate code.
Graceful Shutdown and Resource Elimination
When the standalone application exits, you must explicitly call Shutdown() on the renderer and the Slate application. Properly managing the “elimination” of the renderer ensures that GPU device contexts are released correctly, which helps you eliminate persistent “device lost” errors or memory leaks in the OS.