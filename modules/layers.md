---
layout: default
title: Layers
---

<!-- ai-generation-failed -->

<h1>Layers</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Layers/Layers.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, InputCore, SceneOutliner, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ool designed to simplify complex scenes by allowing you to quickly hide, show, or select specific categories of objects during the design phase.

Practical Usage Tips and Best Practices
1. Distinguish Between Layers and Data Layers

It is critical to understand that the “Layers” module is for editor organization, while “Data Layers” handle runtime loading.

Best Practice: Use the Layers module for temporary working groups (e.g., “Lighting References” or “Work-in-Progress Assets”). This helps you eliminate confusion between your organization tools and your game’s actual streaming performance.
2. Utilize Selection by Type

The Layers panel provides shortcuts to select all Actors of a specific class within a layer (e.g., all Static Meshes or all Lights).

Tip: If you need to swap out all lights in a specific building, put them in a layer and use the “Select Actors” function. This is much faster than searching the Outliner and helps you eliminate the risk of missing hidden or nested Actors.
3. Manage Visibility to Boost Editor Performance

In massive levels, rendering every object can slow down the Viewport’s frame rate.

Action: Move high-poly background dressing or complex foliage into a specific layer and toggle its visibility (the “Eye” icon) off while working on gameplay logic. This helps you eliminate viewport lag and improves your iteration speed.
4. Use the “Details” Panel for Fast Assignment

You don’t always need the Layers Panel open to assign objects.

Tip: With an Actor selected, look at the Layers section in the Details panel. You can quickly add or remove the Actor from layers here, which helps you eliminate unnecessary window management and keeps your workspace clean.
5. Leverage Layers for Bulk Transformations

When you need to move a large group of unrelated objects (e.g., shifting an entire decorative plaza by 50 units):

Action: Select the layer in the panel, right-click, and choose “Select Actors.” You can then transform them all at once, eliminating the need to manually parent them to a folder or a temporary Actor.
6. Clean Up Unused Layers

Over time, levels can become cluttered with empty or redundant layers from deleted assets.

Best Practice: Periodically right-click in the Layers panel and use “Delete” on empty layers. Keeping a tidy layer list helps you eliminate friction for other team members who need to navigate your level.
7. Combine with “Isolate” Mode

If you need to focus entirely on one section of your level:

Tip: Select the layer you want to work on, right-click, and choose “Visibility > Make All Layers Invisible,” then toggle the eye back on for your active layer. This helps you eliminate visual distractions from the rest of the world.
8. Restrict to Editor Modules in C++

The Layers module (ILayers interface) is part of the Unreal Editor and is not available in cooked builds.

Action: If you are writing a tool to automate layer assignment, ensure your code is wrapped in #if WITH_EDITOR macros. This helps you eliminate packaging errors when you build the final executable for players.