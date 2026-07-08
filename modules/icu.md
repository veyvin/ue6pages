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

ernationalization library used by Unreal Engine to handle culture-specific data and text processing. It provides the underlying logic for the FText system, enabling features such as Unicode-compliant string transformations, date/time formatting, and complex language rules.

By integrating ICU, Unreal Engine can eliminate the difficulties of supporting global markets, ensuring that text is sorted, compared, and formatted correctly according to the local laws and customs of the user’s region.

Internationalization Logic and FText

The ICU module is the engine’s primary source for internationalization (I18N). While FString is a simple character array, FText relies on ICU to perform culture-aware operations. This includes:

Culture Correct Formatting: Converting numbers, percentages, and currencies into strings based on the active locale.
Pluralization: Handling complex plural rules (e.g., “1 item” vs. “2 items” vs. “5 items” in languages like Russian or Arabic).
Boundary Analysis: Correctly identifying word breaks and line-wrapping points in languages that do not use spaces (like Japanese or Chinese).
Practical Usage Tips and Best Practices
Select the Correct ICU Data Set
In Project Settings > Packaging, you can choose different ICU data sets (e.g., English, EFIGS, CJK, or All). To eliminate unnecessary bulk in your final build, choose the smallest data set that covers all your target languages. For example, if you only support European languages, avoid the “All” setting to save several megabytes of disk space.
Use FText for All User-Facing Strings
Never use FString for text displayed to the player. Only FText is linked to the ICU module’s localization logic. Using FText helps you eliminate “hard-coded” formatting bugs where dates or numbers appear in the wrong format for international players.
Leverage Culture-Aware Comparison
When sorting lists alphabetically in the UI, use FText::CompareTo or EqualTo. These functions use ICU collation rules to eliminate incorrect sorting of accented characters or non-Latin scripts that would occur with a standard binary string comparison.
Format Dates and Times via ICU
Instead of manually building date strings, use FText::AsDate and FText::AsTime. These functions query ICU to determine if a date should be Day/Month/Year or Month/Day/Year, which helps eliminate confusion for players in different regions.
Use the ‘Culture’ Console Command for Testing
You can change the engine’s active locale at runtime using the culture=[LanguageID] command (e.g., culture=fr). This forces ICU to reload the appropriate data, allowing you to eliminate layout issues (like text clipping) in different languages without restarting the editor.
Handle Plural Forms with Format Arguments
When using FText::Format, use the plural syntax (e.g., {Num} {Num}|plural(one=Apple,other=Apples)). ICU handles the logic for various languages, helping you eliminate grammatically incorrect UI strings in regions with complex pluralization rules.
Avoid Manual Case Conversion
Do not use standard C++ tolower or toupper for user text. Instead, use FText::ToUpper or FText::ToLower. These functions use ICU to handle language-specific rules (like the Turkish “I”), which helps eliminate data corruption in localized strings.
Monitor Memory with ‘stat ICU’
The ICU module loads data tables into memory. Use the stat ICU console command to monitor memory usage. If your memory footprint is too high, evaluate if you can eliminate unused cultures or switch to a more restricted ICU data set in your project settings.