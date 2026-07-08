---
layout: default
title: FreeType2
---

<!-- ai-generation-failed -->

<h1>FreeType2</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/FreeType2/FreeType2.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rce FreeType library, which is the industry standard for rendering fonts. It is located within the engine’s ThirdParty source tree and serves as the underlying “engine” for Slate and UMG to handle TrueType (.ttf) and OpenType (.otf) font files.

This module is responsible for the low-level tasks of loading font faces, extracting glyph outlines, and rasterizing them into bitmaps that the GPU can display. By handling the complex mathematics of font metrics and kerning, it helps eliminate the need for developers to manually manage individual character spacing and scaling logic.

Practical Usage Tips and Best Practices
Configure Font Hinting for Clarity
Inside the Font Face asset, you can choose between different Hinting settings (e.g., Auto, Monochrome, or None). Adjusting these allows the FreeType2 module to align glyphs more accurately with the pixel grid, which helps eliminate blurriness on low-resolution displays or small UI text.
Leverage Signed Distance Fields (SDF)
In UE 5.5+, you can enable Distance Field Mode in your Font Face assets. This uses a specialized rasterization method that allows fonts to be scaled infinitely without losing sharpness. This practice helps eliminate the memory overhead of generating massive font atlas textures for large headlines.
Control Memory via Unload Policy
Use the Slate.UnloadFreeTypeDataOnFlush console variable to manage memory. Enabling this allows the engine to eliminate cached font data from RAM after the textures have been uploaded to the GPU, which is particularly useful for memory-constrained platforms like mobile devices.
Audit Glyph Caching to Prevent Hitches
If your game supports many languages, the FreeType2 module may cause “hitchiness” as it rasterizes new characters on the fly. Use the Slate.DumpFontCacheStats command to see if your font atlas is constantly overflowing. Pre-loading common characters can help eliminate these runtime performance spikes.
Utilize “Lazy Load” for Large Font Files
In the Font Face settings, set the Loading Policy to Lazy Load. This ensures the FreeType2 module only loads the font data into memory when it is actually needed for a widget, helping to eliminate unnecessary startup time and initial memory bloat.
Handle Broken Metrics with Bounding Box
Some custom or stylized fonts have incorrect internal metrics that cause clipping. You can change the Layout Method in the asset settings from Metrics to Bounding Box. This forces the module to use the visual edges of the glyphs, helping to eliminate text being cut off at the top or bottom.
Include Module in Build.cs for Low-Level Tools
If you are writing a custom C++ text renderer or a specialized editor tool, you must add "FreeType2" to your PrivateDependencyModuleNames. This provides access to the raw FreeType headers, but be sure to wrap this in #if WITH_FREETYPE to eliminate build errors on platforms where the library might be substituted.
Verify Character Support with Unicode
FreeType2 handles Unicode, but it can only render what is in the file. If you see “squares” or missing characters, the font file lacks those glyphs. Using the module’s reporting capabilities helps you eliminate localization bugs by identifying missing character ranges before they reach the player.