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

e visual identity of the Unreal Engine interface.

Description

The EditorStyle module (often accessed via the FAppStyle or legacy FEditorStyle classes) serves as a centralized repository for the Unreal Editor’s “look and feel.” It contains the definitions for brushes (textures), fonts, colors, and icons used throughout the UI. Instead of hard-coding a specific color or icon into a tool, developers use this module to request a resource by name (e.g., “Icons.Save”). This ensures that if the engine’s theme is updated—such as the transition from the dark UE4 style to the modern UE5 “Slate” theme—all custom tools and plugins automatically adopt the new visuals without code changes.

Practical Usage Tips and Best Practices
1. Prefer FAppStyle over FEditorStyle

In Unreal Engine 5.x, the legacy FEditorStyle has been largely superseded by FAppStyle. While the old class still exists for compatibility, a best practice for modern C++ development is to use FAppStyle::Get().GetBrush("PropertyName"). This ensures your code is aligned with the latest engine architecture and simplifies future migrations.

2. Use the Widget Reflector to Find Styles

If you want to use an icon or color from an existing part of the editor but don’t know its name, open the Widget Reflector (Tools > Debug > Widget Reflector). Hover over the desired UI element and press F10 to lock it. The reflector will show you the exact style name and the brush being used, which you can then reference in your own Slate code.

3. Reference Style Colors for Theme Support

To ensure your custom UI respects the user’s “Active Theme” (set in Editor Preferences), use FStyleColors. Instead of defining a custom gray, use FStyleColors::Panel. This allows your UI to dynamically update if a user changes their editor theme, supporting the elimination of hard-coded, unreadable color combinations.

4. Leverage the “Editor Icon” Texture Setting

When creating custom icons for your own tools, import your textures as .png files. In the Texture Editor, set the LOD Group to UI and the Compression Settings to UserInterface2D (RGBA). This ensures the EditorStyle system renders them crisply at any DPI scale without compression artifacts.

5. Register Custom Styles via FSlateStyleSet

If your plugin has many custom icons, do not use the engine’s default style set. Instead, create your own FSlateStyleSet class within your module. This allows you to manage your assets independently and prevents namespace collisions with the engine’s internal style names.

6. Use Box Brushes for Scalable Elements

For buttons or borders, use Box Brushes (9-slice scaling). Define these in your style set using FSlateBoxBrush. This tells the module how to stretch the corners and edges of your texture without distorting the center, which is essential for UI that needs to work across different monitor resolutions and scales.

7. Handle Style Unregistration on Shutdown

When your editor module is shut down, you must call FSlateStyleRegistry::UnRegisterSlateStyle for any custom style sets you created. Failing to do so will leave “stale” style references in memory, which can lead to crashes when the editor is closed or when you attempt to hot-reload your C++ code.

8. Utilize Icons with Font-Based Glyphs

Modern Unreal UI increasingly uses font-based icons (like the Font Awesome integration). The EditorStyle module can request these as FSlateFontInfo. Using glyphs instead of textures can lead to the elimination of hundreds of tiny .png files, significantly reducing the memory footprint and improving the scaling quality of your tool’s iconography.