---
layout: default
title: AppFramework
---

<!-- ai-generation-failed -->

<h1>AppFramework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AppFramework/AppFramework.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

that provides high-level UI components and framework logic. Unlike the core Slate module which provides raw primitives (like buttons and boxes), AppFramework contains “Lego kits”—pre-assembled, standardized widgets designed to create consistent professional tools, standalone applications, and complex editor utilities.

It is the primary repository for widgets that need to work across both the Unreal Editor and standalone Slate applications (like the Slate Viewer or specialized profiling tools).

Practical Usage Tips & Best Practices
1. Use for Standalone Tool Development

If you are building a tool that needs to run outside of the Unreal Editor (a “Program” target), AppFramework is essential. It provides the high-level structures needed to manage windowing, docking, and common UI patterns without requiring the overhead of the UnrealEd module.

2. Leverage “Tool Widgets” for Consistency

Instead of styling raw Slate buttons, look for widgets prefixed with S within this module (like SPrimaryButton). These widgets automatically handle padding, hover states, and color palettes to match the modern Unreal Engine “Slate” look and feel.

Best Practice: Use SPrimaryButton (the blue button) for the main action in a dialog (e.g., “Save”) and standard buttons for secondary actions (e.g., “Cancel”) to guide user focus.
3. Implement the SWebBrowser Widget

The AppFramework module is frequently used to house the SWebBrowser component. If your tool needs to display documentation, web-based dashboards, or HTML5 content, you will need to include AppFramework and WebBrowser in your Build.cs to manage the UI wrapper.

4. Utilize the Color Picker and Palettes

This module contains the logic for the engine’s standardized Color Picker (SColorPicker). If your custom editor tool or in-game utility requires advanced color selection—including HDR values and alpha support—reusing the SColorPicker from AppFramework ensures a professional and familiar experience for the user.

5. Handle Framework Events for Elimination of Resources

When building complex UI that manages external resources (like file handles or network sockets), use the framework’s lifecycle delegates. Ensure that when a window is closed, you trigger the elimination of any temporary data structures or “Cleanup” functions to prevent memory leaks in long-running editor sessions.

6. Add Module Dependencies Correctly

Because AppFramework is a runtime-capable module, it can be used in your game project. However, it is most commonly used in Editor or Program modules. Add it to your Build.cs as follows:

C#
	// MyTool.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "Slate", 

	    "SlateCore", 

	    "AppFramework" 

	});
Copy code
7. Explore SWidgetGallery for Reference

The engine contains a tool called the Slate Viewer (accessible in the source code as a standalone program). It heavily utilizes AppFramework. Reviewing the source code for the Slate Viewer is the best way to see how to implement AppFramework widgets like SProgressBar, SCheckBox, and SColorBlock in a professional layout.

8. Prefer Composition over Raw Styling

A core philosophy of AppFramework is Composition. Instead of creating a new widget class and overriding OnPaint, try to compose your UI using existing AppFramework widgets as “slots.” This makes your UI more resilient to engine updates and ensures that font scaling and DPI changes are handled automatically by the framework.