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

that provides a suite of high-level, application-style UI components. It sits between the low-level primitive widgets of SlateCore and the specialized, heavy tools of the Unreal Editor.

Description and Purpose

The module is designed to provide “Application Framework” level widgets that are common across professional software but complex to build from scratch. This includes elements like Color Pickers, Wizards, Error Reporting text boxes, and Standard Windows. Its primary purpose is to offer a consistent UI language for both the Unreal Editor’s internal tools and custom developer-made Editor Utility Widgets or standalone Slate applications. By using AppFramework, developers ensure their tools feel “native” to the Unreal ecosystem.

Practical Usage Tips and Best Practices
Dependency Management
To use these widgets in your C++ tool, you must explicitly add the module to your Build.cs file. It is commonly paired with Slate and SlateCore:
C#
PublicDependencyModuleNames.AddRange(new string[] { "AppFramework", "Slate", "SlateCore" });
Copy code
Leverage SColorPicker for Tooling
Instead of creating custom sliders for color selection, use the SColorPicker. It supports sRGB/Linear conversions, alpha channels, and theme saving out of the box. You can summon it as a modal window or embed it directly into your tool’s layout.
Build Multi-Step Workflows with SWizard
If you are creating a complex setup tool (e.g., a project initializer or an asset importer), use the SWizard widget. It provides built-in “Next,” “Back,” and “Finish” button logic, along with page validation, ensuring a structured user experience.
Standardize Feedback with SErrorText
Use the SErrorText widget for inline validation in your tools. It provides a standard way to display error icons and red warning text that matches the Unreal Editor’s style, which is much more professional than simple Print String or log output for user-facing errors.
Utilize SWindow for Standalone Tools
When creating a tool that needs to live outside the main Editor docking system (a “Nomad” tab or a popup), use SWindow. It handles OS-level window decorations, resizing, and focus management across different platforms.
Handle Complex Data with Property Views
The module contains logic for displaying property-style rows. Use these to create “Details Panel” replicas within your own utility widgets, allowing you to expose UObject variables for editing without writing custom UI for every property type.
Visualizing Elimination Events in Debug Tools
If you are building a custom match-viewing tool, use the high-level list widgets in AppFramework to track gameplay events. For example, use an SListView to create a real-time log of every elimination in a match, allowing you to click an entry to teleport the editor camera to the location of the elimination for instant replay.
Adhere to the “Polling” Tenet
AppFramework widgets, like most of Slate, perform best when you use “Attribute Binds” (using .Text_Lambda or .IsEnabled_Raw) rather than forcing manual updates. This allows the UI to stay in sync with your data automatically and helps eliminate stale state bugs in your custom tools.