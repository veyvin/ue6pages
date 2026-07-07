---
layout: default
title: EditorViewport
---

<!-- ai-generation-failed -->

<h1>EditorViewport</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EditorViewport/EditorViewport.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

uild interactive 3D and 2D rendering windows within the Unreal Editor. It provides the core Slate widgets and logic controllers—specifically SEditorViewport and FEditorViewportClient—that allow developers to create custom viewport panels for asset editors (like the Static Mesh or Animation editors) or unique level editing tools.

This module manages the rendering of a scene, camera navigation (W-A-S-D, orbiting), input handling, and the drawing of editor-specific helper graphics like grid lines and transformation gizmos.

Practical Usage Tips and Best Practices
1. Decouple Logic with FEditorViewportClient

The SEditorViewport is merely a Slate container; all interaction logic should reside in a class inheriting from FEditorViewportClient.

Best Practice: Use the Viewport Client to handle camera movement, raycasts, and selection logic. Keeping the rendering logic separate from the UI widget helps you eliminate code complexity and makes your viewport easier to maintain and debug.
2. Implement a Custom FPreviewScene

Custom viewports usually need their own “world” to render objects without affecting the actual gameplay level.

Tip: Initialize your Viewport Client with a FPreviewScene. This provides a private UWorld where you can spawn temporary actors, lights, and floor meshes. This ensures your editor tool remains isolated, eliminating the risk of accidentally spawning editor-only actors into the user’s active game level.
3. Override InputKey for Custom Shortcuts

If your editor tool requires specific hotkeys (e.g., “R” to reset a preview or “Space” to toggle an animation), do not use the standard Slate input system.

Action: Override the InputKey function in your FEditorViewportClient. This allows you to capture keystrokes directly within the 3D context, eliminating conflicts with the main Editor’s global hotkeys.
4. Use Hit Proxies for Object Selection

Detecting which object a user clicked on in a 3D viewport can be computationally expensive if done with manual physics traces.

Tip: Use Unreal’s Hit Proxy system (e.g., HHitProxy). When rendering your objects, you assign them a proxy ID; the engine then handles the pixel-perfect detection when the user clicks. This helps you eliminate the performance overhead of per-frame raycasting for selection.
5. Draw Debug Overlays with ‘Draw’

Sometimes you need to render lines, text, or shapes that aren’t actual Actors in the world.

Action: Override the Draw(FViewport* Viewport, FCanvas* Canvas) function in your Viewport Client. Use the FCanvas to draw 2D/3D helper graphics. This is the most efficient way to render non-diegetic information, eliminating the need for expensive “Debug Line” actors.
6. Optimize with Real-Time Toggling

By default, viewports may try to render at the maximum possible framerate, which consumes significant GPU resources.

Best Practice: Expose a “Real-Time” toggle in your viewport’s toolbar (using ELevelViewportType). When disabled, the viewport will only redraw when the user interacts with it or the scene changes. This helps eliminate unnecessary power consumption and heat during long dev sessions.
7. Handle Camera Persistence

Users often find it frustrating when the camera resets its position every time they open your custom editor tab.

Tip: Store the camera’s location and rotation in your Viewport Client’s configuration or a UDeveloperSettings class. Restore these values when the viewport is constructed to eliminate the need for users to manually re-frame their view every time they open the tool.
8. Utilize Viewport Scalability

If your custom viewport is used for complex data visualization, it might lag on lower-end hardware.

Action: Use the GetScene()->GetRendererSettings() to adjust scalability specifically for your preview. Lowering the resolution scale or disabling heavy post-processing like Motion Blur for that specific window helps eliminate performance hitches while maintaining high fidelity in the main Level Editor.