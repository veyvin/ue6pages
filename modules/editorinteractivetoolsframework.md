---
layout: default
title: EditorInteractiveToolsFramework
---

<!-- ai-generation-failed -->

<h1>EditorInteractiveToolsFramework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Experimental/EditorInteractiveToolsFramework/EditorInteractiveToolsFramework.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationCore, ApplicationCore, Core, CoreUObject, DesktopPlatform, DeveloperSettings, EditorFramework, EditorStyle, EditorSubsystem, EditorViewport, Engine, InputCore, InteractiveToolsFramework, Json, JsonUtilities, MeshDescription, PropertyEditor, RenderCore, Slate, SlateCore, StaticMeshDescription, ToolWidgets, TypedElementFramework, TypedElementRuntime, ViewportSnapping, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ion of the core Interactive Tools Framework (ITF). It provides the infrastructure for building complex, stateful, and interactive viewport tools—such as those found in Modeling Mode, Fracture Mode, or Foliage.

While the base framework handles generic “Tool” logic (input, gizmos, and lifecycle), this editor-specific module integrates those tools with the Unreal Editor’s selection system, Undo/Redo buffer, and specialized UI panels (the “Details” panel). It allows you to eliminate the need for manual Slate UI coding for tool settings by using reflection-based property sets.

Practical Usage Tips and Best Practices
Implement a Lightweight ToolBuilder
Every tool requires a UInteractiveToolBuilder. Keep this class minimal; its only job is to determine if a tool can run (e.g., checking if the user has a Static Mesh selected) and to spawn the tool instance. This separation helps you eliminate initialization overhead by only loading the heavy tool logic when the user actually activates the tool.
Use Property Sets for Automatic UI
Instead of building custom Slate widgets, define a UInteractiveToolPropertySet class with your settings as UPROPERTY members. When you register these with your tool, the framework automatically generates a synchronized UI in the Tool Settings panel. This eliminates the boilerplate of manual UI-to-variable binding.
Handle Undo/Redo via Transactions
The framework is designed to work with the Editor’s transaction buffer. When your tool modifies an actor, ensure you wrap the change in an FScopedTransaction. This ensures that the “Cancel” button or Ctrl+Z works natively, eliminating the risk of leaving the level in a corrupted or partially modified state.
Route Input through Input Behaviors
Avoid overriding raw mouse events. Instead, register IInputBehavior objects (like USingleClickInputBehavior) within your tool’s Setup(). The framework’s UInputRouter will then handle priorities, helping you eliminate input conflicts between your custom tool and the standard editor camera controls.
Leverage Transform Gizmos Natively
If your tool needs to move elements in 3D space, use the UTransformGizmo. The framework provides a UInteractiveGizmoManager that handles the rendering and hit-testing of these gizmos for you. This allows you to eliminate the complex math of 3D-to-2D projection and manual mouse dragging logic.
Utilize Context Objects for Shared Data
If your tool needs to access specific editor subsystems (like the Asset Registry), use UInteractiveToolManager::GetContextObjectStore(). This pattern helps you eliminate hard-coded dependencies by allowing the Editor Mode to “provide” data that the Tool “consumes” via a generic interface.
Offload Heavy Geometry Math
For tools that perform complex operations (like boolean meshes), use background threads or the FQueuedThreadPool. Keeping the main thread free for the Tick() function eliminates UI stuttering, making the tool feel responsive even when processing high-density Nanite meshes.
Restrict to Editor-Only Modules
Ensure your tool classes are located in an Editor module and wrapped in #if WITH_EDITOR. This ensures that all interactive tool logic is eliminated from the shipping build, preventing bloat and potential linker errors in your final executable.