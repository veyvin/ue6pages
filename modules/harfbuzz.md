---
layout: default
title: HarfBuzz
---

<!-- ai-generation-failed -->

<h1>HarfBuzz</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/HarfBuzz/HarfBuzz.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the industry-standard text-shaping engine. While standard Latin text can often be rendered using simple character spacing, complex scripts (such as Arabic, Devanagari, or Thai) and advanced typography (like ligatures) require “shaping.” HarfBuzz takes a string of Unicode codepoints and a font file to determine the exact glyph IDs and their relative positions, ensuring that text is linguistically and visually accurate across all global cultures supported by Slate and UMG.

Practical Usage Tips & Best Practices
1. Set Text Shaping to “Auto” for Performance

Unreal Engine provides three shaping methods: KerningOnly, FullShaping, and Auto.

Best Practice: Keep your UI widgets set to Auto. This allows the engine to use a faster, simpler path for basic Western text while automatically switching to HarfBuzz only when it detects complex scripts or specific OpenType features. This strategy leads to the elimination of unnecessary CPU overhead for simple strings.
2. Verify Font OpenType Table Support

HarfBuzz is only as good as the data within the font file (TTF/OTF).

Tip: If ligatures or complex script behaviors are not appearing, ensure your font includes GSUB (Substitution) and GPOS (Positioning) tables. Without these tables, HarfBuzz cannot perform its tasks, resulting in the elimination of intended typographic features.
3. Distinguish Between Shaping and BiDi Logic

It is a common mistake to assume HarfBuzz handles the direction of text (Left-to-Right vs. Right-to-Left).

Best Practice: Remember that the ICU (International Components for Unicode) module handles Bi-Directional (BiDi) ordering, while HarfBuzz handles the “shaping” of the characters within those runs. If text appears in the correct order but with disconnected characters, the issue is likely HarfBuzz-related; if the order is reversed, check your ICU or UMG Flow Direction settings.
4. Manually Force “Full Shaping” for Stylistic Ligatures

For high-end artistic projects, you may want “fi” or “fl” ligatures in English text that “Auto” mode might skip for speed.

Tip: If you require advanced typographic features for Western languages, manually set the Text Shaping Method to Full Shaping in the widget properties. This ensures the elimination of standard character separation in favor of professional-grade ligatures.
5. Include the “HarfBuzz” Dependency in Build.cs

If you are developing custom C++ Slate widgets that perform low-level text rendering or manual shaping, you must link the module.

Best Practice: Add "HarfBuzz" to your PublicDependencyModuleNames in your project’s Build.cs. This allows you to access the ITextShaper interface, ensuring the elimination of compilation errors when calling advanced text layout functions.
6. Use “Slate.TextShapingMethod” for Debugging

If you encounter a visual bug in your UI text, you can isolate the cause using console commands.

Tip: Use Slate.TextShapingMethod 1 to force Kerning Only or 2 to force Full Shaping globally. Comparing these two states assists in the elimination of confusion by identifying whether a bug is caused by the font’s basic kerning or the complex HarfBuzz shaping logic.
7. Profile Localized UI with Unreal Insights

HarfBuzz is more computationally expensive than simple kerning because it performs multiple passes over the text buffer.

Best Practice: When localizing into languages like Hindi or Arabic, use Unreal Insights to monitor ShapedText counters. Optimization in these languages often requires the elimination of excessively long text blocks or the use of “Wrap Text At” to reduce the per-frame shaping workload.
8. Monitor Glyph Atlas Growth

Because HarfBuzz can generate unique “shaped” glyph combinations, it may cause the Slate Font Atlas to fill up faster than standard text.

Tip: Use the console command Slate.ShowFontAtlas to visualize the GPU texture. If the atlas is crowded, consider using smaller font faces for complex scripts to facilitate the elimination of memory bloat in your UI rendering pipeline.