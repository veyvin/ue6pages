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

visual appearance of the Unreal Editor. It acts as a centralized repository for UI resources, including brushes (images/icons), fonts, colors, and layout styles used by every window, menu, and button in the editor. While FAppStyle is the modern interface used in UE5, it still draws heavily from this module to ensure that custom tools, plugins, and editor utilities look and feel consistent with the rest of the Unreal ecosystem.

Practical Usage Tips & Best Practices
1. Prefer FAppStyle over FEditorStyle

In modern versions of Unreal (5.0+), the engine has transitioned toward a unified styling system.

Best Practice: Always use FAppStyle::Get() to retrieve brushes or fonts instead of the legacy FEditorStyle. This ensures your custom UI remains compatible with future engine updates and facilitates the elimination of deprecated code paths in your C++ plugins.
2. Use “Style Colors” for Theme Support

Unreal Engine 5 allows users to customize their editor themes (e.g., Dark, Light, or custom colors).

Tip: Instead of hardcoding a hex color like FLinearColor::Gray, use FAppStyle::Get().GetColor("StyleColors.Background"). This allows your UI to adapt automatically when a user changes their theme, leading to the elimination of unreadable text or clashing colors in custom windows.
3. Find Icons via the Widget Reflector

Finding the specific string name for a built-in icon (like the “Save” floppy disk) can be difficult.

Best Practice: Open the Widget Reflector (Ctrl+Shift+W), enable “Snapshot”, and hover over an existing editor icon. It will often show the Style Name and Brush Name used. Using existing icons ensures the elimination of visual “noise” caused by inconsistent UI symbols.
4. Register Custom Styles via FSlateStyleSet

If your plugin has unique icons, you should create a dedicated Style Set rather than trying to inject them into the engine’s default set.

Tip: Create a class inheriting from FSlateStyleSet, register your textures there, and add it to the FSlateStyleRegistry. This modular approach ensures the total elimination of naming conflicts with internal engine assets.
5. Leverage “RootToContentDir” for Paths

When defining custom brushes in C++, paths to textures can be brittle if the plugin is moved.

Best Practice: Use the RootToContentDir function within your Style Set to define relative paths to your plugin’s Resources folder. This leads to the elimination of “Missing Brush” errors when your plugin is installed in different project directories.
6. Use Icons for Tool Bar Buttons

For Editor Utility Widgets or C++ Toolbars, a consistent icon size is vital for a professional look.

Tip: Most toolbar icons are expected to be 16x16 or 32x32 pixels. Referencing FAppStyle::GetBrush("Icons.Save") ensures your buttons match the engine’s padding and scaling, resulting in the elimination of awkward UI alignment issues.
7. Clean Up Styles on Shutdown

Failing to unregister a custom style set can lead to memory leaks or crashes when the editor closes.

Best Practice: Always call FSlateStyleRegistry::UnRegisterSlateStyle in your module’s ShutdownModule function. This practice ensures the permanent elimination of “zombie” style references that could corrupt the editor’s memory state during a hot-reload.
8. Utilize Font Styles for Hierarchy

The EditorStyle module provides standardized font sets like NormalFont, BoldFont, and LargeFont.

Tip: Use FAppStyle::Get().GetFontStyle("NormalFont") for your UI text. Using the built-in hierarchy helps the user distinguish between headers and body text, which assists in the elimination of cluttered and confusing interfaces.