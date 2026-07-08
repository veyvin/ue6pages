---
layout: default
title: FontConfig
---

<!-- ai-generation-failed -->

<h1>FontConfig</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/FontConfig/FontConfig.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

f the industry-standard Fontconfig library, primarily utilized for Linux-based platforms and the Steam Deck. It serves as the engine’s gateway to discovering and managing system-level fonts.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/FontConfig, this module provides a consistent way for Unreal Engine to query the operating system for available fonts. While Windows and macOS have proprietary font management, Linux relies on Fontconfig to handle font substitution and matching.

Primary uses include:

System Font Discovery: Identifying which fonts (like Noto Sans or Ubuntu) are installed on the host Linux distribution.
Font Fallback Management: Providing a “fallback” mechanism when a specific character (glyph) is missing from the primary font, ensuring the elimination of “missing character” boxes (tofu).
Localization Support: Automatically finding suitable fonts for complex scripts (CJK, Arabic, etc.) that may not be bundled directly with the game.
Slate Integration: Feeding font metadata into the Slate UI framework so the engine can render text correctly on cross-platform builds.
Practical Usage Tips and Best Practices
1. Bundle Crucial Fonts via Fab

While FontConfig allows you to find system fonts, you should never rely on them for your UI’s aesthetic. System fonts vary wildly between Linux distros. Always bundle your primary brand fonts as Font Assets imported from Fab or other sources to ensure a consistent visual experience regardless of the OS.

2. Configure Fallback Prioritization

If your game supports multiple languages, use FontConfig’s logic to define a “priority list” of fallback fonts. This ensures that if your primary font doesn’t support Japanese, the engine knows to look for “Noto Sans CJK” next, rather than falling back to a generic, unappealing system serif.

3. Optimize Steam Deck UI

For Steam Deck development, the FontConfig module is essential for identifying the standard fonts used by SteamOS. If you want your game’s system-level messages or “out-of-game” UI to match the Steam Deck’s native look, use the FontConfig module to query the system’s default sans-serif font.

4. Validate Font Licensing

The FontConfig module might “discover” a font on a developer’s machine that is not legally licensed for redistribution. A best practice is to perform an audit of all fonts identified by the module; ensure that any font your game actually uses is either open-source (like Google Fonts) or properly licensed for your project.

5. Use for “User-Generated Content” (UGC)

If your game allows players to type in chat or create signs, use the FontConfig-backed fallback system. This ensures that if a player types in a language you didn’t explicitly plan for, the OS can provide a glyph, resulting in the elimination of broken UI text strings.

6. Debug via the Console

When running on Linux, you can often use engine logs to see how FontConfig is resolving font requests. If a font looks incorrect, check the logs for “Fontconfig” entries; it will often tell you if it failed to find a specific typeface and what “closest match” it chose as a substitute.

7. Keep Font Face Assets “Lazy Loaded”

When using large fonts discovered via the system, ensure your Font Face assets are set to Lazy Load in the asset settings. This ensures that only the required glyphs are loaded into memory, which is critical when FontConfig points to a massive “All-in-one” Unicode font file.

8. Strategic Elimination of Font Bloat

On Linux, system font directories can be massive. If you are using FontConfig to scan for fonts, use a specific “whitelist” of families or directories to scan. This prevents the engine from indexing thousands of unnecessary fonts during startup, which can significantly improve your initial load times.