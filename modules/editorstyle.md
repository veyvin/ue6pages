---
layout: default
title: EditorStyle
---

<!-- ai-generation-failed -->

<h1>EditorStyle</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EditorStyle/EditorStyle.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, EditorFramework, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

isual appearance and “skin” of the Unreal Editor.

Description and Purpose

This module serves as the central repository for all visual assets used by the editor’s UI, including icons, brushes, fonts, and colors. It manages the FAppStyle (formerly FEditorStyle) class, which provides a standardized way for developers to look up and apply engine-consistent styling to their custom tools, windows, and plugins. Its primary purpose is to ensure a unified user experience across the engine’s vast interface, allowing custom-built Editor Utility Widgets or C++ tabs to blend seamlessly with the native Unreal Engine 5 design language.

Practical Usage Tips and Best Practices
Transition to FAppStyle
In modern versions of UE5, the FEditorStyle class has been largely deprecated in favor of FAppStyle. When writing new Slate code or Editor Utility Widgets, always use FAppStyle::Get() to retrieve assets. This will eliminate compilation warnings and ensure your tools are compatible with future engine updates.
Reuse Existing Engine Icons
Before creating a custom icon for a tool—like a button to trigger a player elimination debug event—check the engine’s internal library. You can find common icons (like the “Save” floppy disk or “Settings” gear) by using the Style Browser tool (available under Tools -> Debug -> Style Browser). Reusing these icons helps you eliminate asset bloat and maintains visual consistency.
Utilize Semantic Colors
Instead of hard-coding hex values for colors, use semantic style colors like FAppStyle::Get().GetColor("ErrorReporting.BackgroundColor"). This ensures that if the user changes their Editor Theme (e.g., from Dark to Light mode), your UI will automatically update its palette, helping you eliminate readability issues.
Apply Standard Padding and Spacing
The module defines standard spacing constants. Using FAppStyle::Get().GetMargin("StandardPadding") for your layouts ensures that your custom windows don’t look cramped or misaligned compared to native panels. This practice helps eliminate “visual jitter” when users switch between different tabs.
Reference Styles by FName
When retrieving a brush or font, always use FName keys. For example, FAppStyle::GetBrush("Icons.Delete") is the standard way to retrieve a specific graphic. Checking the Slate Insights tool can help you find the exact string name for any element you see in the editor, which will eliminate guesswork.
Define Custom Styles in a Separate Style Set
If you are building a large plugin, do not attempt to inject your styles into the EditorStyle module directly. Instead, create your own FSlateStyleSet. You can still inherit from or reference FAppStyle for standard elements while keeping your unique assets isolated. This helps you eliminate dependency conflicts.
Use the Content Browser Icon Palette
For developers creating custom Asset Actions or types, the EditorStyle module provides specific brushes for Content Browser thumbnails. Utilizing these allows you to eliminate confusion for users by providing clear, color-coded icons for your custom data types.
Validate Styles in Editor Utility Widgets
If you are using Blueprints (UMG) to build editor tools, you can still access these styles through the “Style” pins on many widgets. Always ensure you are selecting “Editor Style” from the dropdown to eliminate the need to manually import engine textures into your project’s content folder.