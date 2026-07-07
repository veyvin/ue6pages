---
layout: default
title: ICU
---

<!-- ai-generation-failed -->

<h1>ICU</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/ICU/ICU.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unicode-compliant case folding (ToUpper/ToLower), and line-break analysis. It ensures that the engine’s FText system behaves correctly regardless of the user’s regional settings.

Practical Usage Tips and Best Practices
1. Select the Correct Internationalization Support

In Project Settings > Packaging, you can choose the level of ICU data to include (e.g., English, EFIGS, CJK, or All).

Best Practice: Only include the data sets for the regions you officially support. Including “All” adds approximately 15MB to your binary size. By narrowing this down to your target locales, you eliminate unnecessary bloat in your final package.
2. Use FText for All User-Facing Strings

Unlike FString, which is a simple character array, FText is linked to the ICU-powered localization system.

Tip: Always use FText for UI elements. This allows ICU to handle culture-correct pluralization and gender forms through “Format” arguments, eliminating the need for complex, hard-coded string concatenation logic in your Blueprints or C++.
3. Leverage Culture-Correct Comparisons

Standard string comparisons (like ==) do not account for linguistic nuances or accents in different languages.

Action: Use FText::EqualTo or FText::CompareTo with specific ETextComparisonLevel flags. This utilizes ICU’s collation rules to eliminate errors in alphabetizing lists or searching for strings in languages with unique sorting rules (like Swedish or Japanese).
4. Handle Boundary Analysis for UI Wrapping

When creating custom UI widgets that render text, determining where a line can safely break is difficult in non-Latin scripts.

Tip: Use the IBreakIterator interface provided by the ICU module. This allows the engine to identify valid line-break positions in languages like Thai (which doesn’t use spaces). Using proper boundary analysis helps you eliminate “widow” characters or broken words in your UI layout.
5. Format Numbers and Dates via ICU

Manually formatting a date or currency string usually leads to errors in international markets.

Action: Use FText::AsNumber, FText::AsPercent, or FText::AsDate. These functions pass the data through ICU to apply the correct decimal separators (commas vs. periods) and date orders, eliminating confusion for players in different regions.
6. Synchronize Language and Locale

Unreal distinguishes between “Language” (which text is displayed) and “Locale” (how numbers/dates are formatted).

Best Practice: Usually, these should be set to the same value. Use FInternationalization::Get().SetCurrentLanguageAndLocale() to update both simultaneously. This ensures consistency across your game’s interface and helps eliminate “mixed-culture” bugs where the text is French but the currency is formatted as US Dollars.
7. Perform Safe Case Conversions

Some languages have unique rules for capitalization (for example, the Turkish “i” becomes “İ”, not “I”).

Tip: Use FText::ToUpper() or FText::ToLower() instead of FString equivalents for UI text. ICU performs a “locale-aware” transformation that respects these linguistic rules, eliminating disrespectful or confusing typos in localized versions of your game.
8. Use Asset Group Cultures for Audio

You may want your UI text in one language but your voice-over in another.

Action: Configure Asset Group Cultures in your DefaultGame.ini. You can assign the “Audio” group to a specific culture while the rest of the game uses the system default. This provides flexibility for your players and helps eliminate the need for custom, brittle audio-switching code.