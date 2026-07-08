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

ing and managing the 3D interactive viewports within the Unreal Editor. It provides the base classes for rendering a scene, handling camera movement, and processing user input (such as selection and transformation) within the editor environment.

The module is built on a dual-class architecture: the Slate widget (SEditorViewport), which handles the UI and layout, and the Logic Client (FEditorViewportClient), which manages the internal world state, rendering settings, and interaction logic. Developers use this module to create custom asset editors (like a specialized Preview window for a custom mesh type) or to extend the functionality of the standard Level Editor.

Practical Usage Tips and Best Practices
Separate UI from Logic
When building a custom viewport, always derive a new class from FEditorViewportClient to handle the logic and another from SEditorViewport for the UI. Keeping these distinct helps you eliminate “spaghetti code” and allows you to reuse the logic client in different UI configurations if needed.
Use FPreviewScene for Isolated Rendering
If your viewport is for a custom asset editor, use an FPreviewScene instead of the global world. This provides a private, lightweight world for your asset, eliminating visual interference from other actors in the main level and allowing for custom lighting and background setups.
Override Input Handling via the Client
Use the InputKey and InputAxis overrides in your FEditorViewportClient to handle custom shortcuts. This is the standard way to eliminate conflicts with the default editor camera controls, ensuring that your tool-specific hotkeys (like “R” for a custom reset) take priority when the viewport is focused.
Implement Custom Gizmos with Component Visualizers
Rather than drawing raw lines in the viewport, use Component Visualizers to draw handles and gizmos. This framework integrates natively with the EditorViewport module, eliminating the need for complex hit-testing math by allowing the engine to handle clicks on your custom 3D widgets automatically.
Wrap in Preprocessor Guards
The EditorViewport module is strictly for use within the editor. Ensure your code is wrapped in #if WITH_EDITOR and that the module is listed only in the Editor section of your .uplugin or .uproject file. This ensures all editor-only viewport code is eliminated during the packaging of your shipping build.
Optimize Ticking and Performance
Viewports can be performance-heavy. If your custom viewport does not need to update every frame (for example, a static thumbnail preview), disable bIsRealtime by default. This eliminates unnecessary GPU/CPU usage while the user is working in other parts of the editor.
Leverage Draw Helper Functions
Use the FCanvas or FPrimitiveDrawInterface (PDI) within your client’s Draw call to render debug information like wireframes, bounding boxes, or paths. These tools help you eliminate the need for temporary “Debug Actors” in your scene just to visualize technical data.
Handle Selection Callbacks
If your viewport needs to respond when an actor is clicked, use the ProcessClick and IsSelectable methods in the client. This allows you to eliminate unwanted selection behavior, ensuring that users can only select and interact with the specific objects your custom tool was designed to manage.