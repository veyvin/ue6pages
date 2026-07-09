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

e editor framework that manages the rendering and interaction logic of the 3D windows used to view levels and assets. It provides the base classes for creating custom viewports, handling camera navigation, and managing the “Preview Scene”—a private world used for rendering assets like Static Meshes or Blueprints in isolation.

Its primary role is to bridge the Slate UI system with the Rendering Pipeline. By using this module, developers can create specialized editor windows with their own dedicated 3D views, complete with custom gizmos, grid snapping, and selection logic.

Practical Usage Tips and Best Practices
Inherit from SEditorViewport for Custom Tools
When creating a custom editor tool with a 3D view, inherit your widget from SEditorViewport. This “eliminates” the need to write boilerplate code for common editor features, as it provides built-in support for toolbars, view mode menus (Lit/Wireframe), and viewport specific settings.
Implement a Custom FEditorViewportClient
The “Client” class handles the actual logic of the viewport. Override FEditorViewportClient to define how the camera moves and how objects are selected. This “eliminates” standard level editor behavior if you need a specialized interaction model, such as a fixed-orbit camera for an item inspector.
Manage Lifetime with FPreviewScene
To display objects in a custom viewport without them appearing in the actual game world, use FPreviewScene. Ensure you manually add and remove actors from this scene to “eliminate” memory leaks; the preview scene acts as a miniature, isolated UWorld dedicated to that specific viewport.
Override Draw Functions for Debugging
Use the Draw() and DrawCanvas() overrides in your Viewport Client to render custom lines, text, or shapes. This is a best practice for “eliminating” ambiguity in custom tools by drawing specialized handles or bounding boxes that only appear within your tool’s viewport.
Handle Input through InputAxis and InputKey
Instead of using standard Slate input events, override InputKey and InputAxis within your FEditorViewportClient. This “eliminates” conflicts with the rest of the Editor’s UI, ensuring that shortcuts like “W/E/R” for transforms only trigger when the user is actively interacting with your 3D view.
Use AdvancedPreviewScene for Lighting
If your viewport needs to show assets with realistic lighting (like the Static Mesh Editor), use FAdvancedPreviewScene instead of the basic version. This “eliminates” the flat look of unlit assets by providing a built-in skybox, directional light, and post-processing settings that the user can tune via a “Preview Settings” tab.
Optimize with Ticking Controls
Viewports can be performance-heavy. Use SetRealtime(false) when the viewport is not the primary focus to “eliminate” unnecessary GPU usage. You can then call Invalidate() only when the data changes, ensuring the viewport only redraws when absolutely necessary.
Support Transform Gizmos via FWidget::Render
If your custom viewport requires movement gizmos, ensure your Client class implements the Widget logic. This allows you to use the engine’s native translation and rotation widgets, “eliminating” the need to build a custom coordinate manipulation system from scratch.