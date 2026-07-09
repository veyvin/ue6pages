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

lar open-source font engine. Within Unreal Engine, it serves as the foundational technology for the text rendering pipeline, specifically for the Slate and UMG frameworks.

Its primary role is to parse font files (such as .ttf and .otf), manage font faces, and rasterize individual glyphs into bitmaps or distance fields. These are then packed into font atlases for rendering by the GPU. By providing this low-level access, the module allows the engine to handle complex text layouts and international character sets.

Practical Usage Tips and Best Practices
Reference via Engine Macros
When adding this as a dependency in your C++ tool via Build.cs, use the specialized third-party macro: AddEngineThirdPartyPrivateStaticDependencies(Target, "FreeType2");. This “eliminates” the need to manually track platform-specific library paths for Win64, Linux, or mobile.
Protect Headers from Macro Conflicts
FreeType uses many short, global macros that often conflict with Unreal’s naming conventions. Always wrap your includes to “eliminate” compiler errors:
C++
	    #include "Precompile.h"

	    THIRD_PARTY_INCLUDES_START

	    #include <ft2build.h>

	    #include FT_FREETYPE_H

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Prefer Slate Interfaces over Direct Calls**  

	    Before calling FreeType directly, check if the `FSlateFontRenderer` or `ICacheableFontData` interfaces meet your needs. Using the engine's built-in wrappers "eliminates" the complexity of managing font face lifetimes and ensures your text remains compatible with UE's global DPI scaling and font caching.

	 

	*   **Leverage for Runtime Glyph Extraction**  

	    If you are building a custom text effect (like a 3D text generator), use the FreeType module to extract the vector outlines of a glyph via `FT_Load_Glyph` with the `FT_LOAD_NO_BITMAP` flag. This allows you to "eliminate" reliance on static meshes for text by generating geometry dynamically from font data.

	 

	*   **Manual Memory Management**  

	    If you initialize a FreeType library instance (`FT_Init_FreeType`) or load a face (`FT_New_Face`), you are responsible for their destruction. Always call `FT_Done_Face` and `FT_Done_FreeType` in your class's destructor or `ShutdownModule` to "eliminate" memory leaks that can accumulate over long editor sessions.

	 

	*   **Respect the Threading Model**  

	    FreeType is not inherently thread-safe for shared objects. If you are rasterizing glyphs on a background thread (e.g., for a custom loading screen), ensure you have a dedicated `FT_Library` instance per thread. This "eliminates" race conditions that lead to memory corruption or "broken" glyph rendering.

	 

	*   **DPI and Scaling Calculations**  

	    When setting font sizes via `FT_Set_Char_Size`, remember that Unreal Engine internally uses **96 DPI** for its calculations. Aligning your FreeType logic with this standard "eliminates" size mismatches between your custom rendering and the rest of the engine's UI.

	 

	*   **Utilize for SDF Generation (UE 5.5+)**  

	    With the introduction of **Signed Distance Field (SDF)** text rendering in UE 5.5, FreeType is now used to generate the source data for these fields. When working with distance fields, use FreeType to load glyphs at high resolutions (e.g., 64pt or higher) to "eliminate" artifacts in the generated SDF texture.
Copy code
Utilize for Custom Geometry Generation
If you are building a tool to generate 3D text geometry, use FreeType to extract glyph outlines via FT_Load_Glyph with the FT_LOAD_NO_BITMAP flag. This allows you to “eliminate” reliance on static mesh fonts by creating procedural meshes directly from font vectors.
Coordinate with the Slate Font Cache
Avoid creating independent FreeType instances for simple UI tasks. Instead, use the FSlateFontCache. This “eliminates” redundant memory usage by sharing existing font faces and rasterized textures already managed by the engine’s UI system.
Manage Manual Lifetimes Carefully
If you must initialize a manual FT_Library or FT_Face for a custom pipeline, you are responsible for their destruction. Always call FT_Done_Face and FT_Done_FreeType in your destructor to “eliminate” memory leaks during long editor sessions.
Standardize on 96 DPI
Unreal Engine typically assumes a standard resolution of 96 DPI for its font scaling logic. When calling FT_Set_Char_Size, ensure your DPI parameters match this engine standard to “eliminate” size discrepancies between your custom code and standard UMG widgets.
Leverage High-Res Loading for SDFs
For modern Signed Distance Field (SDF) rendering, load your glyphs at a high point size (e.g., 64pt or 128pt) before generating the distance field. This “eliminates” aliasing artifacts and ensures the sharpest possible text rendering at large scales.
Thread Safety Considerations
FreeType library objects are not thread-safe. If you are rasterizing glyphs on a background thread (e.g., for a procedural sign generator), ensure each thread has its own FT_Library instance. This “eliminates” race conditions that can lead to crashes or “broken” glyph data.