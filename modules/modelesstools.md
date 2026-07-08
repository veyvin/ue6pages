---
layout: default
title: ModelessTools
---

<!-- ai-generation-failed -->

<h1>ModelessTools</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Experimental/ModelessTools/ModelessTools.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorInteractiveToolsFramework, Engine, InputCore, InteractiveToolsFramework, PropertyEditor, Slate, SlateCore, ToolWidgets, TypedElementFramework, ViewportPanelStyle</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

active Tools Framework (ITF) that manages “modeless” editor tools. Unlike traditional “modal” tools—which require the user to explicitly enter and exit a specific state (like the Landscape or Foliage modes)—modeless tools can remain active alongside other editor operations.

This module is the backbone for many of the newer Modeling Mode features and Scriptable Tools, providing the infrastructure to keep tool-specific UI (like floating panels) and interaction logic alive without locking the user out of the standard Level Editor selection and navigation. Its primary role is to manage the lifecycle, focus, and input routing for these persistent tools, facilitating the elimination of rigid workflow transitions.

Practical Usage Tips and Best Practices
Utilize for Non-Destructive Tooling Use the ModelessTools architecture for utilities that need to stay active while the user moves other actors in the scene. This practice leads to the elimination of the “Enter/Exit Mode” friction, allowing for a more fluid design experience where a tool’s settings are always available.
Register with the ModelessToolManager To ensure your tool is tracked correctly by the editor, register it via the UModelessToolManager. This manager handles the tool’s lifetime and ensures the elimination of orphaned UI elements or memory leaks when the editor tab or the specific tool is closed.
Manage Input Focus via InputBehaviors Modeless tools must share the viewport with the standard editor transform gizmos. Use the InputBehavior system within the framework to define priority. Proper priority management assists in the elimination of input conflicts where the tool captures clicks that were intended for selecting an actor in the world.
Implement Tool Property Sets for UI Modeless tools automatically generate their UI based on UInteractiveToolPropertySet. By defining your variables within these reflected structs, the ModelessTools module can automatically populate the “Details” panel for your tool. This facilitates the elimination of manual Slate UI coding for simple tool settings.
Handle Multi-Threaded Data Safely Since modeless tools often run complex geometric operations (especially in Modeling Mode), ensure that heavy computations are dispatched to background threads using the TaskGraph. This prevents the elimination of editor responsiveness, ensuring the UI remains interactive while the tool processes data.
Use for “Always-On” Debugging Utilities Modeless tools are ideal for creating visualizers or measurement tools that the user might want to keep open during an entire session. Using this module for such tools leads to the elimination of the need to constantly re-enable debug modes every time a new actor is selected.
Listen for Selection Changes A best practice for modeless tools is to react dynamically to the current editor selection. By binding to the OnSelectionChanged delegate within your tool, you can facilitate the elimination of manual “target” assignment, allowing the tool to update its context automatically as the user clicks around the level.
Properly Shutdown via ShutdownContext When a modeless tool is deactivated, use the Shutdown method to clean up temporary actors or transient preview geometry. Ensuring a clean exit leads to the elimination of “ghost” meshes that might otherwise remain visible in the viewport after the tool has been dismissed.