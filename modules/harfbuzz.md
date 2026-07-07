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

al Engine’s Slate UI framework to handle advanced text shaping and layout.

Description and Purpose

While libraries like FreeType handle the “rasterization” (turning a font into pixels), HarfBuzz is responsible for “shaping.” It takes a string of Unicode characters and determines exactly where each glyph should be placed on a line of text. This is critical for languages with complex scripts—such as Arabic, Hebrew, or Indic languages—where the shape of a character changes based on its neighbors, or where characters must be combined into ligatures. In Unreal Engine, this module ensures that UMG and Slate text widgets correctly display multi-language support, right-to-left (RTL) text flow, and advanced typographic features.

Practical Usage Tips and Best Practices
Enable the “HarfBuzz” Shaping Method for Localization
In your Project Settings under Engine > User Interface, you can set the “Default Text Shaping Method.” Ensure this is set to HarfBuzz (or “Auto”) rather than “Basic” if you plan to support languages like Arabic or Thai. This will eliminate issues where characters appear disconnected or out of order.
Utilize Ligatures for Better Typography
Modern fonts often include ligatures (e.g., combining “f” and “i” into “ﬁ”). Because HarfBuzz handles the shaping logic, enabling these features in your Font assets allows for a more professional UI. This helps you eliminate awkward spacing in high-resolution text blocks.
Test Right-to-Left (RTL) Layouts Early
If you are localizing into Arabic or Hebrew, HarfBuzz handles the character reordering, but you must still ensure your UMG layout supports mirroring. Use the Preview Language setting in the editor to view your UI in an RTL culture; this helps you eliminate overlapping widgets and alignment errors before shipping.
Debug via “Slate.ShowTextDebugging”
You can use the console command Slate.ShowTextDebugging 1 to see how HarfBuzz is breaking down text into “runs” and glyph sequences. This is a vital tool to eliminate confusion when a specific character sequence is not rendering as expected in a custom font.
Combine with ICU for Full Internationalization
HarfBuzz works in tandem with the ICU (International Components for Unicode) library. While HarfBuzz places the glyphs, ICU handles the line-breaking rules. Ensure your project includes the “All” or “EFIGSCJK” internationalization data sets in Project Settings to eliminate incorrect word wrapping in localized text.
Monitor Performance in Text-Heavy Screens
Shaping complex scripts with HarfBuzz is more computationally expensive than simple Latin text. If you have a screen with thousands of updating text elements (like a massive scrolling combat log), consider using Invalidation Panels in UMG. This will eliminate the need for HarfBuzz to re-shape the text every single frame.
Verify Font Support for Script Features
HarfBuzz can only shape what the font allows. If you are seeing “tofu” (empty boxes) or unshaped characters, verify that your Font Face asset actually contains the Unicode ranges for that language. Proper font selection is the best way to eliminate rendering artifacts in global releases.
Use for Signed Distance Field (SDF) Text
In UE 5.6, when using the newer SDF Text Rendering for high-quality scaling, HarfBuzz still handles the initial layout of the glyphs. Combining HarfBuzz’s accurate shaping with SDF rendering helps you eliminate pixelation and layout shifts when dynamically scaling UI elements.