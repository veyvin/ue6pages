---
layout: default
title: AdvancedWidgets
---

<!-- ai-generation-failed -->

<h1>AdvancedWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AdvancedWidgets/AdvancedWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, PropertyEditor, Slate, SlateCore, UMG, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

provides a set of complex, niche widgets that go beyond the standard UMG and Slate offerings. It is primarily used to create professional-grade editor tools, complex settings menus, and specialized gameplay HUDs that require advanced input methods or data visualization.

Description and Purpose

The module contains both Slate (C++) and UMG (Blueprint) versions of widgets like the Radial Slider, Password Editable Text, and Property View. Its purpose is to provide developers with “pre-built” solutions for common but technically difficult UI patterns. Instead of building a circular slider or a masked password field from scratch, developers can leverage this module to maintain consistency with Unreal’s own internal tool design.

Practical Usage Tips and Best Practices
Enable the Module Dependency
The AdvancedWidgets module is not included by default in most projects. To use its C++ classes or ensure Blueprint nodes are available, add the following to your [ProjectName].Build.cs file:
PublicDependencyModuleNames.AddRange(new string[] { "AdvancedWidgets" });
Use the Radial Slider for Controller UX
The URadialSlider is significantly more intuitive for gamepad users than a linear horizontal slider. Use it for character attribute allocation or volume settings. You can customize the “Hand” appearance and define the arc (e.g., a 180-degree semi-circle vs. a full 360-degree circle) to fit your design.
Secure Input with Password Editable Text
When building in-game login systems or “room code” entries for multiplayer, use the UPasswordEditableText widget. It handles character masking automatically and provides a safer foundation for sensitive data entry than a standard text box.
Expose Runtime Properties via Property View
The UPropertyView widget allows you to display a “Details Panel” style interface inside your game or a custom editor tool. This is highly efficient for “Photo Mode” menus or debug menus where you want to expose variable tweaking without manually creating individual sliders and checkboxes for every property.
Leverage SRadialSlider for Editor Utility Widgets
If you are building Editor Utility Widgets to automate your pipeline, use the Slate version (SRadialSlider). It is more performant in tool-heavy environments and offers deeper customization via Slate’s declarative syntax for specialized tool layouts.
Optimization: Avoid Deep Nesting
Advanced widgets like the Property View can be computationally expensive as they use reflection to find and display properties. Avoid placing these inside a Tick function or deeply nested Scroll Boxes; instead, initialize them once when the UI is opened and update them via event-driven logic.
Graceful Logic for Elimination Feedback
When designing a HUD that tracks match progress, you can use the Radial Slider as a “cooldown” or “progress” ring. For example, if a player achieves an elimination, you can use a Radial Slider to visually represent the “respawn” timer or the “streak” expiration, providing clear spatial feedback to the player.
Standardize Styling via Widget Styles
Many Advanced Widgets support the same styling patterns as standard UMG widgets. Ensure you create a centralized SlateWidgetStyleAsset to keep your Radial Sliders and Password fields consistent with the rest of your UI’s look and feel.