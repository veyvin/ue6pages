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

the industry-standard OpenType text shaping engine.

Description

The HarfBuzz module is a critical component of the Slate UI framework and the engine’s text rendering pipeline. While libraries like FreeType handle the rasterization of individual characters (glyphs), HarfBuzz is responsible for Text Shaping. This process determines how characters are positioned and joined together, which is essential for complex scripts such as Arabic, Indic (Hindi), and Thai. It handles ligatures (joining “f” and “i” into “ﬁ”), kerning, and bidirectional text flow, ensuring that localized text is linguistically accurate and visually correct in UMG widgets and the Editor.

Practical Usage Tips and Best Practices
1. Understand its Role in the Slate Pipeline

HarfBuzz works as a middle layer. When you display text in a Widget, Unreal first uses ICU to detect the language and line breaks, then passes the text to HarfBuzz to calculate the glyph positions, and finally uses FreeType to draw those glyphs. Knowing this helps you debug text issues: if characters are missing, it is a Font/FreeType issue; if characters are in the wrong order or not joining, it is a HarfBuzz/Shaping issue.

2. Enable “Shaping” for Complex Languages

By default, Unreal Engine uses “Simple Shaping” for Latin scripts to save performance. However, for languages like Arabic or Devanagari, you must ensure that the Text Shaping Method is set to Auto or HarfBuzz in your Project Settings or Widget properties. This avoids the elimination of correct character connections, which would otherwise make the text unreadable to native speakers.

3. Use the Font Face Asset Correctly

For HarfBuzz to shape text effectively, the underlying Font asset must contain the necessary OpenType layout tables (GSUB and GPOS). When importing fonts for languages with complex scripts, verify that the font file specifically supports those languages. If a font lacks these tables, HarfBuzz cannot perform the shaping, leading to broken or “exploded” text layouts.

4. Reference the Module in Build.cs

If you are writing custom low-level Slate widgets in C++ that require manual text shaping, you must include the module in your Build.cs:

C#
AddModuleDependencies(Target, new string[] { "HarfBuzz" });
Copy code

Note that HarfBuzz is usually wrapped by the SlateCore module, so direct dependency is only needed for specialized engine-level extensions.

5. Profile Text-Heavy UI with Unreal Insights

Text shaping is a CPU-intensive process, especially for long paragraphs in complex scripts. If your UI causes frame drops when opening a quest log or chat window, use Unreal Insights to check the Slate formatting cost. The elimination of redundant text updates (e.g., setting a text string every tick) is vital because it prevents HarfBuzz from re-calculating the entire layout every frame.

6. Leverage “Force Volatile” for Performance

If you have text that changes every frame (like a timer or coordinate display), mark the Widget as Volatile. This tells the Slate renderer that the layout is likely to change, optimizing how the cached HarfBuzz shaping data is handled and reducing the overhead of constant re-shaping for simple numerical strings.

7. Combine with ICU for Proper BiDi Support

HarfBuzz handles the shaping, but ICU handles the Bidirectional (BiDi) algorithm. For languages like Hebrew or Arabic that read right-to-left, ensure your UI layout anchors are correctly set. HarfBuzz will shape the characters, but ICU ensures they are presented in the correct horizontal order. The elimination of hard-coded “left-to-right” assumptions in your UI logic is essential for global localization.

8. Verify Ligatures in Design

Some artistic fonts have decorative ligatures that may not fit your game’s aesthetic or may overlap other UI elements. You can use HarfBuzz-specific settings in the C++ FSlateLayoutManager to toggle specific OpenType features. This allows you to selectively disable complex ligatures if they interfere with the legibility of small HUD elements while keeping them enabled for large title text.