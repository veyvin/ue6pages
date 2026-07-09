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

provides the foundational internationalization (I18N) and localization (L10N) capabilities for Unreal Engine. While FText is the high-level class developers use for localized strings, ICU is the engine “under the hood” that handles the complex linguistic rules of different cultures.

It is used for culture-aware string comparison, date/time/number formatting, word/line boundary analysis (essential for text wrapping), and Unicode-compliant case transformations. By utilizing ICU, the engine “eliminates” the need for developers to manually handle the intricate formatting and sorting rules of hundreds of world languages.

Practical Usage Tips and Best Practices
Reference via Build.cs Macros
To include ICU in a C++ tool or module, use the built-in third-party helper in your Build.cs. This “eliminates” the need to specify platform-specific include or library paths:
C#
	    AddEngineThirdPartyPrivateStaticDependencies(Target, "ICU");

	    ```

	 

	*   **Protect Headers from Macro Collisions**  

	    ICU uses several global macros (like `SUCCESS` or `TEXT`) that conflict with Unreal's own definitions. Always wrap ICU includes to "eliminate" compiler errors:

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include <unicode/locid.h>

	    #include <unicode/timezone.h>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Optimize Package Size via Data Sets**  

	    ICU data can be large. In **Project Settings > Packaging**, you can select "Internationalization Support" levels (e.g., "English", "EFIGS", or "CJK"). This "eliminates" unnecessary cultural data from your final build, potentially saving several megabytes of disk space.

	 

	*   **Trust FText for Standard Operations**  

	    Avoid calling raw ICU functions for simple formatting or case changes. Use `FText::Format` and `FText::ToUpper`. These Unreal functions already utilize ICU internally, "eliminating" the risk of mismatched culture settings between the engine and the library.

	 

	*   **Use for Custom Text Boundary Analysis**  

	    If you are building a custom UI widget or text renderer, use ICU's `BreakIterator` to find valid line breaks. This "eliminates" issues with languages like Japanese or Thai that do not use spaces between words, ensuring text wraps correctly according to linguistic rules.

	 

	*   **Synchronize Culture with Unreal**  

	    If you must use raw ICU objects (like `icu::Locale`), ensure they match the engine's current culture. Access this via `FInternationalization::Get().GetCurrentCulture()`. This "eliminates" discrepancies where the engine displays French text but your custom ICU logic uses the system's default English locale.

	 

	*   **Handle BiDi and Right-to-Left (RTL) Text**  

	    ICU provides the bidirectional (BiDi) algorithm support used by Slate. When rendering text manually, use ICU to detect the base direction of a string. This "eliminates" visual glitches in RTL languages like Arabic or Hebrew by ensuring characters are laid out in the correct order.

	 

	*   **Check ICU Availability**  

	    While ICU is standard on most platforms, some extremely stripped-down builds might disable it. Use `FText::IsLocalized()` or check for the presence of the module before performing deep internationalization tasks to "eliminate" crashes in "Culture Invariant" only environments.
Copy code
Protect Headers from Macro Collisions
ICU uses several global macros (such as SUCCESS or TEXT) that conflict with Unreal’s internal definitions. Always wrap ICU includes to “eliminate” compiler errors:
C#
	    AddEngineThirdPartyPrivateStaticDependencies(Target, "ICU");

	    ```

	 

	*   **Protect Headers from Macro Collisions**  

	    ICU uses several global macros (like `SUCCESS` or `TEXT`) that conflict with Unreal's own definitions. Always wrap ICU includes to "eliminate" compiler errors:

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include <unicode/locid.h>

	    #include <unicode/timezone.h>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Optimize Package Size via Data Sets**  

	    ICU data can be large. In **Project Settings > Packaging**, you can select "Internationalization Support" levels (e.g., "English", "EFIGS", or "CJK"). This "eliminates" unnecessary cultural data from your final build, potentially saving several megabytes of disk space.

	 

	*   **Trust FText for Standard Operations**  

	    Avoid calling raw ICU functions for simple formatting or case changes. Use `FText::Format` and `FText::ToUpper`. These Unreal functions already utilize ICU internally, "eliminating" the risk of mismatched culture settings between the engine and the library.

	 

	*   **Use for Custom Text Boundary Analysis**  

	    If you are building a custom UI widget or text renderer, use ICU's `BreakIterator` to find valid line breaks. This "eliminates" issues with languages like Japanese or Thai that do not use spaces between words, ensuring text wraps correctly according to linguistic rules.

	 

	*   **Synchronize Culture with Unreal**  

	    If you must use raw ICU objects (like `icu::Locale`), ensure they match the engine's current culture. Access this via `FInternationalization::Get().GetCurrentCulture()`. This "eliminates" discrepancies where the engine displays French text but your custom ICU logic uses the system's default English locale.

	 

	*   **Handle BiDi and Right-to-Left (RTL) Text**  

	    ICU provides the bidirectional (BiDi) algorithm support used by Slate. When rendering text manually, use ICU to detect the base direction of a string. This "eliminates" visual glitches in RTL languages like Arabic or Hebrew by ensuring characters are laid out in the correct order.

	 

	*   **Check ICU Availability**  

	    While ICU is standard on most platforms, some extremely stripped-down builds might disable it. Use `FText::IsLocalized()` or check for the presence of the module before performing deep internationalization tasks to "eliminate" crashes in "Culture Invariant" only environments.
Copy code
Optimize Package Size via Data Sets
ICU data can be quite large. In Project Settings > Packaging, you can select “Internationalization Support” levels (e.g., “English”, “EFIGS”, or “CJK”). This “eliminates” unnecessary cultural data from your final build, which can save several megabytes of disk space.
Trust FText for Standard Operations
Avoid calling raw ICU functions for simple formatting or case changes. Use FText::Format and FText::ToUpper. These Unreal functions already utilize ICU internally, “eliminating” the risk of mismatched culture settings between the engine and the library.
Use for Custom Text Boundary Analysis
If you are building a custom UI widget or a text renderer, use ICU’s BreakIterator to find valid line breaks. This “eliminates” issues with languages like Japanese or Thai that do not use spaces between words, ensuring text wraps according to correct linguistic rules.
Synchronize Culture with Unreal
If you must use raw ICU objects (like icu::Locale), ensure they match the engine’s current culture accessed via FInternationalization::Get().GetCurrentCulture(). This “eliminates” discrepancies where the engine displays French text but your custom ICU logic defaults to English.
Handle BiDi and Right-to-Left (RTL) Text
ICU provides the bidirectional (BiDi) algorithm support used by Slate. When rendering text manually, use ICU to detect the base direction of a string. This “eliminates” visual glitches in RTL languages like Arabic or Hebrew by ensuring characters are laid out in the correct logical order.
Check ICU Availability
While ICU is standard on most platforms, some stripped-down builds might disable it. Use FText::IsLocalized() or check for the presence of the module before performing deep internationalization tasks to “eliminate” crashes in “Culture Invariant” only environments.